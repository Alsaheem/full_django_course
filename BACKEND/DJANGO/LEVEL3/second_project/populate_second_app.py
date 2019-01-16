import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')
import django
django.setup()

# Fake pop script
# import random
from second_app.models import user,AccessRecord
from faker import Faker

fakegen=Faker()

def populate(N=5):

    for entry in range(N):

        #Create the fake data for that entry
        fake_first_name=fakegen.first_name()
        fake_last_name=fakegen.last_name()
        fake_email=fakegen.email()
        fake_date = fakegen.date()

        # Create the new user entry
        user_entry = user.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]
        # Create a fake access record for that user_entry

        acc_rec=AccessRecord.objects.get_or_create(first_name=user_entry,date=fake_date)[0]

#This is allow the module to run as a program does not allow it to run as a Module imported from another file

if __name__=='__main__':
    print ("populating script!")
    populate(15)
    print ("Population complete")
