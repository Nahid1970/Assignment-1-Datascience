#!/usr/bin/env python
# coding: utf-8

# # 1. Given two integer numbers return their product. If the product is greater than 1000, then return their sum.

# In[1]:


a=30
b=20
m=a*b


# In[2]:


m


# In[8]:


x=int(input())
y=int(input())


# In[9]:


m1=x*y
m1


# In[10]:


if m1>1000:
    sum=x+y
    print(sum)
else:
    print("Product is smaller than 1000")
    


# # 2. Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration .print the sum of the current number and previous number
# 
#  

# In[18]:


n = list(range(10))
previousNum = 0
for i in n:
    sum = previousNum + i
    print('Current Number '+ str(i) + "\n"'Previous Number ' +  str(previousNum) +"\n" 'sum is ' + str(sum)) 
    previousNum=i


# # 3. Print First 10 natural numbers using while loop.

# In[19]:


i=1
while i<=10:
    print(i)
    i=i+1


# # 4. Accept number from user and calculate the sum of all number from 1 to a given number

# In[1]:


n = int(input("Enter number"))
sum = 0
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of all numbers is: ", sum)


# # 5. Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.

# In[1]:


a=[20,30,200,40,3000,35]
for num in a:
    x=num/5
    if (x>150):
        break
    else:
        print(x)
    


# # 6. Reverse the following list using for loop

# In[10]:


list=[10,20,25,30,45,35]
list.reverse()
list


# In[7]:


list1 = [10,20,25,30,45,35]

for i in range(len(list1) // 2):
    
    list1[i], list1[-1 - i] = list1[-1 - i], list1[i]


list1


# 7. Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function
# For example: print('My', 'Name', 'Is', 'Tamim') will display MyNameIsJames
# So use one of the formatting argument of print() to turn the output into My**Name**Is**Tamim

# In[2]:


a="My"
b="Name"
c="Is"
d="James"
print(a+b+c+d)
print(a+"**"+b+"**"+c+"**"+d)


# # 8. Concatenate two lists index-wise

# In[9]:


list1 = ["My ", "Is", "Nahid"]
list2 = ['Name', ' Hasan','']
  
con = [i + j for i, j in zip(list1, list2)]
  
print ("The list after element concatenation is : " +  str(con))


# # 9. Given a Python list of numbers. Turn every item of a list into its square

# In[13]:


num = [1, 2, 3, 4, 5]

squ_num = [number ** 2 for number in num]

print(squ_num)


# # 10. Access value 20 from the following tuple -> aTuple = ("Orange", [10, 20, 30], (5, 15, 25))

# In[15]:


Tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(Tuple1[1][1])


# In[ ]:




