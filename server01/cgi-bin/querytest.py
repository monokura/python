#! /usr/bin/env python

html_body = """
<!DOCTYPE html>
<html lang="ja">
<head>
	<meta charset="UTF-8">
	<title></title>
</head>
<body>
	foo = %s
</body>
</html>"""

import cgi
form=cgi.FieldStorage()
print "Content-type: text/html\n"
print html_body % form.getvalue('foo', 'N/A')
