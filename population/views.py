from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from health.models import Counties
from population.models import PopulationBySexHouseholdsDensityAndCensusYears, PopulationProjectionsBySelectedAgeGroup, \
    PopulationProjectionsBySpecialAgeGroups, Households_Type_Floor_Material_Main_Dwelling_Unit, \
    Households_By_Main_Source_of_Water, By_Type_of_Disability, Percentage_Households_Ownership_Household_Assets, \
    Distribution_Sex_Number_Households_Area_Density, By_Sex_And_School_Attendance, By_Sex_And_Age_Groups, \
    Kihibs_By_Broad_Age_Group, Kihibs_Children_Under_18_By_Orphanhood, Kihibs_Distribution_By_Sex, \
    Kihibs_Distribution_Of_Households_By_Size, Kihibs_Hholds_By_Sex_Of_Household_Head, \
    Kihibs_Marital_Status_Above_18_Years


def population(request):
    return render(request, template_name='knbs_bi/population.html')

#===================================PopulationBySexHouseholdsDensityAndCensusYears================================#
#Launch Page
def populationSexView(request):
    pop_sex = PopulationBySexHouseholdsDensityAndCensusYears.objects.all()

    pops = []

    if pop_sex:
        for population in pop_sex:
            c = {'no_of_male': population.male, 'no_of_female': population.female, 'total': population.total,
                 'hhs': population.hhs, 'av_hh_size': population.av_hh_size, 'approx_area': population.approx_area,
                 'density': population.density, 'census_year': population.census_year}
            pops.append(c)
            context = {'pops':pops}
    return render(request, 'knbs_bi/population_by_sex_households_density_and_census_years.html', context)

#add Record
def addPopulationSexView(request):
    return render(request, 'knbs_bi/population_by_sex_households_density_and_census_years_add.html')

#edit record
def editPopulationSexView(request):
    return render(request, 'knbs_bi/population_by_sex_households_density_and_census_years_edit.html')

#all records API
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationSex(request):
    pop_sex = PopulationBySexHouseholdsDensityAndCensusYears.objects.all()

    pops = []

    if pop_sex:
        for population in pop_sex:
            c = {'no_of_male': population.male, 'no_of_female': population.female, 'total': population.total,
                 'hhs': population.hhs, 'av_hh_size': population.av_hh_size, 'approx_area': population.approx_area,
                 'density': population.density, 'census_year': population.census_year}
            pops.append(c)
    else:
        pass
    return Response(pops)

#add records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPopulationSex(request):
    pop_add = PopulationBySexHouseholdsDensityAndCensusYears(no_of_male=request.data['male'],
                                                              no_of_female=request.data['female'],
                                                              total=request.data['total'],
                                                              hhs=request.data['hhs'],
                                                              av_hh_size=request.data['av_hh_size'],
                                                              approx_area=request.data['approx_area'],
                                                              density=request.data['density'],
                                                              census_year=request.data['census_year'])

    if pop_add:
        pop_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#edit records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPopulationSex(request):
    pop_edit = PopulationBySexHouseholdsDensityAndCensusYears.objects.get(census_population_id=request.data['census_id'])

    if 'male' in request.data:
        pop_edit.no_of_male = request.data['male']

    if 'female' in request.data:
        pop_edit.no_of_female = request.data['female']

    if 'total' in request.data:
        pop_edit.total = request.data['total']

    if 'hhs' in request.data:
        pop_edit.hhs = request.data['hhs']

    if 'av_hh_size' in request.data:
        pop_edit.av_hh_size = request.data['av_hh_size']

    if 'approx_area' in request.data:
        pop_edit.total = request.data['approx_area']

    if 'density' in request.data:
        pop_edit.density = request.data['density']

    if 'census_year' in request.data:
        pop_edit.census_year = request.data['census_year']

    pop_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


