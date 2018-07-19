from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from environment_and_natural_resources.models import Quantity_Value_Fish_Landed, Record_Sale_Goverment_Products, \
    Trends_Envi_Natural_Resources, Water_Purification_Points, Average_Export_Prices_Ash, Development_Expenditure_Water, \
    Expenditure_Cleaning_Refuse, Government_Forest, Num_High_Risk_Environ_Impact, Population_Wildlife, \
    Quantity_Of_Total_Mineral, Value_Of_Total_Mineral


def environment_and_natural_resources(request):
    return render(request, template_name='knbs_bi/environment_and_natural_resources.html')


# ===============================Quantity_Value_Fish_Landed===============================
# Launch Page
def quantityValueFishLandedView(request):
    quantity = Quantity_Value_Fish_Landed.objects.all()

    quantities = []

    if quantity:
        for qty in quantity:
            c = {'id': qty.quantity_id, 
                 'year': qty.year,
                 'category': qty.category,
                 'value': qty.value,
                 'type': qty.type}
            quantities.append(c)
            context = {'quantities': quantities}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_quantity_value_fish_landed.html', context)


# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def quantityValueFishLanded(request):
    quantity = Quantity_Value_Fish_Landed.objects.all()

    quantities = []

    if quantity:
        for qty in quantity:
            c = {'year': qty.year,
                 'category': qty.category,
                 'value': qty.value,
                 'type': qty.type}
            quantities.append(c)
    else:
        pass
    return Response(quantities)


# Add View
def addQuantityValueFishLandedView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_quantity_value_fish_landed_add.html')


# Edit View
def editQuantityValueFishLandedView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_quantity_value_fish_landed_edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addQuantityValueFishLanded(request):
    quantity_add = Quantity_Value_Fish_Landed(type=request.data['type'],
                                              category=request.data['category'],
                                              value=request.data['value'],
                                              year=request.data['year'])

    if quantity_add:
        quantity_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editQuantityValueFishLanded(request):
    quantity_edit = Quantity_Value_Fish_Landed.objects.get(quantity_id=request.data['quantity_id'])

    if 'type' in request.data:
        quantity_edit.type = request.data['type']

    if 'category' in request.data:
        quantity_edit.category = request.data['category']

    if 'year' in request.data:
        quantity_edit.year = request.data['year']
    
    if 'value' in request.data:
        quantity_edit.value = request.data['value']

    quantity_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

# ===============================Record_Sale_Goverment_Products===============================
# Launch Page
def saleOfGovtProductsView(request):
    record = Record_Sale_Goverment_Products.objects.all()

    records = []

    if record:
        for rec in record:
            c = {'id': rec.record_id, 
                 'year': rec.year,
                 'soft_wood': rec.soft_wood,
                 'fuelwood_charcoal': rec.fuelwood_charcoal,
                 'power_and_telegraph': rec.power_and_telegraph}
            records.append(c)
            context = {'records': records}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_record_sale_goverment_products.html', context)


# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def saleOfGovtProducts(request):
    record = Record_Sale_Goverment_Products.objects.all()

    records = []

    if record:
        for rec in record:
            c = {'year': rec.year,
                 'soft_wood': rec.soft_wood,
                 'fuelwood_charcoal': rec.fuelwood_charcoal,
                 'power_and_telegraph': rec.power_and_telegraph}
            records.append(c)
    else:
        pass
    return Response(records)


# Add View
def addSaleOfGovtProductsView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_record_sale_goverment_products_add.html')


