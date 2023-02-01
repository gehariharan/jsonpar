#python code to parse and use json

import json
data = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
print(data['two']) # or `print data['two']` in Python 2
