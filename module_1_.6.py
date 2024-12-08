my_dict = {'Vera': 1988, 'Petya': 1990, 'Fedor': 1995}
print(my_dict)
print(my_dict.get('Fedor'))
print(my_dict.get('Sveta'))
my_dict.update({'Kostya': 1992,'Nastya': 2000})
del my_dict['Fedor']
print(my_dict)


my_set = {1,2,3, None, 'Vasya', 1, 1, 1, 2, 'Cat', 'Cat'}
print(my_set)
my_set.update([(1, 5, 4.15), 6])
my_set.discard(None)
print(my_set)