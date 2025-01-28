from django.db import models

from django.db.models.signals import post_save
# Create your models here.


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLE_OPTIONS=(
        ("instructor","instructor"),
        ("student","Student"),
    )

    role=models.CharField(max_length=12,choices=ROLE_OPTIONS,default="")

class InstructorProfile(models.Model):

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    expertise=models.CharField(max_length=200)

    picture=models.ImageField(upload_to="profilepics",null=True,blank=True,default="profilepics/default.jpg")

    description=models.CharField(max_length=200,null=True)




def create_instructor_profile(sender,instance,created,**kwargs):

    if created and instance.role =="instructor":

        print(instance,"werrtr")

        InstructorProfile.objects.create(owner=instance)

post_save.connect(create_instructor_profile,User)



class Category(models.Model):

    name=models.CharField(max_length=200,unique=True)


    def __str__(self):
        return self.name