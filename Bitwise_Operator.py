#!/usr/bin/env python
# coding: utf-8

# # NOT Operation 

# In[4]:


#Bitwise NOT operator (~):
#It flips all the bits of a number. For example, if a bit is 0, it turns it to 1, and if it's 1, it turns it to 0.
a = 10 #binary conversion of 10 is 
b= 15
print('~a = ',~a)


# In[ ]:


# ~0 = 1
# ~1 = 0
# data stored as binary format where left most bit indicate sign (positive or negative)
# 0 sign bit means Positive and 1 sign bit means negative 
# when using Not operator (~), sign is also reverse 
'''
Now, 10 binary conversion is 1010
#in stored, 1 means negative                           # 1s complement: flips
                                                       #2s complement: add 1 with 1s complement 1010
                                                                                                  +1
                                                                                            =   1011
            0 means positive
            sign_poition         Binary_number         
        10       0                 1010
        ~10      1.                1011  = (2°3)*1 +(2°2)*0 +(2°1)*1+(2°0)*1 = (8*1)+0+2+1 = 11
        Thus,
        ~10 = -11

'''


# # Bitwise AND operator

# In[5]:


# Bitwise AND operator (&)
print('a&b = ', a&b)


# In[ ]:


'''
Decimal.               Binary 
a = 10                 1 0 1 0
b = 15                 1 1 1 1
AND(multiplication)=   1 0 1 0
Decimal convertion =(2^3 * 1)+(2^2 * 0)+(2^1 * 1)+(2^0 * 0)
                   = 8 + 0 + 2 +0
                   = 10

'''


# # Bitwise OR operator (|)

# In[6]:


# Bitwise OR operator (|)
print('a|b = ', a|b)


# In[ ]:


'''
Decimal.                 Binary 
a = 10                   1 0 1 0
b = 15                   1 1 1 1
common between a and b = 1 1 1 1
decimal                = (2^3 *1)+(2^2 *1)+(2^1 *1)+(2^0 *1) = 8+4+2+1=15
'''


# # Bitwise XOR operator (^)

# In[7]:


# Bitwise XOR operator (^)

'''
If both bits are 0, the result is 0.
If both bits are 1, the result is 0.
If one bit is 0 and the other is 1, the result is 1.

For example:
0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0
'''


# In[ ]:


'''
Decimal.                 Binary 
a = 10                   1 0 1 0
b = 15                   1 1 1 1
a^b                  =   0 1 0 1
now convert it Decimal= (2**3 * 0)+(2**2 * 1)+ (2**1 * 0)+(2**0 * 1)
                      = 0 + 4 + 0 + 1
                      = 5

'''


# In[8]:


a = 10
b = 15
print(a^b)


# # Left shift operator (<<)

# In[ ]:


'''
left shift operator will move the right most bit to the right According to number.
the right most bit will replace by 0 and the left most or the most significant bit will be removed.
For example:
Decimal.                 Binary in 8 bit

a = 10                   0 0 0 0 1 0 1 0
a<<1                     0 0 0 1 0 1 0 0        ----> here left most bit replaced by 0 and the previous left most number moved
                                         to rigth position 00010100 in decimal 
                                =(2**7 * 0)+(2**6 * 0)+(2**5 * 0)+(2**4 * 1)+(2**3 *0)+(2**2 * 1)+(2**1 * 0)+(2**0 *0)
                                = 0 + 0 + 0 + 16 + 0 + 4 + 0 +0 =20

'''


# In[10]:


a = 10
print(a<<1)


# # Right shift operator (>>)
# 

# In[ ]:


'''
similarly the most significant bit will move to left according to number and the most significant bit will be fill
by 0.

a = 10                   0 0 0 0 1 0 1 0
a>>1                     0 0 0 0 0 1 0 1

now convert it decimal = (2**7 * 0)+(2**6 * 0)+(2**5 * 0)+(2**4 * 0)+(2**3 *0)+(2**2 * 1)+(2**1 * 0)+ (2**0 * 1)
                       = 0 + 0 + 0 + 0 + 0 + 4 + 0 + 1
                       = 5

'''


# In[11]:


a = 10
print(a>>1)


# In[ ]:




