import sys, io, cgi
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

if 'simei' in form:
    name = form['simei'].value

if 'age' in form:
    age = form['age'].value

if 'gakka' in form:
    gakka = form['gakka'].value
    match gakka:
        case "ms":
            gakka = "機械システム工学科"
        case "ic":
            gakka = "情報通信システム工学科"
        case "mi":
            gakka = "メディア情報工学科"
        case "br":
            gakka = "生物資源工学科"
    
print('Content-type: text/html; charset=UTF-8\n\n')
print("<html>")
print("<head>")
print('<meta http-equiv="Content-type" content="text/html; charset=UTF-8">')
print("<title>プロフィール</title>")
print("</head>")
print("<body>\n")
print("<p>名前 : %s</p>"%name)
print("<p>年齢 : %s</p>"%age)
print("<p>学科 : %s</p>"%gakka)
print("</body></html>")