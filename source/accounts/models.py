from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    about = models.CharField(max_length=300, blank=True, null=True, verbose_name='About')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    git = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        permissions = [
                ('can_see_users', 'Может просматривать пользователей')
            ]
