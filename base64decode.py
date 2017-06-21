# coding: utf-8
import base64
import clipboard
import appex

source = appex.get_text()
if source == None:
	source = clipboard.get()

decoded = base64.b64decode(source)
print(decoded)
clipboard.set(decoded)