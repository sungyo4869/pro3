import sys
import io
import random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

dice = random.randint(1, 6)

print('Content-type: text/html; charset=UTF-8\r\n')
print("<head>")
print('<meta http-equiv="Content-type" content ="text/html; charset=UTF-8">')
print("<title>サイコロ</title>")
print("</head>")
print("<body>")
print("<p>サイコロの目は%dでした</p>"% dice)
print("</body>")
print("</html>")