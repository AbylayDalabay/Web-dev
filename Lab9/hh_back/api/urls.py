from django.contrib import admin
from django.urls import path
from .views import company_list, company, company_vacancy, vacancy_list, vacancy, vacancies_top

urlpatterns = [
    path("companies/", company_list),
    path('companies/<int:id>/', company),
    path('companies/<int:id>/vacancies/', company_vacancy),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:id>/', vacancy),
    path('vacancies/top_ten/', vacancies_top),
]