# Edit View
def editSaleOfGovtProductsView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_record_sale_goverment_products_edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addSaleOfGovtProducts(request):
    record_add = Record_Sale_Goverment_Products(power_and_telegraph=request.data['power_and_telegraph'],
                                                            soft_wood=request.data['soft_wood'],
                                                                 fuelwood_charcoal=request.data['fuelwood_charcoal'],
                                                                 year=request.data['year'])

    if record_add:
        record_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editSaleOfGovtProducts(request):
    record_edit = Record_Sale_Goverment_Products.objects.get(record_id=request.data['record_id'])

    if 'power_and_telegraph' in request.data:
        record_edit.power_and_telegraph = request.data['power_and_telegraph']

    if 'soft_wood' in request.data:
        record_edit.soft_wood = request.data['soft_wood']

    if 'year' in request.data:
        record_edit.year = request.data['year']
    
    if 'fuelwood_charcoal' in request.data:
        record_edit.fuelwood_charcoal = request.data['fuelwood_charcoal']

    record_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

# ===============================Trends_Envi_Natural_Resources===============================
# Launch Page
def trendsEnvironmentResourcesView(request):
    trend = Trends_Envi_Natural_Resources.objects.all()

    trends = []

    if trend:
        for tre in trend:
            c = {'id': tre.trend_id, 
                 'year': tre.year,
                 'forestry_and_logging': tre.forestry_and_logging,
                 'fishing_and_aquaculture': tre.fishing_and_aquaculture,
                 'mining_and_quarrying': tre.mining_and_quarrying,
                 'water_supply': tre.water_supply,
                 'GDP_at_current_prices': tre.GDP_at_current_prices,
                 'resource_as_percent_of_GDP': tre.resource_as_percent_of_GDP}
            trends.append(c)
            context = {'trends': trends}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_trends_envi_natural_resources.html', context)


# All trends
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def trendsEnvironmentResources(request):
    trend = Trends_Envi_Natural_Resources.objects.all()

    trends = []

    if trend:
        for tre in trend:
            c = {'year': tre.year,
                 'forestry_and_logging': tre.forestry_and_logging,
                 'fishing_and_aquaculture': tre.fishing_and_aquaculture,
                 'mining_and_quarrying': tre.mining_and_quarrying,
                 'water_supply': tre.water_supply,
                 'GDP_at_current_prices': tre.GDP_at_current_prices,
                 'resource_as_percent_of_GDP': tre.resource_as_percent_of_GDP}
            trends.append(c)
    else:
        pass
    return Response(trends)


# Add View
def addTrendsEnvironmentResourcesView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_trends_envi_natural_resources_add.html')


# Edit View
def editTrendsEnvironmentResourcesView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_trends_envi_natural_resources_edit.html')


# Add trend
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTrendsEnvironmentResources(request):
    trend_add = Trends_Envi_Natural_Resources(forestry_and_logging=request.data['forestry_and_logging'],
                                                            fishing_and_aquaculture=request.data['fishing_and_aquaculture'],
                                                            mining_and_quarrying=request.data['mining_and_quarrying'],
                                                            water_supply=request.data['water_supply'],    
                                                            GDP_at_current_prices=request.data['GDP_at_current_prices'],
                                                                 resource_as_percent_of_GDP=request.data['resource_as_percent_of_GDP'],
                                                                 year=request.data['year'])

    if trend_add:
        trend_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit trend
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTrendsEnvironmentResources(request):
    trend_edit = Trends_Envi_Natural_Resources.objects.get(trend_id=request.data['trend_id'])

    if 'forestry_and_logging' in request.data:
        trend_edit.forestry_and_logging = request.data['forestry_and_logging']

    if 'fishing_and_aquaculture' in request.data:
        trend_edit.fishing_and_aquaculture = request.data['fishing_and_aquaculture']

    if 'mining_and_quarrying' in request.data:
        trend_edit.mining_and_quarrying = request.data['mining_and_quarrying']

    if 'water_supply' in request.data:
        trend_edit.water_supply = request.data['water_supply']

    if 'GDP_at_current_prices' in request.data:
        trend_edit.GDP_at_current_prices = request.data['GDP_at_current_prices']

    if 'year' in request.data:
        trend_edit.year = request.data['year']

    if 'resource_as_percent_of_GDP' in request.data:
        trend_edit.resource_as_percent_of_GDP = request.data['resource_as_percent_of_GDP']

    trend_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

