from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime
from django.contrib.auth.models import User


def upload_to(instance, filename):
    return 'images/avatar/{filename}'.format(filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    birthday = models.DateField(validators=[MaxValueValidator(datetime.now().date())], blank=True, null=True)
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{}'s profile".format(self.user.username)


class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followings')

    class Meta:
        unique_together = ('follower', 'following')
        pass


class FollowInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='follow_info')
    followers_quantity = models.PositiveIntegerField(default=0)
    followings_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{}'s follow info".format(self.user.username)

