from django.db import models

# Create your models here.




from health.models import Counties

############################################KIHBIS II############################################
class Kihibs_Undernourished_Children(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    height_for_age = models.DecimalField(max_digits=10, decimal_places=1)
    weight_for_age = models.DecimalField(max_digits=10, decimal_places=1)
    weight_for_height = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_children = models.IntegerField()
    category = models.CharField(max_length=50)

class Kihibs_Dutation_Of_Breastfeeding(models.Model):
    duration_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    breastfeeding = models.DecimalField(max_digits=10, decimal_places=1)
    mean = models.DecimalField(max_digits=10, decimal_places=1)
    median = models.IntegerField()
    no_of_children = models.IntegerField()

class Kihibs_Children_In_Growth_Monitoring_Programmes(models.Model):
    participation_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    participated = models.DecimalField(max_digits=10, decimal_places=1)
    not_participated = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_children = models.IntegerField()

class Kihibs_Children_In_Community_Nutrition_Programmes(models.Model):
    participation_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    participated = models.DecimalField(max_digits=10, decimal_places=1)
    not_participated = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_children = models.IntegerField()

class Kihibs_Children_By_First_Food_Supplement(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    other_milk = models.DecimalField(max_digits=10, decimal_places=1)
    infant_food = models.DecimalField(max_digits=10, decimal_places=1)
    porridge = models.DecimalField(max_digits=10, decimal_places=1)
    fort_porridge = models.DecimalField(max_digits=10, decimal_places=1)
    semi_solids = models.DecimalField(max_digits=10, decimal_places=1)
    water = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_children = models.IntegerField()

class Kihibs_Children_By_Breastfeeding_Status(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    ever_breastfed = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_children = models.IntegerField()
    one_hour = models.DecimalField(max_digits=10, decimal_places=1)
    one_day = models.DecimalField(max_digits=10, decimal_places=1)
    ch_breastfed = models.IntegerField()
