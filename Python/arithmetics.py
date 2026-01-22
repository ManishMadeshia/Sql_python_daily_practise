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


# list practice


# 1. Create a list of 10 numbers and print it.
l = []

for i in range(1,11):
    l.append(i)
print(l)


# 2. Access the 3rd, 5th, and last element of a list.
print(l[2]) # access the 3rd element
print(l[4])  # acces the 5 element
print(l[-1])  # accessing the last element

#3. Replace all even numbers in a list with 0.

for i in range(len(l)):
    if i%2==0:
        l[i]= 0

print(l)


#4. Count how many elements are greater than 50.

count = 0 

for i in l:
    if i > 50:
        count = count + 1
print(f"the total no greater the 50 is {count}")


#5. Find the sum and average of list elements.

sum = 0
print(l)

for i in l:
    sum = sum + i
print(f"the sum of list element : {sum}")
print(f"the avg of list element: {sum // len(l)}")

#6. Find the largest and smallest element in a list.

element = [1,3,1,6,3,8,6,9,5,9,5,1,4]

small_elem = element[0]
largest_elem= element[0]


for num in element:
    if num < small_elem:          #1 < 1 = 1, 1<3 = 1, 1, 
        small_elem = num
    if num > largest_elem:         #1 > 1 = 1, 1>3 = 3,
        largest_elem = num

print(small_elem)
print(largest_elem)


# 7. Find the second largest element.

def find_second_largest_sorted(numbers):
    unique_num = list(set(numbers))  #convert to a set to remove duplicate and then back to list

    if len(unique_num) < 2:
        print("The number length should be greater than 2!")

    unique_num.sort()

    return unique_num[-2]

listt = [1,2,1,2,3,4,2,1,4,33,2244,22,442]
print(f"the second largest element in {listt} is : {find_second_largest_sorted(listt)}")


# Example 
list1 = [11, 22, 1, 2, 5, 67, 21, 32]
print(f"The second largest element in {list1} is: {find_second_largest_sorted(list1)}")

list2 = [10, 5, 10]
print(f"The second largest element in {list2} is: {find_second_largest_sorted(list2)}")



# 8. Reverse a list without using reverse() or slicing.

li = [33,22,66,55,44]

#solving using : in place reversal technique (two pointer)

print(li)
start_index = 0
last_index = len(li)-1

while start_index < last_index:
    li[start_index], li[last_index] = li[last_index], li[start_index]

    #move pointer inward
    start_index += 1
    last_index -= 1

print(li)



#9. Check if a list is sorted or not.
li = [1,2,3,4]
is_sorted = True
for i in range(len(li)-1):
    if li[i] > li[i+1]:
        is_sorted = False
        break
print(is_sorted)


#10 Remove duplicate elements from a list.

ls = [1,2,3,2,1,2,3,4]
new = []
for item in ls:
    if item not in new:
        new.append(item)
print(new)


# 11 Create a new list containing squares of elements.

sq = [i*i for i in range(1,10)]
print(sq)

#12 Separate even and odd numbers into two lists.

li = [1,2,3,4,6,0,8,4,2,5,8]
e = []
o = []


for i in li:
    if i <= 0:
        print("no is equal to zero or less than zero")
        exit
    else:
         if i%2==0:
            e.append(i)
         else:
            o.append(i)
print(f'the even no are {e}')
print(f'the odd no are {o}')


#13 . Merge two lists element-wise.

a = [1,2,3]
b = [5,7,9]

print(list(zip(a,b)))


# 14. Rotate a list left by 1 position.

lst = [1,2,3,4]
lst = lst[1:] + lst[:1]
print(lst)

#15 Find frequency of each element in a list.


li= [1,2,3,2,1,3,4,5,5]

frequency = {}

for i in li:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)


#16. Flatten a nested list [[1,2],[3,4],[5]].

lis = [[1,2],[3,4],[5]]


k = [x for sub in lis for x in sub ]
print(k)

#17. find common element in two list

lis1 = [1,2,3,4]
lis2 = [3,4,5,6]
comm = []
for x in lis1:
    for y in lis2:
        if x == y:
            comm.append(y)

print(f'the command element: {comm}')

#18. Check if a list is palindrome.

li = [2,3,3,2]

if li[0:] == li[::-1]:
    print("li is palindrome")
