from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    id_product = models.IntegerField()
    type = models.CharField(max_length=255)
    price = models.FloatField()
    count_product = models.IntegerField()

    def __unicode__(self):
        return "{0}".format(self.price, )
    

class ETickets(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{0}".format(self.author, )

"""
class AccountManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not username:
            raise ValueError(_('The Username must be set'))
        
        user = self.model(username=username)
        user.set_email(email)
        user.set_password(password)
        user.save()
        return user

"""
    
"""
class Acount(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)
    email = None
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['access_platforms', 'access_mission', 'access_rule_sets', 'access_mdsr']

    objects = AccountManager()

    def __str__(self):
        return ''.join(c for c in self.username if c.isupper())
    
    class Meta:
        db_table = 'auth_user'
"""