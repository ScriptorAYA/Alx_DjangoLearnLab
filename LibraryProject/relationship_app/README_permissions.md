# Permissions and Groups Setup

Models:
- Book model defines custom permissions: can_view, can_create, can_edit, can_delete.

Groups:
- Editors: can_create, can_edit
- Viewers: can_view
- Admins: all permissions

Usage:
- Assign users to groups via Django admin.
- Decorators @permission_required('relationship_app.can_create') etc. protect views.
- Accessing a view without permission returns a 403 error.

