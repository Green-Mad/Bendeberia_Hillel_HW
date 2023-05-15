#merger of companies
#Eleks_employees
#Toshiba_employees

eleks_employees = ['Freya', 'Jasmine', 'Mistress', 'Ariel', 'Kyrylo']
toshiba_employees = ['Zoreslav', 'Moses', 'Kyrylo', 'Lord', 'Marilouise']

toshiba_employees.extend(eleks_employees)
eleks_employees.clear()

print("Toshiba employees:", toshiba_employees)
print("Eleks employees:", eleks_employees)
