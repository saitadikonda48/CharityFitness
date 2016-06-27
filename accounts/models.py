from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
from django.db.models.signals import post_save
import datetime
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('Must include username')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,  password):
        """
        Creates and saves a superuser with the given username, email and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    full_name = models.CharField(
            max_length=120,
            default='John Smith',
            blank=True,
    )
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        # The user is identified by their email address
        return self.full_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.full_name

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Message(models.Model):
    email = models.CharField(max_length=120)
    name = models.CharField(max_length=120, default="Anonymous")
    message = models.TextField()
    def __unicode__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(MyUser)
    full_name = models.CharField(max_length=120, default='John Smith', blank=True)
    hobbies = models.TextField(default="Running", null=True, blank=True)
    age = models.IntegerField(default=20, blank=True)
    height = models.IntegerField(default=165, blank=True)
    startWeight = models.IntegerField(default=180, blank=True)
    goalWeight = models.IntegerField(default=160, blank=True)
    startDate = models.DateField(default=datetime.date.today())
    goalDate = models.DateField(default=datetime.date.today() + datetime.timedelta(days=12))

    def __unicode__(self):
        return self.user.username

def new_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        new_profile, is_created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(new_user_receiver, sender=MyUser)