#===================================PopulationProjectionsBySelectedAgeGroup================================#
#launch page
def populationSelectedAgeView(request):
    pop_select = PopulationProjectionsBySelectedAgeGroup.objects.all()

    pops = []

    if pop_select:
        for population in pop_select:
            county = Counties.objects.get(county_id=population.county_id)
            c = {'county': county.county_name, 'range_0_4': population.range_0_4, 'range_5_9': population.range_5_9,
                 'range_10_14': population.range_10_14, 'range_15_19': population.range_15_19,
                 'range_20_24': population.range_20_24, 'range_25_29': population.range_25_29,
                 'range_30_34': population.range_30_34, 'range_35_39': population.range_35_39,
                 'range_40_44': population.range_40_44, 'range_45_49': population.range_45_49,
                 'range_50_54': population.range_50_54, 'range_55_59': population.range_55_59,
                 'range_60_64': population.range_60_64, 'range_65_69': population.range_65_69,
                 'range_70_74':population.range_70_74, 'range_75_79': population.range_75_79,
                 'range_80_plus': population.range_80_plus, 'total': population.total, 'gender': population.gender,
                 'year': population.year}
            pops.append(c)

            context = {'pops':pops}

    return render(request,'knbs_bi/population_projections_by_selected_age_group.html',context)

#add record
def addPopulationSelectedAgeView(request):
    return render(request, 'knbs_bi/population_projections_by_selected_age_group_add.html')

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationSelectedAge(request):
    pop_select = PopulationProjectionsBySelectedAgeGroup.objects.all()

    pops = []

    if pop_select:
        for population in pop_select:
            county = Counties.objects.get(county_id=population.county_id)
            c = {'county': county.county_name, 'range_0_4': population.range_0_4, 'range_5_9': population.range_5_9,
                 'range_10_14': population.range_10_14, 'range_15_19': population.range_15_19,
                 'range_20_24': population.range_20_24, 'range_25_29': population.range_25_29,
                 'range_30_34': population.range_30_34, 'range_35_39': population.range_35_39,
                 'range_40_44': population.range_40_44, 'range_45_49': population.range_45_49,
                 'range_50_54': population.range_50_54, 'range_55_59': population.range_55_59,
                 'range_60_64': population.range_60_64, 'range_65_69': population.range_65_69,
                 'range_70_74':population.range_70_74, 'range_75_79': population.range_75_79,
                 'range_80_plus': population.range_80_plus,  'gender': population.gender,
                 'year': population.year}
            pops.append(c)
    else:
        pass
    return Response(pops)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationSpecialGroup(request):
    pop_special = PopulationProjectionsBySpecialAgeGroups.objects.all()

    pops = []

    if pop_special:
        for population in pop_special:
            county = Counties.objects.get(county_id=population.county_id)
            c = {'county': county.county_name, 'under_1': population.under_1, 'range_1_2': population.range_1_2,
                 'range_3_5': population.range_3_5, 'range_6_13': population.range_6_13,
                 'range_14_17': population.range_14_17, 'range_18_24': population.range_18_24,
                 'range_18_34': population.range_18_34, 'range_less_18': population.range_less_18,
                 'range_18_plus': population.range_18_plus, 'range_15_49': population.range_15_49,
                 'range_15_64': population.range_15_64, 'range_65_plus': population.range_65_plus,
                 'gender': population.gender, 'year': population.year}
            pops.append(c)
    else:
        pass
    return Response(pops)




#===================================Households_Type_Floor_Material_Main_Dwelling_Unit================================#
#Launch Page
def houseHoldTypeMainDwellingUnitView(request):
    dweling_unit = Households_Type_Floor_Material_Main_Dwelling_Unit.objects.all()

    dweling_units = []

    if dweling_unit:
        for unit in dweling_unit:
            c = {'id':unit.floor_material_id,'material': unit.material, 'household': unit.households}
            dweling_units.append(c)
            context = {'dweling_units':dweling_units}
    return render(request, 'knbs_bi/population_households_type_floor_material_main_dwelling_unit.html', context)

#add Record
def addHouseHoldTypeMainDwellingUnitView(request):
    return render(request, 'knbs_bi/population_households_type_floor_material_main_dwelling_unit_add.html')

