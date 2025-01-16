from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):

    title = models.CharField(max_length=200)

    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    STATUS_CHOICES =(
        ("Completed","Completed"),
        ("Not completed","Not completed")
    )

    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="Notompleted")

    created_at = models.DateTimeField(auto_now_add=True)

    due_date = models.DateField()

    CATEGORY_CHOICES = (
        ("Business","Business"),
        ("Personal","Personal")
    )

    category = models.CharField(max_length=100,choices=CATEGORY_CHOICES,default="Personal")

    PRIORITY_CHOICES = (
        ("Low","Low"),
        ("Medium","Medium"),
        ("High","High")
    )

    priority = models.CharField(max_length=100,choices=PRIORITY_CHOICES,default="High")

    def __str__(self):
        
        return self.title