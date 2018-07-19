from django.db import models

# Create your models here.

class Months(models.Model):
    month_id = models.AutoField(primary_key=True)
    month = models.CharField(max_length=100)

class Sectors(models.Model):
    sector_id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=100)
    report = models.CharField(max_length=100)
    coverage = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    table_name = models.CharField(max_length=100)
    api_url = models.CharField(max_length=100)
    embed_script = models.TextField()

class Counties(models.Model):
    county_id = models.IntegerField(primary_key=True)
    county_name = models.CharField(max_length=200)

class SubCounty(models.Model):
    count_id = models.IntegerField(primary_key=True)
    subcounty_id = models.IntegerField()
    county = models.ForeignKey(Counties)
    subcounty_name = models.CharField(max_length=100)

class DiseaseList(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=150)

class Diseases(models.Model):
    disease_id =  models.AutoField(primary_key=True)
    year = models.IntegerField()
    accidents = models.IntegerField()
    other_diseases = models.IntegerField()
    diarrhoea = models.IntegerField()
    respiratory = models.IntegerField()
    skin = models.IntegerField()
    eye_infection = models.IntegerField()
    intestinal_worms = models.IntegerField()
    malaria = models.IntegerField()
    pneumonia = models.IntegerField()
    joint_pains = models.IntegerField()
    uti = models.IntegerField()

class Death(models.Model):
    death_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    anaemia = models.IntegerField()
    cancer = models.IntegerField()
    heart_disease = models.IntegerField()
    hiv_aids = models.IntegerField()
    malaria = models.IntegerField()
    menengitis = models.IntegerField()
    other_accidents = models.IntegerField()
    other_causes = models.IntegerField()
    pneumonia = models.IntegerField()
    road_traffic = models.IntegerField()
    tuberclosis = models.IntegerField()

class CountyOutpatientMorbidityAboveFive(models.Model):
    morbidity_above_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    disease = models.ForeignKey(DiseaseList)
    data = models.IntegerField()
    year = models.IntegerField()

class County_Outpatient_Morbidity_Below_Five(models.Model):
    morbidity_above_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    disease = models.ForeignKey(DiseaseList)
    data = models.IntegerField()
    year = models.IntegerField()

class Facilities(models.Model):
    facility_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    facilities = models.IntegerField()
    year = models.IntegerField()

class Immunization_Rate(models.Model):
    immunization_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    rate = models.FloatField()
    year = models.IntegerField()

class Medical_Personnel(models.Model):
    medical_personnel_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    bsc_nursing = models.IntegerField()
    clinical_officers = models.IntegerField()
    dentists = models.IntegerField()
    doctors = models.IntegerField()
    enrolled_nurses = models.IntegerField()
    pharmacists = models.IntegerField()
    pharmtech = models.IntegerField()
    health_officer = models.IntegerField()
    health_tech = models.IntegerField()
    registered_nurse = models.IntegerField()
    total = models.IntegerField()

class Nhif_Members(models.Model):
    nhif_member_id = models.AutoField(primary_key=True)
    formal_sector = models.IntegerField()
    informal_sector = models.IntegerField()
    total = models.IntegerField()
    year = models.CharField(max_length=50)

class Nhif_Resources(models.Model):
    resource_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=50)
    benefits = models.BigIntegerField()
    contributions_net_benefits = models.BigIntegerField()
    receipts = models.BigIntegerField()

class HealthFacilitiesByOwnershipOfHealthFacilities_Ids(models.Model):
    health_facility_id = models.AutoField(primary_key=True)
    health_facility = models.CharField(max_length=100)

class HealthFacilitiesByOwnershipOfHealthFacilities(models.Model):
    facility_ownership_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    health_facility = models.ForeignKey(HealthFacilitiesByOwnershipOfHealthFacilities_Ids)
    no_of_facilities = models.IntegerField()
    year = models.IntegerField()

class RegisteredMedicalPersonnel_Ids(models.Model):
    medical_personnel_id = models.AutoField(primary_key=True)
    medical_personnel = models.CharField(max_length=100)

class RegisteredMedicalPersonnel(models.Model):
    registered_medical_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    medical_personnel = models.ForeignKey(RegisteredMedicalPersonnel_Ids)
    no_of_personnel = models.IntegerField()
    gender = models.CharField(max_length=100)
    year = models.IntegerField()

class HospitalBedsAndCots(models.Model):
    bed_cot_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sub_county_id = models.IntegerField()
    beds = models.IntegerField()
    cots = models.IntegerField()
    year = models.IntegerField()