# ===============================Water_Purification_Points===============================
# Launch Page
def waterPurificationPointsView(request):
    point = Water_Purification_Points.objects.all()

    points = []

    if point:
        for pt in point:
            c = {'id': pt.water_id, 
                 'year': pt.year,
                 'boreholes_total': pt.boreholes_total,
                 'public': pt.public,
                 'water_purification_points': pt.water_purification_points}
            points.append(c)
            context = {'points': points}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_water_purification_points.html', context)


# All points
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def waterPurificationPoints(request):
    point = Water_Purification_Points.objects.all()

    points = []

    if point:
        for pt in point:
            c = {'year': pt.year,
                 'boreholes_total': pt.boreholes_total,
                 'public': pt.public,
                 'water_purification_points': pt.water_purification_points}
            points.append(c)
    else:
        pass
    return Response(points)


# Add View
def addWaterPurificationPointsView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_water_purification_points_add.html')


# Edit View
def editWaterPurificationPointsView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_water_purification_points_edit.html')


# Add point
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addWaterPurificationPoints(request):
    point_add = Water_Purification_Points(water_purification_points=request.data['water_purification_points'],
                                                            boreholes_total=request.data['boreholes_total'],
                                                                 public=request.data['public'],
                                                                 year=request.data['year'])

    if point_add:
        point_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit point
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editWaterPurificationPoints(request):
    point_edit = Water_Purification_Points.objects.get(water_id=request.data['water_id'])

    if 'water_purification_points' in request.data:
        point_edit.water_purification_points = request.data['water_purification_points']

    if 'boreholes_total' in request.data:
        point_edit.boreholes_total = request.data['boreholes_total']

    if 'year' in request.data:
        point_edit.year = request.data['year']
    
    if 'public' in request.data:
        point_edit.public = request.data['public']

    point_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

# ===============================Average_Export_Prices_Ash===============================
# Launch Page
def avgExportPriceAshView(request):
    price = Average_Export_Prices_Ash.objects.all()

    prices = []

    if price:
        for prc in price:
            c = {'id': prc.average_id, 
                 'year': prc.year,
                 'sodaash': prc.soda_ash,
                 'fluorspar': prc.fluorspar,
                 }
            prices.append(c)
            context = {'prices': prices}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_average_export_prices_ash.html', context)


# All prices
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def avgExportPriceAsh(request):
    price = Average_Export_Prices_Ash.objects.all()

    prices = []

    if price:
        for prc in price:
            c = {'year': prc.year,
                 'sodaash': prc.soda_ash,
                 'fluorspar': prc.fluorspar,
                 }
            prices.append(c)
    else:
        pass
    return Response(prices)


# Add View
def addAvgExportPriceAshView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_average_export_prices_ash_add.html')


# Edit View
def editAvgExportPriceAshView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_average_export_prices_ash_edit.html')


# Add price
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAvgExportPriceAsh(request):
    price_add = Average_Export_Prices_Ash(soda_ash=request.data['sodaash'],
                                           fluorspar=request.data['fluorspar'],
                                           year=request.data['year'])

    if price_add:
        price_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit price
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAvgExportPriceAsh(request):
    price_edit = Average_Export_Prices_Ash.objects.get(average_id=request.data['average_id'])

    
    if 'sodaash' in request.data:
        price_edit.soda_ash = request.data['sodaash']

    if 'year' in request.data:
        price_edit.year = request.data['year']
    
    if 'fluorspar' in request.data:
        price_edit.fluorspar = request.data['fluorspar']

    price_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


# ===============================Development_Expenditure_Water===============================
# Launch Page
def developmentExpenditureWaterView(request):
    expenditure = Development_Expenditure_Water.objects.all()

    expenditures = []

    if expenditure:
        for exp in expenditure:
            c = {'id': exp.development_id, 
                 'year': exp.year,
                 'water_development': exp.water_development,
                 'training_of_water_development_staff': exp.training_of_water_development_staff,
                 'miscellaneous_and_special_water_programmes': exp.miscellaneous_and_special_water_programmes,
                 'national_water_conservation_and_pipeline_corporation': exp.national_water_conservation_and_pipeline_corporation,
                 'irrigation_development': exp.irrigation_development,
                  'national_irrigation_board': exp.national_irrigation_board,
                 'rural_water_supplies': exp.rural_water_supplies
                 }
            expenditures.append(c)
            context = {'expenditures': expenditures}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_development_expenditure_water.html', context)


