# [UPDATED] 作業要求與測試資料


請見 [homework](homework) 目錄下的 [README.md](homework/README.md) 檔案。


# Introduction to TLS


在這六小時的課程中，我會帶領各位認識密碼學非常重要的一項實際應用：[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security)。各位同學將需要撰寫 Python 程式，去解碼已經側錄好的 TLS 封包，並且實作一個針對沒有 [forward secrecy](https://en.wikipedia.org/wiki/Forward_secrecy) 的協議的攻擊：得知伺服器 RSA 私鑰後，解密已經側錄下來的那些使用較弱 cipher suite 的通訊、取得明文。通過撰寫程式、拆解 TLS 封包的實際練習，各位一定可以對 TLS 有更深刻的認識。


# 重要通知


 1. 建議自備筆電來上課

 2. 上課前，請先完成下面的「課前暖身準備」（因人而異，可能需要 1 到 10 個小時）


# 課前暖身準備


請在上課前準備好一個 Unix-like 作業系統下的 Python 工作環境。你的工作環境至少要能成功執行 `decode.py` 而不拋出任何 exception。接著，請想辦法看懂 `decode.py` 這份程式裡面的各個函式在做什麼。如果你從來沒有接觸過 Python 這個程式語言，正好可以藉此機會把它學起來，搞懂 `decode.py` 裡面用到的各種 Python 語言基本元件的意涵。官方的 [The Python Tutorial][tut_doc]、[The Python Standard Library][lib_doc]、[The Python Language Reference][lan_doc] 是非常不錯的學習與參考資源。

[tut_doc]: https://docs.python.org/3/tutorial/index.html
[lib_doc]: https://docs.python.org/3/library/index.html
[lan_doc]: https://docs.python.org/3/reference/index.html


### Unix-like 作業系統下的 Python 工作環境


這堂課，你所需要的工作環境至少要有：

 1. 純文字編輯器

    我們需要處理以 UTF-8 編碼的純文字檔案。任何你喜歡的純文字編輯器 (plain text editor) 應該都能勝任。本課程的示範，將會以文字終端機底下的 `vim` 為主。

 2. CPython

    CPython 是 Python 這個程式語言的眾多實作之一，也是 python.org 官方的實作。請安裝 3.5 或 3.6 或更新的版本。許多 Linux distribution 預設就會提供 Python 2 或 Python 3 程式。如果版本太舊，你可以上 python.org 官網下載最新版本的[原始碼](https://www.python.org/downloads/source/)來自行編譯、安裝。安裝成功後，在命令列底下應該要有 `python3` 可以使用：

        $ python3 --version
        Python 3.5.2

 3. OpenSSL 的命令列工具

    一般的 Linux distribution 都會提供 `openssl` 這個程式。你可以在命令列底下檢查之：

        $ openssl version
        OpenSSL 1.0.2g  1 Mar 2016


### 測試你的工作環境是否已經設定妥當


一個設定成功的環境，要可以成功執行此 repository 內的 `decode.py` 程式，並且在 standard output 看到 `selftest ok` 字串被印出來。像是這樣子：

    $ python3 decode.py
    selftest ok


### 如果你使用 macOS


蘋果的 macOS 作業系統預設應該就已經有 `openssl` 程式了，但是並沒有 `python3` 程式。

在 macOS 安裝 CPython 有很多種方法。我推薦先安裝 [Homebrew](https://brew.sh/) 這個套件管理工具，然後再 `brew install python3` 就行了。


### 用 VirtualBox 虛擬機造出一個範例工作環境


本課程進行中，使用的範例工作環境是 Ubuntu 16.04 (64-bit x86) 作業系統。你可以利用 VirtualBox 打造出一個幾乎相同的工作環境：


 1. 到 [VirtualBox 官方網站][vb]下載 VirtualBox 安裝檔 (the *platform packages*)

 2. 到[任何一個 Ubuntu release mirror][release_mirror] 下載 `ubuntu-16.04.2-desktop-amd64.iso`（桌面版）或 `ubuntu-16.04.2-server-amd64.iso`（伺服器版），如果你不需要 GUI 則建議用伺服器版的就好，比較省資源

 3. 安裝 VirtualBox

 4. 建立一個 VirtualBox 虛擬機，讓虛擬機用光碟映像檔開機，將 Ubuntu 16.04 作業系統安裝到虛擬機內

    虛擬機資源分配參考：

      - 桌面版：1024 MB 虛擬記憶體、16 GB 虛擬硬碟
      - 伺服器版：512 MB 虛擬記憶體、4 GB 虛擬硬碟

 5. *(optional)* 為虛擬機新增網路介面接到一個 Host-only Adapter，在虛擬機內安裝 OpenSSH 伺服器。（`apt-get install openssh-server`）如此一來就可以直接從 VirtualBox host 用 `ssh` 連線進 VirtualBox guest，也可以用 `scp` 搬移檔案。


[vb]: https://www.virtualbox.org/wiki/Downloads
[release_mirror]: http://tw.releases.ubuntu.com/xenial/


# 筆記與螢幕錄影

- [Handwritten Notes](handwritten-notes)
- [Introduction to TLS - Part 1](https://www.youtube.com/watch?v=hhlkgFQSax4)
- [Introduction to TLS - Part 2](https://www.youtube.com/watch?v=vuApksAUL3M)
- [Introduction to TLS - Part 3](https://www.youtube.com/watch?v=lxxPU5x0k4w)
- [Introduction to TLS - Part 4](https://www.youtube.com/watch?v=Uj5a8iD3NDU)
