#!/usr/bin/env python
# coding: utf-8

# # Variables and Data Types in Python
# ## What is Variables
# - Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value.
# * a = 1
# * b = True
# * c = "Samarth"
# * d = None
# - There are four variables of different data types.
# ## What is Data type?
# * Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# * In python, we can print the type of any operator using type function. 

# In[50]:


a = 1
b = True
c = "Samarth"
d = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# By default, python provides the following built-in data types:
# 1. Numeric data: int, float, complex
# 
# * int: 1,-6, 0
# * float: 7.349, -9.0, 0.0000001
# * complex: 4+2i
# 
# 2. Text data: str
# * str: "Hi Samarth", "Python Programming"
# 
# 3. Boolean Type:
# * Booleans represent one of two values: True or False.
# 4. Sequenced data: list, tuple
# * List: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

# In[51]:


list1=[8, 2.3, [-4, 5], ["apple", "banana"]] 
print(list1)


# * Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

# In[52]:


tuple1=(("apple", "banana"), ("cherry"))
print(tuple1)


# 5. Mapped data: dict
# * Dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

# In[53]:


dict1 = {"name": "Sakshi", "age":20, "canVote": True}
print(dict1)


# ## Python Operators
# * Arithmetic operators:
# 1 +	Addition	x + y	
# 2 -	Subtraction	x - y	
# 3 *	Multiplication	x * y	
# 4 /	Division	x / y	
# 5 %	Modulus	x % y
# 6 //	Floor division	x // y
# 7 **	Exponentiation	x ** y

# In[54]:


print(1+5)
print(5-4)
print(5*5)
print(50/6)
print(50//6)
print(5%3)
print(5**3) #(5*5*5)


# In[55]:


#Calculator using Python
a = 50
b = 5
print( "The Value of", a, "+", b, "=", a+b)
print( "The Value of", a, "-", b, "=", a-b)
print( "The Value of", a, "*", b, "=", a*b)
print( "The Value of", a, "/", b, "=", a/b)


# In[ ]:




