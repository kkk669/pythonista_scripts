# coding: utf-8
import base64
import clipboard
import appex

source = appex.get_text()
if source == None:
	source = clipboard.get()

encoded = base64.b64encode(source)
print(encoded)
clipboard.set(encoded)