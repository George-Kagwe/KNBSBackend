from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from Household_Income.models import Household_Kihibs_Households_That_Sought_Credit
from health.models import Counties

############################################KIHBIS II############################################
####################################Household_Kihibs_Households_That_Sought_Credit####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsCredit(request):
    households_credit = Household_Kihibs_Households_That_Sought_Credit.objects.all()

    households = []

    if households_credit:
        for household in households_credit:
            county = Counties.objects.get(county_id=household.county_id)

            c = {'county': county.county_name, 'h_sought': household.h_sought,
                 'households': household.households, 'h_a_sought': household.h_a_sought, 'hholds_sought': household.hholds_sought}

            households.append(c)
    else:
        pass
    return Response(households)