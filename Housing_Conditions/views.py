from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Housing_Conditions.models import Kihibs_Hholds_By_Type_Of_Housing_Unit, Kihibs_Hholds_By_Habitable_Rooms, \
    Kihibs_Hholds_In_Rented_Dwellings, Kihibs_Hholds_By_Housing_Tenure, Kihibs_Main_Roofing_Material, \
    Kihibs_Main_Wall_Material, Kihibs_Owner_Occupier_Dwellings, Kihibs_Place_For_Washing_Hands_Near_Toilet, \
    Kihibs_Sharing_Of_Toilet_Facility, Kihibs_Waste_Disposal_Method, Kihibs_Time_Taken_To_Fetch_Drinking_Water, \
    Kihibs_Volume_Of_Water_Used, Kihibs_Main_Floor_Material, Kihibs_Main_Source_Of_Lighting_Fuel, \
    Kihibs_Main_Toilet_Facility, Kihibs_Methods_Used_To_Make_Water_Safer, Kihibs_Main_Source_Of_Cooking_Fuel, \
    Kihibs_Primary_Type_Of_Cooking_Appliance, Kihibs_Main_Source_Of_Drinking_Water
from health.models import Counties

############################################KIHBIS II############################################
####################################Kihibs_Hholds_By_Type_Of_Housing_Unit####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsType(request):
    household_type = Kihibs_Hholds_By_Type_Of_Housing_Unit.objects.all()

    households = []

    if household_type:
        for incidence in household_type:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'county': county.county_name, 'bungalow': incidence.bungalow, 'flat': incidence.flat,
                 'maisonnette': incidence.maisonnette, 'swahili': incidence.swahili, 'shanty': incidence.shanty,
                 'manyatta': incidence.manyatta, 'landhi': incidence.landhi, 'other': incidence.other,
                 'not_stated': incidence.not_stated, 'households': incidence.households}

            households.append(c)
    else:
        pass
    return Response(households)

####################################Kihibs_Hholds_By_Habitable_Rooms####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsHabitable(request):
    household_habitable = Kihibs_Hholds_By_Habitable_Rooms.objects.all()

    households = []

    if household_habitable:
        for incidence in household_habitable:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'county': county.county_name, 'one': incidence.one, 'two': incidence.two,
                 'three': incidence.three, 'four': incidence.four, 'five': incidence.five,
                 'six_plus': incidence.six_plus, 'not_stated': incidence.not_stated, 'mean_rooms': incidence.mean_rooms,
                 'households': incidence.households, 'persons_per_room': incidence.persons_per_room}

            households.append(c)
    else:
        pass
    return Response(households)

####################################Kihibs_Hholds_In_Rented_Dwellings####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsRented(request):
    household_rented = Kihibs_Hholds_In_Rented_Dwellings.objects.all()

    households = []

    if household_rented:
        for incidence in household_rented:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'county': county.county_name, 'govt_national': incidence.govt_national, 'govt_county': incidence.govt_county,
                 'parastatal': incidence.parastatal, 'company_directly': incidence.company_directly, 'company_agent': incidence.company_agent,
                 'individual_directly': incidence.individual_directly, 'individual_agent': incidence.individual_agent, 'other': incidence.other,
                 'not_stated': incidence.not_stated, 'households': incidence.households}

            households.append(c)
    else:
        pass
    return Response(households)

####################################Kihibs_Hholds_By_Housing_Tenure####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsTenure(request):
    household_tenure = Kihibs_Hholds_By_Housing_Tenure.objects.all()

    households = []

    if household_tenure:
        for incidence in household_tenure:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'county': county.county_name, 'owner_occupier': incidence.owner_occupier, 'pays_rent': incidence.pays_rent,
                 'no_rent_consent': incidence.no_rent_consent, 'no_rent_squatting': incidence.no_rent_squatting, 'not_stated': incidence.not_stated,
                 'households': incidence.households}

            households.append(c)
    else:
        pass
    return Response(households)

####################################Kihibs_Main_Roofing_Material####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsRoofing(request):
    household_roofing = Kihibs_Main_Roofing_Material.objects.all()

    households = []

    if household_roofing:
        for incidence in household_roofing:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'county': county.county_name, 'grass': incidence.grass, 'mud': incidence.mud,
                 'iron_sheets': incidence.iron_sheets, 'tin_cans': incidence.tin_cans, 'sheet': incidence.sheet,
                 'concrete': incidence.concrete, 'tiles': incidence.tiles, 'not_stated': incidence.not_stated,
                 'households': incidence.households}

            households.append(c)
    else:
        pass
    return Response(households)

