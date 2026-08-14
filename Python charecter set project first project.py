print(' SASHANG PYTHON ' )

str1='PYTHON'
str2='IS'
str3='GOOD'
str4=str1+" "+str2+" "+str3
print(str4)


#Level 1: Arithmetic Operators

a=25
b=5

print('Addition',a + b)

print('\nmultplication',a * b)

print('\nsubtraction',a - b)

print('\ndivision',a / b)

print('\nmodule',a % b)

print('\nfloor division',a // b)

print('\nexponent',a ** b)

#area of rectangle and perimeter of rectanglr

l=15
b=8

print('\nArea Of Rectangle',l*b)
print('\nperimeter of rectangle',2*(l+b))

#diameter,circum,area

r=7

print('\nDiameter',2*r)
print('\nCircumfrence',2*3.14*r*r)
print('\nArea',3.14*r*r)

#A student scored

m=80
s=75
e=90
print('\nTOTAL',m+s+e)
print('\nAVERAGE',m+s+e/3)

#Level 2: Assignment Operators
#these would help to continue calculation in a loop one by one

print('\n')
x=20
print('\nInitial Value:', x)
x += 10
print('\nafter +=10:',x)
x -= 5
print('\nafter -=5:',x)
x *= 2
print('\nafter *=2:',x)
x /= 5
print('\nafter /=5:',x)
x %= 3
print('\nafter %=3:',x)
x //= 2
print('\nafter //=2:',x)
x **= 3
print('\nafter **=3:',x)

#salary

salary=25000
salary += 2500
print('\nsalary 10% inc:',salary)

#bank balance

balance=5000
print('\nInitial balance:',balance)
balance += 2000
print('\nAddDeposite:',balance)
balance -= 1500
print('\nwithdraw:',balance)

#Level 3: Comparison Operators
#this would help to find true or fall

print('\n')
y=12
z=18
print('\ny==z?',y==z)
print('\ny!=z?',y!=z)
print('\ny>z?',y>z)
print('\ny<z?',y<z)
print('\ny>=z?',y==z)
print('\ny<=z?',y<=z)

print('\n' '\a''\t' 'COMPARISON B/W AGE1=21 and AGE2=18')
age1=21
age2=18
print('\nage1==age2?', '\n',age1==age2)
print('\nage1!=age2?', '\n',age1!=age2)
print('\nage1>age2?', '\n',age1>age2)
print('\nage1<age2?', '\n',age1<age2)
print('\nage1>=age2?', '\n',age1==age2)
print('\nage1<=age2?', '\n',age1<=age2)

print('\n''\t''\a''Compare two marks')
std1=87
std2=92
print('\nis std1 = std2?', '\n','\n', std1==std2)
print('\nis std1 > std2?', '\n','\n', std1>std2)
print('\nis std1 < std2?', '\n','\n', std1<std2)

#Level 4: Logical Operators

print('\n''\t''\a''logical operators true or false')
age=22
salary=35000
print('\n guess true or false for job','\n','\n', age>18 and salary>30000)

mark=45
attend=90
print('\n guess true or false for mark','\n','\n', mark>=50 and attend>=85)

temp=40
print('\n guess true or false for temperature','\n','\n', not(temp<35))

#Level 5: Bitwise Operators

print('\n''\t''\a''Bitwise Operators 1 or 0?')
bit1=9
bit2=5
print('\n bit1 & bit2','\n','\n', bit1 & bit2)
print('\n bit1 | bit2','\n','\n', bit1 | bit2)
print('\n bit1 ^ bit2','\n','\n', bit1 ^ bit2)
print('\n bit1 ~ bit2','\n','\n', bit1 - bit2)
print('\n bit1 << bit2','\n','\n', bit1 << bit2)
print('\n bit1 >> bit2','\n','\n', bit1 >> bit2)

bit3=12
print('\n bit3 << 2','\n','\n', bit3 << 2)
print('\n bit3 >>2','\n','\n', bit3 >>2)

#Level 6: Membership Operators

print('\n''\t''\a''Membership Operators in colors')
colors = ["Red", "Blue", "Green"]
print('\n',"Blue" in colors)
print('\n',"Black" in colors)
print('\n',"Black"not in colors)

print('\n''\t''\a''Membership Operators in words')
word = "Engineering"
print('\n',"E" in word)
print('\n',"z" in word)
print('\n',"g" in word)


#Level 7: Identity Operators
print('\n''\t''\a''Identify Operators')
id1=[1,2,3]
id2=id1
print('\n','id1 is id2',id1 is id2)
print('\n','id1 is not id2', id1 is not id2)

ind3=[5,10]
ind4=[5,10]
print('\n','ind3==ind4', ind3==ind4)
print('\n','ind3 is ind4', ind3 is ind4)

p='python'
q=p
print('\n','p is q',p is q)
print('\n','p==q',p==q)

#mixed problems

print('\n''1st sum')

print('\n''\n''\n''\n''\t''\a''MIXED PROBLEMS FOR WORKING')
r=18
s=7
print('\n','SUM','\n',r + s)
print('\n','DIFFERENCE','\n',r - s)
print('\n','PRODUCT','\n',r * s)
print('\n','DIVISION','\n',r / s)
print('\n','COMPARE>','\n',r > s)
print('\n','COMPARE ==','\n',r == s)

print('\n''2nd sum')

year=25
country='india'
print('\n','check : age > 18 and country == India','\n',year>18 and country =='india')

print('\n''3rd sum')

fruits = ['apple','orange','banana']
print('\n','apple is there or not','\n', 'apple' in fruits)
print('\n','mango is there or not','\n', 'mango' not in fruits)

print('\n''4th sum')

u=8
print('\nINITIAL U VALUE','\n', u)
u += 5
print('\nADDED 5 WITH U','\n', u)
u *= 3
print('\nMULTIPLY 3 WITH NEW U','\n', u)
u -= 4
print('\nSUBTRACT NEW U WITH 4','\n', u)
u //= 2
print('\nFINAL VALUE OF U','\n', u)

print('\n''5th sum')

name = 'sashang'
age1 = 24
mark = 92
subjects = ["python","java","c"]
print('\nAGE > 18','\n', age1>18)
print('\nMARKS >= 90','\n', mark>=90)
print('\nPYTHON IS THERE?','\n',"python" in subjects)
print('\nC++ IS NOT THERE?','\n',"c++"not in subjects)
print('\nNAME ==?','\n',name == 'sashang')
print('\nMARK %2?', '\n',mark % 2)
print('\nMARK // 10','\n',mark // 10)
print('\nMARK **2','\n',mark ** 2)





















