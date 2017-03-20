# Introduction to TLS

## 課前暖身作業

### 作業要求

請在 03/25 (六) 上課前，準備好一個 Unix-like 的 Python 工作環境。我們將會用到 `python3` 與 `openssl` 這兩個 command-line 程式。

一個設定成功的環境，要可以成功執行此 git repository 內的 `decode.py` 程式，並且在 standard output 看到 `selftest ok` 字串被印出來，像是這樣子：

```
$ python3 decode.py
selftest ok
```

### Python 要用什麼版本？

建議使用 Python 3.5 或 3.6 或更新的版本。

本課程操作示範所使用的工作環境是：

  - 64-bit x86 machine
  - Ubuntu 16.04
  - SSH
  - terminal emulator
  - bash
  - vim
  - python3
  - openssl

你可以用 VirtualBox 虛擬機來造出一個相同的環境：

 1. 安裝 VirtualBox

 2. 建立一個 VirtualBox 虛擬機

 3. 安裝 Ubuntu 16.04 作業系統 (桌面版或伺服器版都可以)

 4. 打開終端機，在 bash shell 裡確認你已經有 `python3` 與 `openssl` 程式可以使用：

    ```
    $ type -a python3
    python3 is /usr/bin/python3

    $ type -a openssl
    openssl is /usr/bin/openssl

    $ python3
    Python 3.5.2

    $ openssl version
    OpenSSL 1.0.2g  1 Mar 2016
    ```

 5. (Optional) 在虛擬機的 Ubuntu 系統安裝 `openssh-server` 套件。將虛擬機連接到一個 Host-only Adapter，使我們可以從虛擬機外直接用 SSH 連進虛擬機。

### 建議自備筆電來上課