else:
    print("not a palindrome")


#19 Implement list comprehension for filtering numbers > 10.

li = [2,5,7,22,33,55,11,22,8,4,33,55,34,3,55,54]
l = [x for x in li if x>10 ]
print(l)


#--------------------------------

#21 Create a tuple with mixed datatypes.
tup = (1,2,3.3,33.33, True, "Manish")
print(type(tup))


#22' Create a single-element tuple correctly.

li = [1,2,3,4,5]
tup1= tuple(li)

#23 Count occurrences of an element in a tuple.

tu = (4, 2, 9, 1, 7, 3)

for x in tu:
    count = 0
    for y in tu:
        if x == y:
            count += 1
    print(f'the count of {x}: {count}')

#25 Find index of an element without using index().
tu = (4, 2, 9, 1, 7, 3)

count= 0
for x in tu :
    print(f"the index of element {x} is {count}")
    count += 1


#26 Find maximum and minimum element in a tuple.

tu = (1,2,3,4,1,2)

minn = tu[0]
maxx = tu[0]

for x in tu:
    if x < minn:
        minn = x
    if x > maxx:
        maxx = x
print("Maximum element:", minn)
print("Minimum element:", maxx)

#27 Unpack a tuple into variables.

a,b,c = (1,2,3)
print(a)
print(b)
print(c)


#28 Swap two numbers using tuple unpacking.

a = 9
b = 3
print(f'the value of a is {a}')
print(f'the value of b is {b}')


print("after swapping two number using tuple unpacking")
a,b = b,a
print(f'the value of a is {a}')
print(f'the value of b is {b}')

# 29 Check if an element exists in a tuple.

tu = (1,2,3,4)

for x in tu:
    if 5 in tu:
        print("present")
    else:
        print("not present")

#30 Concatenate two tuples.
tu1 =(12,13,14)

print(tu + tu1)


#31 
tupp = ((1,2,3),(5,6,7),(8,9))

tuppp = tuple(x for sub in tupp for x in sub)
print(tuppp)



#--------------------dictionary-------------------

#48 Create a dictionary with 5 key–value pairs.

dic = {
    'name':"Manish",
    'Profile':"Data Engineer",
    'status' : 'Struggling',
    'certification': "grow data skill",
    'exp_salary': '4-5 lpa'
}

print(dic)
print(type(dic))

#49 Access value safely using get().

print(dic.get('names')) # using get function if value not available it does not throw error but using indexing it throw error
print(dic["name"])

#50 Add, update, and delete a key in dictionary.

dic['skills'] = 'Big data Engineer' # adding value
dic["status"] = "Learning"           # updating value 
del dic['skills']
print(dic)  

#51Loop through dictionary and print keys and values.

for k, v in dic.items():
    print(f'the key is : {k}, & it value: {v}')

count = 0

#52 Count number of keys without using len().
for k in dic.keys():
    count = count + 1
print(f'the total no of keys is:{count} ')


#55. Reverse keys and values in dictionary.
d = {"a":1,"b":2,"c":3,"d":4,"e":5}


rev = {v:k for k,v in d.items()}
print(rev)



#56 Check if a key exists.

inp = input("Enter a key: ")

if inp in d:
    print("exist")
    print(inp)
else:
    print("key not exist")

#57 Check if a value exists.

V = int(input("Enter a key: "))

if V in d:
    print("exist")
    print(V)
else:
    print("key not exist")


#58 Create a nested dictionary for students and marks.

studenta_marks={
    "manish":{
        'math': 90,
        'science': 88,
        'English':44,
    },
    "anish":{
        'math': 80,
        'science': 85,
        'English': 88,
    },
    "nish":{
        'math': 88,
        'science': 78,
        'English':89,
    }
}

print(studenta_marks)

studenta_marks["manish"]['math'] = 88
print(studenta_marks)

del studenta_marks["nish"]
print(studenta_marks)


#50 qusetion praticze

