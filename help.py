# Створення змінних john та marta
john = {
    "full_name": "John Smith",
    "age": 35,
    "salary": 50000,
    "gender": "male",
    "coordinates": (40.7128, -74.0060),
    "friends": []
}

marta = {
    "full_name": "Marta Johnson",
    "age": 28,
    "salary": 45000,
    "gender": "female",
    "coordinates": (51.5074, -0.1278),
    "friends": []
}

# Створення друзів для John та Marta
johns_friend = {
    "full_name": "Jane Smith",
    "age": 32,
    "salary": 55000,
    "gender": "female",
    "coordinates": (40.7128, -74.0060),
    "friends": []
}

johns_second_friend = {
    "full_name": "Bob Johnson",
    "age": 40,
    "salary": 60000,
    "gender": "male",
    "coordinates": (40.7128, -74.0060),
    "friends": []
}

martas_friend = {
    "full_name": "John Doe",
    "age": 30,
    "salary": 40000,
    "gender": "male",
    "coordinates": (51.5074, -0.1278),
    "friends": []
}

martas_second_friend = {
    "full_name": "Jane Doe",
    "age": 25,
    "salary": 35000,
    "gender": "female",
    "coordinates": (51.5074, -0.1278),
    "friends": []
}

# Додавання друзів до списків друзів John та Marta
john["friends"].append(johns_friend)
john["friends"].append(johns_second_friend)

marta["friends"].append(martas_friend)
marta["friends"].append(martas_second_friend)

# Виведення полів John та Marta на консоль
print("John's fields:")
for key, value in john.items():
    print(f"{key}: {value}")
print()

print("Marta's fields:")
for key, value in marta.items():
    print(f"{key}: {value}")
