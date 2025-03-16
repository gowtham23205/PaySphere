
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)  
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        extra_fields.setdefault("role", "hr")
        return self.create_user(email, password, **extra_fields)

class UserProfile(AbstractBaseUser):
    ROLE_CHOICES = (("hr", "HR"), ("employee", "Employee"))

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="employee")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Added password field
    phone_no = models.CharField(max_length=12, unique=True)
    dob = models.DateField()
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    designation = models.CharField(max_length=100)
    address = models.TextField(max_length=300)
    department = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_no", "dob"]

    def __str__(self):
        return self.email