# All expenditures
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def developmentExpenditureWater(request):
    expenditure = Development_Expenditure_Water.objects.all()

    expenditures = []

    if expenditure:
        for exp in expenditure:
            c = {'year': exp.year,
                 'water_development': exp.water_development,
                 'training_of_water_development_staff': exp.training_of_water_development_staff,
                 'miscellaneous_and_special_water_programmes': exp.miscellaneous_and_special_water_programmes,
                 'national_water_conservation_and_pipeline_corporation': exp.national_water_conservation_and_pipeline_corporation,
                 'irrigation_development': exp.irrigation_development,
                 'rural_water_supplies': exp.rural_water_supplies}
            expenditures.append(c)
    else:
        pass
    return Response(expenditures)


# Add View
def addDevelopmentExpenditureWaterView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_development_expenditure_water_add.html')


# Edit View
def editDevelopmentExpenditureWaterView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_development_expenditure_water_edit.html')


# Add expenditure
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addDevelopmentExpenditureWater(request):
    expenditure_add = Development_Expenditure_Water(water_development=request.data['water_development'],
                                                    training_of_water_development_staff=request.data['training_of_water_development_staff'],
                                                    miscellaneous_and_special_water_programmes=request.data['miscellaneous_and_special_water_programmes'],
                                                    national_water_conservation_and_pipeline_corporation=request.data['national_water_conservation_and_pipeline_corporation'],
                                                    irrigation_development=request.data['irrigation_development'],
                                                    national_irrigation_board=request.data['national_irrigation_board'],
                                                    rural_water_supplies=request.data['rural_water_supplies'],
                                                    year=request.data['year'])

    if expenditure_add:
        expenditure_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit expenditure
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editDevelopmentExpenditureWater(request):
    expenditure_edit = Development_Expenditure_Water.objects.get(development_id=request.data['development_id'])

    if 'water_development' in request.data:
        expenditure_edit.water_development = request.data['water_development']
    
    if 'training_of_water_development_staff' in request.data:
        expenditure_edit.training_of_water_development_staff = request.data['training_of_water_development_staff']

    if 'miscellaneous_and_special_water_programmes' in request.data:
        expenditure_edit.miscellaneous_and_special_water_programmes = request.data['miscellaneous_and_special_water_programmes']

    if 'national_water_conservation_and_pipeline_corporation' in request.data:
        expenditure_edit.national_water_conservation_and_pipeline_corporation = request.data['national_water_conservation_and_pipeline_corporation']

    if 'year' in request.data:
        expenditure_edit.year = request.data['year']
    
    if 'irrigation_development' in request.data:
        expenditure_edit.irrigation_development = request.data['irrigation_development']
    
    if 'national_irrigation_board' in request.data:
       expenditure_edit.national_irrigation_board = request.data['national_irrigation_board']

    if 'rural_water_supplies' in request.data:
        expenditure_edit.rural_water_supplies = request.data['rural_water_supplies']

    expenditure_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

# ===============================Expenditure_Cleaning_Refuse===============================
# Launch Page
def expenditureCleaningRefuseView(request):
    expenditure = Expenditure_Cleaning_Refuse.objects.all()

    expenditures = []

    if expenditure:
        for prc in expenditure:
            c = {'id': prc.development_id,
                 'year': prc.year,
                 'refuse_removal': prc.refuse_removal
                 }
            expenditures.append(c)
            context = {'expenditures': expenditures}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_expenditure_cleaning_refuse.html', context)