#edit record
def editHouseHoldTypeMainDwellingUnitView(request):
    return render(request, 'knbs_bi/population_households_type_floor_material_main_dwelling_unit_edit.html')

#all records API
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def houseHoldTypeMainDwellingUnit(request):
    dweling_unit = Households_Type_Floor_Material_Main_Dwelling_Unit.objects.all()

    dweling_units = []

    if dweling_unit:
        for unit in dweling_unit:
            c = {'material': unit.material, 'household': unit.households}
            dweling_units.append(c)
    else:
        pass
    return Response(dweling_units)

#add records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addHouseHoldTypeMainDwellingUnit(request):
    unit_add = Households_Type_Floor_Material_Main_Dwelling_Unit(material=request.data['material'],
                                                                 households=request.data['household'])

    if unit_add:
        unit_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#edit records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editHouseHoldTypeMainDwellingUnit(request):
    unit_edit = Households_Type_Floor_Material_Main_Dwelling_Unit.objects.get(floor_material_id=request.data['material_id'])

    if 'material' in request.data:
        unit_edit.material = request.data['material']

    if 'household' in request.data:
        unit_edit.households = request.data['household']

        unit_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)




#===================================Households_By_Main_Source_of_Water================================#
#Launch Page
def houseHoldBySourceOfWaterView(request):
    water_source = Households_By_Main_Source_of_Water.objects.all()

    water_sources = []

    if water_source:
        for source in water_source:
            c = {'id':source.source_of_water_id,'source': source.source, 'total': source.total}
            water_sources.append(c)
            context = {'water_sources':water_sources}
    return render(request, 'knbs_bi/population_households_by_main_source_of_water.html', context)

#add Record
def addHouseHoldBySourceOfWaterView(request):
    return render(request, 'knbs_bi/population_households_by_main_source_of_water_add.html')

#edit record
def editHouseHoldBySourceOfWaterView(request):
    return render(request, 'knbs_bi/population_households_by_main_source_of_water_edit.html')

#all records API
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def houseHoldBySourceOfWater(request):
    water_source = Households_By_Main_Source_of_Water.objects.all()

    water_sources = []

    if water_source:
        for source in water_source:
            c = {'source': source.source, 'total': source.total}
            water_sources.append(c)
    else:
        pass
    return Response(water_sources)

#add records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addHouseHoldBySourceOfWater(request):
    source_add = Households_By_Main_Source_of_Water(source=request.data['source'],
                                                  total=request.data['total'])

    if source_add:
        source_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#edit records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editHouseHoldBySourceOfWater(request):
    source_edit = Households_By_Main_Source_of_Water.objects.get(source_of_water_id=request.data['source_id'])

    if 'source' in request.data:
        source_edit.source = request.data['source']

    if 'total' in request.data:
        source_edit.total = request.data['total']

        source_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)



#===================================By_Type_of_Disability================================#
#Launch Page
def disabilityTypeView(request):
    disability_type = By_Type_of_Disability.objects.all()

    disability_types = []

    if disability_type:
        for disability in disability_type:
            c = {'id':disability.disability_id,'disability': disability.disability,
                 'female': disability.females,'male': disability.males,
                 'total': disability.total_population}
            disability_types.append(c)
            context = {'disability_types':disability_types}
    return render(request, 'knbs_bi/population_type_of_disability.html', context)

#add Record
def addDisabilityTypeView(request):
    return render(request, 'knbs_bi/population_type_of_disability_add.html')

#edit record
def editDisabilityTypeView(request):
    return render(request, 'knbs_bi/population_type_of_disability_edit.html')

#all records API
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def disabilityType(request):
    disability_type = By_Type_of_Disability.objects.all()

    disability_types = []

    if disability_type:
        for disability in disability_type:
            c = {'disability': disability.disability,
                 'female': disability.females, 'male': disability.males,
                 'total': disability.total_population}
            disability_types.append(c)
    else:
        pass
    return Response(disability_types)

