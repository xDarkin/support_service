from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as _UserManager
from users.constants.roles import Role


class UserManager(_UserManager):
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields["is_staff"] = True
        extra_fields["role"] = Role.ADMIN

        return self._create_user(email, password, **extra_fields)

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields["is_staff"] = False
        extra_fields["role"] = Role.USER

        return self._create_user(email, password, **extra_fields)