# All expenditures
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def expenditureCleaningRefuse(request):
    expenditure = Expenditure_Cleaning_Refuse.objects.all()

    expenditures = []

    if expenditure:
        for prc in expenditure:
            c = {'year': prc.year,
                 'refuse_removal': prc.refuse_removal
                 }
            expenditures.append(c)
    else:
        pass
    return Response(expenditures)


# Add View
def addExpenditureCleaningRefuseView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_expenditure_cleaning_refuse_add.html')


# Edit View
def editExpenditureCleaningRefuseView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_expenditure_cleaning_refuse_edit.html')


# Add expenditure
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addExpenditureCleaningRefuse(request):
    expenditure_add = Expenditure_Cleaning_Refuse(refuse_removal=request.data['refuse_removal'],
                                                                 year=request.data['year'])

    if expenditure_add:
        expenditure_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit expenditure
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editExpenditureCleaningRefuse(request):
    expenditure_edit = Expenditure_Cleaning_Refuse.objects.get(development_id=request.data['development_id'])

    
    if 'refuse_removal' in request.data:
        expenditure_edit.refuse_removal = request.data['refuse_removal']

    if 'year' in request.data:
        expenditure_edit.year = request.data['year']
   

    expenditure_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

# ===============================Government_Forest===============================
# Launch Page
def governmentForestView(request):
    forest = Government_Forest.objects.all()

    forests = []

    if forest:
        for fr in forest:
            c = {'id': fr.govt_id, 
                 'year': fr.year,
                 'previous_plantation_area': fr.previous_plantation_area,
                 'area_planted': fr.area_planted,
                 'area_clear_felled': fr.area_clear_felled}
            forests.append(c)
            context = {'forests': forests}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_government_forest.html', context)


# All forests
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def governmentForest(request):
    forest = Government_Forest.objects.all()

    forests = []

    if forest:
        for fr in forest:
            c = {'year': fr.year,
                 'previous_plantation_area': fr.previous_plantation_area,
                 'area_planted': fr.area_planted,
                 'area_clear_felled': fr.area_clear_felled}
            forests.append(c)
    else:
        pass
    return Response(forests)


# Add View
def addGovernmentForestView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_government_forest_add.html')


# Edit View
def editGovernmentForestView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_government_forest_edit.html')


# Add forest
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addGovernmentForest(request):
    forest_add = Government_Forest(area_clear_felled=request.data['area_clear_felled'],
                                   previous_plantation_area=request.data['previous_plantation_area'],
                                   area_planted=request.data['area_planted'],
                                   year=request.data['year'])

    if forest_add:
        forest_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit forest
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editGovernmentForest(request):
    forest_edit = Government_Forest.objects.get(govt_id=request.data['govt_id'])

    if 'area_clear_felled' in request.data:
        forest_edit.area_clear_felled = request.data['area_clear_felled']

    if 'previous_plantation_area' in request.data:
        forest_edit.previous_plantation_area = request.data['previous_plantation_area']

    if 'year' in request.data:
        forest_edit.year = request.data['year']
    
    if 'area_planted' in request.data:
        forest_edit.area_planted = request.data['area_planted']

    forest_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


# ===============================Num_High_Risk_Environ_Impact===============================
# Launch Page
def numberOfHighRiskEnvironmentImpactView(request):
    number = Num_High_Risk_Environ_Impact.objects.all()

    numbers = []

    if number:
        for num in number:
            c = {'id': num.risk_id, 
                 'year': num.year,
                 'transport_and_communication': num.transport_and_communication,
                 'energy': num.energy,
                 'tourism': num.tourism,
                 'mining_and_quarrying': num.mining_and_quarrying,
                 'human_settlements_and_Infrastructure': num.human_settlements_and_Infrastructure,
                 'agriculture_and_forestry': num.agriculture_and_forestry,
                 'water_resources': num.water_resources,
                 'commerce_and_industry': num.commerce_and_industry}
            numbers.append(c)
            context = {'numbers': numbers}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_num_high_risk_environ_impact.html', context)


