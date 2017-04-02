# 作業

每一組都需要繳交一份使用 Python 語言 (版本 3.5) 撰寫的程式。以下我們稱這一個用 UTF-8 編碼的程式為 `decode.py`。這份程式必須要能在 Ubuntu 16.04 環境下，以內建的 Python 3.5 直譯器 (`/usr/bin/python3`) 正常執行、滿足以下要求。

# 要求

在程式執行之前，當前工作目錄下除了你的 `decode.py` 以外，我們還會為你準備好另外三個檔案：

 1. `recorded-tls-traffic-client-to-server`：從 client 到 server 的 TLS 流量
 2. `recorded-tls-traffic-server-to-client`：從 server 到 client 的 TLS 流量
 3. `stolen-rsa-decryption-key-from-server`：server 的 RSA 私鑰

目錄結構如下：

    .
    ├── decode.py
    ├── recorded-tls-traffic-client-to-server
    ├── recorded-tls-traffic-server-to-client
    └── stolen-rsa-decryption-key-from-server

    0 directories, 4 files

在這樣的工作目錄下執行 `python3 decode.py` 指令後，要產生兩個新檔案：

 1. `decrypted-traffic-client-to-server`：從 client 到 server 的明文流量（HTTP request）
 2. `decrypted-traffic-server-to-client`：從 server 到 client 的明文流量（HTTP response）

目錄結構如下：

    .
    ├── decode.py
    ├── decrypted-traffic-client-to-server
    ├── decrypted-traffic-server-to-client
    ├── recorded-tls-traffic-client-to-server
    ├── recorded-tls-traffic-server-to-client
    └── stolen-rsa-decryption-key-from-server

    0 directories, 6 files

在這一份作業，我們假設雙方協議的 TLS 版本是 1.2 而 cipher suite 是 TLS_RSA_WITH_AES_128_CBC_SHA(0x002f)。

# 範例輸入與輸出

在 samples 目錄下已經提供範例題組與答案。

# 補充資訊

本 git repository 已經為大家提供的 `decode.py` 腳本已經內含三個函數，可能會對你們有幫助：

 1. `rsa_decrypt()` 利用 openssl 實作了 RSA 的解密
 2. `tls_prf()` 實作了 RFC 5246 Section 5 的 pseudorandom function
 3. `aes128cbc_decrypt()` 利用 openssl 實作了 AES-128 CBC mode 的解密
