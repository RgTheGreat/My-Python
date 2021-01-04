import json

a = '{"brand":"Honda", "model":"city s", "color":"maroon"}'


# parsing the var a:
b = json.loads(a)

result = a["brand"]

print(result)