# All numbers
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def numberOfHighRiskEnvironmentImpact(request):
    number = Num_High_Risk_Environ_Impact.objects.all()

    numbers = []

    if number:
        for num in number:
            c = {'year': num.year,
                 'transport_and_communication': num.transport_and_communication,
                 'energy': num.energy,
                 'tourism': num.tourism,
                 'mining_and_quarrying': num.mining_and_quarrying,
                 'human_settlements_and_Infrastructure': num.human_settlements_and_Infrastructure,
                 'water_resources': num.water_resources,
                 'agriculture_and_forestry': num.agriculture_and_forestry}
            numbers.append(c)
    else:
        pass
    return Response(numbers)


# Add View
def addNumberOfHighRiskEnvironmentImpactView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_num_high_risk_environ_impact_add.html')


# Edit View
def editNumberOfHighRiskEnvironmentImpactView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_num_high_risk_environ_impact_edit.html')


# Add number
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addNumberOfHighRiskEnvironmentImpact(request):
    number_add = Num_High_Risk_Environ_Impact(transport_and_communication=request.data['transport_and_communication'],
                                              energy=request.data['energy'],
                                              water_resources=request.data['water_resources'],
                                              tourism=request.data['tourism'],
                                              mining_and_quarrying=request.data['mining_and_quarrying'],
                                              human_settlements_and_Infrastructure=request.data['human_settlements_and_Infrastructure'],
                                              agriculture_and_forestry=request.data['agriculture_and_forestry'],
                                              commerce_and_industry=request.data['commerce_and_industry'],
                                              year=request.data['year'])

    if number_add:
        number_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit number
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editNumberOfHighRiskEnvironmentImpact(request):
    number_edit = Num_High_Risk_Environ_Impact.objects.get(risk_id=request.data['risk_id'])

    if 'transport_and_communication' in request.data:
        number_edit.transport_and_communication = request.data['transport_and_communication']
    
    if 'energy' in request.data:
        number_edit.energy = request.data['energy']

    if 'tourism' in request.data:
        number_edit.tourism = request.data['tourism']

    if 'mining_and_quarrying' in request.data:
        number_edit.mining_and_quarrying = request.data['mining_and_quarrying']

    if 'human_settlements_and_Infrastructure' in request.data:
        number_edit.human_settlements_and_Infrastructure = request.data['human_settlements_and_Infrastructure']

    if 'year' in request.data:
        number_edit.year = request.data['year']
    
    if 'agriculture_and_forestry' in request.data:
        number_edit.agriculture_and_forestry = request.data['agriculture_and_forestry']
    
    if 'commerce_and_industry' in request.data:
       number_edit.commerce_and_industry = request.data['commerce_and_industry']
    
    if 'water_resources' in request.data:
       number_edit.water_resources = request.data['water_resources']

    number_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


# ===============================Population_Wildlife===============================
# Launch Page
def wildLifePopulationView(request):
    population = Population_Wildlife.objects.all()

    populations = []

    if population:
        for pop in population:
            c = {'id': pop.population_id, 
                 'year': pop.year,
                 'buffalo': pop.buffalo,
                 'burchell_zebra': pop.burchell_zebra,
                 'eland': pop.eland,
                 'elephant': pop.elephant,
                 'gerenuk': pop.gerenuk,
                 'grant_gazelle': pop.grant_gazelle,
                 'giraffe': pop.giraffe,
                 'warthog': pop.warthog,
                 'grevy_zebra': pop.grevy_zebra,
                 'hunters_hartebeest': pop.hunters_hartebeest,
                 'impala': pop.impala,
                 'kongoni': pop.kongoni,
                 'kudu': pop.kudu,
                 'oryx': pop.oryx,
                 'ostrich': pop.ostrich,
                 'thomson_gazelle': pop.thomson_gazelle,
                 'topi': pop.topi,
                 'wildebeest': pop.wildebeest,
                 'waterbuck': pop.waterbuck
                 }
            populations.append(c)
            context = {'populations': populations}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_population_wildlife.html', context)


