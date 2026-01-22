import json
d={
    "id":"2031",
    "name":"raj",
}
print("type of d is",type(d))

print("now convert into json")
obj=json.dumps(d,indent=4)
print("json file is ready",type(obj))
print(obj)