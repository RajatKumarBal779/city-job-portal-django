import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobsproject.settings')
import django
django.setup()
from testapp.models import Jobs
from faker import Faker
from random import *

fake=Faker()
def phonenumber():
    num=str(randint(6,9))
    for i in range(9):
        num+=str(randint(0,9))
    return int(num)

CITY=['HYD','BNG','PUN']
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility=fake.random_element(elements=('BCA','MCA','B.TECH','M.TECH','MBA','BSC'))
        fsal=fake.random_int(min=12000,max=40000)
        faddress=fake.address()
        femail=fake.email()
        fphno=phonenumber()
        fcity=choice(CITY)
        Jobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            salary=fsal,
            address=faddress,
            email=femail,
            phonenumber=fphno,
            city=fcity
            
        )
n=int(input("Enter No of Records : "))
populate(n)
print(f'{n} Records Inserted Successfully.')