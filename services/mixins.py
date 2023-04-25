# abstact model for created_at and updated_at include for all models
# https://django-mptt.readthedocs.io/en/latest/tutorial.html

# CKeditor
# https://django-ckeditor.readthedocs.io/en/latest/

from django.db import models

class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



