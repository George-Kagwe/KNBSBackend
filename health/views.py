from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.defaultfilters import register
from django.utils import translation
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from health.models import CountyOutpatientMorbidityAboveFive, Counties, DiseaseList, Diseases, Death, \
    County_Outpatient_Morbidity_Below_Five, Facilities, Medical_Personnel, Nhif_Members, Nhif_Resources, \
    Immunization_Rate, HealthFacilitiesByOwnershipOfHealthFacilities, HealthFacilitiesByOwnershipOfHealthFacilities_Ids, \
    RegisteredMedicalPersonnel, RegisteredMedicalPersonnel_Ids, HospitalBedsAndCots, SubCounty, \
    Current_Use_Of_Contraception_By_County, DistributionOfOutpatientVisitsByTypeOfHealthcareProvider, \
    Insurance_Coverage_By_Counties_And_Types, Maternal_Care, Nutritional_Status_Of_Children, \
    Nutritional_Status_Of_Women, Registered_Medical_Laboratories_By_Counties, Use_Of_Mosquito_Nets_By_Children, \
    Hiv_Aids_Awareness_And_Testing, Registered_Active_Nhif_Members_By_County, Sectors, \
    Kihibs_Incidence_Of_Sickness_Injury, Kihibs_Reported_Being_Sick_Injured_By_Type_Of_Sickness, \
    Kihibs_Reported_Sickness_By_Age_Group, Kihibs_Reported_Being_Sick_Injured_By_Cause, \
    Kihibs_Who_Diagnosed_Illness_Injury, Kihibs_Reported_Sickness_By_No_Of_Days_Missed, \
    kihibs_reported_sickness_by_health_provider, Kihibs_Type_Of_Health_Care_Sought, \
    Kihibs_Received_Free_Medical_Services, Kihibs_Disability_By_Type, Kihibs_Disability_That_Had_Difficulty, \
    Kihibs_Health_Insurance_Cover_By_Type, Kihibs_Children_By_Place_Of_Delivery, \
    Kihibs_Children_By_Who_Assisted_At_Birth, Kihibs_Children_Immmunized_Against_Measles, \
    Kihibs_Children_That_Had_Diarrhoea, Kihibs_Type_Of_Food_Given_During_Diarrhoea, \
    Kihibs_Type_Of_Fluid_Of_Food_Given_During_Diarrhoea, Kihibs_Children_By_Additional_Supplement


@register.filter(name = 'range')
def filter_year(start, end):
    return range(start, end)

# @register.filter(name = 'kaunti')
# def counties(request):
#     all_counties = Counties.objects.all()
#     return render(request, all_counties)

def index(request):
    return render(request, template_name='knbs_bi/index.html')


def health(request):
     return render(request, template_name='knbs_bi/health.html')
#===============================Health Sectors===============================
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def healthSectors(request):
    all_sectors = Sectors.objects.all()

    sectors = []

    if all_sectors:
        for sector in all_sectors:
            c = {'sector_name': sector.sector_name, 'report': sector.report, 'coverage': sector.coverage,
                 'source': sector.source, 'api_url': sector.api_url}
            sectors.append(c)
    else:
        pass
    return Response(sectors)

#===============================County Full Immunization Coverage Rate===============================
#Launch Page
def allImmunizationRate(request):
    immunization = Immunization_Rate.objects.all()

    rates = []

    if immunization:
        for rate in immunization:
            counties = Counties.objects.get(county_id=rate.county_id)
            c = {'immune_id':rate.immunization_id, 'county': counties.county_name, 'rate': rate.rate, 'year': rate.year}
            rates.append(c)
            context = {'rates': rates}

    return render(request, 'knbs_bi/health_immunization_history.html', context)

# All Immunization
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def immunizationRate(request):
    all_immunization = Immunization_Rate.objects.all()

    rates = []

    if all_immunization:
        for rate in all_immunization:
            counties = Counties.objects.get(county_id=rate.county_id)
            c = {'county': counties.county_name, 'rate': rate.rate, 'year': rate.year}
            rates.append(c)
    else:
        pass
    return Response(rates)

# Add Immunization
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addImmunization(request):
    # name = request.data["county"]
    # return HttpResponse("Before")
    counties = Counties.objects.get(county_name=request.data['county'])
    #kaunti = counties.county_id
    # return HttpResponse(kaunti)

    if counties:
        kaunti = counties.county_id

        immune_add = Immunization_Rate(county_id=kaunti, rate=request.data['rate'],
                                       year=request.data['year'])

        if immune_add:
            immune_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Immunization
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editImmunization(request):
    immune_edit = Immunization_Rate.objects.get(immunization_id=request.data['immune_id'])




    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        #print("Got it")
        if counties:
            immune_edit.county_id = counties.county_id
    if 'rate' in request.data:
        immune_edit.rate = request.data['rate']
    if 'year' in request.data:
        immune_edit.year = request.data['year']

    immune_edit.save()
    #response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

#Immunization Add View
def addImmunizationView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    # translation.activate('en')
    return render(request, 'knbs_bi/health_immunization_add.html', context)

#Immunization Edit View
def editImmunizationView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_immunization_edit.html', context)

#===============================COUNTY MORBIDITY FOR PATIENTS ABOVE FIVE===============================
#Launch Page
def morbidityAbove(request):
    morb_above = CountyOutpatientMorbidityAboveFive.objects.all()

    records = []

    if morb_above:
        for record in morb_above:
            counties = Counties.objects.get(county_id=record.county_id)
            disease = DiseaseList.objects.get(disease_id=record.disease_id)
            c = {'morb_id': record.morbidity_above_id, 'county': counties.county_name, 'county_id': record.county_id,
                 'disease': disease.disease_name, 'data': record.data,
                 'year': record.year}
            records.append(c)
            context = {'records': records}
    return render(request, 'knbs_bi/health_morbidity_above_history.html', context)

#Add Morbidity View
def addMorbidityAboveView(request):
    all_counties = Counties.objects.all()
    all_diseases = DiseaseList.objects.all()
    context = {'counties': all_counties, 'diseases': all_diseases}
    return render(request, 'knbs_bi/health_morbidity_above_add.html', context)

