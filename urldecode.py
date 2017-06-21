# coding: utf-8
import urllib2
import clipboard
import appex

source = appex.get_url()
if source == None:
	source = appex.get_text()
	if source == None:
		source = clipboard.get()

decoded = urllib2.unquote(source).encode('raw_unicode_escape').decode('utf-8')
print(decoded)