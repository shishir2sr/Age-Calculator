print('----------- AGE CALCULATOR ---------------')
print('BIRTHDATE: ')
bd = int(input('Enter your birthdate(eg, 01): '))
bm = int(input('Enter your birthh month(eg, 01): '))
by = int(input('Enter your birth year(eg,1995 )  : '))
print()
print('PRESENT DATE:')
pd = int(input('Present Date:'))
pm = int(input('Enter Present Month: '))
py = int(input('Enter present Year: '))

if (bd>30 or pd>30) or (bm>12 or pm>12) or (by>py) or (bd or pd)<0 or (bm<0 or pm<0 or py<0 or by<0):
    print()
    print('Invalid entry!!')
    exit()

age = py - by
month = pm - bm
day = pd - bd

if day<0:
    day += 30
    month -= 1

if month<0:
    month += 12
    age -= 1

print()
print('You are aproximately,', age, 'years,', month, 'months and', day, 'days old')
