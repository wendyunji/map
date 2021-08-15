from django.db import models

class Trench(models.Model):
    trench_num = models.IntegerField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        managed = False
        db_table = 'trench'