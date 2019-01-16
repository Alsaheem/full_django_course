from django.db import models

# Create your models here.
class user(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128,unique=True)

    def __str__ (self):
        return self.first_name
        return self.last_name
        return str(self.email)


class AccessRecord(models.Model):
    first_name = models.ForeignKey(user,on_delete=models.CASCADE,)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
