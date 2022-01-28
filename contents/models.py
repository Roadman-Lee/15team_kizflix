from django.db import models

# Create your models here.

class PostModel(models.Model):
    class Meta:
        db_table = "posts"

    post_id = models.CharField(max_length=10, null=False)
    post_title = models.CharField(max_length=200, null=False)
    post_category = models.CharField(max_length=200, null=False)
    like_count = models.IntegerField()

