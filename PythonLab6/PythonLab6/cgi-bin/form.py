import cgi

form = cgi.FieldStorage()
a = int(form.getfirst('a'))
b = int(form.getfirst('b'))

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

result = a + b

print('Content-type: text/html\n')
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Варіант 2</title>
        </head>
        <body>""")

print('<h1  align="center">Результат: {}</h1>'.format(result))
print('</body></html>')