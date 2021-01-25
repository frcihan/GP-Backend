from django.db import models
from django.contrib.auth.models import User
# from PIL import Image

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(
        max_length=5000, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTayBxqNcpOECgVloLid0g8WYj7qn6w7k-dhQ&usqp=CAU")
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)