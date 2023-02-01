#Parse and use json in python 3.x
import json
data = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
print(data['two']) # or `print data['two']` in Python 2 



#From JSON file
f = open('data.json',)
data = json.load(f)
for i in data['two']:
    print(i)
f.close() # Write JSON string to file
data = {
'employees' : [
    {
        'name' : 'John Doe',
        'department' : 'Marketing',
        'place' : 'Remote'
    },
    {
        'name' : 'Jane Doe',
        'department' : 'Software Engineering',
        'place' : 'Remote'
    }
]
} json_string = json.dumps(data)
# Using a JSON string
with open('json_data.json', 'w') as outfile:
    outfile.write(json_string)
