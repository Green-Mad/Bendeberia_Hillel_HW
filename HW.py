#task 1
john_salary = 666.13
marta_salary = 1488.01
print('john_salary is ' ,john_salary,'GBP')
print('marta_salary is ' ,marta_salary,'USD')
print('''Enda of task

''')

#task 2
john_age = 32
marta_age = 30
print('john_age is ' ,john_age)
print('marta_age is ' ,marta_age)
print('''Enda of task

''')

#task 3
john_name = 'Albert'
marta_name = 'Sakura'
print('john_name is ', john_name)
print('marta_name is ', marta_name)
print('''Enda of task

''')

#task 4
john_gender = False
marta_gender = True
print(john_gender)
print(marta_gender)
print('''Enda of task

''')

#task 5
john_friends = ['Table', 'Chair', 'Wall', 'Pillow']
marta_friends = ['Petro', 'Stepan', 'Vera', 'Khrystyna']
print('john_friends is', john_friends)
print('marta_friends is', marta_friends)
print('''Enda of task

''')

#task 6
john_and_marta_notfriends = {'Howard', 'Svyatoslav', 'Yaropolk', 'Dmytro', 'Howard'}
print(john_and_marta_notfriends)
print('''Enda of task

''')

#task 7
not_my_coordinates1 = (50.50412968962568, 30.529968804830524)
not_my_coordinates2 = (50.529968804830524, 30.50412968962568)
print(not_my_coordinates1)
print(not_my_coordinates2)
print('''Enda of task

''')

#task 8
john = {'full_name':john_name, 'age':john_age, 'salery':john_salary, 'gender':john_gender,
        'john_friends':[], 'coordinates':not_my_coordinates1}
marta = {'full_name':marta_name, 'age':marta_age, 'salery':marta_salary, 'gender':marta_gender,
         'marta_friends':[], 'coordinates':not_my_coordinates2}

johns_friend1 = {"full_name": "Belle", "age": 32, "salary": 5000, "gender": True,
                "coordinates": (40.7128, -74.0060), "friends": ['Lolik', 'Bolik']
}

johns_friend2 = {"full_name": "Tim Minchin", "age": 40, "salary": 60000, "gender": False,
                 "coordinates": (40.0060, -74.7128), "friends": ['Alpha', 'Omega']
}

martas_friend1 = {"full_name": "John Doe", "age": 30, "salary": 40000, "gender": False,
                 "coordinates": (51.1278, -0.5074), "friends": ['Sabina', 'Sabrina']
}

martas_friend2 = {"full_name": "John Weak", "age": 25, "salary": 35000, "gender": True,
                        "coordinates": (51.5074, -0.1278), "friends": ['George', 'Orwel']
}

john['john_friends'].append(johns_friend1)
john['john_friends'].append(johns_friend2)

marta['marta_friends'].append(martas_friend1)
marta['marta_friends'].append(martas_friend2)

for key, value in john.items():
    print(key, value)

for key,value in marta.items():
    print(key, value)