####################################Kihibs_Main_Wall_Material####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def mainWallMaterial(request):
    main_wall = Kihibs_Main_Wall_Material.objects.all()

    materials = []

    if main_wall:
        for incidence in main_wall:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'county': county.county_name, 'lime_stone': incidence.lime_stone, 'bricks': incidence.bricks,
                 'cement_blocks': incidence.cement_blocks, 'cement_finish': incidence.cement_finish, 'wood': incidence.wood,
                 'adobe': incidence.adobe, 'iron_sheets': incidence.iron_sheets, 'bamboo': incidence.bamboo,
                 'stone': incidence.stone, 'cane': incidence.cane, 'plywood': incidence.plywood,
                 'not_stated': incidence.not_stated, 'households': incidence.households}

            materials.append(c)
    else:
        pass
    return Response(materials)

####################################Kihibs_Owner_Occupier_Dwellings####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def ownerOccupier(request):
    owner_occupier = Kihibs_Owner_Occupier_Dwellings.objects.all()

    owners = []

    if owner_occupier:
        for incidence in owner_occupier:
            county = Counties.objects.get(county_id=incidence.county_id)

            c = {'county': county.county_name, 'purchased_cash': incidence.purchased_cash, 'purchased_loan': incidence.purchased_loan,
                 'purchased_cash_loan': incidence.purchased_cash_loan, 'constructed_cash': incidence.constructed_cash, 'constructed_loan': incidence.constructed_loan,
                 'constructed_cash_loan': incidence.constructed_cash_loan, 'inherited': incidence.inherited, 'gift': incidence.gift,
                 'bartered': incidence.bartered, 'other': incidence.other, 'households': incidence.households}

            owners.append(c)
    else:
        pass
    return Response(owners)

####################################Kihibs_Place_For_Washing_Hands_Near_Toilet####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def placeWashing(request):
    place_washing = Kihibs_Place_For_Washing_Hands_Near_Toilet.objects.all()

    places = []

    if place_washing:
        for record in place_washing:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'place': record.place, 'no_place': record.no_place,
                 'not_stated': record.not_stated, 'households': record.households}

            places.append(c)
    else:
        pass
    return Response(places)