#add records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addDisabilityType(request):
    disabilty_add = By_Type_of_Disability(disability=request.data['disability'],
                                       females=request.data['female'],
                                       males=request.data['male'],
                                       total_population=request.data['total'])

    if disabilty_add:
        disabilty_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#edit records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editDisabilityType(request):
    disabilty_edit = By_Type_of_Disability.objects.get(disability_id=request.data['disability_id'])

    if 'disability' in request.data:
        disabilty_edit.disability = request.data['disability']

    if 'female' in request.data:
        disabilty_edit.females = request.data['female']
    if 'male' in request.data:
        disabilty_edit.males = request.data['male']
    if 'total' in request.data:
        disabilty_edit.total_population = request.data['total']

    disabilty_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


#===================================Percentage_Households_Ownership_Household_Assets================================#
#Launch Page
def houseOwnershipHouseholdAssetsView(request):
    household_asset = Percentage_Households_Ownership_Household_Assets.objects.all()

    household_assets = []

    if household_asset:
        for asset in household_asset:
            c = {'id':asset.ownership_id,'asset': asset.asset,
                 'percentage': asset.percentage}
            household_assets.append(c)
            context = {'household_assets':household_assets}
    return render(request, 'knbs_bi/population_percentage_households_ownership_household_assets.html', context)

#add Record
def addHouseOwnershipHouseholdAssetsView(request):
    return render(request, 'knbs_bi/population_percentage_households_ownership_household_assets_add.html')

#edit record
def editHouseOwnershipHouseholdAssetsView(request):
    return render(request, 'knbs_bi/population_percentage_households_ownership_household_assets_edit.html')

#all records API
@api_view(http_method_names=['GET'])
def houseOwnershipHouseholdAssets(request):
    household_asset = Percentage_Households_Ownership_Household_Assets.objects.all()

    household_assets = []

    if household_asset:
        for asset in household_asset:
            c = {'asset': asset.asset,
                 'percentage': asset.percentage}
            household_assets.append(c)
    else:
        pass
    return Response(household_assets)

#add records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addHouseOwnershipHouseholdAssets(request):
    asset_add = Percentage_Households_Ownership_Household_Assets(
        asset=request.data['asset'],
        percentage=request.data['percentage'])

    if asset_add:
        asset_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#edit records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editHouseOwnershipHouseholdAssets(request):
    asset_edit = Percentage_Households_Ownership_Household_Assets.objects.get(ownership_id=request.data['ownership_id'])

    if 'asset' in request.data:
        asset_edit.asset = request.data['asset']

    if 'percentage' in request.data:
        asset_edit.percentage = request.data['percentage']

    asset_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)



#===================================Distribution_Sex_Number_Households_Area_Density================================#
# #Launch Page
# def distributionSexHouseholdsAreaDensityView(request):
#     distribution = Distribution_Sex_Number_Households_Area_Density.objects.all()
#
#     distributions = []
#
#     if distribution:
#         for dist in distribution:
#             c = {'id':dist.disability_id,'disability': dist.disability,
#                  'females': dist.females,'males': dist.males,
#                  'total': dist.total_population}
#             distributions.append(c)
#             context = {'disability_types':distributions}
#     return render(request, 'knbs_bi/populatiom_distribution_sex_number_households_area_density.html', context)
#
# #add Record
# def addDistributionSexHouseholdsAreaDensityView(request):
#     return render(request, 'knbs_bi/populatiom_distribution_sex_number_households_area_density_add.html')
#
# #edit record
# def editDistributionSexHouseholdsAreaDensityView(request):
#     return render(request, 'knbs_bi/populatiom_distribution_sex_number_households_area_density_edit.html')
#
# #all records API
# @api_view(http_method_names=['GET'])
# @renderer_classes((JSONRenderer,))
# def distributionSexHouseholdsAreaDensity(request):
#     disability_type = Distribution_Sex_Number_Households_Area_Density.objects.all()
#
#     disability_types = []
#
#     if disability_type:
#         for disability in disability_type:
#             c = {'disability': disability.disability,
#                  'females': disability.females, 'males': disability.males,
#                  'total': disability.total_population}
#             disability_types.append(c)
#     else:
#         pass
#     return Response(disability_types)
#
# #add records API
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def addDistributionSexHouseholdsAreaDensity(request):
#     disabilty_add = Distribution_Sex_Number_Households_Area_Density(disability=request.data['disability'],
#                                        females=request.data['female'],
#                                        males=request.data['male'],
#                                        total_population=request.data['total'])
#
#     if disabilty_add:
#         disabilty_add.save()
#         return Response(status=status.HTTP_201_CREATED)
#     return Response(status=status.HTTP_400_BAD_REQUEST)
#
# #edit records API
# @api_view(http_method_names=['POST'])
# @renderer_classes((JSONRenderer,))
# def editDistributionSexHouseholdsAreaDensity(request):
#     disabilty_edit = Distribution_Sex_Number_Households_Area_Density.objects.get(disability_id=request.data['disability_id'])
#
#     if 'disability' in request.data:
#         disabilty_edit.disability = request.data['disability']
#
#     if 'female' in request.data:
#         disabilty_edit.females = request.data['female']
#     if 'male' in request.data:
#         disabilty_edit.males = request.data['male']
#     if 'total' in request.data:
#         disabilty_edit.total_population = request.data['total']
#
#         disabilty_edit.save()
#     # response = {'success'}
#     return Response(status=status.HTTP_201_CREATED)
#


