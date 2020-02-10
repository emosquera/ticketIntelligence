# -*- encoding: utf-8 -*-

from rest_framework import serializers, validators
from models import State, City, Customer, Company, Branch
from django.contrib.auth.models import User


class CustomSerializer(serializers.ModelSerializer):
    def custom_validator(self, typevalidator, field, message, *args, **kwargs):
        for validator in self.fields[field].validators:
            if isinstance(validator, typevalidator):
                validator.message = message
            else:
                validator.message = {"message" : validator.message}


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name')


class StateSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many = True)

    class Meta:
        model = State
        fields = ('id', 'name', 'cities')


class UserSerializer(CustomSerializer):

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        # Find UniqueValidator and set custom message
        self.custom_validator(validators.UniqueValidator, "username", {"message": "El correo electrónico ingresado ya se encuentra registrado"})

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class CustomerSerializer(CustomSerializer):
    city = CitySerializer(many=False)
    user = UserSerializer(many=False, required=False)
    address = serializers.CharField(max_length=1000, required=False, allow_blank=True)
    homePhone = serializers.CharField(max_length=20, required=False, allow_blank=True)
    cellPhone = serializers.CharField(max_length=20, required=False, allow_blank=True)

    def __init__(self, *args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)
        self.custom_validator(validators.UniqueValidator, "identityDoc", {"message": "La cédula ingresada ya se encuentra registrada"})

    class Meta:
        model = Customer
        fields = ('id', 'name', 'lastName', 'address', 'identityDoc', 'homePhone', 'cellPhone', 'email', 'city', 'type',
                  'user')


class CompanySerializer(CustomSerializer):
    city = CitySerializer(many=False, required=False)
    user = UserSerializer(many=False, required=False)
    address = serializers.CharField(max_length=1000, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=True)
    identityDoc = serializers.CharField(max_length=12, required=False)

    def __init__(self, *args, **kwargs):
        super(CompanySerializer, self).__init__(*args, **kwargs)
        self.custom_validator(validators.UniqueValidator, "identityDoc", {"message": "El Rif ingresado ya se encuentra registrado"})

    class Meta:
        model = Company
        fields = ('id', 'name', 'address', 'identityDoc', 'phone', 'city', 'type',
                  'user')


class BranchSerializer(CustomSerializer):
    city = CitySerializer(many=False, required=False)
    company = CompanySerializer(many=False)
    user = UserSerializer(many=False, required=False)
    address = serializers.CharField(max_length=1000, required=False, allow_blank=True)
    phone = serializers.CharField(max_length=20, required=False, allow_blank=True)

    class Meta:
        model = Branch
        fields = ('id', 'nickName', 'address', 'phone', 'city', 'branchCompany', 'type',
                  'user')
