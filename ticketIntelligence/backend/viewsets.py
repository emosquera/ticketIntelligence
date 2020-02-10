# -*- encoding: utf-8 -*-
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.contrib.auth.models import User, Permission
from enums.enums import UserPermissions, UserType
from django.contrib.auth import authenticate, login
from models import State, City, Customer, Company, Branch
from serializers import StateSerializer, CitySerializer, CustomerSerializer, UserSerializer, CompanySerializer, \
    BranchSerializer
from ticketIntelligence.utils import auth_user, get_user, make_error, save_user


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def create(self, request, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            user = save_user(request.data, UserPermissions.IS_CUSTOMER)
            city = City(**request.data["city"])
            customer = Customer(
                name=request.data["name"],
                type=UserType.CUSTOMER,
                lastName=request.data["lastName"],
                address=request.data["address"],
                identityDoc=request.data["identityDoc"],
                homePhone=request.data["homePhone"],
                cellPhone=request.data["cellPhone"],
                email=request.data["email"],
                city=city,
                user=user)

            customer.save()
            return Response(
                {"status": "SUCCESS", "msg_status": "Cliente creado satisfactoriamente. Puede ingresar con su nueva contrasena."})
        else:
            messages = []
            make_error(serializer.errors.values(), messages)
            return Response({"status": "FAILURE", "msg_status" : messages})


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def create(self, request, **kwargs):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            user = save_user(request.data, UserPermissions.IS_COMPANY)
            city = City(**request.data["city"])
            company = Company(
                name=request.data["name"],
                type=UserType.COMPANY,
                address=request.data["address"],
                identityDoc=request.data["identityDoc"],
                phone=request.data["phone"],
                city=city,
                user=user)

            company.save()
            return Response(
                {"status": "SUCCESS", "msg_status": "Estabecimiento creado satisfactoriamente. Puede ingresar con su nueva contrasena."})
        else:
            messages = []
            make_error(serializer.errors.values(), messages)
            return Response({"status": "FAILURE", "msg_status" : messages})


class BranchViewSet(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()

    def create(self, request, **kwargs):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            user = save_user(request.data, UserPermissions.IS_BRANCH)
            company = Company(**request.data["company"])
            city = City(**request.data["city"])
            branch = Branch(
                nickName=request.data["nickName"],
                type=UserType.BRANCH,
                address=request.data["address"],
                phone=request.data["phone"],
                branchCompany=company,
                city=city,
                user=user)
            branch.save()
            return Response(
                {"status": "SUCCESS", "msg_status": "Sucursal creada satisfactoriamente. Puede ingresar con su nueva contrasena."})
        else:
            messages = []
            make_error(serializer.errors.values(), messages)
            return Response({"status": "FAILURE", "msg_status" : messages})


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @list_route(methods=['post'])
    def authenticate(self, request, *args, **kwargs):
        user = authenticate(username=request.data["username"], password=request.data["password"])
        result = auth_user(user, request)
        if result["status"] == "SUCCESS":
            login(request, user)
        return Response(result)