#===================================By_Sex_And_School_Attendance================================#
#Launch Page
def bySexAndAttendanceView(request):
    record = By_Sex_And_School_Attendance.objects.all()

    records = []

    if record:
        for rec in record:
            c = {'id':rec.attendance_id,'education': rec.education_level,
                 'female': rec.female,'male': rec.male,
                 'total': rec.total_population}
            records.append(c)
            context = {'records':records}
    return render(request, 'knbs_bi/population_sex_and_school_attendance.html', context)

#add Record
def addBySexAndAttendanceView(request):
    return render(request, 'knbs_bi/population_sex_and_school_attendance_add.html')

#edit record
def editBySexAndAttendanceView(request):
    return render(request, 'knbs_bi/population_sex_and_school_attendance_edit.html')

#all records API
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def bySexAndAttendance(request):
    record = By_Sex_And_School_Attendance.objects.all()

    records= []

    if record:
        for rec in record:
            c = {'education': rec.education_level,
                 'female': rec.female, 'male': rec.male,
                 'total': rec.total_population}
            records.append(c)
    else:
        pass
    return Response(records)

#add records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addBySexAndAttendance(request):
    record_add = By_Sex_And_School_Attendance(education_level=request.data['education'],
                                              female=request.data['female'],
                                              male=request.data['male'],
                                              total_population=request.data['total'])

    if record_add:
        record_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#edit records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editBySexAndAttendance(request):
    record_edit = By_Sex_And_School_Attendance.objects.get(attendance_id=request.data['attendance_id'])

    if 'education' in request.data:
        record_edit.education_level = request.data['education']
    if 'female' in request.data:
        record_edit.female = request.data['female']
    if 'male' in request.data:
        record_edit.male = request.data['male']
    if 'total' in request.data:
        record_edit.total_population = request.data['total']

    record_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


#===================================By_Sex_And_Age_Groups================================#
#Launch Page
def bySexAndAgeGroupView(request):
    record = By_Sex_And_Age_Groups.objects.all()

    records = []

    if record:
        for rec in record:
            c = {'id':rec.group_id,'female': rec.female,
                 'male': rec.male,'total': rec.total_population,
                 'age_group': rec.age_group}
            records.append(c)
            context = {'records':records}
    return render(request, 'knbs_bi/population_by_sex_and_age_groups.html', context)

#add Record
def addBySexAndAgeGroupView(request):
    return render(request, 'knbs_bi/population_by_sex_and_age_groups_add.html')

#edit record
def editBySexAndAgeGroupView(request):
    return render(request, 'knbs_bi/population_by_sex_and_age_groups_edit.html')