class Current_Use_Of_Contraception_By_County(models.Model):
    contraception_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    any_modem_method = models.DecimalField(max_digits=10, decimal_places=2)

class DistributionOfOutpatientVisitsByTypeOfHealthcareProvider(models.Model):
    health_facility_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    public = models.DecimalField(max_digits=10, decimal_places=2)
    private = models.DecimalField(max_digits=10, decimal_places=2)
    faith_based = models.DecimalField(max_digits=10,decimal_places=2)
    others = models.DecimalField(max_digits=10, decimal_places=2)

class Insurance_Coverage_By_Counties_And_Types(models.Model):
    insurance_coverage_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    insured = models.DecimalField(max_digits=10, decimal_places=2)
    nhif = models.DecimalField(max_digits=10, decimal_places=2)
    cbhi = models.DecimalField(max_digits=10, decimal_places=2)
    private = models.DecimalField(max_digits=10, decimal_places=2)
    others = models.DecimalField(max_digits=10, decimal_places=2)

class Maternal_Care(models.Model):
    maternal_care_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    percent_receiving_antenatal_care_from_a_skilled_provider = models.DecimalField(max_digits=10, decimal_places=2)
    percent_delivered_in_a_health_facility = models.DecimalField(max_digits=10, decimal_places=2)
    percent_delivered_by_a_skilled_provider = models.DecimalField(max_digits=10, decimal_places=2)

class Nutritional_Status_Of_Children(models.Model):
    nutrition_child_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    stunted = models.DecimalField(max_digits=10, decimal_places=2)
    wasted = models.DecimalField(max_digits=10, decimal_places=2)
    under_weight = models.DecimalField(max_digits=10, decimal_places=2)

class Nutritional_Status_Of_Women(models.Model):
    nutrition_adult_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    undernutrition = models.DecimalField(max_digits=10, decimal_places=2)
    normal = models.DecimalField(max_digits=10, decimal_places=2)
    overweight = models.DecimalField(max_digits=10, decimal_places=2)
    obese = models.DecimalField(max_digits=10, decimal_places=2)

class Registered_Medical_Laboratories_By_Counties(models.Model):
    reg_med_lab_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    class_a = models.IntegerField()
    class_b = models.IntegerField()
    class_c = models.IntegerField()
    class_d = models.IntegerField()
    class_e = models.IntegerField()
    class_f = models.IntegerField()
    unknown = models.IntegerField()

class Use_Of_Mosquito_Nets_By_Children(models.Model):
    use_mosquito_net_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    children_under_five_years_who_slept_under_nets_last_night = models.DecimalField(max_digits=10, decimal_places=2)

class Hiv_Aids_Awareness_And_Testing(models.Model):
    awareness_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    male = models.DecimalField(max_digits=10, decimal_places=2)
    female = models.DecimalField(max_digits=10, decimal_places=2)
    hiv_awareness = models.CharField(max_length=100)

class Registered_Active_Nhif_Members_By_County(models.Model):
    member_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    formal = models.IntegerField()
    informal = models.IntegerField()
    year = models.CharField(max_length=10)

class Registered_Active_Nhif_Members_Nationally(models.Model):
    member_id = models.AutoField(primary_key=True)
    formal = models.IntegerField()
    informal = models.IntegerField()
    year = models.CharField(max_length=10)


