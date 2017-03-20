### 暖身作業

請在 3/25 (六) 上課前，準備好一個陽春的 Unix-like Python 開發、工作環境。建議使用 Python 3.5 或比這更新的版本。

一個設定成功的環境，要可以成功執行 decode.py 程式，並且看到 selftest ok 字串被印出來。

```bash
$ python3 decode.py
selftest ok
```

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

    ```bash
    $ type -a python3
    python3 is /usr/bin/python3

    $ type -a openssl
    openssl is /usr/bin/openssl

    $ python3
    Python 3.5.2

    $ openssl version
    OpenSSL 1.0.2g  1 Mar 2016
    ```

建議自備筆電來上課。
