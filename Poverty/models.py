from django.db import models

# Create your models here.

from health.models import Counties

############################################KIHBIS II############################################
class Overall_Estimates_By_Residence_And_County(models.Model):
    poverty_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    headcount_rate = models.DecimalField(max_digits=10, decimal_places=1)
    distribution_of_the_poor = models.DecimalField(max_digits=10, decimal_places=1)
    poverty_gap = models.DecimalField(max_digits=10, decimal_places=1)
    severity_of_poverty = models.DecimalField(max_digits=10, decimal_places=1)
    population = models.IntegerField()
    number_of_poor = models.IntegerField()

class Hardcore_Estimates_By_residence_And_County(models.Model):
    poverty_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    headcount_rate = models.DecimalField(max_digits=10, decimal_places=1)
    distribution_of_the_poor = models.DecimalField(max_digits=10, decimal_places=1)
    poverty_gap = models.DecimalField(max_digits=10, decimal_places=1)
    severity_of_poverty = models.DecimalField(max_digits=10, decimal_places=1)
    population = models.IntegerField()
    number_of_poor = models.IntegerField()

class Food_Estimates_By_Residence_And_County(models.Model):
    poverty_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    headcount_rate = models.DecimalField(max_digits=10, decimal_places=1)
    distribution_of_the_poor = models.DecimalField(max_digits=10, decimal_places=1)
    poverty_gap = models.DecimalField(max_digits=10, decimal_places=1)
    severity_of_poverty = models.DecimalField(max_digits=10, decimal_places=1)
    population = models.IntegerField()
    number_of_poor = models.IntegerField()

class Food_And_Non_Food_Expenditure_Per_Adult_Equivalent(models.Model):
    poverty_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    food = models.DecimalField(max_digits=10, decimal_places=2)
    non_food = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)

class Distribution_Of_Households_By_PointOfPurchasedFoodItems(models.Model):
    poverty_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    supermarket = models.DecimalField(max_digits=10, decimal_places=2)
    open_market = models.DecimalField(max_digits=10, decimal_places=2)
    kiosk = models.DecimalField(max_digits=10, decimal_places=2)
    general_shop = models.DecimalField(max_digits=10, decimal_places=2)
    specialised_shop = models.DecimalField(max_digits=10, decimal_places=2)
    informal_sources = models.DecimalField(max_digits=10, decimal_places=2)
    other_formal_points = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_observations = models.IntegerField()

class Distribution_Of_Household_Food_Consumption(models.Model):
    poverty_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    purchases = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    own_production = models.DecimalField(max_digits=10, decimal_places=2)
    gifts = models.DecimalField(max_digits=10, decimal_places=2)

class Consumption_Expenditure_And_Quintile_Distribution(models.Model):
    poverty_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    mean = models.IntegerField()
    median = models.IntegerField()
    quarter1 = models.DecimalField(max_digits=10, decimal_places=2)
    quarter2 = models.DecimalField(max_digits=10, decimal_places=2)
    quarter3 = models.DecimalField(max_digits=10, decimal_places=2)
    quarter4 = models.DecimalField(max_digits=10, decimal_places=2)
    quarter5 = models.DecimalField(max_digits=10, decimal_places=2)