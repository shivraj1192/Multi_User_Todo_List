from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    status_choice = [
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
    ]
    priority_choice = [
        ('1', '1️⃣'),
        ('2', '2️⃣'),
        ('3', '3️⃣'),
        ('4', '4️⃣'),
        ('5', '5️⃣'),
        ('6', '6️⃣'),
        ('7', '7️⃣'),
        ('8', '8️⃣'),
        ('9', '9️⃣'),
        ('10', '🔟'),
    ]
    title=models.CharField(max_length=105)
    status=models.CharField(max_length=10 , choices=status_choice)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=2 , choices=priority_choice)
    duedate_start = models.DateTimeField(null=True, blank=True)
    duedate_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    

class Contact(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    email=models.EmailField(max_length=254, unique=True)
    number = models.IntegerField()
    msg=models.TextField(max_length=500)
    
    

   
