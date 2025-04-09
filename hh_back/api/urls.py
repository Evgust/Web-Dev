from django.urls import path
from .views import (
    CompanyListView, CompanyDetailView, CompanyVacancyListView,
    VacancyListView, VacancyDetailView, TopTenVacancyView
)

urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:id>/', CompanyDetailView.as_view(), name='company-detail'),
    path('companies/<int:id>/vacancies/', CompanyVacancyListView.as_view(), name='company-vacancies'),
    path('vacancies/', VacancyListView.as_view(), name='vacancy-list'),
    path('vacancies/<int:id>/', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('vacancies/top_ten/', TopTenVacancyView.as_view(), name='top-ten-vacancies'),
]
