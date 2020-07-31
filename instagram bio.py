#!/usr/bin/env python
# coding: utf-8

# In[2]:


import instaloader
l=instaloader.Instaloader()
#ENTER THE USERNAME OF THE PERSON IN THE BELOW LINE WHERE WRITTEN AS USERNAME
profile=instaloader.Profile.from_username(l.context,'username')
print(profile.biography)


# In[ ]:




