from django.db import models

# Create your models here.
class Website(models.Model):
    idwebsite = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'website'
