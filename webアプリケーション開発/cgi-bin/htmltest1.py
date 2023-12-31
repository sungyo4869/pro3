import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print('Content-type: text/html; charset=UTF-8\r\n')
print("<head>")
print('<meta http-equiv="Content-type" content ="text/html; charset=UTF-8">')
print("<title>テスト DGI</title>")
print("</head>")
print("<body>")
print("<h1>Hello CGI world!</h1>")
print("<h2>日本語の表示はうまくいくかな？</h2>")
print("</body>")
print("</html>")