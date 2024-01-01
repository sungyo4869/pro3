import sys
import io

from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print('Content-type: text/html; charset=UTF-8\r\n')
print("<head>")
print('<meta http-equiv="Content-type" content ="text/html; charset=UTF-8">')
print("<title>現在の時刻</title>")
print("</head>")
print("<body>")
print("<p>現在時刻 : %s</p>"%datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
print("</body>")
print("</html>")