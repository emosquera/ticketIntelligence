# -*- encoding: utf-8 -*-
from django.contrib.auth.hashers import make_password

from backend.models import Customer, Company
from backend.serializers import CustomerSerializer
from django.contrib.auth.models import User, Permission

__author__ = 'conamerica15'


def auth_user(user, request):
    if user is None:
        result = {
            "status": "FAILURE",
            "msg_status": ("Datos incorrectos"),
        }
        return result

    if user.is_active is False:
        result = {
            "status": "FAILURE",
            "msg_status": ("El usuario se encuentra suspendido"),
        }
        return result

    result = {
        "status": "SUCCESS",
        "msg_status": "Usuario correcto",
    }
    return result


def get_user(user):
    if user.has_perm("backend.is_customer") is True:
        return Customer.objects.get(user=user)


def make_error(errors, errormessages):
    """
    Método que hace una iteración recursiva por todos los valores que devuelve serializer.errors.values()
    y concatena y adiciona en una lista todos los valores que contengan la clave "message"
    :param errors: Lista [].values()
    :param errormessages: Lista []
    :return: Lista [] recibida por parámetro de entrada (errormessages)
    """
    for error in errors:
        if error.has_key("message"):
            errormessages.append(error)
        else:
            make_error(error.values(), errormessages)
    return errormessages;


def save_user(data, userpermission):
    user = User.objects.create(**data["user"])
    user.first_name = data["name"]
    user.last_name = data["lastName"]
    perm = Permission.objects.get(codename=userpermission)
    user.user_permissions.add(perm)
    user.password = make_password(user.password)
    user.save()
    return user
