from django.contrib import admin

# Register your models here.



from instructor.models import User,Category

admin.site.register(User)

admin.site.register(Category)

