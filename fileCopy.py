#!/usr/bin/python
#encoding: utf-8

import os
import shutil

def showDir(path):
	print "==========================="
	for dirpath,dirnames,filenames in os.walk(path):
		for dirname in dirnames:
			print os.path.join(dirpath, dirname)

if __name__ == "__main__":
	filepath = "/Users/shirakura/Programs/python"

	testDir = filepath + "/dir01"

	if os.path.exists(testDir):
		print testDir + u"はすでに存在しています"
	else:
		os.mkdir(testDir)
	
	testDir2 = testDir + "/dir02/dir03"

	if os.path.exists(testDir2):
		print testDir2 + u"はすでに存在しています"
	else:
		os.makedirs(testDir2)
	
	showDir(testDir)
	showDir(testDir2)

	os.rmdir(testDir2)
	shutil.rmtree(testDir)

	shutil.copy(filepath + "/test.txt", filepath + "test2.txt")

