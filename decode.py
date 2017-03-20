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


################################ self test ################################


def selftest():
    selftest_hmac_sha256()
    selftest_aes128cbc_decrypt()
    selftest_rsa_decrypt()
    print('selftest ok')


def selftest_hmac_sha256():
    key = b'key'
    msg = b'The quick brown fox jumps over the lazy dog'
    mac = bytes.fromhex(
        'f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8')
    assert hmac_sha256(key, msg) == mac


def selftest_aes128cbc_decrypt():
    secret_key = bytes.fromhex('88ac8bcb7caacdb3ebcc11b3e9b5ed48')
    ini_vector = bytes.fromhex('4546e4d490a69e35a50be37491486642')
    ciphertext = bytes.fromhex(
        '684b6073f6faf22536a7813cb08c6a8816daa214f7d0a32769c6e2007b0305e2'
        '3d05bce38259dce49a3c25a2f964b634')
    plaintext = bytes.fromhex(
        '2ff760fba67f4b76341c2a387a4edde37a61d99b1c1a83e35e7678039ab47d98'
        '26f6811d1d7d1deb794c3dd3e5677482')
    assert aes128cbc_decrypt(secret_key, ini_vector, ciphertext) == plaintext


def selftest_rsa_decrypt():

    rsa_private_key_file_content = (
        b'-----BEGIN RSA PRIVATE KEY-----\n'
        b'MIIEowIBAAKCAQEAyxvs6e5MXZLX/xFQgMpZXEM70w9yjVYa2/FZGlnJz4n8wO4H\n'
        b'A9nOSL8iDCZJ8Ny9AXtTVOrIgN7fpjFpWJe4gTScvNvqyo112W17zGcwQVXvTfMR\n'
        b'BpU9B0h9D8byhBbgIZxBjHezqk4KfhMnHFin0dZJ+3siG6FncJQ5xPzu2OIlS++g\n'
        b'+iYOthuv3yRRoJxkMtD4KoEJA06yQNZCXezLxPAcbUNXTrJuofkavWsM4Y348wQ9\n'
        b'j/ztE3VxwgGhleBipywQf+7cz3QHbHCGZMIfoVyNvkyfvlfnNRy8bSYmS/uo58AF\n'
        b'M47OoLhcPDhQMZQNB8op2vVbrijz94N+8rjg4wIDAQABAoIBACvnD2DJZ6xaT2IN\n'
        b'Bg+wrXwp9EZ88k/mqsub8Zymh97afs3dJZsJe3NyDRP/OsBblmc5lxul3E0u37z2\n'
        b'tUS3FuSm0LJp/uhlh3HGHppiO6YDw0RgI+/+VkC6xH2ijU1L/IqHUgvg2+8WC2KR\n'
        b'FUUlTLEo1rkLNqYuT0OgZpRT7/TlGkqaNvvKQmtfFRdgQNJteryeit6Lw66NAy32\n'
        b'aYhnlt4HRBtk9AmcytVH4UWqvIDIb3rqf4qnXlsOtJEQcCOHOfqh6g3Gc0+64HXn\n'
        b'pkmyHsFRBTGgufu0F6PxDe2gotC7yajugmhhRW2NCf/s6RsYrrUCpUeGDFhtF4bv\n'
        b'gsndgTECgYEA871c8j62WnMoqND+P4RMNNs9fh0XVCopZPfyS1PWoaPIYpuTfkFV\n'
        b'GgXMxyTod0Zp6DcJ8I0uCrDxQeTaKNQ4sAy1szogjq0T5az5WdDCeRTcnBBUz/uh\n'
        b'ROyMZcVcB7ULrdoDSLz1a+2agHykornBOziaEIebfb/PDFQIVs9fU/8CgYEA1VNc\n'
        b'nssHERVGE1Xnd7toofMKJKCKA5kNRZGUyPqGXX7VyZoB+YjQSv6mTHvZQH+MAe1r\n'
        b'7P6ioI+afnFSY0CHLZBhY5pxgb44Xwg4GfCynzjVRKbirM17jVsqM3ngvKdfHOgS\n'
        b'xKbRztxGYfcvLoi+ATv9WV4iPtJQgi9fFCmPox0CgYEAnHHSA8bO4tWBpoGmf3xa\n'
        b'MZ77JERl4ebB9QXUphbk75EhoHE9RU+H4RER9EyzTUOL3LnfDmB/yeryn5nVkVlO\n'
        b'HWm7ApPvq8RZvhS9Y7HD8VW7mAw/c9OOGqA+KWB5BpVlLqx9aSWn3SOABLJ8NdpG\n'
        b'tc1JzgxMeHUx3zbct2OZS18CgYA9BbKZ7ePgnCBGia1Dz8U3hmlhXtb7/n0QaHuS\n'
        b'Hi/vcMfA+qAT/HHw8fUqLcdQruui5YKY8aIdodaE0u/JWn0QqJtjPZu4jGxdquE5\n'
        b'cmP2LfC7ya1P1xu/rNNelD+YV5xajXxI6ptbvCEaBvZlLlKD0eA//zB2nfzPsLNW\n'
        b'9iiTdQKBgGSWVXyXMckt87gYSOBUdd95dC+PSoa1IQrF8YfQmEeiEoR+i+oef/7c\n'
        b'vt6Patbn+pFJwn9c47D5qOhb/eTsE+NhOqI8+lU3aKVb/w3RQKf8QD+TZI/jTU/h\n'
        b'A5jWIEciBE/HZNb65J1usBLFznGgS7yQlpQtXdwLA2+ZyaQPBQMC\n'
        b'-----END RSA PRIVATE KEY-----\n')

    ciphertext = bytes.fromhex(
        '438758729a7b2e81d4589fc7ff7c07a7b3dd81e1b3531c44a58e54fda73b9c27'
        'd0e36dbc273a16561ed74adc52da9751c68fa966979374397467d27f55870f73'
        '4a69ac4e18c262b6a38079cb6cb1910d527242f54aeebd6c15465ae106d1e3fe'
        'bfd7b3d4e2261be2a42324b061d407cfc7d5fc7555fd22af574c064b211e31bf'
        'b3a9e68d20171ce856b47d104ff6dbbe28057b6f0b62fba276bc535c5c0457d5'
        'fd3db6519b404bd6f8148e330cba1de7899aad94ee8d0f9ce6e9f6d812ca5176'
        'c8ebd068c01101a7dca8471e4a3c829d0575f6cece69064ee38ddb904e902bec'
        '53614a28f9e8eb851e8669c0aae588f8494e79850574ac553f22f1495222e65d')

    plaintext = bytes.fromhex(
        '0303391fbf91d81d91e1fb7b2c941472eb44b63ff6e860ca35298edef82b316f'
        'b516d916c72343b6b38074df2967ca56')

    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile() as tmp_f:
        tmp_f.file.write(rsa_private_key_file_content)
        tmp_f.file.flush()
        tempfilename = tmp_f.name
        assert rsa_decrypt(tempfilename, ciphertext) == plaintext


if __name__ == '__main__':
    selftest()
