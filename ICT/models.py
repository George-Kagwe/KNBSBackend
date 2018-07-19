from django.db import models

# Create your models here.
from health.models import Counties


class Kihibs_Households_Owned_Ict_Equipment_Services(models.Model):
    household_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    computer = models.DecimalField(max_digits=10, decimal_places=1)
    television = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Households_With_Internet_By_Type(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    fixed_wired = models.DecimalField(max_digits=10, decimal_places=1)
    fixed_wireless = models.DecimalField(max_digits=10, decimal_places=1)
    mobile_broadband = models.DecimalField(max_digits=10, decimal_places=1)
    mobile = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Households_With_Tv(models.Model):
    household_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    digital_tv = models.DecimalField(max_digits=10, decimal_places=1)
    pay_tv = models.DecimalField(max_digits=10, decimal_places=1)
    free_to_air = models.DecimalField(max_digits=10, decimal_places=1)
    ip_tv = models.DecimalField(max_digits=10, decimal_places=1)
    none = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Households_Without_Internet_By_Reason(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    dont_need = models.DecimalField(max_digits=10, decimal_places=1)
    lack_skills = models.DecimalField(max_digits=10, decimal_places=1)
    no_network = models.DecimalField(max_digits=10, decimal_places=1)
    access_elsewhere = models.DecimalField(max_digits=10, decimal_places=1)
    doesnt_meet_needs = models.DecimalField(max_digits=10, decimal_places=1)
    service_cost_high = models.DecimalField(max_digits=10, decimal_places=1)
    equipment_cost_high = models.DecimalField(max_digits=10, decimal_places=1)
    cultural_reasons = models.DecimalField(max_digits=10, decimal_places=1)
    other_reasons = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Population_Above18By_ReasonNotHaving_Phone(models.Model):
    population_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    population = models.IntegerField()
    too_young = models.DecimalField(max_digits=10, decimal_places=1)
    dont_need = models.DecimalField(max_digits=10, decimal_places=1)
    restricted = models.DecimalField(max_digits=10, decimal_places=1)
    no_network = models.DecimalField(max_digits=10, decimal_places=1)
    gender_bias = models.DecimalField(max_digits=10, decimal_places=1)
    no_electricity = models.DecimalField(max_digits=10, decimal_places=1)
    phone_expe = models.DecimalField(max_digits=10, decimal_places=1)
    maintain_expe = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)

class Kihibs_Population_Above18Subscribed_MobileMoney(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    mobile_money = models.DecimalField(max_digits=10, decimal_places=1)
    mobile_banking = models.DecimalField(max_digits=10, decimal_places=1)
    population = models.IntegerField()

class Kihibs_Population_By_IctEquipment_And_ServicesUsed(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    television = models.DecimalField(max_digits=10, decimal_places=1)
    radio = models.DecimalField(max_digits=10, decimal_places=1)
    mobile = models.DecimalField(max_digits=10, decimal_places=1)
    computer = models.DecimalField(max_digits=10, decimal_places=1)
    internet = models.DecimalField(max_digits=10, decimal_places=1)
    population = models.IntegerField()

class Kihibs_Population_That_DidntUseInternet_By_Reason(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    too_young = models.DecimalField(max_digits=10, decimal_places=1)
    dont_need = models.DecimalField(max_digits=10, decimal_places=1)
    lack_skill = models.DecimalField(max_digits=10, decimal_places=1)
    expensive = models.DecimalField(max_digits=10, decimal_places=1)
    no_internet = models.DecimalField(max_digits=10, decimal_places=1)
    culture = models.DecimalField(max_digits=10, decimal_places=1)
    control = models.DecimalField(max_digits=10, decimal_places=1)
    security = models.DecimalField(max_digits=10, decimal_places=1)
    others = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    population = models.IntegerField()

class Kihibs_Population_That_Used_Internet_By_Purpose(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    seek_info = models.DecimalField(max_digits=10, decimal_places=1)
    make_app = models.DecimalField(max_digits=10, decimal_places=1)
    get_info = models.DecimalField(max_digits=10, decimal_places=1)
    newspaper = models.DecimalField(max_digits=10, decimal_places=1)
    banking = models.DecimalField(max_digits=10, decimal_places=1)
    voip = models.DecimalField(max_digits=10, decimal_places=1)
    selling = models.DecimalField(max_digits=10, decimal_places=1)
    ordering = models.DecimalField(max_digits=10, decimal_places=1)
    course = models.DecimalField(max_digits=10, decimal_places=1)
    research = models.DecimalField(max_digits=10, decimal_places=1)
    informative = models.DecimalField(max_digits=10, decimal_places=1)
    write_article = models.DecimalField(max_digits=10, decimal_places=1)
    social_nets = models.DecimalField(max_digits=10, decimal_places=1)
    movie = models.DecimalField(max_digits=10, decimal_places=1)
    search_work = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    population = models.IntegerField()

class Kihibs_Population_Who_Used_Internet_By_Place(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    mobility = models.DecimalField(max_digits=10, decimal_places=1)
    work = models.DecimalField(max_digits=10, decimal_places=1)
    cyber = models.DecimalField(max_digits=10, decimal_places=1)
    ed_centre = models.DecimalField(max_digits=10, decimal_places=1)
    comm_centre = models.DecimalField(max_digits=10, decimal_places=1)
    another_home = models.DecimalField(max_digits=10, decimal_places=1)
    at_home = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    population = models.IntegerField()

class Kihibs_Population_WithMobilePhone_AndAverageSims(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    phone = models.DecimalField(max_digits=10, decimal_places=1)
    population = models.IntegerField()
    avg_sims = models.DecimalField(max_digits=10, decimal_places=1)
    population_sims = models.IntegerField()