#all records API
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def bySexAndAgeGroup(request):
    record = By_Sex_And_Age_Groups.objects.all()

    records= []

    if record:
        for rec in record:
            c = {'female': rec.female,
                 'male': rec.male, 'total': rec.total_population,
                 'age_group': rec.age_group}
            records.append(c)
    else:
        pass
    return Response(records)

#add records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addBySexAndAgeGroup(request):
    record_add = By_Sex_And_Age_Groups(female=request.data['female'],
                                       male=request.data['male'],
                                       total_population=request.data['total'],
                                       age_group=request.data['age_group'])

    if record_add:
        record_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#edit records API
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editBySexAndAgeGroup(request):
    record_edit = By_Sex_And_Age_Groups.objects.get(group_id=request.data['group_id'])

    if 'female' in request.data:
        record_edit.female = request.data['female']

    if 'male' in request.data:
        record_edit.male = request.data['male']
    if 'total' in request.data:
        record_edit.total_population = request.data['total']
    if 'age_group' in request.data:
        record_edit.age_group = request.data['age_group']

    record_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

############################################KIHBIS II############################################
####################################Kihibs_By_Broad_Age_Group####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def broadAgeGroup(request):
    age_group = Kihibs_By_Broad_Age_Group.objects.all()

    records = []

    if age_group:
        for record in age_group:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'range_0_14': record.range_0_14, 'range_15_64': record.range_15_64,
                 'over_65': record.over_65, 'not_stated': record.not_stated, 'age_depend_ratio': record.age_depend_ratio,
                 'child_depend_ratio': record.child_depend_ratio, 'old_age_depend_ratio': record.old_age_depend_ratio, 'individuals': record.individuals}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Children_Under_18_By_Orphanhood####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def orphanHood(request):
    orphan_hood = Kihibs_Children_Under_18_By_Orphanhood.objects.all()

    records = []

    if orphan_hood:
        for record in orphan_hood:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'living_with_both': record.living_with_both, 'father_alive': record.father_alive,
                 'father_deceased': record.father_deceased, 'mother_alive': record.mother_alive, 'mother_deceased': record.mother_deceased,
                 'both_alive': record.both_alive, 'only_father_alive': record.only_father_alive, 'only_mother_alive': record.only_mother_alive,
                 'both_parents_deceased': record.both_parents_deceased, 'missing_info': record.missing_info, 'orphanhood': record.orphanhood,
                 'individuals': record.individuals}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Distribution_By_Sex####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def distributionBySex(request):
    dist_sex = Kihibs_Distribution_By_Sex.objects.all()

    records = []

    if dist_sex:
        for record in dist_sex:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'male_individuals': record.male_individuals, 'male_per_cent': record.male_per_cent,
                 'female_individuals': record.female_individuals, 'female_per_cent': record.female_per_cent, 'sex_ratio': record.sex_ratio,
                 'individuals': record.individuals}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Distribution_Of_Households_By_Size####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def distributionHouseholdsSize(request):
    dist_households = Kihibs_Distribution_Of_Households_By_Size.objects.all()

    records = []

    if dist_households:
        for record in dist_households:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'range_1_2_persons': record.range_1_2_persons, 'range_3_4_persons': record.range_3_4_persons,
                 'range_5_6_persons': record.range_5_6_persons, 'over_7_persons': record.over_7_persons, 'households': record.households,
                 'mean_hhold_size': record.mean_hhold_size}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Hholds_By_Sex_Of_Household_Head####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdHead(request):
    household_head = Kihibs_Hholds_By_Sex_Of_Household_Head.objects.all()

    records = []

    if household_head:
        for record in household_head:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'male': record.male, 'female': record.female,
                 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Marital_Status_Above_18_Years####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def maritalStatus(request):
    marital_status = Kihibs_Marital_Status_Above_18_Years.objects.all()

    records = []

    if marital_status:
        for record in marital_status:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'monogamous': record.monogamous, 'polygamous': record.polygamous,
                 'living_together': record.living_together, 'seperated': record.seperated, 'divorced': record.divorced,
                 'widow_widower': record.widow_widower, 'never_married': record.never_married, 'individuals': record.individuals}

            records.append(c)
    else:
        pass
    return Response(records)











