def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])  # 响应西悉尼
    file_name = environ['PATH_INFO'][1:] or 'index.html'  # 读取url参数
    HTML_ROOT_DIR = './'  # 设置html文件目录

    try:
        print("================================")
        print(HTML_ROOT_DIR + file_name)
        print("================================")
        file = open(HTML_ROOT_DIR + file_name, 'rb')  # 打开文件
    except IOError:
        response = 'The file is not found!'  # 如果异常返回404
    else:
        file_data = file.read()  # 读取文件内容
        file.close()  # 关闭文件
        response = file_data.decode("utf-8")  # 构造响应数据
        print("==========================================")
        print(response)
        print("==========================================")

    return [response.encode('utf-8')]  # 返回数据
