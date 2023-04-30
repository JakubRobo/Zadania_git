zdanie = input('Podaj jakieś zdanie: ')

y = zdanie.split()
for i in reversed(y):
    print(i)