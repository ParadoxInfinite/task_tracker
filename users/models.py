from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    '''
    Creating UserProfile model which links to the default auth.models for User from django.contrib
    Link - https://docs.djangoproject.com/en/3.1/topics/auth/customizing/
        - user (1 to 1 relation with the built in User)
        - user_image
        - description
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_image = models.ImageField('User Image',upload_to='profile_pictures/', default='default_profile.jpg')
    description = models.CharField('Description', max_length=1024)
    updated_on = models.DateTimeField('Updated On', auto_now=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name +' '+ self.user.last_name}'s Profile"
        return f"{self.user.username}'s Profile"