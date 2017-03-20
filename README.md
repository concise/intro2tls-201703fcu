# Introduction to TLS


### ### 通知 ###

 1. 建議自備筆電來上課

 2. 在上課之前，請先完成「課前暖身作業」（因人而異，可能需要 1 到 10 個小時）


### ### 課前暖身作業 ###


請在上課前，準備好一個 Unix-like 的 Python 工作環境。你至少需要有：

 1. 純文字編輯器

    我們需要處理以 UTF-8 編碼的純文字檔案。任何你喜歡的純文字編輯器 (plain text editor) 應該都能勝任。本課程的示範操作，將會在純文字終端機底下使用 `vim`。

 2. CPython

    CPython 是 Python 程式語言的眾多實作其中之一，也是官方的實作。請安裝 3.5 或 3.6 或更新的版本。安裝成功後，在命令列底下應該要有 `python3` 可以使用：

        $ python3 --version
        Python 3.5.2

    許多 Linux distribution 預設就會提供 Python 2 或 Python 3 程式。如果版本太舊，你可以上 python.org 官網下載原始碼來自行編譯、安裝。

 3. OpenSSL 的命令列工具

    一般的 Linux distribution 都會提供 `openssl` 這個程式。你可以在命令列底下檢查之：

        $ openssl version
        OpenSSL 1.0.2g  1 Mar 2016

一個設定成功的環境，要可以成功執行此 repository 內的 `decode.py` 程式，並且在 standard output 看到 `selftest ok` 字串被印出來。像是這樣子：

    $ python3 decode.py
    selftest ok

如果成功了，請想辦法看懂 `decode.py` 這份程式。


### 範例工作環境

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

    $ python3 --version
    Python 3.5.2

    $ openssl version
    OpenSSL 1.0.2g  1 Mar 2016
    ```

 5. (Optional) 在虛擬機的 Ubuntu 系統安裝 `openssh-server` 套件。將虛擬機連接到一個 Host-only Adapter，使我們可以從虛擬機外直接用 SSH 連進虛擬機。
