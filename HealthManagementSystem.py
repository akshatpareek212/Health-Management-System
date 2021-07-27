#!/usr/bin/env python
# coding: utf-8

# In[2]:


def getdate():
    import datetime
    return datetime.datetime.now()

c=getdate()


# In[3]:


def client_ret(n):
        
        i=int(input('What do you wanna retrieve: 1-Diet or 2-Exercise'))
        while i not in range(1,3):
            i=int('Enter a valid input')
        if i==1:
            
        
            f= open(str(n)+"_diet.txt")
            contents=f.read()
            print(contents)
            f.close()
            
        else:
           
            f= open(str(n)+"_ex.txt")
            contents=f.read()
            print(contents)
            f.close()


# In[4]:


def client_log(n):
        
        i=int(input('What do you wanna log: 1-Diet or 2-Exercise'))
        while i not in range(1,3):
            i=int('Enter a valid input')
        if i==1:
            d=input("What food do you wanna add to {}'s diet".format(n))
        
            f= open(str(n)+"_diet.txt",'a')
            f.write("At {} time ,eat {}".format(c,d))
            f.close()
            
        else:
            e=input("What exercise do you wanna add to {}'s workout".format(n))
            f= open(str(n)+"_ex.txt",'a')
            f.write("At {} time ,perform {}".format(c,e))
            f.close()


# In[7]:


a=int(input("Press 1 to log client data or press 2 to retrieve client data "))
while a not in range(1,3):
    a=int(input("enter valid input"))
name=input("Which client's data would you like to access? ")
if a==1:
    client_log(name)
elif a==2:
    client_ret(name)
    


# In[1]:


cd Documents


# In[ ]:




