
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class User(AbstractBaseUser, BaseModel):
    username = models.CharField(max_length=40, unique=True)
    
    USERNAME_FIELD = "username"
