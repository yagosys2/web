import json

data = {}
data['name'] ='andy'
data['age'] = '80'

with open('data.txt','w') as file:
    json.dump(data,file)

with open('data.txt','r') as file:
    data = json.load(file)

print(data)
print(type(data))

data = json.dumps(data)


print(data)
print(type(data))

data = json.loads(data)
print(data)
print(type(data))

