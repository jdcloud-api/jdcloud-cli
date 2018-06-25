# 京东云CLI
京东云CLI提供使用命令行的方式访问您的云中资源。

## 安装须知
京东云CLI基于Python语言和京东云Python SDK开发，使用CLI前请安装Python 2.7版本和pip包管理工具。请访问官网下载并安装Python2.7和pip。

### Python2.7安装
#### 官网下载安装：
  https://www.python.org/downloads
#### 操作系统包管理工具安装
- CentOS
  `yum install python`
- Ubuntu
  `apt-get install python2.7`
- macOS
  `brew install python@2`

### pip安装
- 官网安装请参考：https://pip.pypa.io/

  具体命令为
  ```
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py
  ```

- 使用各发行版包管理工具安装pip，请参考[安装方法](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)

### 京东云Python SDK依赖说明
京东云Python SDK不用手动安装，Python包管理工具会自动下载并安装对应版本的依赖包。如果您已经安装了京东云Python SDK，并且因为CLI版本与之不对应而不能正常工作，请参考下面的版本对应表，安装对应版本SDK或删除旧的Python SDK并重新安装CLI。

|发布日期|京东云CLI|京东云Python SDK|
|---|---|---|
|2018.06.04|0.1.0|1.1.1|
|2018.06.23|0.2.0|1.1.1|
|2018.06.25|0.2.1|1.1.2|


## CLI安装方法：
### Linux & Mac
pip安装：
`pip install -U jdcloud_cli`

源码安装（不依赖pip）：
`python setup.py install`

安装后执行以下脚本，打开自动完成功能：
```
echo 'eval "$(register-python-argcomplete jdc)"' >> .bashrc
echo 'export COLUMNS=100' >> .bashrc
source ~/.bashrc
```


### Windows
京东云CLI在Windows上运行依赖Git 2.9.0以上版本，建议使用最新版本。

下载地址为：https://git-scm.com/download/win
  
请注意：安装时模拟终端选项要选择“Use MinTTY (the default terminal of MSYS2)”。

pip安装：
`pip install jdcloud_cli`

源码安装（不依赖pip）：
`python setup.py install`

安装后在git bash中执行以下脚本，打开自动完成功能：
```
curl https://raw.githubusercontent.com/jdcloud-api/jdcloud-cli/master/jdcloud_cli/resources/jdc.rc > ~/jdc.rc
echo 'source ~/jdc.rc' >> ~/.bashrc
echo 'export PYTHONIOENCODING="UTF-8"' >> ~/.bashrc
source ~/.bashrc
```

## CLI使用方法
### 配置鉴权信息
jdc configure add --access-key your-ak --secret-key your-sk

说明：access-key和secret-key可以从京东云控制台申请开通。默认为华北区域。

### 执行产品命令
jdc [options] command sub-command [--parameters values]

例如：
jdc vm describe-instances

目前支持Linux、Mac、Windows三种平台的Bash中的自动完成功能，输入两次tab键，可提示辅助信息。

创建资源时，json串的获取可以使用各产品线子命令下的 generate-skeleton 获取，如：
           
`jdc vm generate-skeleton --api create-instances`

更多帮助信息及OpenAPI官方文档，请见：
https://www.jdcloud.com/help/faq?act=3

## 已知问题
Windows平台中，容器交互命令为exprimental阶段。在命令前需要增加winpty前缀，如：

`winpty jdc nc attach --container-id c-abcdefg`

建议使用Linux 或 Mac平台。
