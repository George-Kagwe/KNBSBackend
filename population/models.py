
from django.db import models

# Create your models here.
from health.models import Counties


class PopulationBySexHouseholdsDensityAndCensusYears(models.Model):
    census_population_id = models.AutoField(primary_key=True)
    male = models.CharField(max_length=100)
    female = models.CharField(max_length=100)
    total = models.CharField(max_length=100)
    hhs = models.CharField(max_length=100)
    av_hh_size = models.CharField(max_length=100)
    approx_area = models.CharField(max_length=100)
    density = models.CharField(max_length=100)
    census_year = models.CharField(max_length=100)

class PopulationProjectionsBySelectedAgeGroup(models.Model):
    population_projection_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    range_0_4 = models.CharField(max_length=100)
    range_5_9 = models.CharField(max_length=100)
    range_10_14 = models.CharField(max_length=100)
    range_15_19 = models.CharField(max_length=100)
    range_20_24 = models.CharField(max_length=100)
    range_25_29 = models.CharField(max_length=100)
    range_30_34 = models.CharField(max_length=100)
    range_35_39 = models.CharField(max_length=100)
    range_40_44 = models.CharField(max_length=100)
    range_45_49 = models.CharField(max_length=100)
    range_50_54 = models.CharField(max_length=100)
    range_55_59 = models.CharField(max_length=100)
    range_60_64 = models.CharField(max_length=100)
    range_65_69 = models.CharField(max_length=100)
    range_70_74 = models.CharField(max_length=100)
    range_75_79 = models.CharField(max_length=100)
    range_80_plus = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

class PopulationProjectionsBySpecialAgeGroups(models.Model):
    selected_age_group_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    under_1 = models.CharField(max_length=100)
    range_1_2 = models.CharField(max_length=100)
    range_3_5 = models.CharField(max_length=100)
    range_6_13 = models.CharField(max_length=100)
    range_14_17 = models.CharField(max_length=100)
    range_18_24 = models.CharField(max_length=100)
    range_18_34 = models.CharField(max_length=100)
    range_less_18 = models.CharField(max_length=100)
    range_18_plus = models.CharField(max_length=100)
    range_15_49 = models.CharField(max_length=100)
    range_15_64 = models.CharField(max_length=100)
    range_65_plus = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

class Households_Type_Floor_Material_Main_Dwelling_Unit(models.Model):
    floor_material_id = models.AutoField(primary_key=True)
    material = models.CharField(max_length=100)
    households = models.IntegerField()

class Households_By_Main_Source_of_Water(models.Model):
    source_of_water_id = models.AutoField(primary_key=True)
    source = models.CharField(max_length=100)
    total = models.IntegerField()

class By_Type_of_Disability(models.Model):
    disability_id = models.AutoField(primary_key=True)
    disability = models.IntegerField()
    females = models.IntegerField()
    males = models.IntegerField()
    total_population = models.IntegerField()

class Percentage_Households_Ownership_Household_Assets(models.Model):
    ownership_id = models.AutoField(primary_key=True)
    asset = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=30, decimal_places=5)

class Distribution_Sex_Number_Households_Area_Density(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    area_in_square_km = models.DecimalField(max_digits=30, decimal_places=2)
    county_name = models.CharField(max_length=100)
    density = models.DecimalField(max_digits=30, decimal_places=7)
    female = models.IntegerField()
    male = models.IntegerField()
    no_of_houseHolds = models.IntegerField()
    total_population = models.IntegerField()

class By_Sex_And_School_Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    education_level = models.CharField(max_length=100)
    female = models.IntegerField()
    male = models.IntegerField()
    total_population = models.IntegerField()

class By_Sex_And_Age_Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    female = models.IntegerField()
    male = models.IntegerField()
    total_population = models.IntegerField()
    age_group = models.CharField(max_length=100)

############################################KIHBIS II############################################
class Kihibs_By_Broad_Age_Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    range_0_14 = models.DecimalField(max_digits=10, decimal_places=1)
    range_15_64 = models.DecimalField(max_digits=10, decimal_places=1)
    over_65 = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    age_depend_ratio = models.DecimalField(max_digits=10, decimal_places=1)
    child_depend_ratio = models.DecimalField(max_digits=10, decimal_places=1)
    old_age_depend_ratio = models.DecimalField(max_digits=10, decimal_places=1)
    individuals = models.IntegerField()

class Kihibs_Children_Under_18_By_Orphanhood(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    living_with_both = models.DecimalField(max_digits=10, decimal_places=1)
    father_alive = models.DecimalField(max_digits=10, decimal_places=1)
    father_deceased = models.DecimalField(max_digits=10, decimal_places=1)
    mother_alive = models.DecimalField(max_digits=10, decimal_places=1)
    mother_deceased = models.DecimalField(max_digits=10, decimal_places=1)
    both_alive = models.DecimalField(max_digits=10, decimal_places=1)
    only_father_alive = models.DecimalField(max_digits=10, decimal_places=1)
    only_mother_alive = models.DecimalField(max_digits=10, decimal_places=1)
    both_parents_deceased = models.DecimalField(max_digits=10, decimal_places=1)
    missing_info = models.DecimalField(max_digits=10, decimal_places=1)
    orphanhood = models.DecimalField(max_digits=10, decimal_places=1)
    individuals = models.IntegerField()

class Kihibs_Distribution_By_Sex(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    male_individuals = models.IntegerField()
    male_per_cent = models.DecimalField(max_digits=10, decimal_places=1)
    female_individuals = models.IntegerField()
    female_per_cent = models.DecimalField(max_digits=10, decimal_places=1)
    sex_ratio = models.DecimalField(max_digits=10, decimal_places=1)
    individuals = models.IntegerField()

class Kihibs_Distribution_Of_Households_By_Size(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    range_1_2_persons = models.DecimalField(max_digits=10, decimal_places=1)
    range_3_4_persons = models.DecimalField(max_digits=10, decimal_places=1)
    range_5_6_persons = models.DecimalField(max_digits=10, decimal_places=1)
    over_7_persons = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()
    mean_hhold_size = models.DecimalField(max_digits=10, decimal_places=1)

class Kihibs_Hholds_By_Sex_Of_Household_Head(models.Model):
    head_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    male = models.DecimalField(max_digits=10, decimal_places=1)
    female = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Marital_Status_Above_18_Years(models.Model):
    status_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    monogamous = models.DecimalField(max_digits=10, decimal_places=1)
    polygamous = models.DecimalField(max_digits=10, decimal_places=1)
    living_together = models.DecimalField(max_digits=10, decimal_places=1)
    seperated = models.DecimalField(max_digits=10, decimal_places=1)
    divorced = models.DecimalField(max_digits=10, decimal_places=1)
    widow_widower = models.DecimalField(max_digits=10, decimal_places=1)
    never_married = models.DecimalField(max_digits=10, decimal_places=1)
    individuals = models.IntegerField()

