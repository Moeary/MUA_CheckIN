# MUA签到脚本

## 项目描述

这是一个用于自动签到MUA网站的Python脚本。脚本使用Selenium和undetected-chromedriver来模拟浏览器操作，并通过GitHub Actions定时运行。

## 使用方法


### 使用GitHub Actions自动运行(推荐)

1. 获取COOKIE到Secrets
    首先通过F12抓取到在浏览器中抓取Cookie.
    使用电脑浏览器登入[MUA用户中心](https://skin.mualliance.ltd/user)后键盘按下F12
    
    ![](https://raw.githubusercontent.com/Moeary/pic_bed/main/img/202410150933709.png)
    
    然后按下Ctrl+R进行重新加载

    ![](https://raw.githubusercontent.com/Moeary/pic_bed/main/img/202410150934552.png)

    再点击user那一栏 往下翻找到Cookie 将里面的值全部Ctrl+C复制到剪切板(这边拦住了点 保护隐私要紧:P)

    ![](https://raw.githubusercontent.com/Moeary/pic_bed/main/img/202410150946824.png)

2. Fork本项目
    - 在[本项目](https://github.com/Moeary/MUA_CheckIN)右上角点击Fork 即可复制项目到你自己的仓库里面 方便后续配置
    - 进入你的GitHub仓库。
    - 点击右上角的 `Settings`。

    ![](https://raw.githubusercontent.com/Moeary/pic_bed/main/img/202410150939010.png)

    - 在左侧菜单中选择 `Secrets and variables` -> `Actions`。

    ![](https://raw.githubusercontent.com/Moeary/pic_bed/main/img/202410150939581.png)

    - 点击 `New repository secret`。

    ![](https://raw.githubusercontent.com/Moeary/pic_bed/main/img/202410150940085.png)

    - 添加一个新的Secret，名称必须为 `COOKIE`，值为你的完整cookie字符串。将刚才复制来的COOKIE全部粘贴过来(Ctrl+V)

    ![](https://raw.githubusercontent.com/Moeary/pic_bed/main/img/202410150942419.png)

    - 点击Add secret即可看到COOKIE添加成功

    ![](https://raw.githubusercontent.com/Moeary/pic_bed/main/img/202410150943470.png)


2. 等待明天GitHub Actions自动运行 每天8点(UTC+8)自动运行一次


### 本地运行(不推荐,我都跑脚本了 还真不如自己手动上线签到)

1. 克隆仓库：
    ```sh
    git clone https://github.com/yourusername/MUA_CheckIN.git
    cd MUA_CheckIN
    ```

2. 创建并激活虚拟环境（可选）：
    ```sh
    python -m venv venv
    source venv/bin/activate  # 对于Windows用户，使用 `venv\Scripts\activate`
    ```

3. 安装依赖项：
    ```sh
    python -m pip install --upgrade pip
    pip install setuptools
    pip install undetected-chromedriver selenium
    ```

4. 设置环境变量：
    ```sh
    export COOKIE="your_cookie_string"  # 对于Windows用户，使用 `set COOKIE=your_cookie_string`
    ```

5. 运行脚本：
    ```sh
    python mua.py
    ```