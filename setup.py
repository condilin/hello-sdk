from setuptools import setup, find_packages

"""
从setuptools中导入setup和findpackages，各参数的含义如下：
name:               包的名字
version:            版本号，对保持适当的依赖关系很重要
packages:           需要包含的子包列表，用find_packages()查找
url：               包的链接，通常为 Github 上的链接，或者是 readthedocs 链接
long_description：  将说明文件设置为README.md
"""

setup(
    name="condihello",
    version="1.0",
    url='https://github.com/jinimp/hello-sdk.git',
    long_description=open('README.md', encoding='utf-8').read(),
    packages=find_packages(),
)
