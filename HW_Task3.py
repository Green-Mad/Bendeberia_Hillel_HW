friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]
for friend in friends:
    if friend == 'James':
        print(f"{friend} is my best friend")
    elif friend in enemies:
        print(f"{friend} we are not friends anymore")
    else:
        print(f"{friend} we are the best friends")
