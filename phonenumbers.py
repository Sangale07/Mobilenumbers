#!/usr/bin/env python
# coding: utf-8

# In[12]:


import phonenumbers
from phonenumbers import carrier, geocoder,timezone

mobileNo = input("Enter your Number with Country code: ")
mobileNo =phonenumbers.parse(mobileNo)

print(timezone.time_zones_for_number(mobileNo))
print(carrier.name_for_number(mobileNo,"en"))
print(geocoder.description_for_number(mobileNo,"en"))
print("Valid Mobile Number : ",phonenumbers.is_valid_number(mobileNo))
print("cheaking possibility of number:",phonenumbers.is_possible_number(mobileNo))


# In[ ]:




