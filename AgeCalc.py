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

age = py-by
month = pm-bm
day = pd-bd


if month<0:
    month+=12
    age-=1
if day<0:
    day+=30
    month-=1

print()
print('You are aproximately,',age,'years,',month,'months and',day,'days old')