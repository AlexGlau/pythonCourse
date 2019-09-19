age = input('Enter your age: ')

def define_age(age):
    age = int(age)

    if 3 <= age < 7:
        return 'Kindergarten'
    elif 7 <= age <= 18:
        return 'School'
    elif 18 < age <= 23:
        return 'College'
    else:
        return 'Some job'

res = define_age(age)
print(res)
