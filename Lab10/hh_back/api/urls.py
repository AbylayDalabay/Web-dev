from django.urls import path

from api import views

app_name = 'api'
urlpatterns = [
    path('companies/', views.companies_list),
    path('companies/<int:id>/vacancies/', views.company_vacancy),
    path('companies/<int:id>/', views.company_by_id),
    path('vacancies/', views.VacancyListAPIView.as_view()),
    path('vacancies/<int:id>/', views.VacancyByIdAPIView.as_view()),
    path('vacancies/top_ten/', views.top_ten)
]