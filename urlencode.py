# coding: utf-8
import urllib2
import clipboard
import appex

source = appex.get_text()
if source == None:
	source = clipboard.get()

encoded = urllib2.quote(source.encode('utf-8'))
print(encoded)