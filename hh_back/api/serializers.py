from rest_framework import serializers
from .models import Company, Vacancy

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    vacancies = VacancySerializer(many=True, read_only=True) 

    class Meta:
        model = Company
        fields = '__all__'
