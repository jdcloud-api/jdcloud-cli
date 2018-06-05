# 京东云CLI
京东云CLI提供使用命令行的方式访问您的云中资源。

## 安装须知
京东云CLI基于Python语言和京东云Python SDK开发，使用CLI前请安装Python 2.7版本和pip包管理工具。请访问官网下载并安装Python2.7和pip。

### Python2.7和pip安装
通过官网安装：
- Python：https://www.python.org/downloads
- pip：https://pip.pypa.io/

使用各发行版包管理工具安装pip，请参考：

https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers

### 京东云Python SDK依赖说明
京东云Python SDK不用手动安装，Python包管理工具会自动下载并安装对应版本的依赖包。如果您已经安装了京东云Python SDK，并且因为CLI版本与之不对应而不能正常工作，请参考下面的版本对应表，安装对应版本SDK或删除旧的Python SDK并重新安装CLI。

|发布日期|京东云CLI|京东云Python SDK|
|---|---|---|
|2018.06.04|0.1.0|1.1.1|


## 安装方法：
### Linux && Mac
pip安装：
`pip install jdcloud_cli`

源码安装：
`python setup.py install`

安装后执行以下脚本，打开自动完成功能：
```
echo 'eval "$(register-python-argcomplete jdc)"' >> .bashrc
echo 'export COLUMNS=100' >> .bashrc
source ~/.bashrc
```


### Windows
开发验证中。
