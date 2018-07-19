from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from health.models import Counties
from trade_and_commerce.models import Revenue_Collection_By_Title, Revenue_Collection_By_Id, \
    Revenue_Collection_By_Amount, Trading_Centres, Trading_Centres_Ids, Balance_Of_Trade, Import_Trade_Africa_Countries, \
    Quantities_Principal_Domestic_Exports, Quantities_Principal_Imports, Values_Of_Principal_Domestic_Exports, \
    Values_Of_Principal_Imports, Value_Of_Total_Exports_All_Destinations, Value_of_Total_Exports_European_Union, \
    Value_Total_Exports_East_Africa_Communities


def trade_and_commerce(request):
    return render(request, template_name='knbs_bi/trade_and_commerce.html')

#===============================Revenue_Collection_By_Title===============================
#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def tradeTitle(request):
    trade_title = Revenue_Collection_By_Title.objects.all()

    titles = []

    if trade_title:
        for title in trade_title:
            c = {'trade_and_commerce_title': title.tradeandcommerce_title}
            titles.append(c)
    else:
        pass

    return Response(titles)

#===============================Revenue_Collection_By_Id===============================
#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def tradeID(request):
    trade_id = Revenue_Collection_By_Id.objects.all()

    ids = []

    if trade_id:
        for id in trade_id:
            c = {'revenue_collection_title': id.revenuecollection_title}
            ids.append(c)
    else:
        pass

    return Response(ids)

#===============================Trade and Commerce Amount===============================
#Launch Page
def tradeAmountView(request):
    trade_amount = Revenue_Collection_By_Amount.objects.all()

    prices = []
    context={}

    if trade_amount:
        for price in trade_amount:
            county = Counties.objects.get(county_id=price.county_id)
            revenue = Revenue_Collection_By_Id.objects.get(revenuecollection_id=price.revenuecollection_id)
            c = {'county': county.county_name, 'revenue_collection_industry': revenue.revenuecollection_title,
                 'amount': price.amount, 'year': price.year}
            prices.append(c)
            context = {'prices': prices}

    return render(request, 'knbs_bi/trade_and_commerce_revenue_collection_by_amount.html', context)


#Trade and Commerce Add View
def addTradeAmountView(request):
    all_counties = Counties.objects.all()
    revenue = Revenue_Collection_By_Id.objects.all()
    context = {'counties': all_counties, 'revenues': revenue}
    # translation.activate('en')
    return render(request, 'knbs_bi/trade_and_commerce_revenue_collection_by_amount_add.html', context)

#Trade and Commerce Edit View
def editTradeAmountView(request):
    all_counties = Counties.objects.all()
    revenue = Revenue_Collection_By_Id.objects.all()
    context = {'counties': all_counties, 'revenues': revenue}
    return render(request, 'knbs_bi/trade_and_commerce_revenue_collection_by_amount_edit.html', context)

@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def tradeAmount(request):
    trade_amount = Revenue_Collection_By_Amount.objects.all()

    prices = []

    if trade_amount:
        for price in trade_amount:
            county = Counties.objects.get(county_id=price.county_id)
            revenue = Revenue_Collection_By_Id.objects.get(revenuecollection_id=price.revenuecollection_id)
            c = {'county': county.county_name, 'revenue_collection_industry': revenue.revenuecollection_title,
                 'amount': price.amount, 'year': price.year}
            prices.append(c)
    else:
        pass

    return Response(prices)

