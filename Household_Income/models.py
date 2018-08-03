from django.db import models

# Create your models here.

from health.models import Counties

############################################KIHBIS II############################################
class Household_Kihibs_Households_That_Sought_Credit(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    h_sought = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()
    h_a_sought = models.DecimalField(max_digits=10, decimal_places=1)
    hholds_sought = models.IntegerField()