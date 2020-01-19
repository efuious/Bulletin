#!C:\Users\vanilla\AppData\Local\Programs\Python\Python38\python.exe

print('Content-type: text/html\n')

import pymysql

conn = pymysql.connect(host='149.129.121.250', user='test', passwd='inkzyq', db='bulletin', port=3306, charset='utf8mb4')
curs = conn.cursor()

print("""
<html>
    <head>
        <meta charset='UTF-8'>
        <title>The FooBar Bulletin Board</title>
    </head>
    <body>
        <h1 align='center'>---公告板---</h1>
        <hr />
""")

#do mysql cmd
curs.execute('select * from messages')

names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]
toplevel = []
children = {}

for row in rows:
    parent_id = row['reply_to']  # 获取reply_to的的值
    if parent_id is None:  # 如果reply_to为空，那么就是toplevel
        toplevel.append(row)
    else:  # 如果reply_to不为空，则添加到子列表中
        children.setdefault(parent_id, []).append(row)


def format(row):
    print('<p><a href="view.py?id=%i">%s</a></p>' % (row['id'], row['subject']))
    try:
        kids = children[row['id']]
    except KeyError:
        pass
    else:
        print('<blockquote>')
        for kid in kids:
            format(kid)
        print('</blockquote>')


print('<p>')

for row in toplevel:
    format(row)

print("""
        </p>
        <hr />
        <p><a href="edit.py">发布公告</a></p>
    </body>
</html>
""")
