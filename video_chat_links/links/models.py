from django.db import models
from django.urls import reverse

# Create your models here.
class Link(models.Model):
	# blank = False  Something should be there
	title = models.CharField(max_length=200, blank=False)
	url = models.URLField(max_length=200, blank=False)
	description = models.TextField(blank=False, null=True) # blank is for required, null is for database

	def get_absolute_url(self):
		return reverse("links:link-list", kwargs={})

	def get_create_url(self):
		return reverse("links:link-create", kwargs={})