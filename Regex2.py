'''you have a list of variable names in camel case format ["FirstItem", "FriendsList", "MyTuple"] convert it to a list
of variable names for python in snake case format ["first_item", "friends_list", "my_tuple"]'''

import re

camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = [re.sub(r'([A-Z])', r'_\1', variable_name).lower()[1:] for variable_name in camel_case_list]

print(snake_case_list)
