from django.db import models
#from django.contrib.auth.hashers import make_password

#DataFlair Models
class SignUp(models.Model):
    name = models.TextField(max_length = 50)
    username = models.TextField(max_length = 50)
    birthdate = models.DateField()
    email = models.EmailField(blank = True,max_length=50)
    phone = models.TextField(max_length = 10)
    password = models.TextField(max_length = 50)
    def __str__(self):
        return self.name 

class Comment(models.Model):
    comment=models.TextField(max_length = 100)
    def __str__(self):
        return self.comment

    