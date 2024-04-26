from rest_framework import serializers
from api.models import Company,Vacancy
class CompanySerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    # description = serializers.CharField(max_length=1000)
    # city = serializers.CharField(max_length=255)
    # address = serializers.CharField(max_length=1000)
    def create(self, validated_data):
        company = Company.objects.create(**validated_data)
        return company
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class VacancySerializer1(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    # description = serializers.TextField(max_length=1000)
    salary = serializers.FloatField(default=1000)
    # company = serializers.ForeignKey("Company",on_delete=models.CASCADE,default=0)

class CompanySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','name','description','city')


class VacancySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id','name','description','salary')