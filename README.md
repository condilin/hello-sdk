# hello-sdk

- 生成sdk
- 创建纯 Python 或者平台 Wheels 的命令是：python setup.py bdist_wheel
- 创建源发布文件.tar.gz命令是：python setup.py sdist

## 安装和使用SDK

### 安装
执行上面命令后，会生成build、condihello.egg-info 、dist三个目录，在dist目录下就有xxx.whl文件
```python
pip install xxx.whl
```

### 使用
```python
import CondiHello
CondiHello.hello()
```



