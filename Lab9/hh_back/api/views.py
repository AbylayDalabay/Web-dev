from django.shortcuts import render
from .models import Company, Vacancy
from django.http import HttpResponse, JsonResponse

# Create your views here.
# def get_companies(request):
#     companies = Company.objects.all()
#     return HttpResponse(companies) 

def company_list(request):
    try:
        comp = Company.objects.all()
    except:
        return HttpResponse("No companies yet")

    return JsonResponse([i.to_json() for i in comp], safe=False)


def vacancy_list(request):
    try:
        vac = Vacancy.objects.all()
    except:
        return HttpResponse("No vacancies yet")

    return JsonResponse([i.to_json() for i in vac], safe=False)


def company(request, id):
    try:
        comp = Company.objects.get(id=id)
    except:
        return HttpResponse("No info about a company")

    return JsonResponse(comp.to_json())


def company_vacancy(request, id):
    try:
        vac = Vacancy.objects.get(id=id)
    except:
        return HttpResponse("No info about a vacancy")

    return JsonResponse(vac.to_json())


def vacancy(request, id):
    try:
        vac = Vacancy.objects.filter(company=id)
    except:
        return HttpResponse('Company has no vacancies yet')

    return JsonResponse([i.to_json() for i in vac], safe=False)


def vacancies_top(request):
    vac = Vacancy.objects.order_by('-salary')

    return JsonResponse([i.to_json() for i in vac], safe=False)