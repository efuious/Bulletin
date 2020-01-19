#!C:\Users\vanilla\AppData\Local\Programs\Python\Python38\python.exe

print('Content-type: text/html\n')

import cgi
import pymysql
import sys


def quote(string):
    if string:
        return string.replace("'", "\\'")
    else:
        return string


conn = pymysql.connect(host='149.129.121.250', user='test', passwd='inkzyq', db='bulletin', port=3306, charset='utf8mb4')
curs = conn.cursor()

form = cgi.FieldStorage()
sender = quote(form.getvalue('sender'))
subject = quote(form.getvalue('subject'))
text = quote(form.getvalue('text'))
reply_to = form.getvalue('reply_to')

if not (sender and subject and text):
    print('Please supply sender, subject, and text')
    sys.exit()

if reply_to is not None:
    query = """
    insert into messages values(null, \'%s\', \'%s\', %i, \'%s\')
    """ % (subject, sender, int(reply_to), text)
elif reply_to is None:
	query = """
    insert into messages values(null, \'%s\', \'%s\', null, \'%s\')
    """ % (subject, sender, text)
else:
    sys.exit()

#print(query)

curs.execute(query)
conn.commit()

print("""
<html>
    <head>
        #<meta charset='UTF-8'>
        <title>Message Saved</title>
    </head>
        <h1>发送成功</h1>
        <hr />
        <a href='main.py'>返回主页</a>
    </body>
</html>""")
