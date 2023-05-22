'''there is a string " name=Amanda=sssss&age=32&&salary=1500&currency=euro ". Convert this string to a dictionary {name:
 Amanda, age: 32, salary: 1500, currency: euro}'''

import re

string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
updated_string = re.sub(r"=sssss", "", string)
pairs = updated_string.split("&")
result = {}

for pair in pairs:
    if "=" in pair:
        key, value = pair.split("=", maxsplit=1)
        if value:
            value = value.replace("=", "")
            result[key] = value

print(result)
