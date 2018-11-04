# 从wsgiref模块导入
from wsgiref.simple_server import make_server
# 导入编写得application函数
from chapter15.Views.application import app

# 创建一个服务器,IP地址为空,端口是8000,处理函数是app
httpd = make_server('', 8000, app)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求
httpd.serve_forever()
