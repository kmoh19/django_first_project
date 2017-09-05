import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings') #mapping object for setting up python environment
import django
django.setup()

from first_app.models import Topic,Webpage,AccessRecord
from faker import Faker
import random


fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for _ in range(N):
        
        top=add_topic() # create a topic
        
        fake_url=fakegen.url() # create fake data
        fake_date=fakegen.date()
        fake_name=fakegen.company()
        
        # create the new webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        
        webpg.save()
        
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
        acc_rec.save()
        
        
if __name__== '__main__':
    
    print ('populating now')     
    
    populate(20)
    
    print ('populating complete')
    
    
    