# All populations
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def wildLifePopulation(request):
    population = Population_Wildlife.objects.all()

    populations = []

    if population:
        for pop in population:
            c = {'year': pop.year,
                 'buffalo': pop.buffalo,
                 'burchell_zebra': pop.burchell_zebra,
                 'eland': pop.eland,
                 'elephant': pop.elephant,
                 'gerenuk': pop.gerenuk,
                 'grant_gazelle': pop.grant_gazelle,
                 'giraffe': pop.giraffe,
                 'warthog': pop.warthog,
                 'grevy_zebra': pop.grevy_zebra,
                 'hunters_hartebeest': pop.hunters_hartebeest,
                 'impala': pop.impala,
                 'kongoni': pop.kongoni,
                 'kudu': pop.kudu,
                 'oryx': pop.oryx,
                 'ostrich': pop.ostrich,
                 'thomson_gazelle': pop.thomson_gazelle,
                 'topi': pop.topi,
                 'wildebeest': pop.wildebeest,
                 'waterbuck': pop.waterbuck}
            populations.append(c)
    else:
        pass
    return Response(populations)


# Add View
def addWildLifePopulationView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_population_wildlife_add.html')


# Edit View
def editWildLifePopulationView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_population_wildlife_edit.html')


# Add population
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addWildLifePopulation(request):
    population_add = Population_Wildlife(buffalo=request.data['buffalo'],
                                         burchell_zebra=request.data['burchell_zebra'],
                                         grant_gazelle=request.data['grant_gazelle'],
                                         eland=request.data['eland'],
                                         elephant=request.data['elephant'],
                                         gerenuk=request.data['gerenuk'],
                                         giraffe=request.data['giraffe'],
                                         grevy_zebra=request.data['grevy_zebra'],
                                         year=request.data['year'],
                                         hunters_hartebeest=request.data['hunters_hartebeest'],
                                         impala=request.data['impala'],
                                         kongoni=request.data['kongoni'],
                                         kudu=request.data['kudu'],
                                         oryx=request.data['oryx'],
                                         ostrich=request.data['ostrich'],
                                         thomson_gazelle=request.data['thomson_gazelle'],
                                         topi=request.data['topi'],
                                         warthog=request.data['warthog'],
                                         waterbuck=request.data['waterbuck'],
                                         wildebeest=request.data['wildebeest'])

    if population_add:
        population_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit population
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editWildLifePopulation(request):
    population_edit = Population_Wildlife.objects.get(population_id=request.data['population_id'])

    if 'buffalo' in request.data:
        population_edit.buffalo = request.data['buffalo']
    
    if 'burchell_zebra' in request.data:
        population_edit.burchell_zebra = request.data['burchell_zebra']

    if 'eland' in request.data:
        population_edit.eland = request.data['eland']

    if 'elephant' in request.data:
        population_edit.elephant = request.data['elephant']

    if 'gerenuk' in request.data:
        population_edit.gerenuk = request.data['gerenuk']

    if 'year' in request.data:
        population_edit.year = request.data['year']
    
    if 'giraffe' in request.data:
        population_edit.giraffe = request.data['giraffe']
    
    if 'grevy_zebra' in request.data:
       population_edit.grevy_zebra = request.data['grevy_zebra']
    
    if 'grant_gazelle' in request.data:
       population_edit.grant_gazelle = request.data['grant_gazelle']
    
    if 'hunters_hartebeest' in request.data:
        population_edit.hunters_hartebeest = request.data['hunters_hartebeest']
    
    if 'impala' in request.data:
        population_edit.impala = request.data['impala']

    if 'kongoni' in request.data:
        population_edit.kongoni = request.data['kongoni']

    if 'kudu' in request.data:
        population_edit.kudu = request.data['kudu']

    if 'oryx' in request.data:
        population_edit.oryx = request.data['oryx']

    if 'ostrich' in request.data:
        population_edit.ostrich = request.data['ostrich']
    
    if 'thomson_gazelle' in request.data:
        population_edit.thomson_gazelle = request.data['thomson_gazelle']
    
    if 'topi' in request.data:
       population_edit.topi = request.data['topi']
    
    if 'warthog' in request.data:
       population_edit.warthog = request.data['warthog']
    
    if 'waterbuck' in request.data:
       population_edit.waterbuck = request.data['waterbuck']
    
    if 'wildebeest' in request.data:
       population_edit.wildebeest = request.data['wildebeest']


    population_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

