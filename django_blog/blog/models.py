from django.db import models
from django.contrib.auth.models import User


# -----------------------------------------------------------
# Post Model
# -----------------------------------------------------------
# Represents a blog post written by a user.
# Each user can have multiple posts (one-to-many relationship).
# -----------------------------------------------------------

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    # ForeignKey creates relationship:
    # One User -> Many Posts
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title

