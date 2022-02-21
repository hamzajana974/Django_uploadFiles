from django.db import models

#create your models here
class FilesUpload(models.Model):
    files1 = models.FileField()