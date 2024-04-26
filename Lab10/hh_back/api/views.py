from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from api.models import Company, Vacancy
from api.serializers import CompanySerializer1,CompanySerializer2

from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Company, Vacancy
from api.serializers import VacancySerializer1,VacancySerializer2
from rest_framework import status
import json

class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer2(vacancies,many=True)
        return Response(serializer.data)
    def post(self, request):
        data = json.loads(request.body)
        vacancy_name = data.get('name', '')
        vacancy_company = Company.objects.get(id=data.get('company',''))
        vacancy = Vacancy.objects.create(name=vacancy_name,company=vacancy_company)
        return Response(vacancy.to_json())
class VacancyByIdAPIView(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(id=id)
        except:
            return Response({'error'}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        instance = self.get_object(id)
        serializer = VacancySerializer2(instance)
        return Response(serializer.data)
    def put(self, request, id):
        instance = self.get_object(id)
        serializer = VacancySerializer2(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        instance = self.get_object(id)
        instance.delete()
        return Response({'deleted': True})


@api_view(['GET','POST'])
def companies_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer1(companies,many=True)
        return Response(
            serializer.data
        )
    if request.method == 'POST':
        # data = json.loads(request.body)
        serializer = CompanySerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def company_by_id(request,id):
    try:
        company = Company.objects.get(id=id)
    except:
        return Response({'error'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = CompanySerializer2(company,many=False)
        return Response(serializer.data)
    if request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})
    if request.method == 'PUT':
        # data = json.loads(request.body)
        serializer = CompanySerializer2(instance=company,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
def company_vacancy(request, id):
    if request.method == 'GET':
        temp = []
        for i in list(Vacancy.objects.values()):
            if str(i['company_id']) == str(id):
                temp.append(i)
        # if len(temp) != 0:
        return JsonResponse(temp, safe=False, json_dumps_params={'indent': 2})

@csrf_exempt
def top_ten(request):
    return JsonResponse(
        list(Vacancy.objects.order_by('-salary')[:10].values()), safe=False, json_dumps_params={'indent': 2}
    )