'''
num = 3

if num%2 == 0 :
    print("even")
elif num%2 == 1:
    print("odd")
else:
    print("not define")

x = True + False
print(x)
print(type(x))

i = 10
s = str(i)
print(s)
print(type(s))
print(type(None))


num = 13

if num >= 10 and num <=50:
    print("num in between 10 and 50")
else:
    print("sorry")

print(False or False)
print(1 < 5 < 10)

num = 1
if num == 0:
    print("zero")
else:
    if num > 0:
        print("positive")
    else: 
        print("negative")


age = 11

if age == 0 and age <= 0 or age> 100:
    print("Please Enter Correct age")
else:
    if age <18 :
        print("teenage")
    elif age > 18 :
        print("adult")
    elif age > 50 :
        print("senior citizen")

for i in range(1,11):
    if i == 5:
        pass
    else:
        print(i)

for i in range(3):
    for j in range(2):
        print(i, j)

sum = 0

print(900//10)

for i in range(1,11):
    print(f'the multiplication table of 5 is {5}*{i} = {5*i}')

l = [i*i for i in range(1,11)]
print(l)

l = [1,2,3,2,1,2]
l = set(l)
print(l)
l = [1,2,3,4,5,6,7,8,6,5,4]

print(l[::-1])


for i in range(len(l)):
    print(l[::-1])

largest = l[0]

for i in l:
    if i > largest:
        largest = i
print(largest)


l = [i for i in l if i%2 ==0 ]
print(l)


s = ['s','d','g','h','t']
upp_s = []
for i in s:
    i = i.upper()
    upp_s.append(i)
print(upp_s)

#------------------------------------

tpl = (2,)
print(type(tpl))
    
s1 = {1,2,3}
s2 = {4,3,5}

s3 = s1.intersection(s2)
print(s3)

def squ(num):
    return num * num

print(squ(3))

l = [1,2,3,4,5]
print(l[1])
l.append(5)
print(l)
l.remove(4)
print(l)

print(l[::-1])

sum = 0
for i in l:
    sum = sum +i
print(sum)

count  = 0
n = 5
for i in l:
    if i==n:
        count = count+1
print(count)

max = l[0]
min = l[1]

for i in l:
    if i < min:
        min = i
    if i > max:
        max = i
print(max)
print(min)


f = [i*i for i in range(1,11)]
print(f)

e = [i for i in range(1,20) if i%2==0]
print(e)

e = [i for i in range(1,50) if i%3==0 or i%5==0]
print(e)

l = ['w','e','t','y','u']
f = [i.upper() for i in l ]
print(f)

l = ['manish','bipin','mohan','sav']

f = [len(word) for word in l]
print(f)

l = [1,2,3,4,3,2,1]

i = 0,1,2
j = 1,2,3


a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)
print([1, 2, 3] * 3)
print(len([[]] * 3))


a = [1, 2, 3]
print(a == a[:])
print(a is a[:])

lst = []
lst.append(lst)
print(len(lst))

l = ['manish','bipin','mohan','sav']

long_str = l[0]

for i in l :
    if len(i) > len(long_str):
        long_str = len[i]
print(long_str)

l = [i for i in l if len(i)>4]
print(l)


l = [1,2,1]

if l[0:] == l[::-1]:
    print("list is palindrome")
else:
    print("List is not palindrome")

l = [1,2,3,4]
n = []

for i in l:
    if i%2 == 0:
        i = i*i
        n.append(i)
print(i)
print(n)

l = [1, 2, 3]
ls = [1, 2, 4]

n = []

for i in l:
    if i in ls and i not in n:
        n.append(i)

print(n)

l = ['manish','mohan','apache']
n = []
for i in l:
    if len(i) > 5:
        print(f"the lenth of {i} is {len(i)} ")
        n.append(i)
print("the element which are present in l and length greater than 5: ")
print(n)


l = [1,0,6,-4,8,-88,-44,-3]

for i in range(len(l)) :
    if l[i] < 0:
        l[i]=0
print(l)

ls = [ [(i*j) for j in range(3)] for i in range(3)]
print(ls)

l = [[1,2],[3,4],[5,6]]

n = []
for i in l:
    for j in i:
        n.append(j)
print(n)


l = [1, 2, 3, 4, 5, 6, 7]
target = 8
pairs = []

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] + l[j] == target:
            pairs.append((l[i],l[j]))

print(pairs)


l = [1, 2, 3, 4, 5, 6, 7]

odd = []
even = []

for i in l:
    if i%2==0:
        even.append(i)
    elif i%2 != 0:
        odd.append(i)

print(f'odd number are {odd}')
print(f'even number are {even}')