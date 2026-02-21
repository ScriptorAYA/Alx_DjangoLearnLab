from django.db import models
from django.urls import reverse
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')



    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



    # ForeignKey creates relationship:
    # One User -> Many Posts
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

