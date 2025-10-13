from django.db import models

# Create your models here.
# เราจะตั้งว่าเก็บฐานข้อมูลอะไรไว้บ้าง ในไฟล์นี้
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)
    date = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"username = {self.name} , email = {self.email}"
