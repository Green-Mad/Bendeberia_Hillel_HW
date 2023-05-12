non_unik_name = ['John', 'Marta', 'Alex', 'John', 'Sarah', 'Alex', 'Kate', 'Marta']
unique_names_dict = {}
for key in non_unik_name:
    unique_names_dict[key] = None
unique_names = list(unique_names_dict.keys())
print(unique_names)
