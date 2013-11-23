#! /usr/bin/env python
# coding: utf-8

import cgi
from datetime import datetime

html_body = u"""
<!DOCTYPE html>
<html lang="ja">
<head>
	<meta  http-equiv="content-type" content="text/html;charset="UTF-8">
	<title></title>
</head>
<body>
	%s
</body>
</html>
"""
content=''

form=cgi.fieldStorage()
year_str=form.getvalue('year', '')
if not year_str.isdigit() :
	content=u"西暦を入力してください"
else:
	year=int(year_str)
	friday13==0
	for omonth in range(1, 13):
		date=datetime(year, month, 13)
		if date.weekday()==4:
			friday13+=1
			content+=u"%d年%d月13日は金曜日です" % (year, date.month)
			content+=u"<br />"
		if friday13:
