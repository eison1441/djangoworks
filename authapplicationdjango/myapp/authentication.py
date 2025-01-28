from django.contrib.auth.backends import BaseBackend
from myapp.models import User
from django.db import models
from django.db.models.signals import post_save

class EmailBackend(BaseBackend):


    def authenticate(self,request,username=None,password=None,**kwargs):

        try:
            user_instance=User.objects.get(email=username)

            if user_instance.check_password(password):

                return user_instance
            else:
                    
                    return None
            
        except:
             
             return None
        
    def get_user(self,user_id):
            
            try:
                
                user_instance=User.objects.get(id=user_id)
                
                return user_instance
            
            except:
                
                return None

class PhoneBackend(BaseBackend):
     
    def authenticate(self, request, username=None,Password=None,**kwargs):
          
        try:
             
            user_instance=User.objects.get(phone=username)

            if user_instance.check_password(Password):
                 
                 return user_instance
            
            else:
                 
                 return None
            
        except:
             
             return None
        

    def get_user(self,user_id):
            
            try:
                
                user_instance=User.objects.get(id=user_id)
                
                return user_instance
            
            except:
                
                return None


