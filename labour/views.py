from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# from knbs_api.models import Sectors, Counties
from health.models import Counties  # , Sectors
from labour.models import Employment_Public_Sector, Sectors, Average_Wage_Earnings_Per_Employee_Private_Sector, \
    Average_Wage_Earnings_Per_Employee_Public_Sector, Memorandum_Items_In_Public_Sector, Total_Recorded_Employment, \
    Wage_Employment_By_Industry_And_Sex, Wage_Employment_By_Industry_In_Private_Sector, \
    Wage_Employment_By_Industry_In_Public_Sector


# Create your views here.
def labour(request):
    return render(request, template_name='knbs_bi/labour.html')


def no_records(request):
    datasets = Sectors.objects.order_by('Labour').count()
    context = {'labour_count': datasets}
    return render(request, 'knbs_bi/index.html', context)


@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def allSectors(request):
    all_sectors = Sectors.objects.all()

    sectors = []

    if all_sectors:
        for sector in all_sectors:
            c = {'sector_name': sector.sector_name}
            sectors.append(c)
    else:
        pass
    return Response(sectors)


# ===============================Employment Public Sector===============================
# Launch Page
def allPublicSectorView(request):
    public_sector = Employment_Public_Sector.objects.all()

    p_sectors = []

    if public_sector:
        for sector in public_sector:
            county = Counties.objects.get(county_id=sector.county_id)
            s_id = Sectors.objects.get(sector_id=sector.sector_id)

            c = {'id': sector.wage_employment_id, 'county': county.county_name, 'year': sector.year,
                 'sector': s_id.sector_name, 'wage_employment': sector.wage_employment}

            p_sectors.append(c)
            context = {'sectors': p_sectors}
    return render(request, 'knbs_bi/labour_employment_public_sector.html', context)


# Public Sector Add View
def addPublicSectorView(request):
    all_counties = Counties.objects.all()
    all_sectors = Sectors.objects.all()
    context = {'counties': all_counties, 'sectors': all_sectors}
    # translation.activate('en')
    return render(request, 'knbs_bi/labour_employment_public_sector_add.html', context)


# Public Sector Edit View
def editPublicSectorView(request):
    all_counties = Counties.objects.all()
    all_sectors = Sectors.objects.all()
    context = {'counties': all_counties, 'sectors': all_sectors}
    return render(request, 'knbs_bi/labour_employment_public_sector_edit.html', context)


# All Public Sector
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def publicSector(request):
    public_sector = Employment_Public_Sector.objects.all()

    p_sectors = []

    if public_sector:
        for sector in public_sector:
            county = Counties.objects.get(county_id=sector.county_id)
            s_id = Sectors.objects.get(sector_id=sector.sector_id)

            c = {'county': county.county_name, 'year': sector.year,
                 'sector': s_id.sector_name, 'wage_employment': sector.wage_employment_id}

            p_sectors.append(c)
    else:
        pass
    return Response(p_sectors)


# Add Public Sector
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addPublicSector(request):
    counties = Counties.objects.get(county_name=request.data['county'])
    sectors = Sectors.objects.get(sector_name=request.data['sector'])

    if counties and sectors:
        kaunti = counties.county_id
        sekta = sectors.sector_id

        public_add = Employment_Public_Sector(county_id=kaunti, year=request.data['year'], sector_id=sekta,
                                              wage_employment=request.data['wage'])

        if public_add:
            public_add.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Public Sector
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editPublicSector(request):
    public_edit = Employment_Public_Sector.objects.get(wage_employment_id=request.data['wage_id'])

    if 'county' in request.data:
        counties = Counties.objects.get(county_name=request.data['county'])
        # print("Got it")
        if counties:
            public_edit.county_id = counties.county_id

    if 'year' in request.data:
        public_edit.year = request.data['year']
    if 'sector' in request.data:
        s_id = Sectors.objects.get(sector_name=request.data['sector'])

        if s_id:
            public_edit.sector_id = s_id.sector_id
    if 'wage' in request.data:
        public_edit.wage_employment = request.data['wage']

    public_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


# ===============================Average_Wage_Earnings_Per_Employee_Private_Sector===============================
# Launch Page
def avgEarningsPrivateView(request):
    wages = Average_Wage_Earnings_Per_Employee_Private_Sector.objects.all()

    earnings = []

    if wages:
        for earning in wages:
            c = {'id': earning.wage_earnings_id, 'private_sector': earning.private_sector,
                 'wage_earnings': earning.wage_earnings,
                 'year': earning.year}
            earnings.append(c)
            context = {'earnings': earnings}
    else:
        pass
    return render(request, 'knbs_bi/labour_average_wage_earnings_per_employee_private_sector.html', context)


# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def avgEarningsPrivate(request):
    wages = Average_Wage_Earnings_Per_Employee_Private_Sector.objects.all()

    earnings = []

    if wages:
        for earning in wages:
            c = {'private_sector': earning.private_sector,
                 'wage_earnings': earning.wage_earnings,
                 'year': earning.year}
            earnings.append(c)
    else:
        pass
    return Response(earnings)


# Add View
def addAvgEarningsPrivateView(request):
    return render(request, 'knbs_bi/labour_average_wage_earnings_per_employee_private_sector_add.html')


# Edit View
def editAvgEarningsPrivateView(request):
    return render(request, 'knbs_bi/labour_average_wage_earnings_per_employee_private_sector_edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAvgEarningsPrivate(request):
    wage_add = Average_Wage_Earnings_Per_Employee_Private_Sector(private_sector=request.data['private'],
                                                                 wage_earnings=request.data['wage'],
                                                                 year=request.data['year'])

    if wage_add:
        wage_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAvgEarningsPrivate(request):
    wage_edit = Average_Wage_Earnings_Per_Employee_Private_Sector.objects.get(wage_earnings_id=request.data['earnings'])

    if 'private' in request.data:
        wage_edit.private_sector = request.data['private']

    if 'wage' in request.data:
        wage_edit.wage_earnings = request.data['wage']

    if 'year' in request.data:
        wage_edit.year = request.data['year']

    wage_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


# ===============================Average_Wage_Earnings_Per_Employee_Public_Sector===============================
# Launch Page
def avgEarningsPublicView(request):
    wages = Average_Wage_Earnings_Per_Employee_Public_Sector.objects.all()

    earnings = []

    if wages:
        for earning in wages:
            c = {'id': earning.wage_earnings_id, 'public_sector': earning.public_sector,
                 'wage_earnings': earning.wage_earnings,
                 'year': earning.year}
            earnings.append(c)
            context = {'earnings': earnings}
    else:
        pass
    return render(request, 'knbs_bi/labour_average_wage_earnings_per_employee_public_sector.html', context)


# All Records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def avgEarningsPublic(request):
    wages = Average_Wage_Earnings_Per_Employee_Public_Sector.objects.all()

    earnings = []

    if wages:
        for earning in wages:
            c = {'public_sector': earning.public_sector,
                 'wage_earnings': earning.wage_earnings,
                 'year': earning.year}
            earnings.append(c)
    else:
        pass
    return Response(earnings)


# Add View
def addAvgEarningsPublicView(request):
    return render(request, 'knbs_bi/labour_average_wage_earnings_per_employee_public_sector_add.html')


# Edit View
def editAvgEarningsPublicView(request):
    return render(request, 'knbs_bi/labour_average_wage_earnings_per_employee_public_sector_edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addAvgEarningsPublic(request):
    wage_add = Average_Wage_Earnings_Per_Employee_Public_Sector(public_sector=request.data['public'],
                                                                wage_earnings=request.data['wage'],
                                                                year=request.data['year'])

    if wage_add:
        wage_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editAvgEarningsPublic(request):
    wage_edit = Average_Wage_Earnings_Per_Employee_Public_Sector.objects.get(wage_earnings_id=request.data['earnings'])

    if 'public' in request.data:
        wage_edit.public_sector = request.data['public']

    if 'wage' in request.data:
        wage_edit.wage_earnings = request.data['wage']

    if 'year' in request.data:
        wage_edit.year = request.data['year']

    wage_edit.save()
    # response = {'success'}
    return Response(status=status.HTTP_201_CREATED)


# ==========================Memorandum_Items_In_Public_Sector=============================================#

# launch_page
def memorandumItemsPublicView(request):
    items = Memorandum_Items_In_Public_Sector.objects.all()

    memorandum_items = []

    if items:
        for item in items:
            c = {
                'id': item.memorandum_item_id,
                'memorandum': item.memorandum_item,
                'wage': item.wage_earnings,
                'year': item.year
            }

            memorandum_items.append(c)

            context = {'memorandum_items': memorandum_items}
    else:
        pass
    return render(request, 'knbs_bi/labour_memorandum_items_in_public_sector.html', context)


# all_records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def memorandumItemsPublic(request):
    items = Memorandum_Items_In_Public_Sector.objects.all()

    memorandum_items = []

    if items:
        for item in items:
            c = {'memorandum': item.memorandum_item,
                'wage': item.wage_earnings,
                'year': item.year}

            memorandum_items.append(c)
    else:
        pass
    return Response(memorandum_items)


# Add View
def addMemorandumItemsPublicView(request):
    return render(request, 'knbs_bi/labour_memorandum_items_in_public_sector_add.html')


# Edit View
def editMemorandumItemsPublicView(request):
    return render(request, 'knbs_bi/labour_memorandum_items_in_public_sector__edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addMemorandumItemsPublic(request):
    item_add = Memorandum_Items_In_Public_Sector(memorandum_item=request.data['memorandum'],
                                                 wage_earnings=request.data['wage'],
                                                 year=request.data['year'])
    if item_add:
        item_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editMemorandumItemsPublic(request):
    item_edit = Memorandum_Items_In_Public_Sector(memorandum_item_id=request.data['memorandum_id'])

    if 'memorandum' in request.data:
        item_edit.memorandum_item = request.data['memorandum']

    if 'wage' in request.data:
        item_edit.wage_earnings = request.data['wage']

    if 'year' in request.data:
        item_edit.year = request.data['year']

    item_edit.save()

    return Response(status=status.HTTP_201_CREATED)

#================================Total_Recorded_Employment=======================================#

# launch_page
def totalRecordedEmploymentView(request):
    records = Total_Recorded_Employment.objects.all()

    employment_records = []

    if records:
        for record in records:
            c = {
                'id': record.total_employment_id,
                'sector': record.sector_category,
                'total': record.total_employment,
                'year': record.year
            }

            employment_records.append(c)

            context = {'employment_records': employment_records}
    else:
        pass
    return render(request, 'knbs_bi/labour_total_recorded_employment.html', context)


# all_records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def totalRecordedEmployment(request):
    records = Total_Recorded_Employment.objects.all()

    employment_records = []

    if records:
        for record in records:
            c = {'sector': record.sector_category,
                'total': record.total_employment,
                'year': record.year}

            employment_records.append(c)
    else:
        pass
    return Response(employment_records)


# Add View
def addTotalRecordedEmploymentView(request):
    return render(request, 'knbs_bi/labour_total_recorded_employment_add.html')


# Edit View
def editTotalRecordedEmploymentView(request):
    return render(request, 'knbs_bi/labour_total_recorded_employment_edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addTotalRecordedEmployment(request):
    record_add = Total_Recorded_Employment(sector_category=request.data['sector'],
                                         total_employment=request.data['total'],
                                                 year=request.data['year'])
    if record_add:
        record_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editTotalRecordedEmployment(request):
   record_edit = Total_Recorded_Employment(total_employment_id=request.data['employment_id'])

   if 'sector' in request.data:
       record_edit.sector_category = request.data['sector']
   if 'total' in request.data:
       record_edit.total_employment = request.data['total']
   if 'year' in request.data:
       record_edit.year = request.data['year']

   record_edit.save()

   return Response(status=status.HTTP_201_CREATED)

#===============================Wage_Employment_By_Industry_And_Sex==============================#


# launch_page
def wageEmploymentByIndustryAndSexView(request):
    wages = Wage_Employment_By_Industry_And_Sex.objects.all()

    wage_records = []

    if wages:
        for wage in wages:
            c = {
                'id': wage.wage_employment_id,
                'industry': wage.industry,
                'wage': wage.wage_employment,
                'gender': wage.gender,
                'year': wage.year
            }

            wage_records.append(c)

            context = {'wage_records': wage_records}
    else:
        pass
    return render(request, 'knbs_bi/labour_wage_employment_by_industry_and_sex.html', context)


# all_records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def wageEmploymentByIndustryAndSex(request):
    wages = Wage_Employment_By_Industry_And_Sex.objects.all()

    wage_records = []

    if wages:
        for wage in wages:
            c = {'industry': wage.industry,
                'wage': wage.wage_employment,
                'gender': wage.gender,
                'year': wage.year}

            wage_records.append(c)
    else:
        pass
    return Response(wage_records)


# Add View
def addwageEmploymentByIndustryAndSexView(request):
    return render(request, 'knbs_bi/labour_wage_employment_by_industry_and_sex_add.html')


# Edit View
def editwageEmploymentByIndustryAndSexView(request):
    return render(request, 'knbs_bi/labour_wage_employment_by_industry_and_sex_edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addWageEmploymentByIndustryAndSex(request):
    wage_add = Wage_Employment_By_Industry_And_Sex(industry=request.data['industry'],
                                                   wage_employment=request.data['wage'],
                                                   gender=request.data['gender'],
                                                   year=request.data['year'])
    if wage_add:
        wage_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editWageEmploymentByIndustryAndSex(request):
   wage_edit = Wage_Employment_By_Industry_And_Sex(wage_employment_id=request.data['wage_id'])

   if 'industry' in request.data:
       wage_edit.industry = request.data['industry']
   if 'wage' in request.data:
       wage_edit.wage_employment = request.data['wage']
   if 'gender' in request.data:
       wage_edit.gender = request.data['gender']
   if 'year' in request.data:
       wage_edit.year = request.data['year']

   wage_edit.save()

   return Response(status=status.HTTP_201_CREATED)

#=======================================Wage_Employment_By_Industry_In_Private_Sector======================================#



# launch_page
def wageEmploymentByIndustryPrivateView(request):
    wages = Wage_Employment_By_Industry_In_Private_Sector.objects.all()

    wage_records = []

    if wages:
        for wage in wages:
            c = {
                'id': wage.wage_employment_id,
                'private': wage.private_sector,
                'wage': wage.wage_employment,
                'year': wage.year
            }

            wage_records.append(c)

            context = {'wage_records': wage_records}
    else:
        pass
    return render(request, 'knbs_bi/labour_wage_employment_by_industry_in_private_sector.html', context)


# all_records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def wageEmploymentByIndustryPrivate(request):
    wages = Wage_Employment_By_Industry_In_Private_Sector.objects.all()

    wage_records = []

    if wages:
        for wage in wages:
            c = {'private': wage.private_sector,
                'wage': wage.wage_employment,
                'year': wage.year}

            wage_records.append(c)
    else:
        pass
    return Response(wage_records)


# Add View
def addWageEmploymentByIndustryPrivateView(request):
    return render(request, 'knbs_bi/labour_wage_employment_by_industry_in_private_sector_add.html')


# Edit View
def editWageEmploymentByIndustryPrivateView(request):
    return render(request, 'knbs_bi/labour_wage_employment_by_industry_in_private_sector_edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addWageEmploymentByIndustryPrivate(request):
    wage_add = Wage_Employment_By_Industry_In_Private_Sector(private_sector=request.data['private'],
                                                   wage_employment=request.data['wage'],
                                                   year=request.data['year'])
    if wage_add:
        wage_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editWageEmploymentByIndustryPrivate(request):
   wage_edit = Wage_Employment_By_Industry_In_Private_Sector(wage_employment_id=request.data['wage_id'])

   if 'private' in request.data:
       wage_edit.private_sector = request.data['private']
   if 'wage' in request.data:
       wage_edit.wage_employment = request.data['wage']
   if 'year' in request.data:
       wage_edit.year = request.data['year']

   wage_edit.save()

   return Response(status=status.HTTP_201_CREATED)


#=======================================Wage_Employment_By_Industry_In_Public_Sector======================================#



# launch_page
def wageEmploymentByIndustryPublicView(request):
    wages = Wage_Employment_By_Industry_In_Public_Sector.objects.all()

    wage_records = []

    if wages:
        for wage in wages:
            c = {
                'id': wage.wage_employment_id,
                'public': wage.public_sector,
                'wage': wage.wage_employment,
                'year': wage.year
            }

            wage_records.append(c)

            context = {'wage_records': wage_records}
    else:
        pass
    return render(request, 'knbs_bi/labour_wage_employment_by_industry_in_public_sector.html', context)


# all_records
@api_view(http_method_names=['GET'])
@renderer_classes((JSONRenderer,))
def wageEmploymentByIndustryPublic(request):
    wages = Wage_Employment_By_Industry_In_Public_Sector.objects.all()

    wage_records = []

    if wages:
        for wage in wages:
            c = {'public': wage.public_sector,
                'wage': wage.wage_employment,
                'year': wage.year}

            wage_records.append(c)
    else:
        pass
    return Response(wage_records)


# Add View
def addWageEmploymentByIndustryPublicView(request):
    return render(request, 'knbs_bi/labour_wage_employment_by_industry_in_public_sector_add.html')


# Edit View
def editWageEmploymentByIndustryPublicView(request):
    return render(request, 'knbs_bi/labour_wage_employment_by_industry_in_public_sector_edit.html')


# Add Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def addWageEmploymentByIndustryPublic(request):
    wage_add = Wage_Employment_By_Industry_In_Public_Sector(public_sector=request.data['public'],
                                                   wage_employment=request.data['wage'],
                                                   year=request.data['year'])
    if wage_add:
        wage_add.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Edit Record
@api_view(http_method_names=['POST'])
@renderer_classes((JSONRenderer,))
def editWageEmploymentByIndustryPublic(request):
   wage_edit = Wage_Employment_By_Industry_In_Public_Sector(wage_employment_id=request.data['wage_id'])

   if 'public' in request.data:
       wage_edit.public_sector = request.data['public']
   if 'wage' in request.data:
       wage_edit.wage_employment = request.data['wage']
   if 'year' in request.data:
       wage_edit.year = request.data['year']

   wage_edit.save()
   return Response(status=status.HTTP_201_CREATED)
