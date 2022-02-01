#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from contents.models import PostModel

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    nickname = models.CharField(max_length=256, null=False)

class UserLikes(models.Model):
    class Meta:
        db_table = "user_likes"
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    post_id = models.ForeignKey(PostModel, on_delete=models.CASCADE)


class UserProfiles(models.Model):
    class Meta:
        db_table = "user_profile"
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    pf_image = models.URLField(max_length=200)


