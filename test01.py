#!/usr/bin/python
# -*- coding: UTF-8 -*-

print u"モジュールのロード"

def test(hoge):
	print hoge;
	print u"を呼び出しました"

if __name__ == "__main__":

	print u"test01"
	test(u"hoge")