####################################Kihibs_Sharing_Of_Toilet_Facility####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def sharingToilet(request):
    sharing_toilet = Kihibs_Sharing_Of_Toilet_Facility.objects.all()

    records = []

    if sharing_toilet:
        for record in sharing_toilet:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'shared_toilet': record.shared_toilet, 'not_shared': record.not_shared,
                 'not_stated': record.not_stated, 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Waste_Disposal_Method####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def wasteDisposal(request):
    waste_disposal = Kihibs_Waste_Disposal_Method.objects.all()

    records = []

    if waste_disposal:
        for record in waste_disposal:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'county_gov': record.county_gov, 'community': record.community,
                 'private_co': record.private_co, 'dumped_compound': record.dumped_compound, 'dumped_street': record.dumped_street,
                 'dumped_latrine': record.dumped_latrine, 'burnt': record.burnt, 'buried': record.buried,
                 'other': record.other, 'not_stated': record.not_stated, 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Time_Taken_To_Fetch_Drinking_Water####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def drinkingWater(request):
    drinking_water = Kihibs_Time_Taken_To_Fetch_Drinking_Water.objects.all()

    records = []

    if drinking_water:
        for record in drinking_water:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'zero': record.zero, 'less_thirty_min': record.less_thirty_min,
                 'over_thirty_min': record.over_thirty_min, 'not_stated': record.not_stated, 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Volume_Of_Water_Used####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def waterUsed(request):
    water_used = Kihibs_Volume_Of_Water_Used.objects.all()

    records = []

    if water_used:
        for record in water_used:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'lit_0_1000': record.lit_0_1000, 'lit_1001_2000': record.lit_1001_2000,
                 'lit_2001_3000': record.lit_2001_3000, 'over_3000_lit': record.over_3000_lit, 'not_stated': record.not_stated,
                 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Main_Floor_Material####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def floorMaterials(request):
    floor_materials = Kihibs_Main_Floor_Material.objects.all()

    records = []

    if floor_materials:
        for record in floor_materials:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'tiles': record.tiles, 'cement': record.cement,
                 'wood': record.wood, 'cow_dung': record.cow_dung, 'sand': record.sand,
                 'carpet': record.carpet, 'other': record.other, 'not_stated': record.not_stated,
                 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Main_Source_Of_Drinking_Water####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def sourceDrinkingWater(request):
    drinking_water = Kihibs_Main_Source_Of_Drinking_Water.objects.all()

    records = []

    if drinking_water:
        for record in drinking_water:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'piped_dwelling': record.piped_dwelling, 'piped_yard': record.piped_yard,
                 'piped_tap': record.piped_tap, 'tubewell': record.tubewell, 'protected_well': record.protected_well,
                 'protected_spring': record.protected_spring, 'rain_water': record.rain_water, 'bottled_water': record.bottled_water,
                 'unprotected_well': record.unprotected_well, 'unprotected_spring': record.unprotected_spring, 'vendor_truck': record.vendor_truck,
                 'vendor_drum': record.vendor_drum, 'vendor_bicycles': record.vendor_bicycles, 'surface_water': record.surface_water,
                 'other': record.other, 'not_stated': record.not_stated, 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Main_Source_Of_Lighting_Fuel####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def lightingFuel(request):
    lighting_fuel = Kihibs_Main_Source_Of_Lighting_Fuel.objects.all()

    records = []

    if lighting_fuel:
        for record in lighting_fuel:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'electricity': record.electricity, 'generator': record.generator,
                 'solar_energy': record.solar_energy, 'paraffin_lantern': record.paraffin_lantern, 'paraffin_tin_lamp': record.paraffin_tin_lamp,
                 'paraffin_pressure_lamp': record.paraffin_pressure_lamp, 'fuel_wood': record.fuel_wood, 'gas_lamp': record.gas_lamp,
                 'battery_lamp': record.battery_lamp, 'candles': record.candles, 'biogas': record.biogas,
                 'other': record.other, 'not_stated': record.not_stated, 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Main_Toilet_Facility####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def toiletFacility(request):
    toilet_facility = Kihibs_Main_Toilet_Facility.objects.all()

    records = []

    if toilet_facility:
        for record in toilet_facility:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'piped_sewer': record.piped_sewer, 'septic_tank': record.septic_tank,
                 'latrine': record.latrine, 'vip': record.vip, 'latrine_slab': record.latrine_slab,
                 'composting_toilet': record.composting_toilet, 'somewhere_else': record.somewhere_else, 'unknown_place': record.unknown_place,
                 'without_slab': record.without_slab, 'bucket_toilet': record.bucket_toilet, 'hanging_toilet': record.hanging_toilet,
                 'bush': record.bush, 'other': record.other, 'not_stated': record.not_stated,
                 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Methods_Used_To_Make_Water_Safer####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def waterSafer(request):
    water_safer = Kihibs_Methods_Used_To_Make_Water_Safer.objects.all()

    records = []

    if water_safer:
        for record in water_safer:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'boil': record.boil, 'add_bleach': record.add_bleach,
                 'water_filter': record.water_filter, 'solar': record.solar, 'sieve_cloth': record.sieve_cloth,
                 'stand_settle': record.stand_settle, 'stand_settle': record.stand_settle, 'other': record.other,
                 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Main_Source_Of_Cooking_Fuel####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def cookingFuel(request):
    cooking_fuel = Kihibs_Main_Source_Of_Cooking_Fuel.objects.all()

    records = []

    if cooking_fuel:
        for record in cooking_fuel:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'firewood': record.firewood, 'electricity': record.electricity,
                 'lpg': record.lpg, 'biogas': record.biogas, 'kerosene': record.kerosene,
                 'charcoal': record.charcoal, 'shrubs': record.shrubs, 'animal_dung': record.animal_dung,
                 'crop_residue': record.crop_residue, 'other': record.other, 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)

####################################Kihibs_Primary_Type_Of_Cooking_Appliance####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def cookingAppliance(request):
    cooking_appliance = Kihibs_Primary_Type_Of_Cooking_Appliance.objects.all()

    records = []

    if cooking_appliance:
        for record in cooking_appliance:
            county = Counties.objects.get(county_id=record.county_id)

            c = {'county': county.county_name, 'stone_fire': record.stone_fire, 'imp_stone_fire': record.imp_stone_fire,
                 'ordinary_jiko': record.ordinary_jiko, 'improved_jiko': record.improved_jiko, 'stove': record.stove,
                 'gas_cooker': record.gas_cooker, 'electric_cooker': record.electric_cooker, 'elec_gas_cooker': record.elec_gas_cooker,
                 'other': record.other, 'not_stated': record.not_stated, 'households': record.households}

            records.append(c)
    else:
        pass
    return Response(records)