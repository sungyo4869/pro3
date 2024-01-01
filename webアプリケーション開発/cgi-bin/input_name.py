import sys, io, cgi
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

if 'namae' in form:
    name = form['namae'].value

else:
    name = "名無し"
    
print('Content-type: text/html; charset=UTF-8\n\n')
print("<html>")
print("<head>")
print('<meta http-equiv="Content-type" content="text/html; charset=UTF-8">')
print("<title>名前</title>")
print("</head>")
print("<body>\n")
print("%sさんようこそ"%name)
print("</body></html>")