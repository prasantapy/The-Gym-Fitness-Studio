
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','The_G_F_Studio.settings')
import django
import random
django.setup()
from gym.models import (Member,
                        Contact,
                        Enquiry,
                        Equipment,
                        Plan)
from datetime import date
from faker import Faker

fake = Faker()
def Members(n):
    
    for _ in range(n):  
        
            genders = ['Male', 'Female', 'Other']
            plans = ['Gold', 'Silver', 'Bronze']
            amounts = ['1000', '1500', '2000', '2500']

            Member.objects.create(
                name=fake.name(),
                contact=fake.phone_number(),
                email=fake.email(),
                gender=random.choice(genders),
                plan=random.choice(plans),
                joindate=fake.date_between(start_date='-1y', end_date='today'),
                initamount=random.choice(amounts)

            )
#n = int(input("Enter number of records:"))
#Members(n)
#print(f'{n} Records inserted successfully......')

def create_contacts(n):
    
    for _ in range(n):
        Contact.objects.create(
            name=fake.name(),
            emailid=fake.email(),
            contact='9' + ''.join([str(random.randint(0, 9)) for _ in range(9)]),  
            subject=fake.sentence(nb_words=6),
            message=fake.paragraph(nb_sentences=3),
            msgdate=fake.date_between(start_date='-6M', end_date='today'),
            isread=random.choice(['Yes', 'No'])
        )

#n = int(input("Enter number of contact records: "))
#create_contacts(n)
#print(f"{n} Contact records inserted successfully!")

def create_Enquiry(n):
     
     for _ in range(n):
          genders_choices= ['Male', 'Female', 'Other']
          Enquiry.objects.create(
               name=fake.name(),
               
               mobile=random.choice(['9', '8', '7', '6']) + ''.join([str(random.randint(0, 9)) for _ in range(9)]),
               email =fake.email(),
               age=random.randint(18, 60),
               gender=random.choice(genders_choices)
               

          )
#n=int(input('enter number of Enquiry records: '))
#create_Enquiry(n)
#print(f'{n} Enquiry records inserted successfully!')

def create_Equipment(n):
     for _ in range(n):
          amounts = ['1000', '1500', '2000', '2500']
          Equipment.objects.create(
               name=fake.name(),
               price=random.choice(amounts),
               unit=random.randint(20, 50),
               purchasedate=fake.date_between(start_date='-1y', end_date='today'),
               description = fake.sentence()

          )
#n=int(input('Enter  Create_Equipment records :'))
#create_Equipment(n)
#print(f'{n} Equipment recored inserted successfully!!')

def create_plan(n):
    for _ in range(n):
         amounts = ['1000', '1500', '2000', '2500']
         Plan.objects.create(
              name=fake.name(),
              amount=random.choice(amounts),
              duration=random.randint(1,10),

         )
n=int(input())
create_plan(n)
