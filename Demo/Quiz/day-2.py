# Fibonacci series in python
# The sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# ####### Sample if statement ##############

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# ######### sample for condition #########

users = ['jack', 'Jim', 'john', 'Ajay']

for i in users:
    print(i, len(i))

user_list = {'Jack': 'Inactive', 'Jim': 'Active', 'John': 'Active', 'Ajay': 'Inactive'}

for user, status in user_list.copy().items():
    if status == 'Inactive':
        del user_list[user]
print(user_list)

# Create new item

activate_user = {}

for user, status in user_list.items():
    if status == 'Active':
        activate_user[user] = status
