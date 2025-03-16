# # # # from django.db import models

# # # # # Create your models here.
# # # from django.db import models

# # # class User(models.Model):
# # #     first_name = models.CharField(max_length=100)
# # #     last_name = models.CharField(max_length=100)
# # #     email = models.EmailField(unique=True)
# # #     password = models.CharField(max_length=100)

# # #     def __str__(self):
# # #         return self.email

# # #     class Meta:
# # #         db_table = 'user'


# # from django.db import models

# # class User(models.Model):
# #     GROUP_CHOICES = [
# #         ('HR', 'HR'),
# #         ('Employee', 'Employee')
# #     ]
    
# #     GENDER_CHOICES = [
# #         ('Male', 'Male'),
# #         ('Female', 'Female'),
# #         ('Other', 'Other')
# #     ]
    
# #     first_name = models.CharField(max_length=100)
# #     last_name = models.CharField(max_length=100)
# #     email = models.EmailField(unique=True)
# #     profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
# #     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
# #     dob = models.DateField()
# #     password = models.CharField(max_length=100)
# #     designation = models.CharField(max_length=50)
# #     address = models.TextField()
# #     group = models.CharField(max_length=10, choices=GROUP_CHOICES)
# #     phone_no = models.CharField(max_length=15, unique=True)
# #     department = models.CharField(max_length=50)
# #     active = models.BooleanField(default=True)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     modified_at = models.DateTimeField(auto_now=True)
# #     created_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_users')
# #     modified_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='modified_users')
    
# #     def __str__(self):
# #         return self.email

# #     class Meta:
# #         db_table = 'user'

# from django.db import models
# from django.contrib.auth.models import AbstractUser,AbstractBaseUser, BaseUserManager


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("Email is required")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)  # Hash password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         return self.create_user(email, password, **extra_fields)

# class UserProfile(AbstractBaseUser):
    
#     ROLE_CHOICES = (
#         ('admin', 'Admin'),
#         ('employee', 'Employee'),
#     )
    
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     ]
    
#     GROUP_CHOICES = [
#         ('HR', 'HR'),
#         ('Employee', 'Employee'),
#     ]

#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     dob = models.DateField()
#     designation = models.CharField(max_length=100)
#     address = models.TextField(max_length=300)
#     group = models.CharField(max_length=10, choices=GROUP_CHOICES)
#     phone_no = models.CharField(max_length=12, unique=True)
#     department = models.CharField(max_length=100)
    
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
#     is_active = models.BooleanField(default=True)  # Active/Inactive Status
#     is_staff = models.BooleanField(default=False)  # Required for Django Admin
#     is_superuser = models.BooleanField(default=False)  # Required for Django Admin
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
#     created_by = models.CharField(max_length=100)
#     modified_by = models.CharField(max_length=100)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_no', 'dob']

#     def __str__(self):
#         return self.email





# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("Email is required")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)  # Hash password
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         return self.create_user(email, password, **extra_fields)

# class UserProfile(AbstractBaseUser):
#     ROLE_CHOICES = (
#         ('hr', 'HR'),
#         ('employee', 'Employee'),
#     )
    
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
#     is_active = models.BooleanField(default=True)  # Active/Inactive Status
    
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     phone_no = models.CharField(max_length=12, unique=True)
#     dob = models.DateField()
#     profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
#     designation = models.CharField(max_length=100)
#     address = models.TextField(max_length=300)
#     department = models.CharField(max_length=100)
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_no', 'dob']

#     def __str__(self):
#         return self.email



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
