#

if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}:
    print(1)
    print(2)
    if 'x' in 'qux':
        print(3)
print(4)

a = 100
b = 50

if a < b:
    print(f"{a} is less than {b}")
    m = a
    print(m)
else:
    print(f"{b} is less than {a}")
    m = b
    print(m)

# The following if/elif/else statement will raise a KeyError exception:

d = {'a': 0, 'b': 1, 'c': 0}

if d[ 'a' ] > 0:
    print('ok')
elif d[ 'b' ] > 0:
    print('ok')

print('a' + 'x' if '123'.isdigit() else 'y' + 'b')

gotsweets=False

if gotsweets == True:
    print(":(")

print('This is the system admin with 4 + years experience in cloud and linux other '
      'than the devops and windows also having the experience')
