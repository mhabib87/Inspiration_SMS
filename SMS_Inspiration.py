
# coding: utf-8

# In[12]:


from twilio.rest import Client
from credentials import*
import random


# In[15]:



client = Client(account_sid, auth_token)
fortunes = ["Good things come to those who wait.",
            "Patience is a virtue.",
            "The early bird gets the worm.",
            "A wise man once said, everything in its own time and place.",
            "Fortune cookies rarely share fortunes.","Look up to see more!",
           "Read more!","Close your mouth when you eat!","Don't be judgemental!",
            "Problems are not stop signs, they are guidelines. -Robert H. Schuller",
           "Believe in yourself! Have faith in your abilities!",
            "Always do your best. What you plant now, you will harvest later. -Og Mandino",
           "Expect problems and eat them for breakfast. -Alfred A. Montapert"
           ]

top = random.choice(fortunes)
message = client.messages                 .create(
                     body= top,
                     from_=tw_phone,
                     to= cell_phone
                 )

