#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assigning variables
a = 'Arif'
b=2
c = 2.1
print(a)
print(b)
print(c)


# In[3]:


#AsSigning variables in a single line
a,B,c ='Arif',10,20.2
print(a)
print(b)
print(c)


# In[4]:


#Multiple variables assigned the same value 
a=b=c='arif'
print(a)
print(b)
print(c)


# # Checking if the objects referenced by a and b are not the same

# In[5]:


#Variable operators 
c
print(a is not b)


# In[6]:


a = 10 
b = '10'
print(a is not b)


# # Operator precedence

# In[ ]:


# Python follows the PEMDAS rules in the case of operation order
# 1.Parenthesis 
# 2.Exponents (i.e., powers and roots)
# 3.Division and Multiplication(from left to right)
#4.Addition and Subtraction (from left to right)


# In[8]:


# Expression: value = (1+1)*2**4//3+4-1



# In[ ]:


# first the parentheses work will be done
#(1+1)--> 2


# In[ ]:


#Next exponent operator
#2**4 --> 16


# In[ ]:


#Now devision operator work
#16//3 --> 5
# '/'provides result with floating data, but '//'provide quotient with nearest round number


# In[ ]:


# net operator priority will be multiplication 
# 2 * 5 --> 10


# In[ ]:


#next operator will be addition
#10+4 --> 14


# In[ ]:


# Now, the final operator will be subtraction
#14-1 ---> 13


# In[9]:


#now ´we can run the code
value


# # Arithmetic Operation

# In[10]:


#Addition operator '+'
a=1
b=2
print(a+b)


# In[11]:


# Subtraction '-'
# Performing subtraction operation and printing the result
a = 4
b = 2
total = a - b
print(total)


# In[12]:


# Multiplication '*'
# Performing multiplication operation and printing the result
# print(4*2)
a = 6
b = 3
value = a * b
print(value)


# In[13]:


# Divison
# Performing division operation and printing the result
# print(4/2)
a = 4
b = 2
value = a / b
print(value)
# Printing the type of the result
print(type(value))


# In[18]:


# Modulus '%'
# Modulus gives the remainder of a division
#two types of Modulus positive and negative modulus
# in the negative modulus, remainder sign will acome accordings to devisor sign
# print(5%2)
a = 5
b = 2
c= -10
d = 3
e= 10
f = -3
value = a % b
value1 = c % d
value2 = e % f
print('Positive modulus example:', value) 
print('negative modulus example:', value1) 
print('negative modulus example:', value2) 


# In[19]:


# Exponent
# Performing exponentiation operation and printing the result
# print(5**2)
a = 5
b = 2
value = a**b
print(value)


# In[20]:


# Floor Division Positive
# Performing floor division operation with positive operands and printing the result
#However, // returns only the integer part of the division result, which is 2.
# print(5//2)
a = 5
b = 2
value = a//b
print(value)


# In[21]:


# Floor Division Negative
# Performing floor division operation with negative operands and printing the result
# print(-5//2)
a = -5
b = 2
value = a//b
print(value)


# # Comparison Operator 

# In[22]:


# Less than comparison
# Checking if 7 is less than 2 and printing the result
# print(7<2)
a = 7
b = 2
value = a < b
print(value)


# In[23]:


# Greater than comparison
# Checking if 7 is greater than 2 and printing the result
# print(7>2)
a = 7
b = 2
value = a > b
print(value)


# In[24]:


# Less than or equal to comparison
# Checking if 7 is less than or equal to 2 and printing the result
# print(7<=2)
a = 7
b = 2
value = a <= b
print(value)


# In[25]:


# Greater than or equal to comparison
# Checking if 7 is greater than or equal to 2 and printing the result
# print(7>=2)
a = 7
b = value = a >= b
print(value)


# In[26]:


# Equality comparison
# Checking if 7 is equal to 2 and printing the result
# print(7==2)
a = 7
b = 2
value = a == b
print(value)


# In[27]:


# Inequality comparison
# Checking if 7 is not equal to 2 and printing the result
# print(7!=2)
a = 7
b = 2
value = a != b
print(value)


# # Logical Operator

# In[ ]:


# Assigning values to variables
a = 7
b = 2
c = 3
d = 300


# In[31]:


print("******* Logical and *******")
# Checking if a is greater than b and a is greater than c
print('a is greater than b and c:',a > b and a > c)
# Checking if a is greater than b and a is less than c
print('a is grater than b and a is less than c:',a > b and a < c)
# Checking if a is less than b and a is greater than c
print('a is less than b and a is grater than c:',a < b and a > c)
# Checking if a is less than b and a is less than c
print('a is less than b and a is less than c:',a < b and a < c)
# Checking if a is greater than b and c (no comparison with a)
print('a is greater than b and c :',a > b and c)
# Checking if a is greater than b and both c and d
print('a is greater than b and both c and d:',a > b and c and d)
# Checking if a is less than b and c (no comparison with d)
print('a is less than b and c:',a < b and c)
# Checking if a is less than b and both c and d
print('a is less than b and both c and d:',a < b and c and d)


# In[33]:


# Assigning values to variables
a = 7
b = 2
c = 3
d = 300
# Logical or operator
print("####### Logical or #######")
# Checking if a is greater than b or a is greater than c
print('a is greater than b or a is greater than c:',a > b or a > c)
# Checking if a is greater than b or a is less than c
print('a is greater than b or a is less than c:',a > b or a < c)
# Checking if a is less than b or a is greater than c
print('a is less than b or a is greater than c:',a < b or a > c)
# Checking if a is less than b or a is less than c
print('a is less than b or a is less than c:',a < b or a < c)
# Checking if a is greater than b or c (no comparison with a)
print('a is greater than b or c :',a > b or c)
# Checking if a is greater than b or both c and d
print('a is greater than b or both c and d:',a > b or c or d)
# Checking if a is less than b or c (no comparison with d)
print('a is less than b or c:',a < b or c)
# Checking if a is less than b or both c and d
print('a is less than b or both c and d:',a < b or c or d)


# In[34]:


# Logical not operator
print("******* Logical not *******")
# Negating the result of a < b
print(not(a < b))
# Negating the result of a > b
print(not(a > b))
# a is less than b(a<b), but using not befor (a>b) express it as no, a is not less b


# # Assignment operators

# In[35]:


# Assigning values to variables
a = 10
b = 20
m = 15


# In[36]:


# Adding a and b, and assigning the result to y
y = a + b
print(y)


# In[37]:


# Incrementing m by 10
m += 10
print(m)


# In[38]:


# Decrementing m by 10
m -= 10
print(m)


# In[39]:


# Multiplying m by 10
m *= 10
print(m)


# In[40]:


# Dividing m by 10
m /= 10
print(m)


# In[41]:


# Finding the modulus of m divided by 10
m %= 10
print(m)


# In[42]:


# Exponentiating m to the power of 2
m **= 2
print(m)


# In[43]:


# Performing floor division of m by 10
m //= 10
print(m)


# In[ ]:




