import sqlite3

# 连接到到Sqlite数据库
# 数据库文件是mrsoft.db 如果问及那不存在,会自动在当前目录创建
conn = sqlite3.connect('mrsoft.db')

# 创建一个cursor
cursor = conn.cursor();

# 执行一条sql语句,创建user表
cursor.execute('create table user (id int(10) primary key ,name varchar(20))')
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
