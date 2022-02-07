from django.db import models


# Create your models here.


class PostModel(models.Model):
    class Meta:
        db_table = "posts"

    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=200, null=False)
    post_url = models.CharField(max_length=200, default="", null=True)
    post_category = models.CharField(max_length=200, null=False)
    like_count = models.IntegerField(null=True)
    post_file = models.FileField(upload_to='uploads/%Y/%m/%d')
    post_thumbnail = models.URLField(max_length=200)


class RecommendModel(models.Model):
    class Meta:
        db_table = "recommend"
    re_id = models.AutoField(primary_key=True)
    re_title = models.CharField(max_length=200, null=False)
