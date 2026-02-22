from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model with self-referential following relationship.
    """
    following = models.ManyToManyField(
        "self",
        symmetrical=False,      # A follows B != B follows A
        related_name="followers",  # Reverse lookup for followers
        blank=True
    )

    def __str__(self):
        return self.username
