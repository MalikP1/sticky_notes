from django.db import models

'''
Model representing a sticky note post.
'''


class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255, null=True)
