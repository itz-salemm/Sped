from django.db import models

# Create your models here.

class FileText(models.Model):
	file = models.FileField()


	def __str__(self):
		return self.file




