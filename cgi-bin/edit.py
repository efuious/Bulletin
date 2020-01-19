#!C:\Users\vanilla\AppData\Local\Programs\Python\Python38\python.exe

print('Content-type: text/html\n')

import cgi
import pymysql

conn = pymysql.connect(host='149.129.121.250', user='test', passwd='inkzyq', db='bulletin', port=3306, charset='utf8mb4')
curs = conn.cursor()

form = cgi.FieldStorage()
reply_to = form.getvalue('reply_to')

print("""
<html>
    <head>
        <meta charset='UTF-8'>
        <title>Compose Message</title>
    </head>
    <body>
        <h1 align='center'>---编辑消息---</h1>
        <form action='save.py' method='POST'>
""")

subject = ''
if reply_to is not None:
    print('<input type="hidden" name="reply_to" value="%s" />' % reply_to)
    curs.execute('select subject from messages where id = %s' % reply_to)
    subject = curs.fetchone()[0]
    if not subject.startswith('Re: '):
        subject = 'Re: ' + subject

print("""
    <b>标题:</b><br />
    <input type='text' size='40' name='subject' value='%s' /><br />
    <b>发信人:</b><br />
    <input type='text' size='40' name='sender' /><br />
    <b>内容:</b><br />
    <textarea name='text' cols='40' rows='20'></textarea><br />
    <input type='submit' value='保存'>
    </form>
    <hr />
    <a href='main.py'>返回主页</a>
    </body>
</html>""" % subject)