# ===============================Quantity_Of_Total_Mineral===============================
# Launch Page
def totalMineralView(request):
    mineral = Quantity_Of_Total_Mineral.objects.all()

    minerals = []

    if mineral:
        for min in mineral:
            c = {'id': min.quantity_id, 
                 'year': min.year,
                 'category': min.category,
                 'description': min.description,
                 'amount': min.amount}
            minerals.append(c)
            context = {'minerals': minerals}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_quantity_of_total_mineral.html', context)


# All minerals
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def totalMineral(request):
    mineral = Quantity_Of_Total_Mineral.objects.all()

    minerals = []

    if mineral:
        for min in mineral:
            c = {'year': min.year,
                 'category': min.category,
                 'description': min.description,
                 'amount': min.amount}
            minerals.append(c)
    else:
        pass
    return Response(minerals)


# Add View
def addTotalMineralView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_quantity_of_total_mineral_add.html')


# Edit View
def editTotalMineralView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_quantity_of_total_mineral_edit.html')


# Add mineral
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTotalMineral(request):
    mineral_add = Quantity_Of_Total_Mineral(amount=request.data['amount'],
                                            category=request.data['category'],
                                            description=request.data['description'],
                                            year=request.data['year'])

    if mineral_add:
        mineral_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit mineral
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTotalMineral(request):
    mineral_edit = Quantity_Of_Total_Mineral.objects.get(quantity_id=request.data['quantity_id'])

    if 'amount' in request.data:
        mineral_edit.amount = request.data['amount']

    if 'category' in request.data:
        mineral_edit.category = request.data['category']

    if 'year' in request.data:
        mineral_edit.year = request.data['year']
    
    if 'description' in request.data:
        mineral_edit.description = request.data['description']

    mineral_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


# ===============================Value_Of_Total_Mineral===============================
# Launch Page
def valueOfTotalMineralView(request):
    value = Value_Of_Total_Mineral.objects.all()

    values = []

    if value:
        for val in value:
            c = {'id': val.value_id,
                 'year': val.year,
                 'category': val.category,
                 'description': val.description,
                 'amount': val.amount}
            values.append(c)
            context = {'values': values}
    else:
        pass
    return render(request, 'knbs_bi/environment_and_natural_resources_value_of_total_mineral.html', context)


# All values
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def valueOfTotalMineral(request):
    mineral = Value_Of_Total_Mineral.objects.all()

    values = []

    if mineral:
        for val in mineral:
            c = {'year': val.year,
                 'category': val.category,
                 'description': val.description,
                 'amount': val.amount}
            values.append(c)
    else:
        pass
    return Response(values)


# Add View
def addValueOfTotalMineralView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_value_of_total_mineral_add.html')


# Edit View
def editValueOfTotalMineralView(request):
    return render(request, 'knbs_bi/environment_and_natural_resources_value_of_total_mineral_edit.html')


# Add mineral
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addValueOfTotalMineral(request):
    mineral_add = Value_Of_Total_Mineral(amount=request.data['amount'],
                                         category=request.data['category'],
                                         description=request.data['description'],
                                         year=request.data['year'])

    if mineral_add:
        mineral_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit mineral
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editValueOfTotalMineral(request):
    mineral_edit = Value_Of_Total_Mineral.objects.get(value_id=request.data['value_id'])

    if 'amount' in request.data:
        mineral_edit.amount = request.data['amount']

    if 'category' in request.data:
        mineral_edit.category = request.data['category']

    if 'year' in request.data:
        mineral_edit.year = request.data['year']
    
    if 'description' in request.data:
        mineral_edit.description = request.data['description']

    mineral_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

