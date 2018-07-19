from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from health.models import Counties

from Nutrition.models import Kihibs_Undernourished_Children, Kihibs_Dutation_Of_Breastfeeding, \
    Kihibs_Children_In_Growth_Monitoring_Programmes, Kihibs_Children_In_Community_Nutrition_Programmes, \
    Kihibs_Children_By_First_Food_Supplement, Kihibs_Children_By_Breastfeeding_Status


############################################KIHBIS II############################################
####################################Kihibs_Undernourished_Children####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def undernourisedChildren(request):
    under_nourished = Kihibs_Undernourished_Children.objects.all()

    reports = []

    if under_nourished:
        for report in under_nourished:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'height_for_age': report.height_for_age,
                 'weight_for_age': report.weight_for_age, 'weight_for_height': report.weight_for_height,
                 'no_of_children': report.no_of_children, 'category': report.category}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Dutation_Of_Breastfeeding####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def durationBreastFeeding(request):
    breast_feeding = Kihibs_Dutation_Of_Breastfeeding.objects.all()

    reports = []

    if breast_feeding:
        for report in breast_feeding:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'breastfeeding': report.breastfeeding,
                 'mean': report.mean, 'median': report.median,
                 'no_of_children': report.no_of_children}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Children_In_Growth_Monitoring_Programmes####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def childrenGrowth(request):
    children_growth = Kihibs_Children_In_Growth_Monitoring_Programmes.objects.all()

    reports = []

    if children_growth:
        for report in children_growth:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'participated': report.participated,
                 'not_participated': report.not_participated, 'not_stated': report.not_stated,
                 'no_of_children': report.no_of_children}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Children_In_Community_Nutrition_Programmes####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def childrenCommunity(request):
    children_community = Kihibs_Children_In_Community_Nutrition_Programmes.objects.all()

    reports = []

    if children_community:
        for report in children_community:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'participated': report.participated,
                 'not_participated': report.not_participated, 'not_stated': report.not_stated,
                 'no_of_children': report.no_of_children}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Children_By_First_Food_Supplement####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def childrenFirst(request):
    children_first = Kihibs_Children_By_First_Food_Supplement.objects.all()

    reports = []

    if children_first:
        for report in children_first:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'other_milk': report.other_milk, 'infant_food': report.infant_food,
                 'porridge': report.porridge, 'fort_porridge': report.fort_porridge, 'semi_solids': report.semi_solids,
                 'water': report.water, 'not_stated': report.not_stated, 'no_of_children': report.no_of_children}

            reports.append(c)
    else:
        pass
    return Response(reports)

####################################Kihibs_Children_By_Breastfeeding_Status####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def childrenBreastFeeding(request):
    children_breastfeeding = Kihibs_Children_By_Breastfeeding_Status.objects.all()

    reports = []

    if children_breastfeeding:
        for report in children_breastfeeding:
            county = Counties.objects.get(county_id=report.county_id)

            c = {'county': county.county_name, 'ever_breastfed': report.ever_breastfed, 'no_of_children': report.no_of_children,
                 'one_hour': report.one_hour, 'one_day': report.one_day, 'ch_breastfed': report.ch_breastfed}

            reports.append(c)
    else:
        pass
    return Response(reports)