############################################KIHBIS II############################################
class Kihibs_Incidence_Of_Sickness_Injury(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    sick_injured = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()
    gender = models.CharField(max_length=10)

class Kihibs_Reported_Being_Sick_Injured_By_Type_Of_Sickness(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    fever_malaria = models.DecimalField(max_digits=10, decimal_places=1)
    stomach_problems = models.DecimalField(max_digits=10, decimal_places=1)
    diarrhoea = models.DecimalField(max_digits=10, decimal_places=1)
    vomiting = models.DecimalField(max_digits=10, decimal_places=1)
    upper_respiratory_infection = models.DecimalField(max_digits=10, decimal_places=1)
    lower_respiratory_infection = models.DecimalField(max_digits=10, decimal_places=1)
    flu = models.DecimalField(max_digits=10, decimal_places=1)
    asthma = models.DecimalField(max_digits=10, decimal_places=1)
    headache = models.DecimalField(max_digits=10, decimal_places=1)
    skin_problem = models.DecimalField(max_digits=10, decimal_places=1)
    dental_problem = models.DecimalField(max_digits=10, decimal_places=1)
    eye_problem = models.DecimalField(max_digits=10, decimal_places=1)
    ear_nose_throat = models.DecimalField(max_digits=10, decimal_places=1)
    backache = models.DecimalField(max_digits=10, decimal_places=1)
    tb = models.DecimalField(max_digits=10, decimal_places=1)
    heart_problem = models.DecimalField(max_digits=10, decimal_places=1)
    blood_pressure = models.DecimalField(max_digits=10, decimal_places=1)
    pain_while_passing_urine = models.DecimalField(max_digits=10, decimal_places=1)
    diabetes = models.DecimalField(max_digits=10, decimal_places=1)
    mental_disorder = models.DecimalField(max_digits=10, decimal_places=1)
    stis = models.DecimalField(max_digits=10, decimal_places=1)
    burn = models.DecimalField(max_digits=10, decimal_places=1)
    fracture = models.DecimalField(max_digits=10, decimal_places=1)
    wound_cut = models.DecimalField(max_digits=10, decimal_places=1)
    poisoning = models.DecimalField(max_digits=10, decimal_places=1)
    pregnancy_related = models.DecimalField(max_digits=10, decimal_places=1)
    cancer = models.DecimalField(max_digits=10, decimal_places=1)
    other_long_term_illness = models.DecimalField(max_digits=10, decimal_places=1)
    hiv_aids = models.DecimalField(max_digits=10, decimal_places=1)
    typhoid = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Reported_Sickness_By_Age_Group(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    percentage_distribution = models.DecimalField(max_digits=10, decimal_places=1)
    age_group = models.CharField(max_length=10)

class Kihibs_Reported_Being_Sick_Injured_By_Cause(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    percentage_distribution = models.DecimalField(max_digits=10, decimal_places=1)
    cause = models.CharField(max_length=10)

class Kihibs_Who_Diagnosed_Illness_Injury(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    health_worker = models.DecimalField(max_digits=10, decimal_places=1)
    traditional_healer = models.DecimalField(max_digits=10, decimal_places=1)
    non_household_member = models.DecimalField(max_digits=10, decimal_places=1)
    self = models.DecimalField(max_digits=10, decimal_places=1)
    herbalist = models.DecimalField(max_digits=10, decimal_places=1)
    faith_healer = models.DecimalField(max_digits=10, decimal_places=1)
    household_member = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Reported_Sickness_By_No_Of_Days_Missed(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    percentage = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_days = models.CharField(max_length=10)

class kihibs_reported_sickness_by_health_provider(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    percentage_distribution = models.DecimalField(max_digits=10, decimal_places=1)
    health_provider = models.CharField(max_length=10)

class Kihibs_Type_Of_Health_Care_Sought(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    curative = models.DecimalField(max_digits=10, decimal_places=1)
    promotive_preventive = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Received_Free_Medical_Services(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    percentage_distribution = models.DecimalField(max_digits=10, decimal_places=1)
    service_type = models.CharField(max_length=10)

class Kihibs_Disability_By_Type(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    visual = models.DecimalField(max_digits=10, decimal_places=1)
    hearing = models.DecimalField(max_digits=10, decimal_places=1)
    speech = models.DecimalField(max_digits=10, decimal_places=1)
    physical = models.DecimalField(max_digits=10, decimal_places=1)
    mental = models.DecimalField(max_digits=10, decimal_places=1)
    self_care = models.DecimalField(max_digits=10, decimal_places=1)
    others = models.DecimalField(max_digits=10, decimal_places=1)
    any_disability = models.DecimalField(max_digits=10, decimal_places=1)
    no_disability = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Disability_That_Had_Difficulty(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    yes = models.DecimalField(max_digits=10, decimal_places=1)
    no = models.DecimalField(max_digits=10, decimal_places=1)
    dont_know = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Health_Insurance_Cover_By_Type(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    nhif = models.DecimalField(max_digits=10, decimal_places=1)
    private_contributory = models.DecimalField(max_digits=10, decimal_places=1)
    private_non_contributory = models.DecimalField(max_digits=10, decimal_places=1)
    employee_contributory = models.DecimalField(max_digits=10, decimal_places=1)
    employee_non_contributory = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Children_By_Place_Of_Delivery(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    hospital = models.DecimalField(max_digits=10, decimal_places=1)
    health_centre = models.DecimalField(max_digits=10, decimal_places=1)
    clininc_dispensary = models.DecimalField(max_digits=10, decimal_places=1)
    maternity_home = models.DecimalField(max_digits=10, decimal_places=1)
    at_home = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Children_By_Who_Assisted_At_Birth(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    doctor = models.DecimalField(max_digits=10, decimal_places=1)
    midwife_nurse = models.DecimalField(max_digits=10, decimal_places=1)
    tba = models.DecimalField(max_digits=10, decimal_places=1)
    ttba = models.DecimalField(max_digits=10, decimal_places=1)
    self = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Children_Immmunized_Against_Measles(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    measles_vaccination = models.CharField(max_length=50)
    proportion = models.DecimalField(max_digits=10, decimal_places=1)

class Kihibs_Children_That_Had_Diarrhoea(models.Model):
    proportion_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    yes = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Type_Of_Food_Given_During_Diarrhoea(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    nothing = models.DecimalField(max_digits=10, decimal_places=1)
    commercial = models.DecimalField(max_digits=10, decimal_places=1)
    other_semi_solid = models.DecimalField(max_digits=10, decimal_places=1)
    fruits = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Type_Of_Fluid_Of_Food_Given_During_Diarrhoea(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    nothing = models.DecimalField(max_digits=10, decimal_places=1)
    breastmilk = models.DecimalField(max_digits=10, decimal_places=1)
    porridge = models.DecimalField(max_digits=10, decimal_places=1)
    water_alone = models.DecimalField(max_digits=10, decimal_places=1)
    other_milk = models.DecimalField(max_digits=10, decimal_places=1)
    other = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

class Kihibs_Children_By_Additional_Supplement(models.Model):
    distribution_id = models.AutoField(primary_key=True)
    county = models.ForeignKey(Counties)
    zinc_solution = models.DecimalField(max_digits=10, decimal_places=1)
    sugar_salt_solution = models.DecimalField(max_digits=10, decimal_places=1)
    other_solutions = models.DecimalField(max_digits=10, decimal_places=1)
    none = models.DecimalField(max_digits=10, decimal_places=1)
    not_stated = models.DecimalField(max_digits=10, decimal_places=1)
    no_of_individuals = models.IntegerField()

############################################Gender Fact Sheet############################################

class Early_Childhood_Mortality_Rates_By_Sex (models.Model):
    rate_id = models.AutoField(primary_key=True)
    mortality_rate = models.DecimalField(max_digits=10, decimal_places=1)
    status = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    year = models.CharField(max_length=10)

class Fertility_By_Education_Status (models.Model):
    fertility_id = models.AutoField(primary_key=True)
    fertility = models.DecimalField(max_digits=10, decimal_places=1)
    education_status = models.CharField(max_length=20)
    year = models.CharField(max_length=10)

class Fertility_Rate_By_Age_And_Residence (models.Model):
    fertility_id = models.AutoField(primary_key=True)
    fertility_rate = models.DecimalField(max_digits=10, decimal_places=1)
    age_group = models.CharField(max_length=10)
    residence = models.CharField(max_length=10)
    year = models.CharField(max_length=10)

class Percentage_Adults_Who_Are_Current_Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    age_group = models.CharField(max_length=10)
    women = models.DecimalField(max_digits=10, decimal_places=1)
    men = models.DecimalField(max_digits=10, decimal_places=1)
    category = models.CharField(max_length=10)

class Percentage_Incidence_Of_Diseases_In_Kenya (models.Model):
    incidence_id  = models.AutoField(primary_key=True)
    percentage_incidence = models.DecimalField(max_digits=10, decimal_places=1)
    disease  = models.CharField(max_length=20)
    year = models.IntegerField()

class Percentage_Who_Drink_Alcohol_By_Age (models.Model):
    percentage_id  = models.AutoField(primary_key=True)
    age = models.CharField(max_length=10)
    women = models.DecimalField(max_digits=10, decimal_places=1)
    men = models.DecimalField(max_digits=10, decimal_places=1)

class Place_Of_Delivery (models.Model):
    place_id  = models.AutoField(primary_key=True)
    number = models.DecimalField(max_digits=10, decimal_places=1)
    place = models.CharField(max_length=20)
    year = models.CharField(max_length=10)

class Prevalence_Of_Overweight_And_Obesity(models.Model):
    prevalence_id = models.AutoField(primary_key=True)
    age_group = models.CharField(max_length=10)
    women = models.IntegerField()
    men = models.IntegerField()
    total = models.IntegerField()
    category = models.CharField(max_length=20)


