from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# user profile model


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_email = models.EmailField(max_length=240, null=True, blank=True)
    default_phone_number = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=100, null=True,  blank=True)
    default_street_address2 = models.CharField(max_length=100, null=True,  blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True,  blank=True)
    default_county = models.CharField(max_length=100, null=True,  blank=True)
    default_country = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=40, null=True,  blank=True)

    def __str__(self):
        return str(self.user)


# create or update user profile model


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Create user profile """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

