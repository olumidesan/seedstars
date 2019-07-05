from django.db import models

Base = models.Model

class Details(Base):
    name = models.CharField(max_length=255)
    email_address = models.EmailField(unique=True)
    created_at = models.DateTimeField()