#Edit Morbidity View
def editMorbidityAboveView(request):
    all_counties = Counties.objects.all()
    all_diseases = DiseaseList.objects.all()
    context = {'counties': all_counties, 'diseases': all_diseases}
    return render(request, 'knbs_bi/health_morbidity_above_edit.html', context)

#All Morbidity Below Five
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def aboveFive(request):
    above_five = CountyOutpatientMorbidityAboveFive.objects.all()

    records = []

    if above_five:
        for record in above_five:
            counties = Counties.objects.get(county_id=record.county_id)
            disease = DiseaseList.objects.get(disease_id=record.disease_id)
            c = {'county': counties.county_name, 'disease': disease.disease_name, 'data': record.data, 'year':record.year}
            records.append(c)
    else:
        pass
    return Response(records)

#Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAboveFive(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    disease = DiseaseList.objects.get(disease_name=request.data['disease'])

    if counties and disease:
        kaunti = counties.county_id
        disease = disease.disease_id

        above_five_add = CountyOutpatientMorbidityAboveFive(county_id=kaunti, disease_id=disease,
                                                                data=request.data['data'], year=request.data['year'])
        if above_five_add:
            above_five_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAboveFive(request):
    above_five_edit = CountyOutpatientMorbidityAboveFive.objects.get(morbidity_above_id=request.data['morb_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            above_five_edit.county_id = counties.county_id

    if 'disease' in request.data:
        disease = DiseaseList.objects.get(disease_name=request.data['disease'])
        if disease:
            above_five_edit.disease_id = disease.disease_id

    if 'data' in request.data:
        above_five_edit.data = request.data['data']

    if 'year' in request.data:
        above_five_edit.year = request.data['year']

    above_five_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================COUNTY MORBIDITY FOR PATIENTS BELOW FIVE===============================
#Launch Page
def morbidityBelow(request):
    morb_below = County_Outpatient_Morbidity_Below_Five.objects.all()

    records = []

    if morb_below:
        for record in morb_below:
            counties = Counties.objects.get(county_id=record.county_id)
            disease = DiseaseList.objects.get(disease_id=record.disease_id)
            c = {'morb_id':record.morbidity_above_id, 'county': counties.county_name, 'county_id': record.county_id, 'disease': disease.disease_name, 'data': record.data,
                 'year': record.year}
            records.append(c)
            context = {'records': records}
    return render(request, 'knbs_bi/health_morbidity_below_history.html', context)

#Add Morbidity View
def addMorbidityView(request):
    all_counties = Counties.objects.all()
    all_diseases = DiseaseList.objects.all()
    context = {'counties': all_counties, 'diseases': all_diseases}
    return render(request, 'knbs_bi/health_morbidity_below_add.html', context)

#Edit Morbidity View
def editMorbidityView(request):
    all_counties = Counties.objects.all()
    all_diseases = DiseaseList.objects.all()
    context = {'counties': all_counties, 'diseases': all_diseases}
    return render(request, 'knbs_bi/health_morbidity_below_edit.html', context)

#All Morbidity Below Five
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def belowFive(request):
    below_five = County_Outpatient_Morbidity_Below_Five.objects.all()

    records = []

    if below_five:
        for record in below_five:
            counties = Counties.objects.get(county_id=record.county_id)
            disease = DiseaseList.objects.get(disease_id=record.disease_id)
            c = {'county': counties.county_name, 'disease': disease.disease_name, 'data': record.data, 'year':record.year}
            records.append(c)
    else:
        pass
    return Response(records)

#Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addBelowFive(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    disease = DiseaseList.objects.get(disease_name=request.data['disease'])

    if counties and disease:
        kaunti = counties.county_id
        disease = disease.disease_id

        below_five_add = County_Outpatient_Morbidity_Below_Five(county_id=kaunti, disease_id=disease,
                                                                data=request.data['data'], year=request.data['year'])
        if below_five_add:
            below_five_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editBelowFive(request):
    below_five_edit = County_Outpatient_Morbidity_Below_Five.objects.get(morbidity_above_id=request.data['morb_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            below_five_edit.county_id = counties.county_id

    if 'disease' in request.data:
        disease = DiseaseList.objects.get(disease_name=request.data['disease'])
        if disease:
            below_five_edit.disease_id = disease.disease_id

    if 'data' in request.data:
        below_five_edit.data = request.data['data']

    if 'year' in request.data:
        below_five_edit.year = request.data['year']

    below_five_edit.save()
    response = {'Successfully Updated'}
    return Response(response)


#===============================County Health Facilities by Ownership===============================
#Launch Page
def healthFacility(request):
    health = HealthFacilitiesByOwnershipOfHealthFacilities.objects.all()

    facilities = []

    if health:
        for facility in health:
            counties = Counties.objects.get(county_id=facility.county_id)
            fcl = HealthFacilitiesByOwnershipOfHealthFacilities_Ids.objects.get(health_facility_id=facility.health_facility_id)
            c = {'ownership_id': facility.facility_ownership_id, 'county': counties.county_name, 'facility': fcl.health_facility,
                 'no_facilities': facility.no_of_facilities, 'year': facility.year}
            facilities.append(c)
            context = {'facilities': facilities}
    return render(request, 'knbs_bi/health_facilities_by_ownership.html', context)

#Edit Health Facilities Ownership
def editHealthOwnershipView(request):
    all_counties = Counties.objects.all()
    facility = HealthFacilitiesByOwnershipOfHealthFacilities_Ids.objects.all()
    context = {'counties': all_counties, 'facilities': facility}
    return render(request, 'knbs_bi/health_facilities_by_ownership_edit.html', context)

#Add Health Facilities Ownership
def addHealthOwnershipView(request):
    all_counties = Counties.objects.all()
    facility = HealthFacilitiesByOwnershipOfHealthFacilities_Ids.objects.all()
    context = {'counties': all_counties, 'facilities': facility}
    return render(request, 'knbs_bi/health_facilities_by_ownership_add.html', context)


#===============================County Health Facilities===============================
#Launch Page
def healthFacilityView(request):
    health = Facilities.objects.all()

    facilities = []

    if health:
        for facility in health:
            counties = Counties.objects.get(county_id=facility.county_id)
            c = {'id': facility.facility_id, 'county': counties.county_name, 'no_of_facilities':facility.facilities, 'year': facility.year}
            facilities.append(c)
            context = {'facilities': facilities}
    return render(request, 'knbs_bi/health_facilities.html', context)

#All Health Facilities
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allHealthFacilities(request):
    all_facilities = Facilities.objects.all()

    facilities = []

    if all_facilities:
        for facility in all_facilities:
            counties = Counties.objects.get(county_id=facility.county_id)
            c = {'county': counties.county_name, 'no_of_facilities':facility.facilities, 'year':facility.year}
            facilities.append(c)
    else:
        pass

    return Response(facilities)


#===============================Registered Medical Personnel===============================
#Launch Page
def registeredMedicalPersonnelView(request):
    all_personnel = RegisteredMedicalPersonnel.objects.all()

    personnel = []

    if all_personnel:
        for person in all_personnel:
            counties = Counties.objects.get(county_id=person.county_id)
            medic = RegisteredMedicalPersonnel_Ids.objects.get(medical_personnel_id=person.medical_personnel_id)
            c = {'id':person.registered_medical_id, 'county':counties.county_name, 'medical_personnel':medic.medical_personnel, 'no_of_personnel':person.no_of_personnel,
                 'gender':person.gender, 'year': person.year}
            personnel.append(c)
            context = {'personnel': personnel}
    else:
        pass

    return render(request, 'knbs_bi/health_registered_medical_personnel.html', context)

#===============================Hospital Beds and Cots===============================
#Launch Page
def hospitalBedsCotsView(request):
    beds_cots = HospitalBedsAndCots.objects.all()

    records = []

    if beds_cots:
        for record in beds_cots:
            counties = Counties.objects.get(county_id=record.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=record.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'id':record.bed_cot_id, 'county':counties.county_name, 'subcounty':sc.subcounty_name, 'beds':record.beds,
                         'cots':record.cots, 'year': record.year}
                    records.append(c)
                    context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_hospital_beds_and_cots.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def hospitalBedsCots(request):
    beds_cots = HospitalBedsAndCots.objects.all()

    records = []

    if beds_cots:
        for record in beds_cots:
            counties = Counties.objects.get(county_id=record.county_id)
            subcounty = SubCounty.objects.filter(subcounty_id=record.sub_county_id)

            if subcounty:
                for sc in subcounty:
                    c = {'county':counties.county_name, 'subcounty':sc.subcounty_name, 'beds':record.beds,
                         'cots':record.cots, 'year': record.year}
                    records.append(c)
    else:
        pass

    return Response(records)

#Add Morbidity View
def addHospitalBedsCotsView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/health_hospital_beds_and_cots_add.html', context)

#Edit Morbidity View
def editHospitalBedsCotsView(request):
    all_counties = Counties.objects.all()
    sub_county = SubCounty.objects.all()
    context = {'counties': all_counties, 'sub': sub_county}
    return render(request, 'knbs_bi/health_hospital_beds_and_cots_edit.html', context)

# #All Morbidity Below Five
# @api_view(http_method_names=['GET'])
# @renderer_classes((JSONRenderer,))
# def belowFive(request):
#     below_five = County_Outpatient_Morbidity_Below_Five.objects.all()
#
#     records = []
#
#     if below_five:
#         for record in below_five:
#             counties = Counties.objects.get(county_id=record.county_id)
#             disease = DiseaseList.objects.get(disease_id=record.disease_id)
#             c = {'county': counties.county_name, 'disease': disease.disease_name, 'data': record.data, 'year':record.year}
#             records.append(c)
#     else:
#         pass
#     return Response(records)

#Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addHospitalBedsCots(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])

    if counties and sub:
        kaunti = counties.county_id

        beds_add = HospitalBedsAndCots(county_id=kaunti, sub_county_id=sub.subcounty_id, beds=request.data['beds'], cots=request.data['cots'],
                                       year=request.data['year'])
        if beds_add:
            beds_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editHospitalBedsCots(request):
    beds_edit = HospitalBedsAndCots.objects.get(bed_cot_id=request.data['bed_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            beds_edit.county_id = counties.county_id

    if 'sub_county' in request.data:
        sub = SubCounty.objects.get(subcounty_name=request.data['sub_county'])
        if sub:
            beds_edit.sub_county_id = sub.subcounty_id

    if 'beds' in request.data:
        beds_edit.beds = request.data['beds']

    if 'cots' in request.data:
        beds_edit.cots = request.data['cots']

    if 'year' in request.data:
        beds_edit.year = request.data['year']

    beds_edit.save()
    response = {'Successfully Updated'}
    return Response(response)
#===============================NHIF Resources===============================
#Launch Page
def allNhifResourcesView(request):
    all_resources = Nhif_Resources.objects.all()

    resources = []

    if all_resources:
        for resource in all_resources:
            c = {'id':resource.resource_id, 'year': resource.year, 'benefits':resource.benefits, 'contributions_net_benefits':resource.contributions_net_benefits, 'receipts':resource.receipts}
            resources.append(c)
            context = {'resources': resources}
    else:
        pass

    return render(request, 'knbs_bi/health_nhif_resources.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allNhifResources(request):
    all_resources = Nhif_Resources.objects.all()

    resources = []

    if all_resources:
        for resource in all_resources:
            c = {'year': resource.year, 'benefits':resource.benefits, 'contributions_net_benefits':resource.contributions_net_benefits, 'receipts':resource.receipts}
            resources.append(c)
    else:
        pass

    return Response(resources)

#===============================NHIF Members===============================
#Launch Page
def allMembersView(request):
    all_members = Nhif_Members.objects.all()

    members = []

    if all_members:
        for member in all_members:
            c = {'id':member.nhif_member_id, 'no_of_formal': member.formal_sector, 'no_of_informal':member.informal_sector, 'total':member.total, 'year':member.year}
            members.append(c)
            context = {'members': members}
    else:
        pass

    return render(request, 'knbs_bi/health_nhif_members.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allMembers(request):
    all_members = Nhif_Members.objects.all()

    members = []

    if all_members:
        for member in all_members:
            c = {'no_of_formal': member.formal_sector, 'no_of_informal':member.informal_sector, 'total':member.total, 'year':member.year}
            members.append(c)
    else:
        pass

    return Response(members)

#==============================================================
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def diseaseList(request):
    disease_list = DiseaseList.objects.all()

    diseases = []

    if disease_list:
        for disease in diseases:
            c = {'disease_name': disease.disease_name}
            diseases.append(c)
    else:
        pass
    return Response(diseases)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allDiseases(request):
    all_diseases = Diseases.objects.all()

    diseases = []

    if all_diseases:
        for disease in all_diseases:
            #print(reg_births[birth].county)
            c = {'year': disease.year, 'no_of_accidents':disease.accidents, 'no_of_other_diseases':disease.other_diseases, 'no_diarrhoea_cases':disease.diarrhoea,'no_respiratory_cases':disease.respiratory,
                 'no_skin_cases':disease.skin, 'no_of_eye_infections':disease.eye_infection,  'no_of_worms':disease.intestinal_worms, 'no_of_malaria':disease.malaria,
                 'no_pneumonia_cases':disease.pneumonia, 'no_joints_cases':disease.joint_pains, 'no_uti_cases':disease.uti}
            diseases.append(c)
    else:
        pass

    return Response(diseases)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def Deaths(request):
    all_deaths = Death.objects.all()

    deaths = []

    if all_deaths:
        for death in all_deaths:
            #print(reg_births[birth].county)
            c = {'year': death.year, 'anaemia_cases':death.anaemia, 'cancer_cases':death.cancer, 'heart_cases':death.heart_disease,'hiv_cases':death.hiv_aids,
                 'malaria_cases':death.malaria, 'menengitis_cases':death.menengitis, 'accidents_cases':death.other_accidents, 'causes_cases':death.other_causes,
                 'pneumonia_cases':death.pneumonia, 'traffic_cases':death.road_traffic, 'tuberculosis_cases':death.tuberclosis}
            deaths.append(c)
    else:
        pass

    return Response(deaths)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allPersonnel(request):
    all_personnel = Medical_Personnel.objects.all()

    personnel = []

    if all_personnel:
        for person in all_personnel:
            #print(reg_births[birth].county)
            c = {'year': person.year, 'no_of_nursing':person.bsc_nursing, 'no_of_clinical_officers':person.clinical_officers, 'no_of_dentists':person.dentists,'no_of_doctors':person.doctors,
                 'no_of_nurses':person.enrolled_nurses, 'no_of_pharmacists':person.pharmacists,  'no_of_pharmtech':person.pharmtech, 'no_of_health_officer':person.health_officer,
                 'no_of_tech':person.health_tech, 'no_of_reg_nurse':person.registered_nurse, 'no_of_total':person.total}
            personnel.append(c)
    else:
        pass

    return Response(personnel)

#===============================Current_Use_Of_Contraception_By_County===============================
#Launch Page
def contraceptionUseCountyView(request):
    cont_use = Current_Use_Of_Contraception_By_County.objects.all()

    records = []

    if cont_use:
        for record in cont_use:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id':record.contraception_id, 'county':counties.county_name, 'modem_method': record.any_modem_method}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_current_use_of_contraception_by_county.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def contraceptionUseCounty(request):
    cont_use = Current_Use_Of_Contraception_By_County.objects.all()

    records = []

    if cont_use:
        for record in cont_use:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county':counties.county_name, 'modem_method': record.any_modem_method}
            records.append(c)
    else:
        pass

    return Response(records)

#Add Morbidity View
def addContraceptionUseCountyView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_current_use_of_contraception_by_county_add.html', context)

#Edit Morbidity View
def editContraceptionUseCountyView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_current_use_of_contraception_by_county_edit.html', context)

#Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addContraceptionUseCounty(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        cont_add = Current_Use_Of_Contraception_By_County(county_id=kaunti, any_modem_method=request.data['method'])
        if cont_add:
            cont_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editContraceptionUseCounty(request):
    cont_edit = Current_Use_Of_Contraception_By_County.objects.get(contraception_id=request.data['cont_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            cont_edit.county_id = counties.county_id

    if 'method' in request.data:
        cont_edit.any_modem_method = request.data['method']

    cont_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================DistributionOfOutpatientVisitsByTypeOfHealthcareProvider===============================
def distributionOutpatientProviderView(request):
    dist_outpatient = DistributionOfOutpatientVisitsByTypeOfHealthcareProvider.objects.all()

    records = []

    if dist_outpatient:
        for record in dist_outpatient:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id':record.health_facility_id, 'county':counties.county_name, 'public': record.public, 'private': record.private, 'faith_based': record.faith_based,
                 'others': record.others}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_distribution_of_outpatient_visits_by_type_of_healthcare_provider.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def distributionOutpatientProvider(request):
    dist_outpatient = DistributionOfOutpatientVisitsByTypeOfHealthcareProvider.objects.all()

    records = []

    if dist_outpatient:
        for record in dist_outpatient:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county':counties.county_name, 'pub_lic': record.public, 'pri_vate': record.private, 'faith_based': record.faith_based,
                 'others': record.others}
            records.append(c)
    else:
        pass

    return Response(records)

#Add Morbidity View
def addDistributionOutpatientProviderView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_distribution_of_outpatient_visits_by_type_of_healthcare_provider_add.html', context)

#Edit Morbidity View
def editDistributionOutpatientProviderView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_distribution_of_outpatient_visits_by_type_of_healthcare_provider_edit.html', context)

#Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addDistributionOutpatientProvider(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        dist_outpatient_add = DistributionOfOutpatientVisitsByTypeOfHealthcareProvider(county_id=kaunti, public=request.data['public'], private=request.data['private'],
                                                                                       faith_based=request.data['faith_based'], others=request.data['others'])
        if dist_outpatient_add:
            dist_outpatient_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editDistributionOutpatientProvider(request):
    dist_outpatient_edit = DistributionOfOutpatientVisitsByTypeOfHealthcareProvider.objects.get(health_facility_id=request.data['facility_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            dist_outpatient_edit.county_id = counties.county_id

    if 'public' in request.data:
        dist_outpatient_edit.public = request.data['public']

    if 'private' in request.data:
        dist_outpatient_edit.private = request.data['private']

    if 'faith_based' in request.data:
        dist_outpatient_edit.faith_based = request.data['faith_based']

    if 'others' in request.data:
        dist_outpatient_edit.others = request.data['others']

    dist_outpatient_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================Insurance_Coverage_By_Counties_And_Types===============================
def insuranceCoverageView(request):
    insurance = Insurance_Coverage_By_Counties_And_Types.objects.all()

    records = []

    if insurance:
        for record in insurance:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id':record.insurance_coverage_id, 'county':counties.county_name, 'insured': record.insured, 'nhif': record.nhif, 'cbhi': record.cbhi,
                 'private': record.private, 'others': record.others}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_insurance_coverage_by_counties_and_types.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def insuranceCoverage(request):
    insurance = Insurance_Coverage_By_Counties_And_Types.objects.all()

    records = []

    if insurance:
        for record in insurance:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county':counties.county_name, 'insured': record.insured, 'nhif': record.nhif, 'cbhi': record.cbhi,
                 'private': record.private, 'others': record.others}
            records.append(c)
    else:
        pass

    return Response(records)

#Add Morbidity View
def addInsuranceCoverageView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_insurance_coverage_by_counties_and_types_add.html', context)

#Edit Morbidity View
def editInsuranceCoverageView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_insurance_coverage_by_counties_and_types_edit.html', context)

#Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addInsuranceCoverage(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        insurance_add = Insurance_Coverage_By_Counties_And_Types(county_id=kaunti, insured=request.data['insured'], nhif=request.data['nhif'],
                                                                                       cbhi=request.data['cbhi'], private=request.data['private'], others=request.data['others'])
        if insurance_add:
            insurance_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editInsuranceCoverage(request):
    insurance_edit = Insurance_Coverage_By_Counties_And_Types.objects.get(insurance_coverage_id=request.data['insurance_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            insurance_edit.county_id = counties.county_id

    if 'insured' in request.data:
        insurance_edit.insured = request.data['insured']

    if 'nhif' in request.data:
        insurance_edit.nhif = request.data['nhif']

    if 'cbhi' in request.data:
        insurance_edit.cbhi = request.data['cbhi']

    if 'private' in request.data:
        insurance_edit.private = request.data['private']

    if 'others' in request.data:
        insurance_edit.others = request.data['others']

    insurance_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================Maternal_Care===============================
def maternalCareView(request):
    maternal = Maternal_Care.objects.all()

    records = []

    if maternal:
        for record in maternal:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id':record.maternal_care_id, 'county':counties.county_name, 'antenatal_care': record.percent_receiving_antenatal_care_from_a_skilled_provider,
                 'delivered_in_health_facility': record.percent_delivered_in_a_health_facility,
                 'delivered_by_skilled_provider': record.percent_delivered_by_a_skilled_provider}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_maternal_care.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def maternalCare(request):
    maternal = Maternal_Care.objects.all()

    records = []

    if maternal:
        for record in maternal:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county':counties.county_name, 'antenatal_care': record.percent_receiving_antenatal_care_from_a_skilled_provider,
                 'delivered_in_health_facility': record.percent_delivered_in_a_health_facility,
                 'delivered_by_skilled_provider': record.percent_delivered_by_a_skilled_provider}
            records.append(c)
    else:
        pass

    return Response(records)

#Add Morbidity View
def addMaternalCareView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_maternal_care_add.html', context)

#Edit Morbidity View
def editMaternalCareView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_maternal_care_edit.html', context)

#Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addMaternalCare(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        maternal_add = Maternal_Care(county_id=kaunti, percent_receiving_antenatal_care_from_a_skilled_provider=request.data['antenatal'],
                                     percent_delivered_in_a_health_facility=request.data['health_facility'],
                                     percent_delivered_by_a_skilled_provider=request.data['skilled_provider'])
        if maternal_add:
            maternal_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editMaternalCare(request):
    maternal_edit = Maternal_Care.objects.get(maternal_care_id=request.data['maternal_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            maternal_edit.county_id = counties.county_id

    if 'antenatal' in request.data:
        maternal_edit.percent_receiving_antenatal_care_from_a_skilled_provider = request.data['antenatal']

    if 'health_facility' in request.data:
        maternal_edit.percent_delivered_in_a_health_facility = request.data['health_facility']

    if 'skilled_provider' in request.data:
        maternal_edit.percent_delivered_by_a_skilled_provider = request.data['skilled_provider']

    maternal_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================Nutritional_Status_Of_Children===============================
#Launch Page
def nutritionChildrenView(request):
    nutrition = Nutritional_Status_Of_Children.objects.all()

    records = []

    if nutrition:
        for record in nutrition:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id':record.nutrition_child_id, 'county':counties.county_name, 'stunted': record.stunted,
                 'wasted': record.wasted,
                 'under_weight': record.under_weight}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_nutritional_status_of_children.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def nutritionChildren(request):
    nutrition = Nutritional_Status_Of_Children.objects.all()

    records = []

    if nutrition:
        for record in nutrition:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county':counties.county_name, 'stunted': record.stunted,
                 'wasted': record.wasted,
                 'under_weight': record.under_weight}
            records.append(c)
    else:
        pass

    return Response(records)

#Add Morbidity View
def addNutritionChildrenView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_nutritional_status_of_children_add.html', context)

#Edit Morbidity View
def editNutritionChildrenView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_nutritional_status_of_children_edit.html', context)

#Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addNutritionChildren(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        nutrition_add = Nutritional_Status_Of_Children(county_id=kaunti, stunted=request.data['stunted'],
                                     wasted=request.data['wasted'],
                                     under_weight=request.data['under_weight'])
        if nutrition_add:
            nutrition_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editNutritionChildren(request):
    nutrition_edit = Nutritional_Status_Of_Children.objects.get(nutrition_child_id=request.data['nutrition_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            nutrition_edit.county_id = counties.county_id

    if 'stunted' in request.data:
        nutrition_edit.stunted = request.data['stunted']

    if 'wasted' in request.data:
        nutrition_edit.wasted = request.data['wasted']

    if 'under_weight' in request.data:
        nutrition_edit.under_weight = request.data['under_weight']

    nutrition_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================Nutritional_Status_Of_Women===============================
#Launch Page
def nutritionWomenView(request):
    nutrition = Nutritional_Status_Of_Women.objects.all()

    records = []

    if nutrition:
        for record in nutrition:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id':record.nutrition_adult_id, 'county':counties.county_name, 'under_nutrition': record.undernutrition,
                 'normal': record.normal, 'over_weight': record.overweight,
                 'obese': record.obese}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_nutritional_status_of_women.html', context)

#All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def nutritionWomen(request):
    nutrition = Nutritional_Status_Of_Women.objects.all()

    records = []

    if nutrition:
        for record in nutrition:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county':counties.county_name, 'under_nutrition': record.undernutrition,
                 'normal': record.normal, 'over_weight': record.overweight,
                 'obese': record.obese}
            records.append(c)
    else:
        pass

    return Response(records)

#Add Morbidity View
def addNutritionWomenView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_nutritional_status_of_women_add.html', context)

#Edit Morbidity View
def editNutritionWomenView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_nutritional_status_of_women_edit.html', context)

#Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addNutritionWomen(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        nutrition_add = Nutritional_Status_Of_Women(county_id=kaunti, undernutrition=request.data['nutrition'],
                                     normal=request.data['normal'], overweight=request.data['over_weight'],
                                     obese=request.data['obese'])
        if nutrition_add:
            nutrition_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editNutritionWomen(request):
    nutrition_edit = Nutritional_Status_Of_Women.objects.get(nutrition_adult_id=request.data['nutrition_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            nutrition_edit.county_id = counties.county_id

    if 'nutrition' in request.data:
        nutrition_edit.undernutrition = request.data['nutrition']

    if 'normal' in request.data:
        nutrition_edit.normal = request.data['normal']

    if 'over_weight' in request.data:
        nutrition_edit.overweight = request.data['over_weight']

    if 'obese' in request.data:
        nutrition_edit.obese = request.data['obese']

    nutrition_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================Registered_Medical_Laboratories_By_Counties===============================
#Launch Page
def registeredLabsView(request):
    labs = Registered_Medical_Laboratories_By_Counties.objects.all()

    records = []

    if labs:
        for record in labs:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id': record.reg_med_lab_id, 'county': counties.county_name, 'class_a': record.class_a, 'class_b': record.class_b,
                 'class_c': record.class_c, 'class_d': record.class_d,
                 'class_e': record.class_e, 'class_f': record.class_f,
                 'unknown': record.unknown}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_registered_medical_laboratories_by_counties.html', context)


# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def registeredLabs(request):
    labs = Registered_Medical_Laboratories_By_Counties.objects.all()

    records = []

    if labs:
        for record in labs:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county': counties.county_name, 'class_a': record.class_a, 'class_b': record.class_b,
                 'class_c': record.class_c, 'class_d': record.class_d,
                 'class_e': record.class_e, 'class_f': record.class_f,
                 'unknown': record.unknown}
            records.append(c)
    else:
        pass

    return Response(records)

# Add Morbidity View
def addRegisteredLabsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_registered_medical_laboratories_by_counties_add.html', context)


# Edit Morbidity View
def editRegisteredLabsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_registered_medical_laboratories_by_counties_edit.html', context)


# Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addRegisteredLabs(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        labs_add = Registered_Medical_Laboratories_By_Counties(county_id=kaunti, class_a=request.data['class_a'], class_b=request.data['class_b'],
                                                               class_c=request.data['class_c'], class_d=request.data['class_d'],
                                                               class_e=request.data['class_e'], class_f=request.data['class_f'],
                                                               unknown=request.data['unknown'])
        if labs_add:
            labs_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editRegisteredLabs(request):
    labs_edit = Registered_Medical_Laboratories_By_Counties.objects.get(reg_med_lab_id=request.data['lab_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            labs_edit.county_id = counties.county_id

    if 'class_a' in request.data:
        labs_edit.class_a = request.data['class_a']

    if 'class_b' in request.data:
        labs_edit.class_b = request.data['class_b']

    if 'class_c' in request.data:
        labs_edit.class_c = request.data['class_c']

    if 'class_d' in request.data:
        labs_edit.class_d = request.data['class_d']

    if 'class_e' in request.data:
        labs_edit.class_e = request.data['class_e']

    if 'class_f' in request.data:
        labs_edit.class_f = request.data['class_f']

    if 'unknown' in request.data:
        labs_edit.unknown = request.data['unknown']

    labs_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================Use_Of_Mosquito_Nets_By_Children===============================
#Launch Page
def mosquitoNetsView(request):
    nets = Use_Of_Mosquito_Nets_By_Children.objects.all()

    records = []

    if nets:
        for record in nets:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id': record.use_mosquito_net_id, 'county': counties.county_name, 'children': record.children_under_five_years_who_slept_under_nets_last_night}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_use_of_mosquito_nets_by_children.html', context)


# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def mosquitoNets(request):
    nets = Use_Of_Mosquito_Nets_By_Children.objects.all()

    records = []

    if nets:
        for record in nets:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county': counties.county_name, 'children': record.children_under_five_years_who_slept_under_nets_last_night}
            records.append(c)
    else:
        pass

    return Response(records)

# Add Morbidity View
def addMosquitoNetsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_use_of_mosquito_nets_by_children_add.html', context)


# Edit Morbidity View
def editMosquitoNetsView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_use_of_mosquito_nets_by_children_edit.html', context)


# Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addMosquitoNets(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        nets_add = Use_Of_Mosquito_Nets_By_Children(county_id=kaunti, children_under_five_years_who_slept_under_nets_last_night=request.data['children'])
        if nets_add:
            nets_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editMosquitoNets(request):
    nets_edit = Use_Of_Mosquito_Nets_By_Children.objects.get(use_mosquito_net_id=request.data['net_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            nets_edit.county_id = counties.county_id

    if 'children' in request.data:
        nets_edit.children_under_five_years_who_slept_under_nets_last_night = request.data['children']

    nets_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================Hiv_Aids_Awareness_And_Testing===============================
#Launch Page
def hivAwarenessView(request):
    awareness = Hiv_Aids_Awareness_And_Testing.objects.all()

    records = []

    if awareness:
        for record in awareness:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id': record.awareness_id, 'county': counties.county_name, 'male': record.male, 'female': record.female, 'hiv_awareness': record.hiv_awareness}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_hiv_aids_awareness_and_testing.html', context)


# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def hivAwareness(request):
    awareness = Hiv_Aids_Awareness_And_Testing.objects.all()

    records = []

    if awareness:
        for record in awareness:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county': counties.county_name, 'male': record.male, 'female': record.female, 'hiv_awareness': record.hiv_awareness}
            records.append(c)
    else:
        pass

    return Response(records)

# Add Morbidity View
def addHivAwarenessView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_hiv_aids_awareness_and_testing_add.html', context)


# Edit Morbidity View
def editHivAwarenessView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_hiv_aids_awareness_and_testing_edit.html', context)


# Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addHivAwareness(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        awareness_add = Hiv_Aids_Awareness_And_Testing(county_id=kaunti, male=request.data['male'], female=request.data['female'],
                                                  hiv_awareness=request.data['hiv_awareness'])
        if awareness_add:
            awareness_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editHivAwareness(request):
    awareness_edit = Hiv_Aids_Awareness_And_Testing.objects.get(awareness_id=request.data['awareness_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            awareness_edit.county_id = counties.county_id

    if 'male' in request.data:
        awareness_edit.male = request.data['male']

    if 'female' in request.data:
        awareness_edit.female = request.data['female']

    if 'hiv_awareness' in request.data:
        awareness_edit.hiv_awareness = request.data['hiv_awareness']

    awareness_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

#===============================Registered_Active_Nhif_Members_By_County===============================
#Launch Page
def nhifActiveMembersView(request):
    members = Registered_Active_Nhif_Members_By_County.objects.all()

    records = []

    if members:
        for record in members:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'id': record.member_id, 'county': counties.county_name, 'formal': record.formal, 'informal': record.informal, 'year': record.year}
            records.append(c)
            context = {'records': records}
    else:
        pass

    return render(request, 'knbs_bi/health_registered_active_nhif_members_by_county.html', context)


# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def nhifActiveMembers(request):
    members = Registered_Active_Nhif_Members_By_County.objects.all()

    records = []

    if members:
        for record in members:
            counties = Counties.objects.get(county_id=record.county_id)

            c = {'county': counties.county_name, 'formal': record.formal, 'informal': record.informal, 'year': record.year}
            records.append(c)
    else:
        pass

    return Response(records)

# Add Morbidity View
def addNhifActiveMembersView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_registered_active_nhif_members_by_county_add.html', context)


# Edit Morbidity View
def editNhifActiveMembersView(request):
    all_counties = Counties.objects.all()
    context = {'counties': all_counties}
    return render(request, 'knbs_bi/health_registered_active_nhif_members_by_county_edit.html', context)


# Add Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addNhifActiveMembers(request):
    counties = Counties.objects.get(county_name=request.data['county'])

    if counties:
        kaunti = counties.county_id

        members_add = Registered_Active_Nhif_Members_By_County(county_id=kaunti, formal=request.data['formal'], informal=request.data['informal'],
                                                  year=request.data['year'])
        if members_add:
            members_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Morbidity Below Five
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editNhifActiveMembers(request):
    member_edit = Registered_Active_Nhif_Members_By_County.objects.get(member_id=request.data['member_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            member_edit.county_id = counties.county_id

    if 'formal' in request.data:
        member_edit.formal = request.data['formal']

    if 'informal' in request.data:
        member_edit.informal = request.data['informal']

    if 'year' in request.data:
        member_edit.year = request.data['year']

    member_edit.save()
    response = {'Successfully Updated'}
    return Response(response)

############################################KIHBIS II############################################
####################################Kihibs_Incidence_Of_Sickness_Injury####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def incidenceSickness(request):
    inc_sick = Kihibs_Incidence_Of_Sickness_Injury.objects.all()

    incidences = []

    if inc_sick:
        for incidence in inc_sick:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'county': county.county_name, 'sick_injured': incidence.sick_injured,
                 'no_of_individuals': incidence.no_of_individuals, 'gender': incidence.gender}

            incidences.append(c)
    else:
        pass
    return Response(incidences)

####################################Kihibs_Reported_Being_Sick_Injured_By_Type_Of_Sickness####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def injuredTypeSickness(request):
    reported_sick = Kihibs_Reported_Being_Sick_Injured_By_Type_Of_Sickness.objects.all()

    reports = []

    if reported_sick:
        for report in reported_sick:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'fever_malaria': report.fever_malaria,
                 'stomach_problems': report.stomach_problems, 'diarrhoea': report.diarrhoea, 'vomiting': report.vomiting,
                 'upper_respiratory_infection': report.upper_respiratory_infection, 'lower_respiratory_infection': report.lower_respiratory_infection, 'flu': report.flu,
                 'asthma': report.asthma, 'headache': report.headache, 'skin_problem': report.skin_problem,
                 'dental_problem': report.dental_problem, 'eye_problem': report.eye_problem, 'ear_nose_throat': report.ear_nose_throat,
                 'backache': report.backache, 'tb': report.tb, 'heart_problem': report.heart_problem,
                 'blood_pressure': report.blood_pressure, 'pain_while_passing_urine': report.pain_while_passing_urine, 'diabetes': report.diabetes,
                 'mental_disorder': report.mental_disorder, 'stis': report.stis, 'burn': report.burn,
                 'fracture': report.fracture, 'wound_cut': report.wound_cut, 'poisoning': report.poisoning,
                 'pregnancy_related': report.pregnancy_related, 'cancer': report.cancer, 'other_long_term_illness': report.other_long_term_illness,
                 'hiv_aids': report.hiv_aids, 'typhoid': report.typhoid, 'other': report.other,
                 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Reported_Sickness_By_Age_Group####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def sicknessAgeGroup(request):
    reported_sick = Kihibs_Reported_Sickness_By_Age_Group.objects.all()

    reports = []

    if reported_sick:
        for report in reported_sick:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'percentage_distribution': report.percentage_distribution,
                 'age_group': report.age_group}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Reported_Being_Sick_Injured_By_Cause####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def sickInjuredCause(request):
    reported_sick = Kihibs_Reported_Being_Sick_Injured_By_Cause.objects.all()

    reports = []

    if reported_sick:
        for report in reported_sick:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'percentage_distribution': report.percentage_distribution,
                 'cause': report.cause}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Who_Diagnosed_Illness_Injury####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def diagnosedIllness(request):
    diagnosed_illness = Kihibs_Who_Diagnosed_Illness_Injury.objects.all()

    reports = []

    if diagnosed_illness:
        for report in diagnosed_illness:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'health_worker': report.health_worker,
                 'traditional_healer': report.traditional_healer, 'non_household_member': report.non_household_member, 'self': report.self,
                 'herbalist': report.herbalist, 'faith_healer': report.faith_healer, 'household_member': report.household_member,
                 'other': report.other, 'not_stated': report.not_stated, 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Reported_Sickness_By_No_Of_Days_Missed####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def sicknessDaysMissed(request):
    sickness_days = Kihibs_Reported_Sickness_By_No_Of_Days_Missed.objects.all()

    reports = []

    if sickness_days:
        for report in sickness_days:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'percentage': report.percentage,
                 'no_of_days': report.no_of_days}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################kihibs_reported_sickness_by_health_provider####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def sicknessHealthProvider(request):
    sickness_health = kihibs_reported_sickness_by_health_provider.objects.all()

    reports = []

    if sickness_health:
        for report in sickness_health:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'percentage_distribution': report.percentage_distribution,
                 'health_provider': report.health_provider}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Type_Of_Health_Care_Sought####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def healthCareSought(request):
    healthcare_sought = Kihibs_Type_Of_Health_Care_Sought.objects.all()

    reports = []

    if healthcare_sought:
        for report in healthcare_sought:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'curative': report.curative,
                 'promotive_preventive': report.promotive_preventive, 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Received_Free_Medical_Services####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def freeMedical(request):
    free_medical = Kihibs_Received_Free_Medical_Services.objects.all()

    reports = []

    if free_medical:
        for report in free_medical:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'percentage_distribution': report.percentage_distribution,
                 'service_type': report.service_type}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Disability_By_Type####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def disabilityByType(request):
    disability_type = Kihibs_Disability_By_Type.objects.all()

    reports = []

    if disability_type:
        for report in disability_type:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'visual': report.visual,
                 'hearing': report.hearing, 'speech': report.speech, 'physical': report.physical,
                 'mental': report.mental, 'self_care': report.self_care, 'others': report.others,
                 'any_disability': report.any_disability, 'no_disability': report.no_disability, 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Disability_That_Had_Difficulty####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def disabilityDifficulty(request):
    disability_difficulty = Kihibs_Disability_That_Had_Difficulty.objects.all()

    reports = []

    if disability_difficulty:
        for report in disability_difficulty:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'yes': report.yes,
                 'no': report.no, 'dont_know': report.dont_know, 'not_stated': report.not_stated,
                 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Health_Insurance_Cover_By_Type####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def insuranceCover(request):
    insurance_cover = Kihibs_Health_Insurance_Cover_By_Type.objects.all()

    reports = []

    if insurance_cover:
        for report in insurance_cover:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'nhif': report.nhif,
                 'private_contributory': report.private_contributory, 'private_non_contributory': report.private_non_contributory, 'employee_contributory': report.employee_contributory,
                 'employee_non_contributory': report.employee_non_contributory, 'other': report.other, 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Children_By_Place_Of_Delivery####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def placeDelivery(request):
    place_delivery = Kihibs_Children_By_Place_Of_Delivery.objects.all()

    reports = []

    if place_delivery:
        for report in place_delivery:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'hospital': report.hospital,
                 'health_centre': report.health_centre, 'clininc_dispensary': report.clininc_dispensary, 'maternity_home': report.maternity_home,
                 'at_home': report.at_home, 'other': report.other, 'not_stated': report.not_stated,
                 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Children_By_Who_Assisted_At_Birth####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def childrenAssisted(request):
    children_assisted = Kihibs_Children_By_Who_Assisted_At_Birth.objects.all()

    reports = []

    if children_assisted:
        for report in children_assisted:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'doctor': report.doctor,
                 'midwife_nurse': report.midwife_nurse, 'tba': report.tba, 'ttba': report.ttba,
                 'self': report.self, 'other': report.other, 'not_stated': report.not_stated,
                 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Children_Immmunized_Against_Measles####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def childrenImmunised(request):
    children_immunised = Kihibs_Children_Immmunized_Against_Measles.objects.all()

    reports = []

    if children_immunised:
        for report in children_immunised:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'measles_vaccination': report.measles_vaccination,
                 'proportion': report.proportion}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Children_That_Had_Diarrhoea####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def childrenDiarrhoea(request):
    children_diarrhoea = Kihibs_Children_That_Had_Diarrhoea.objects.all()

    reports = []

    if children_diarrhoea:
        for report in children_diarrhoea:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'yes': report.yes,
                 'not_stated': report.not_stated, 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Type_Of_Food_Given_During_Diarrhoea####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def duringDiarrhoea(request):
    during_diarrhoea = Kihibs_Type_Of_Food_Given_During_Diarrhoea.objects.all()

    reports = []

    if during_diarrhoea:
        for report in during_diarrhoea:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'nothing': report.nothing,
                 'commercial': report.commercial, 'other_semi_solid': report.other_semi_solid, 'fruits': report.fruits,
                 'other': report.other, 'not_stated': report.not_stated, 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Type_Of_Fluid_Of_Food_Given_During_Diarrhoea####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def foodDuringDiarrhoea(request):
    during_diarrhoea = Kihibs_Type_Of_Fluid_Of_Food_Given_During_Diarrhoea.objects.all()

    reports = []

    if during_diarrhoea:
        for report in during_diarrhoea:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'nothing': report.nothing,
                 'breastmilk': report.breastmilk, 'porridge': report.porridge, 'water_alone': report.water_alone,
                 'other_milk': report.other_milk, 'other': report.other, 'not_stated': report.not_stated,
                 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Children_By_Additional_Supplement####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def additionalSupplement(request):
    additional_supplement = Kihibs_Children_By_Additional_Supplement.objects.all()

    reports = []

    if additional_supplement:
        for report in additional_supplement:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'zinc_solution': report.zinc_solution,
                 'sugar_salt_solution': report.sugar_salt_solution, 'other_solutions': report.other_solutions, 'none': report.none,
                 'not_stated': report.not_stated, 'no_of_individuals': report.no_of_individuals}

            reports.append(c)
    else:
        pass
    return Response(reports)


