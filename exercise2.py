family = {}
names = []
ages = []
family_members_number = int(input("enter your family members number: "))

for i in range(family_members_number):
    user_names = input("enter the member name: ")
    user_ages = int(input("enter its age: "))

    names.append(user_names)
    ages.append(user_ages)
print(names)
print(ages)

family = dict(zip(names, ages))
print(family)

for key, value in family.items():
    if value < 3:
        print(f"for {key} the ticket if free")

    elif 3 < value < 12:
        print(f"for {key} the ticket costs $10")

    elif value > 12:
        print(f"for {key} the ticket is for $15")

