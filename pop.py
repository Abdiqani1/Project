import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'project.settings')

import django
django.setup()

from app.models import signup
from faker import Faker

fakegen = Faker()


def pop(N=6):
    for entry in range(N):
        fake_name = fakegen.name().splite()
        fake_name1 = fakegen.name[0]
        fake_male = fakegen.email()
        fake_user = fakegen.name[1]
        fake_pass = fakegen.name[2]
        fake_phon = fakegen.phone()
        fake_add = fakegen.address()
        
        account = signup.objects.get_or_create(F_Name=fake_name1,
                                                E_mail=fake_male,
                                                Username=fake_user,
                                                Password=fake_pass,
                                                Phone=fake_phon,
                                                Address=fake_add)[0]

    if __name__ == "__main__":
        print("POP DATE")
        pop(50)
        print("DATA COMPLETE!!!!1")