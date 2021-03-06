from django.db import models

# Create your models here.

from health.models import Counties

############################################KIHBIS II############################################
class Kihibs_Hholds_By_Type_Of_Housing_Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    bungalow = models.DecimalField(max_digits=10, decimal_places=1)
    flat = models.DecimalField(max_digits=10, decimal_places=1)
    maisonnette = models.DecimalField(max_digits=10, decimal_places=1)
    swahili = models.DecimalField(max_digits=10, decimal_places=1)
    shanty = models.DecimalField(max_digits=10, decimal_places=1)
    manyatta = models.DecimalField(max_digits=10, decimal_places=1)
    landhi = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Hholds_By_Habitable_Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    one = models.DecimalField(max_digits=10, decimal_places=1)
    two = models.DecimalField(max_digits=10, decimal_places=1)
    three = models.DecimalField(max_digits=10, decimal_places=1)
    four = models.DecimalField(max_digits=10, decimal_places=1)
    five = models.DecimalField(max_digits=10, decimal_places=1)
    six_plus = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    mean_rooms = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()
    persons_per_room = models.DecimalField(max_digits=10, decimal_places=1)

class Kihibs_Hholds_In_Rented_Dwellings(models.Model):
    dwelling_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    govt_national = models.DecimalField(max_digits=10, decimal_places=1)
    govt_county = models.DecimalField(max_digits=10, decimal_places=1)
    parastatal = models.DecimalField(max_digits=10, decimal_places=1)
    company_directly = models.DecimalField(max_digits=10, decimal_places=1)
    company_agent = models.DecimalField(max_digits=10, decimal_places=1)
    individual_directly = models.DecimalField(max_digits=10, decimal_places=1)
    individual_agent = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Hholds_By_Housing_Tenure(models.Model):
    tenure_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    owner_occupier = models.DecimalField(max_digits=10, decimal_places=1)
    pays_rent = models.DecimalField(max_digits=10, decimal_places=1)
    no_rent_consent = models.DecimalField(max_digits=10, decimal_places=1)
    no_rent_squatting = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Main_Roofing_Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    grass = models.DecimalField(max_digits=10, decimal_places=1)
    mud = models.DecimalField(max_digits=10, decimal_places=1)
    iron_sheets = models.DecimalField(max_digits=10, decimal_places=1)
    tin_cans = models.DecimalField(max_digits=10, decimal_places=1)
    sheet = models.DecimalField(max_digits=10, decimal_places=1)
    concrete = models.DecimalField(max_digits=10, decimal_places=1)
    tiles = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Main_Wall_Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    lime_stone = models.DecimalField(max_digits=10, decimal_places=1)
    bricks = models.DecimalField(max_digits=10, decimal_places=1)
    cement_blocks = models.DecimalField(max_digits=10, decimal_places=1)
    cement_finish = models.DecimalField(max_digits=10, decimal_places=1)
    wood = models.DecimalField(max_digits=10, decimal_places=1)
    adobe = models.DecimalField(max_digits=10, decimal_places=1)
    iron_sheets = models.DecimalField(max_digits=10, decimal_places=1)
    bamboo = models.DecimalField(max_digits=10, decimal_places=1)
    stone = models.DecimalField(max_digits=10, decimal_places=1)
    cane = models.DecimalField(max_digits=10, decimal_places=1)
    plywood = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Owner_Occupier_Dwellings(models.Model):
    dwelling_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    purchased_cash = models.DecimalField(max_digits=10, decimal_places=1)
    purchased_loan = models.DecimalField(max_digits=10, decimal_places=1)
    purchased_cash_loan = models.DecimalField(max_digits=10, decimal_places=1)
    constructed_cash = models.DecimalField(max_digits=10, decimal_places=1)
    constructed_loan = models.DecimalField(max_digits=10, decimal_places=1)
    constructed_cash_loan = models.DecimalField(max_digits=10, decimal_places=1)
    inherited = models.DecimalField(max_digits=10, decimal_places=1)
    gift = models.DecimalField(max_digits=10, decimal_places=1)
    bartered = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Place_For_Washing_Hands_Near_Toilet(models.Model):
    place_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    place = models.DecimalField(max_digits=10, decimal_places=1)
    no_place = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Sharing_Of_Toilet_Facility(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    shared_toilet = models.DecimalField(max_digits=10, decimal_places=1)
    not_shared = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Waste_Disposal_Method(models.Model):
    method_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    county_gov = models.DecimalField(max_digits=10, decimal_places=1)
    community = models.DecimalField(max_digits=10, decimal_places=1)
    private_co = models.DecimalField(max_digits=10, decimal_places=1)
    dumped_compound = models.DecimalField(max_digits=10, decimal_places=1)
    dumped_street = models.DecimalField(max_digits=10, decimal_places=1)
    dumped_latrine = models.DecimalField(max_digits=10, decimal_places=1)
    burnt = models.DecimalField(max_digits=10, decimal_places=1)
    buried = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Time_Taken_To_Fetch_Drinking_Water(models.Model):
    time_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    zero = models.DecimalField(max_digits=10, decimal_places=1)
    less_thirty_min = models.DecimalField(max_digits=10, decimal_places=1)
    over_thirty_min = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Volume_Of_Water_Used(models.Model):
    volume_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    lit_0_1000 = models.DecimalField(max_digits=10, decimal_places=1)
    lit_1001_2000 = models.DecimalField(max_digits=10, decimal_places=1)
    lit_2001_3000 = models.DecimalField(max_digits=10, decimal_places=1)
    over_3000_lit = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Main_Floor_Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    tiles = models.DecimalField(max_digits=10, decimal_places=1)
    cement = models.DecimalField(max_digits=10, decimal_places=1)
    wood = models.DecimalField(max_digits=10, decimal_places=1)
    cow_dung = models.DecimalField(max_digits=10, decimal_places=1)
    sand = models.DecimalField(max_digits=10, decimal_places=1)
    carpet = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Main_Source_Of_Drinking_Water(models.Model):
    source_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    piped_dwelling = models.DecimalField(max_digits=10, decimal_places=1)
    piped_yard = models.DecimalField(max_digits=10, decimal_places=1)
    piped_tap = models.DecimalField(max_digits=10, decimal_places=1)
    tubewell = models.DecimalField(max_digits=10, decimal_places=1)
    protected_well = models.DecimalField(max_digits=10, decimal_places=1)
    protected_spring = models.DecimalField(max_digits=10, decimal_places=1)
    rain_water = models.DecimalField(max_digits=10, decimal_places=1)
    bottled_water = models.DecimalField(max_digits=10, decimal_places=1)
    unprotected_well = models.DecimalField(max_digits=10, decimal_places=1)
    unprotected_spring = models.DecimalField(max_digits=10, decimal_places=1)
    vendor_truck = models.DecimalField(max_digits=10, decimal_places=1)
    vendor_drum = models.DecimalField(max_digits=10, decimal_places=1)
    vendor_bicycles = models.DecimalField(max_digits=10, decimal_places=1)
    surface_water = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Main_Source_Of_Lighting_Fuel(models.Model):
    source_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    electricity = models.DecimalField(max_digits=10, decimal_places=1)
    generator = models.DecimalField(max_digits=10, decimal_places=1)
    solar_energy = models.DecimalField(max_digits=10, decimal_places=1)
    paraffin_lantern = models.DecimalField(max_digits=10, decimal_places=1)
    paraffin_tin_lamp = models.DecimalField(max_digits=10, decimal_places=1)
    paraffin_pressure_lamp = models.DecimalField(max_digits=10, decimal_places=1)
    fuel_wood = models.DecimalField(max_digits=10, decimal_places=1)
    gas_lamp = models.DecimalField(max_digits=10, decimal_places=1)
    battery_lamp = models.DecimalField(max_digits=10, decimal_places=1)
    candles = models.DecimalField(max_digits=10, decimal_places=1)
    biogas = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Main_Toilet_Facility(models.Model):
    facility_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    piped_sewer = models.DecimalField(max_digits=10, decimal_places=1)
    septic_tank = models.DecimalField(max_digits=10, decimal_places=1)
    latrine = models.DecimalField(max_digits=10, decimal_places=1)
    vip = models.DecimalField(max_digits=10, decimal_places=1)
    latrine_slab = models.DecimalField(max_digits=10, decimal_places=1)
    composting_toilet = models.DecimalField(max_digits=10, decimal_places=1)
    somewhere_else = models.DecimalField(max_digits=10, decimal_places=1)
    unknown_place = models.DecimalField(max_digits=10, decimal_places=1)
    without_slab = models.DecimalField(max_digits=10, decimal_places=1)
    bucket_toilet = models.DecimalField(max_digits=10, decimal_places=1)
    hanging_toilet = models.DecimalField(max_digits=10, decimal_places=1)
    bush = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Methods_Used_To_Make_Water_Safer(models.Model):
    method_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    boil = models.DecimalField(max_digits=10, decimal_places=1)
    add_bleach = models.DecimalField(max_digits=10, decimal_places=1)
    water_filter = models.DecimalField(max_digits=10, decimal_places=1)
    solar = models.DecimalField(max_digits=10, decimal_places=1)
    sieve_cloth = models.DecimalField(max_digits=10, decimal_places=1)
    stand_settle = models.DecimalField(max_digits=10, decimal_places=1)
    stand_settle = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Main_Source_Of_Cooking_Fuel(models.Model):
    source_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    firewood = models.DecimalField(max_digits=10, decimal_places=1)
    electricity = models.DecimalField(max_digits=10, decimal_places=1)
    lpg = models.DecimalField(max_digits=10, decimal_places=1)
    biogas = models.DecimalField(max_digits=10, decimal_places=1)
    kerosene = models.DecimalField(max_digits=10, decimal_places=1)
    charcoal = models.DecimalField(max_digits=10, decimal_places=1)
    shrubs = models.DecimalField(max_digits=10, decimal_places=1)
    animal_dung = models.DecimalField(max_digits=10, decimal_places=1)
    crop_residue = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()

class Kihibs_Primary_Type_Of_Cooking_Appliance(models.Model):
    appliance_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    stone_fire = models.DecimalField(max_digits=10, decimal_places=1)
    imp_stone_fire = models.DecimalField(max_digits=10, decimal_places=1)
    ordinary_jiko = models.DecimalField(max_digits=10, decimal_places=1)
    improved_jiko = models.DecimalField(max_digits=10, decimal_places=1)
    stove = models.DecimalField(max_digits=10, decimal_places=1)
    gas_cooker = models.DecimalField(max_digits=10, decimal_places=1)
    electric_cooker = models.DecimalField(max_digits=10, decimal_places=1)
    elec_gas_cooker = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    households = models.IntegerField()
