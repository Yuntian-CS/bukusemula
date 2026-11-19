from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    uuid = models.DecimalField(max_digits=40, decimal_places=0)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(
            max_length=15,  # Adjust based on your needs
            validators=[
                RegexValidator(
                    regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                    )
                ]
            )
    study_field = models.CharField(max_length=30)
    picture = models.CharField(max_length=20, unique=True)

class UserDetail(models.Model):
    user = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            primary_key=True,
            )
    uuid = models.DecimalField(max_digits=40, decimal_places=0, unique=True)
    email = models.EmailField(blank=True, unique=True)
    phone_number = models.CharField(
            max_length=15,  
            unique=True,# Adjust based on your needs
            validators=[
                RegexValidator(
                    regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
                    )
                ]
            )
    study_field = models.CharField(max_length=30)
    picture = models.CharField(max_length=20, unique=True)

