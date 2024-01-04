import sys, io, cgi

teihen, takasa = 0,0

form = cgi.FieldStorage()

if 'teihen' in form:
    teihen = int(form['teihen'].value)
if 'takasa' in form:
    takasa = int(form['takasa'].value)
    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print('Content-type: text/html; charset=UTF-8\n\n')
print("<html>")
print("<head>")
print('<meta http-equiv="Content-type" content="text/html; charset=UTF-8">')
print("<title>名前</title></head><body>\n")
print("<p>底辺 = %d</p>" % teihen)
print("<p>高さ = %d</p>" % takasa)
print("<p>面積 = %d * %d / 2 = %d</p>" % (teihen, takasa, teihen*takasa/2))
print("</body></html>")