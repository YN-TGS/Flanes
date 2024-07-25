import uuid
from django.db import models

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

#---------------ESTE SERIA EL REQ 3 LA IMAGEN 1 --------------------------------------
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    #---------------------------------------------------------------------