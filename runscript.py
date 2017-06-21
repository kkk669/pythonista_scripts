#coding: utf-8
import appex

inputFile = appex.get_file_path()
if inputFile != None:
	f = open(inputFile, 'r')
	script = f.read()
else:
	script = appex.get_text()
	if script == None:
		print('no script found')
		exit()

exec(script)