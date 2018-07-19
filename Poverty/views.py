from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Poverty.models import Overall_Estimates_By_Residence_And_County, Hardcore_Estimates_By_residence_And_County, \
    Food_Estimates_By_Residence_And_County, Food_And_Non_Food_Expenditure_Per_Adult_Equivalent, \
    Distribution_Of_Households_By_PointOfPurchasedFoodItems, Distribution_Of_Household_Food_Consumption, \
    Consumption_Expenditure_And_Quintile_Distribution
from health.models import Counties

############################################KIHBIS II############################################
####################################Overall_Estimates_By_Residence_And_County####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def overallEstimates(request):
    overall_estimates = Overall_Estimates_By_Residence_And_County.objects.all()

    reports = []

    if overall_estimates:
        for report in overall_estimates:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'headcount_rate': report.headcount_rate,
                 'distribution_of_the_poor': report.distribution_of_the_poor, 'poverty_gap': report.poverty_gap,
                 'severity_of_poverty': report.severity_of_poverty, 'population': report.population,
                 'number_of_poor': report.number_of_poor}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Hardcore_Estimates_By_residence_And_County####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def hardcoreEstimates(request):
    hardcore_estimates = Hardcore_Estimates_By_residence_And_County.objects.all()

    reports = []

    if hardcore_estimates:
        for report in hardcore_estimates:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'headcount_rate': report.headcount_rate,
                 'distribution_of_the_poor': report.distribution_of_the_poor, 'poverty_gap': report.poverty_gap,
                 'severity_of_poverty': report.severity_of_poverty, 'population': report.population,
                 'number_of_poor': report.number_of_poor}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Food_Estimates_By_Residence_And_County####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def foodEstimates(request):
    food_estimates = Food_Estimates_By_Residence_And_County.objects.all()

    reports = []

    if food_estimates:
        for report in food_estimates:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'headcount_rate': report.headcount_rate,
                 'distribution_of_the_poor': report.distribution_of_the_poor, 'poverty_gap': report.poverty_gap,
                 'severity_of_poverty': report.severity_of_poverty, 'population': report.population,
                 'number_of_poor': report.number_of_poor}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Food_And_Non_Food_Expenditure_Per_Adult_Equivalent####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def foodNonFood(request):
    food_nonFood = Food_And_Non_Food_Expenditure_Per_Adult_Equivalent.objects.all()

    reports = []

    if food_nonFood:
        for report in food_nonFood:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'food': report.food,
                 'non_food': report.non_food, 'category': report.category}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Distribution_Of_Households_By_PointOfPurchasedFoodItems####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def distributionHouseholds(request):
    dist_households = Distribution_Of_Households_By_PointOfPurchasedFoodItems.objects.all()

    reports = []

    if dist_households:
        for report in dist_households:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'supermarket': report.supermarket, 'open_market': report.open_market,
                 'kiosk': report.kiosk, 'general_shop': report.general_shop, 'specialised_shop': report.specialised_shop,
                 'informal_sources': report.informal_sources, 'other_formal_points': report.other_formal_points, 'number_of_observations': report.number_of_observations}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Distribution_Of_Household_Food_Consumption####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def distributionHouseholdsFood(request):
    dist_households = Distribution_Of_Household_Food_Consumption.objects.all()

    reports = []

    if dist_households:
        for report in dist_households:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'purchases': report.purchases, 'stock': report.stock,
                 'own_production': report.own_production, 'gifts': report.gifts}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Consumption_Expenditure_And_Quintile_Distribution####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def consumptionExpenditure(request):
    consumption_expenditure = Consumption_Expenditure_And_Quintile_Distribution.objects.all()

    reports = []

    if consumption_expenditure:
        for report in consumption_expenditure:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'mean': report.mean, 'median': report.median,
                 'quarter1': report.quarter1, 'quarter2': report.quarter2, 'quarter3': report.quarter3,
                 'quarter4': report.quarter4, 'quarter5': report.quarter5}

            reports.append(c)
    else:
        pass
    return Response(reports)