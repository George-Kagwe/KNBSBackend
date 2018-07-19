from django.shortcuts import render

# Create your views here.


from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from ICT.models import Kihibs_Households_Owned_Ict_Equipment_Services, Kihibs_Households_With_Internet_By_Type, \
    Kihibs_Households_With_Tv, Kihibs_Households_Without_Internet_By_Reason, \
    Kihibs_Population_Above18By_ReasonNotHaving_Phone, Kihibs_Population_Above18Subscribed_MobileMoney, \
    Kihibs_Population_By_IctEquipment_And_ServicesUsed, Kihibs_Population_That_DidntUseInternet_By_Reason, \
    Kihibs_Population_That_Used_Internet_By_Purpose, Kihibs_Population_Who_Used_Internet_By_Place, \
    Kihibs_Population_WithMobilePhone_AndAverageSims
from health.models import Counties

############################################KIHBIS II############################################
####################################Kihibs_Households_Owned_Ict_Equipment_Services####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsOwned(request):
    house_owned = Kihibs_Households_Owned_Ict_Equipment_Services.objects.all()

    households = []

    if house_owned:
        for house in house_owned:
            county = Counties.objects.get(county_id=house.county_id)

            c = {'county': county.county_name, 'computer': house.computer,
                 'television': house.television, 'households': house.households}

            households.append(c)
    else:
        pass
    return Response(households)

####################################Kihibs_Households_With_Internet_By_Type####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsInternet(request):
    house_internet = Kihibs_Households_With_Internet_By_Type.objects.all()

    households = []

    if house_internet:
        for house in house_internet:
            county = Counties.objects.get(county_id=house.county_id)

            c = {'county': county.county_name, 'fixed_wired': house.fixed_wired, 'fixed_wireless': house.fixed_wireless,
                 'mobile_broadband': house.mobile_broadband, 'mobile': house.mobile, 'other': house.other,
                 'households': house.households}

            households.append(c)
    else:
        pass
    return Response(households)

####################################Kihibs_Households_With_Tv####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsTV(request):
    house_tv = Kihibs_Households_With_Tv.objects.all()

    households = []

    if house_tv:
        for house in house_tv:
            county = Counties.objects.get(county_id=house.county_id)

            c = {'county': county.county_name, 'digital_tv': house.digital_tv, 'pay_tv': house.pay_tv,
                 'free_to_air': house.free_to_air, 'ip_tv': house.ip_tv, 'none': house.none,
                 'households': house.households}

            households.append(c)
    else:
        pass
    return Response(households)

####################################Kihibs_Households_Without_Internet_By_Reason####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def householdsWithoutInternet(request):
    house_internet = Kihibs_Households_Without_Internet_By_Reason.objects.all()

    households = []

    if house_internet:
        for house in house_internet:
            county = Counties.objects.get(county_id=house.county_id)

            c = {'county': county.county_name, 'dont_need': house.dont_need, 'lack_skills': house.lack_skills,
                 'no_network': house.no_network, 'access_elsewhere': house.access_elsewhere, 'doesnt_meet_needs': house.doesnt_meet_needs,
                 'service_cost_high': house.service_cost_high, 'equipment_cost_high': house.equipment_cost_high, 'cultural_reasons': house.cultural_reasons,
                 'other_reasons': house.other_reasons, 'households': house.households}

            households.append(c)
    else:
        pass
    return Response(households)

####################################Kihibs_Population_Above18By_ReasonNotHaving_Phone####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationNoPhone(request):
    pop_phone = Kihibs_Population_Above18By_ReasonNotHaving_Phone.objects.all()

    population = []

    if pop_phone:
        for pop in pop_phone:
            county = Counties.objects.get(county_id=pop.county_id)

            c = {'county': county.county_name, 'population': pop.population, 'too_young': pop.too_young,
                 'dont_need': pop.dont_need, 'restricted': pop.restricted, 'no_network': pop.no_network,
                 'gender_bias': pop.gender_bias, 'no_electricity': pop.no_electricity, 'phone_expe': pop.phone_expe,
                 'maintain_expe': pop.maintain_expe, 'other': pop.other}

            population.append(c)
    else:
        pass
    return Response(population)

