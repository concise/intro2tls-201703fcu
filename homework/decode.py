def b2i(val):
    assert type(val) is bytes
    return int.from_bytes(val, byteorder='big')


def i2b(val, length):
    assert type(val) is int
    assert type(length) is int and length >= 0
    assert 0 <= val < 256 ** length
    return int.to_bytes(val, length, byteorder='big')


def bytes_to_hex(val):
    assert type(val) is bytes
    return val.hex()


def hmac_sha256(key, msg):
    import hmac
    return hmac.new(key, msg, 'sha256').digest()


def tls_prf(secret, label, seed, n_bytes):
    assert type(secret) is bytes
    assert type(label) is bytes
    assert type(seed) is bytes
    assert type(n_bytes) is int and n_bytes >= 0
    last_a = label + seed
    result = b''
    while len(result) < n_bytes:
        last_a = hmac_sha256(secret, last_a)
        result += hmac_sha256(secret, last_a + label + seed)
    return result[:n_bytes]


def system(command, stdin=None):
    from subprocess import Popen, PIPE
    proc = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout, stderr = proc.communicate(stdin)
    return stdout, stderr, proc.returncode


def aes128cbc_decrypt(secret_key, ini_vector, ciphertext):
    assert type(secret_key) is bytes and len(secret_key) == 16
    assert type(ini_vector) is bytes and len(ini_vector) == 16
    assert type(ciphertext) is bytes and len(ciphertext) % 16 == 0
    stdout, stderr, retcode = system((
        'openssl', 'enc', '-aes-128-cbc', '-d', '-nopad',
        '-K', bytes_to_hex(secret_key),
        '-iv', bytes_to_hex(ini_vector)
    ), stdin=ciphertext)
    assert retcode == 0 and stderr == b''
    return stdout


def rsa_decrypt(skfilename, ciphertext):
    assert type(skfilename) is str
    assert type(ciphertext) is bytes
    stdout, stderr, retcode = system((
        'openssl', 'rsautl', '-decrypt',
        '-inkey', skfilename
    ), stdin=ciphertext)
    assert retcode == 0 and stderr == b''
    return stdout
