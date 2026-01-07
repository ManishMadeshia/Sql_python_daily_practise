'''

a = 5
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b) #division
print(a//b) #floor divisiom
print(a%b) #modulos oper


name = "maniosh"
age = 24
print(f"my name is {name} and age {age}")


a= b =c=  100
print(a,b,c)

x =5
x = 15
print(x)

p = 99.99
print(type(p))



print(20 / 4)
print(20 // 4)


num = 4
if num%2 ==0 :
    print("even")
else:
    print("odd")


print(True and False or True)


x = 5
x += 3  
x *= 5 
print(x)

#Check whether "i" exists in string "Manish".

a = [1,2,3]
b = a

x = 10
y = 20
print(not x > y)


n = input("enter a num: ")
print(n)
print(type(n))
a_int = int(n)
print(a_int)
print(type(a_int))

num1 = int(input("Enter a num: "))
num2 = int(input("enter a num2: "))
print(num1+num2) 

print(type(int(10.5)))

nu = "100"
num_int = int(nu)
print(num_int*5)


age = int(input("enter a age: "))
if age > 18 :
    print("adult")
else:
    print("minor")


age = int(input("Enter a age: "))


if age < 13 :
    print("child")
elif age > 13 and age < 19:
    print("teen")
else:
    print("20+")




marks = int(input("enter a marks"))

if marks >= 75 :
    print("Distinction")
elif marks > 40 and marks <= 74:
    print("pass")
else:
    print("fail")


num = int(input("enter a num: "))

if num%3 ==0 and num%5==0:
    print("divisible by 3 and 5")
elif num%3 ==0:
    print("divisible by 3")
elif num%5 == 0 :
    print("divisible by 5")
else:
    print("not divisible")



num1 = int(input("enter a num1: "))
num2 = int(input("enter a num2: "))
num3 = int(input("enter a num3: "))


if num1 > num2 and num1 > num3:
    print("num1 is greater")
elif num2 > num3 and num2 > num1:
    print("num2 is greater")
else:
    print("num3 is greater")



ch = input("enter a character: ").lower()
vowel = "aeiou"

if ch in vowel:
    print("vowel")
else:
    print("Constant")




user = "Manish"
passs = "pass@1234"

username = input("Enter a username: ")
password= input("Enter a password: ")

if user == username and passs == password:
    print("Login Successful")
else:
    print("Invalid credentials")


i = 10
while i> 0:
     print(i)
     i = i-1

for i in range(2,21,2):
    print(i)


sum = 0
for i in range(1,8):
    sum = sum+i
print(sum)



num = int(input("enter a num: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")



digit  = int(input("Enter a num: "))

if digit < 9:
    print("single digit")
elif digit > 9 and digit < 99:
    print("two digit")
else:
    print("third digit")


for i in range(1,20):
    if i%3 != 0:
        print(i)


count = 0
for i in range(1,101): 
        if i%3==0 :
             count = count +1
print(count)

n = 1

while n <= 10:
     print(n)
     n = n+1


for i in range(1,11):
    if i == 7:
         break
    print(i)

for i in range(1,11):
     if i == 5 or i == 8 or i == 10:
          continue
     print(i)


for i in range(1,21):
     if i%4 == 0 or i%6 == 0:
          continue
     print(i)

for i in range(1, 5):          # rows
    for j in range(1, i + 1):  # columns
        print(j, end="")
    print()



for i in range(1, 5):          # rows
    for j in range(1, i + 1):  # columns
        print(j, end="")
    print()

# list
number = [1,2,3,4]
print(number)
number[0] = 33
print(number)
n = [1,2.2,3.3,'manish', True]
print(n)
print(n[3])
n[3]= 90
print(n)

n.append(333) #add
n.insert(1,22) #insert at index
n.remove(1)
n.pop()
n.reverse()
print(len(n))


for i in n:
     print(i)

square = []
for i in range(1,5):
     square.append(i*i)
print(square)

square = [i*i for i in range(1,5)]
print(square)

odd = [i*i for i in range(1,5) if i%2==0]
print(odd)

od = ['even' if i%2 == 0 else 'odd' for i in range(1,10)]
print(od)

# ----------------------------------------------

lst = [i for i in range(1,6)]
print(lst)

print(lst[0])
print(lst[-1])
lst[1]= 100
print(lst)
lst.append(44)
print(lst)
lst.remove(44)
print(lst)


count=0
for i in lst:
     count = count + 1

print(count)
print(len(lst))


squ = [i*i for i in range(1,11)]
print(squ)

even = [ i for i in range(1,21) if i%2==0 ]
print(even)

odd = [i for i in range(1,21) if i%2 ==1]
print(odd)

lst = [1,2,3,4,5]
new_lst = [i*i for i in lst]
print(new_lst)

result = []
for i in lst:
     if i > 3:
          result.append(i)

print(result)


nums = [10, 20, 30, 40, 50]


print(nums[0:3])
print(nums[2:])
print(nums[1:2])
print(nums[::-1])

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][2])  
print(matrix[0][1])

names = ["ram", "Amit", "manish"]
names.sort()
print(names)

a = [1, 2, 3]
b = a
b.append(4)
print(a)

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)

a = [1, 2]
a.extend([3, 4])
print(a)



s = {1,2,3,4,2,2,2,3,3,4,4,5}
print(s)
print(type(s))
print(s)
s.add(10)
print(s)
s.remove(10)
print(s)
s.remove(3)
print(s)


a = {1,2,3}
b = {1,2,4,5,6}

c = a.union(b)
print(c)

c = a.intersection(b)
print(c)

c = a.difference(c)
print(c)


s = [1,2,3,2,3,2,3,4,5,5,7,9,65,44,33,44,33,]
print(type(s))

w = set(s)
print(w)

e = list(w)
print(e)


student = {
    'name' : "Manish",
    'age' : 23,
    "course": "Data Engineer"
}

print(student.get("age"))

student["city"] = "mumbai"
print(student)

student["age"] = 24
print(student.get('age'))

student.pop("age")
student.popitem()
print(student)

del student['name']
print(student)


students = {
    "name": "Manish",
    "age": 23,
    "course": "Python"
}

for key in students:
    print(key, students[key])




dic = {
    "name":"Manish",
    "age" : 24,
    "city" : "Mumbai"
}


print(dic)

for i, j in dic.items():
    print(f"{i}, {j}")

print(dic.get('age'))
dic["course"] = "science"
print(dic)

dic["course"] = "bio"
print(dic)


for i,j in dic.items():
    print("first key, second value:")
    print(i)
    print(j)


bio = {
    'student1':{
        "name": "Manish",
        'age': 32,
        "class": "beit"
    },
    'student2': {
        "name": "Manish1",
        'age' : 23,
        "class": "ddds"
    }
}

print(bio)
print(bio["student1"].get('age'))

keys = ["name", "age", "city"]
values = ["Manish", 23, "Mumbai"]


dic = dict(zip(keys,values))
print(dic)

s = {}
print(type(s))

s['name']= 'Manish'
s['age']=24,
s['degree']= 'Beit'

print(s)


x = {}

for i in range(1,5):
    x[i]= i**i

print(x)

print(s.get('ages'))

x['4']= 22
print(x)

for k in x:
    print(k)

for value in x.values():
    print(value)

for k in x.keys():
    print(k)

print(x)


count = 0

for k in x.keys():
    count = count + 1
    print(k)
print("The total count of key:")
print(count)

values = 1

if values in x.values():
    print(f'the value {values} exists in the dictionary')
else:
    print(f"the value {values} does not exists in the dictinaory")


d = {'a':1,'b':2,'c':3}

print(d)

d.pop('b')
print(d)
d.popitem()
print(d)

d.clear()
print(d)

d1 = {"a": 1, "b": 2, "c": 3}
d2 = d1.copy()
print(d1)
print(d2)
d2['d'] = 3
print(d2)

d2['d']= 33
print(d2)

d1 = {"a": 1}
d2 = {"b": 2}

d3 = d1 | d2
print(d3)



employees = {
    101: {"name": "Amit", "salary": 50000},
    102: {"name": "Ravi", "salary": 60000}
}



for emp_id, details in employees.items():
    print(emp_id,details['name'])

'''


data = (10, "Python", 3.5, True)
print(data)
print(data[0])
print(data[2])
print(data[-1])


t = 10,20,30
a ,b,c = t
print(a)


t = (1,2,3,"manish", True, 3.11)
print(t)
print(type(t))
print(t[0])
print(t[-1])

print(len(t)//2)

a = 10,20,30
print(a)

b,c,d = a
print(b)
print(c)
print(d)


a = 2
b= 3
a,b = b,a

print(a)
print(b)

t = (1,2,3,4,3,4,3,4,3,4)
a = 3
count = 0
for i in t:
    if i == a:
        count = count + 1
print(f"the count of 1 in t is {count}")

count = 0
for i in t:
    count += 1
    print(f"the index no: {count} ,and value: {i}")

l = list(t)
print(l)
print(type(l))
print("----------------")

tp = tuple(l)
print(tp)
print(type(tp))