####################################Kihibs_Population_Above18Subscribed_MobileMoney####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationMobileMoney(request):
    pop_money = Kihibs_Population_Above18Subscribed_MobileMoney.objects.all()

    population = []

    if pop_money:
        for pop in pop_money:
            county = Counties.objects.get(county_id=pop.county_id)

            c = {'county': county.county_name, 'mobile_money': pop.mobile_money, 'mobile_banking': pop.mobile_banking,
                 'population': pop.population}

            population.append(c)
    else:
        pass
    return Response(population)

####################################Kihibs_Population_By_IctEquipment_And_ServicesUsed####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationIctEquipment(request):
    pop_ict = Kihibs_Population_By_IctEquipment_And_ServicesUsed.objects.all()

    population = []

    if pop_ict:
        for pop in pop_ict:
            county = Counties.objects.get(county_id=pop.county_id)

            c = {'county': county.county_name, 'television': pop.television, 'radio': pop.radio,
                 'mobile': pop.mobile, 'computer': pop.computer, 'internet': pop.internet,
                 'population': pop.population}

            population.append(c)
    else:
        pass
    return Response(population)

####################################Kihibs_Population_That_DidntUseInternet_By_Reason####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationIctNotUseInternet(request):
    pop_internet = Kihibs_Population_That_DidntUseInternet_By_Reason.objects.all()

    population = []

    if pop_internet:
        for pop in pop_internet:
            county = Counties.objects.get(county_id=pop.county_id)

            c = {'county': county.county_name, 'too_young': pop.too_young, 'dont_need': pop.dont_need,
                 'lack_skill': pop.lack_skill, 'expensive': pop.expensive, 'no_internet': pop.no_internet,
                 'culture': pop.culture, 'control': pop.control, 'security': pop.security,
                 'others': pop.others, 'not_stated': pop.not_stated, 'population': pop.population}

            population.append(c)
    else:
        pass
    return Response(population)

####################################Kihibs_Population_That_Used_Internet_By_Purpose####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationIctUsedInternet(request):
    pop_internet = Kihibs_Population_That_Used_Internet_By_Purpose.objects.all()

    population = []

    if pop_internet:
        for pop in pop_internet:
            county = Counties.objects.get(county_id=pop.county_id)

            c = {'county': county.county_name, 'seek_info': pop.seek_info, 'make_app': pop.make_app,
                 'get_info': pop.get_info, 'newspaper': pop.newspaper, 'banking': pop.banking,
                 'voip': pop.voip, 'selling': pop.selling, 'ordering': pop.ordering,
                 'course': pop.course, 'research': pop.research, 'informative': pop.informative,
                 'write_article': pop.write_article, 'social_nets': pop.social_nets, 'movie': pop.movie,
                 'search_work': pop.search_work, 'other': pop.other, 'population': pop.population}

            population.append(c)
    else:
        pass
    return Response(population)

####################################Kihibs_Population_Who_Used_Internet_By_Place####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationInternetPlace(request):
    pop_internet = Kihibs_Population_Who_Used_Internet_By_Place.objects.all()

    population = []

    if pop_internet:
        for pop in pop_internet:
            county = Counties.objects.get(county_id=pop.county_id)

            c = {'county': county.county_name, 'mobility': pop.mobility, 'work': pop.work,
                 'cyber': pop.cyber, 'ed_centre': pop.ed_centre, 'comm_centre': pop.comm_centre,
                 'another_home': pop.another_home, 'at_home': pop.at_home, 'other': pop.other,
                 'population': pop.population}

            population.append(c)
    else:
        pass
    return Response(population)

####################################Kihibs_Population_WithMobilePhone_AndAverageSims####################################
# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def populationWithMobile(request):
    pop_mobile = Kihibs_Population_WithMobilePhone_AndAverageSims.objects.all()

    population = []

    if pop_mobile:
        for pop in pop_mobile:
            county = Counties.objects.get(county_id=pop.county_id)

            c = {'county': county.county_name, 'phone': pop.phone, 'population': pop.population,
                 'avg_sims': pop.avg_sims, 'population_sims': pop.population_sims}

            population.append(c)
    else:
        pass
    return Response(population)