# Add Trade and Commerce
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTradeAmount(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    revenue = Revenue_Collection_By_Id.objects.get(revenuecollection_title=request.data['revenue'])

    if counties and revenue:
        kaunti = counties.county_id
        rev_id = revenue.revenuecollection_id

        trade_add = Revenue_Collection_By_Amount(county_id=kaunti, revenuecollection_id=rev_id, amount=request.data['amount'],
                                              year=request.data['year'])

        if trade_add:
            trade_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Edit Trade and Commerce
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTradeAmount(request):
    trade_edit = Revenue_Collection_By_Amount.objects.get(tradeandcommerce_id=request.data['trade_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        if counties:
            trade_edit.county_id = counties.county_id

    if 'revenue' in request.data:
        revenue = Revenue_Collection_By_Id.objects.get(revenuecollection_title=request.data['revenue'])
        if revenue:
            trade_edit.revenuecollection_id = revenue.revenuecollection_id

    if 'amount' in request.data:
        trade_edit.amount = request.data['amount']
    if 'year' in request.data:
        trade_edit.year = request.data['year']

    trade_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)

#===============================Trading_Centres===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def tradeCenters(request):
    trading_center = Trading_Centres.objects.all()

    centers = []

    if trading_center:
        for center in trading_center:
            county = Counties.objects.get(county_id=center.county_id)
            trading = Trading_Centres_Ids.objects.get(trading_centre_id=center.trading_centre_id)
            c = {'county': county.county_name, 'trading_center': trading.trading_centre,
                 'number': center.number, 'year': center.number}
            centers.append(c)
    else:
        pass

    return Response(centers)

#===============================Balance_Of_Trade===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def balanceTrade(request):
    balance_trade = Balance_Of_Trade.objects.all()

    balance = []

    if balance_trade:
        for trade in balance_trade:
            c = {'description': trade.description, 'amount_in_millions': trade.amount_in_millions,
                 'year': trade.year}
            balance.append(c)
    else:
        pass

    return Response(balance)

#===============================Import_Trade_Africa_Countries===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def importTrade(request):
    import_trade = Import_Trade_Africa_Countries.objects.all()

    imports = []

    if import_trade:
        for trade in import_trade:
            c = {'zones': trade.zones, 'country': trade.country,
                 'values': trade.values, 'year': trade.year}
            imports.append(c)
    else:
        pass

    return Response(imports)

#===============================Quantities_Principal_Domestic_Exports===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def domesticExports(request):
    domestic_exports = Quantities_Principal_Domestic_Exports.objects.all()

    exports = []

    if domestic_exports:
        for domestic in domestic_exports:
            c = {'description': domestic.description, 'quantity': domestic.quantity,
                 'year': domestic.year}
            exports.append(c)
    else:
        pass

    return Response(exports)

#===============================Quantities_Principal_Imports===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def principalImports(request):
    principal_imports = Quantities_Principal_Imports.objects.all()

    imports = []

    if principal_imports:
        for principal in principal_imports:
            c = {'commodity': principal.commodity, 'unit_of_quantity': principal.unit_of_quantity,
                 'quantity': principal.quantity, 'year': principal.year}
            imports.append(c)
    else:
        pass

    return Response(imports)

#===============================Values_Of_Principal_Domestic_Exports===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def principalExports(request):
    principal_exports = Values_Of_Principal_Domestic_Exports.objects.all()

    exports = []

    if principal_exports:
        for principal in principal_exports:
            c = {'description': principal.description, 'values': principal.values,
                 'year': principal.year}
            exports.append(c)
    else:
        pass

    return Response(exports)

#===============================Values_Of_Principal_Imports===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def valuesPrincipalImports(request):
    principal_imports = Values_Of_Principal_Imports.objects.all()

    imports = []

    if principal_imports:
        for principal in principal_imports:
            c = {'description': principal.description, 'quantity': principal.quantity,
                 'year': principal.year}
            imports.append(c)
    else:
        pass

    return Response(imports)

#===============================Value_Of_Total_Exports_All_Destinations===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def valuesExports(request):
    values_exports = Value_Of_Total_Exports_All_Destinations.objects.all()

    exports = []

    if values_exports:
        for total in values_exports:
            c = {'region': total.region, 'country': total.country,
                 'values_in_millions': total.value_in_millions, 'year': total.year}
            exports.append(c)
    else:
        pass

    return Response(exports)

#===============================Value_of_Total_Exports_European_Union===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def valuesExportsEuropean(request):
    values_exports = Value_of_Total_Exports_European_Union.objects.all()

    exports = []

    if values_exports:
        for total in values_exports:
            c = {'country': total.country, 'values_in_millions': total.value_in_millions,
                 'year': total.year}
            exports.append(c)
    else:
        pass

    return Response(exports)

#===============================Value_Total_Exports_East_Africa_Communities===============================
#Launch Page

#All
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def valuesExportsEastAfrica(request):
    values_exports = Value_Total_Exports_East_Africa_Communities.objects.all()

    exports = []

    if values_exports:
        for total in values_exports:
            c = {'country': total.country, 'values_in_millions': total.value_in_millions,
                 'year': total.year}
            exports.append(c)
    else:
        pass

    return Response(exports)

