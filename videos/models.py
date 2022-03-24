from django.db import models

class Videos(models.Model):
    idvideos = models.AutoField(primary_key=True)
    subcategory_id = models.IntegerField(blank=True, null=True)
    video = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'videos'