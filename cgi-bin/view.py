#!C:\Users\vanilla\AppData\Local\Programs\Python\Python38\python.exe

print('Content-type: text/html\n')

import cgi
import pymysql
import sys

conn = pymysql.connect(host='149.129.121.250', user='test', passwd='inkzyq', db='bulletin', port=3306, charset='utf8mb4')
curs = conn.cursor()

form = cgi.FieldStorage()
id = form.getvalue('id')

print("""
<html>
    <head>
        <meta charset='UTF-8'>
        <title>View Message</title>
    </head>
    <body>
        <h1 align='center'>---查看公告---</h1>
""")

try:
    id = int(id)
except:
    print('Invalid message ID')
    sys.exit()

#-----
curs.execute('select * from messages where id=%i' % id)
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]

if not rows:
    print('Unknown message ID')
    sys.exit()

row = rows[0]

print("""
        <p><b>标题：</b>%s<br />
        <b>发信人：</b>%s<br />
        <b>内容：</b>%s
        </p>
        <hr />
        <a href='main.py'>返回主页</a>
        | <a href="edit.py?reply_to=%s">回复</a>
    </body>
</html>
""" % (row['subject'], row['sender'], row['text'], row['id']))
