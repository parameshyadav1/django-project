# backend/todo/models.py
from django.db import models

class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicit primary key
    title = models.CharField(max_length=200)
    # ... other fields ...