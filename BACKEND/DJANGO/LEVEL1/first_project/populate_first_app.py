import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()

# Fake pop script
import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen=Faker()
topics=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        top=add_topic()

        #Create the fake data for that entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        # Create the new Webpage entry
        webpg=WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        # Create a fake access record for that Webpage
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
#This is allow the module to run as a program does not allow it to run as a Module imported from another file
if __name__=='__main__':
    print ("populating script!")
    populate(20)
    print ("Population complete")
