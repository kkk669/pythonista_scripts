# coding: utf-8
import uuid
import clipboard

id = uuid.uuid4()
print(id)
clipboard.set(str(id))