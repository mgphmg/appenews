import django
import os

# Load Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enews_project.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()


admin_email = "admin@enewsapp.com"
admin_password = "Admin@123"

user, created = User.objects.get_or_create(
    email=admin_email,
    defaults={
        "username": "admin@enewsapp.com",
        "first_name": "Enews App Admin",
        "last_name": "Enews App Admin",
        "role": "admin",
        "is_staff": True,
        "is_superuser": True,
    }
)

if created:
    user.set_password(admin_password)
    user.save()
    print("Admin created:")
    print("Email:", admin_email)
    print("Password:", admin_password)
else:
    print("Admin already exists.")