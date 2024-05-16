
# 项目简介
1.自动用设置的校园账号密码，连接"LZU"或"iLZU"WiFi，由于使用的是@eLearning登录，理论上没有流量限制。

2.@eLearning限制登录设备一台，请确保账号下没有其他设备登录。

# 所需库与环境

## 库依赖
该项目依赖以下 Python 库：

- `requests`：用于检查互联网连接状态。
- `selenium`：用于自动化登录校园网页面。
- `subprocess`：用于执行系统命令，如获取当前连接的 WiFi SSID 和连接指定的 WiFi。
- `time`：用于暂停执行，等待操作完成。

这些库可以通过以下命令安装：

```bash
pip install requests selenium
```

# 实现步骤

## Step 1: 用户名和密码变量

```python
username = "校园网账号"
password = "校园网密码"
chrome_driver_path = r'C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe'
```

将 `auto_login.py` 中的以上变量替换为实际情况。
`chromedriver.exe`提供了最新版本，如果不符合当前环境要求，可自行官网下载适合版本。

## Step 2: 批处理文件

右键编辑或自行用记事本创建 `auto_login.bat` 的批处理文件，并将以下内容粘贴进去：

```batch
@echo off
"E:\Anaconda\envs\opencv_env\python.exe" ""E:\Auto_login\auto_login.py""
pause
```

1. 将以上变量替换成实际情况， `E:\Anaconda\envs\opencv_env\python.exe` 为python环境路径，`E:\Auto_login\auto_login.py`为py文件路径。
2. 保持电脑WiFi开关为开，运行bat文件即可自动登录校园网。

## Step 3: 将批处理文件添加到启动项（可选）

1. 打开“启动”文件夹：
    - 按下 `Win + R` 键打开“运行”对话框。
    - 输入 `shell:startup` 并按下回车键。这将打开“启动”文件夹。

2. 将 `auto_login.bat` 文件复制到“启动”文件夹：
    - 任何放在这个文件夹中的程序或脚本都会在系统启动时自动运行。
