import json
filename="testdict.json"
sample= dict(name='fred', age=31, grades=[1,34,55])

with open(filename, 'wt') as f:
    json.dump(sample,f)