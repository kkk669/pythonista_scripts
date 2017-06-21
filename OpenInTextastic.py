# coding: utf-8

import appex
from objc_util import *
from urlparse import urlsplit

def main():
	if not appex.is_running_extension():
		print 'This script is intended to be run from the sharing extension.'
		return
	
	app=UIApplication.sharedApplication()
	text = appex.get_text()
	url = appex.get_url()
	
	if text:
		openurl = nsurl('textastic://x-callback-url/new?name=foo.txt&text=' + text)
	
	if url:
		url = urlsplit(url)
		openurl = nsurl('textastic://' + url.netloc + url.path + url.query + url.fragment)
	
	if not openurl:
		print 'No input URL or text found.'
		return
	
	print openurl
	app.openURL_(openurl)
	appex.finish()
	
if __name__ == '__main__':
	main()