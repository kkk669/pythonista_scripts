# coding: utf-8
import hashlib
import clipboard
import appex

source = appex.get_text()
if source == None:
	source = clipboard.get()

print('MD5:')
print(hashlib.md5(source).hexdigest())

print('SHA256:')
print(hashlib.sha256(source).hexdigest())