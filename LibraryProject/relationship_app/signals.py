# LibraryProject/relationship_app/signals.py
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'relationship_app':
        # Create groups
        editors, created = Group.objects.get_or_create(name='Editors')
        viewers, created = Group.objects.get_or_create(name='Viewers')
        admins, created = Group.objects.get_or_create(name='Admins')

        # Get permissions
        Book = apps.get_model('relationship_app', 'Book')
        can_create = Permission.objects.get(codename='can_create', content_type__app_label='relationship_app')
        can_edit = Permission.objects.get(codename='can_edit', content_type__app_label='relationship_app')
        can_delete = Permission.objects.get(codename='can_delete', content_type__app_label='relationship_app')
        can_view = Permission.objects.get(codename='can_view', content_type__app_label='relationship_app')

        # Assign permissions to groups
        editors.permissions.set([can_create, can_edit])
        viewers.permissions.set([can_view])
        admins.permissions.set([can_create, can_edit, can_delete, can_view])

