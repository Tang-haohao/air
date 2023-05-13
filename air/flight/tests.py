from django.test import TestCase

# Create your tests here.
# test.py

from django.db import models
from django.shortcuts import HttpResponse
from datetime import datetime
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json


class Flight(models.Model):
    airCode = models.CharField(max_length=100)
    create_time = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    reserve1 = models.CharField(max_length=100)
    reserve2 = models.CharField(max_length=100)
    reserve3 = models.CharField(max_length=100)
    reserve4 = models.CharField(max_length=100)
    reserve5 = models.CharField(max_length=100)
    comCode = models.CharField(max_length=100)
    flag = models.CharField(max_length=100)
    fliAaddress = models.CharField(max_length=100)
    fliAtime = models.CharField(max_length=100)
    fliBaddress = models.CharField(max_length=100)
    fliBtime = models.CharField(max_length=100)
    fliCfare = models.CharField(max_length=100)
    fliCnumber = models.CharField(max_length=100)
    fliDiscount = models.CharField(max_length=100)
    fliFfare = models.CharField(max_length=100)
    fliFnumber = models.CharField(max_length=100)
    fliNo = models.CharField(max_length=100)
    fliRefundtime = models.CharField(max_length=100)
    fliYfare = models.CharField(max_length=100)
    fliYnumber = models.CharField(max_length=100)

    class Meta:
        db_table = 'flight'
        verbose_name = "Flight"
        verbose_name_plural = verbose_name

    def __str__(self):
        return ""


def prepare_response(success, message, data, total=None):
    response = {
        'success': success,
        'message': message,
        'data': data,
    }
    if total is not None:
        response['total'] = total
    return JsonResponse(response, safe=False)


@csrf_exempt
def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    flight = Flight()
    for field in Flight._meta.fields:
        if field.name != 'id' and field.name != 'create_time':
            setattr(flight, field.name, jsonData.get(field.name, None))
    flight.create_time = now
    flight.save()
    return prepare_response(True, 'Successfully added', jsonData)


@csrf_exempt
def update(request):
    jsonData = json.loads(request.body.decode())
    flight = Flight.objects.get(id=jsonData['id'])
    for field in Flight._meta.fields:
        if field.name != 'id' and field.name != 'create_time':
            setattr(flight, field.name, jsonData.get(field.name, None))
    flight.save()
    return prepare_response(True, 'Successfully modified', jsonData)


def page(request):
    data = json.loads(request.body.decode())
    pageNum = data['pageNum']
    pageSize = data['pageSize']
    search = data.get('search', None)
    if search:
        flights = Flight.objects.filter(reserve1=search)
    else:
        flights = Flight.objects.all()
    paginator = Paginator(flights, pageSize)
    page = paginator.get_page(pageNum)
    resList = [model_to_dict(flight) for flight in page.object_list]
    return prepare_response(True, 'Query was successful', resList, total=flights.count())


def page1(request):
    # ... continuing from previous part

    data = json.loads(request.body.decode())
    pageNum = data['pageNum']
    pageSize = data['pageSize']
    search = data.get('search', None)
    if search:
        flights = Flight.objects.filter(**search)
    else:
        flights = Flight.objects.all()
    paginator = Paginator(flights, pageSize)
    page = paginator.get_page(pageNum)
    resList = [model_to_dict(flight) for flight in page.object_list]
    return prepare_response(True, 'Query was successful', resList, total=flights.count())


@csrf_exempt
def list(request):
    flights = Flight.objects.all()
    flight_list = [model_to_dict(flight) for flight in flights]
    data = {
        'success': True,
        'message': 'Query was successful',
        'data': flight_list
    }
    return JsonResponse(data, safe=False)


@csrf_exempt
def info(request):
    flight_id = request.GET.get('id')
    try:
        flight = Flight.objects.get(id=flight_id)
        flight_info = model_to_dict(flight)
        data = {
            'success': True,
            'message': 'Query was successful',
            'data': flight_info
        }
    except Flight.DoesNotExist:
        data = {
            'success': False,
            'message': 'Flight does not exist',
        }
    return JsonResponse(data, safe=False)


@csrf_exempt
def delete(request):
    flight_id = request.GET.get('id')
    try:
        flight = Flight.objects.get(id=flight_id)
        flight.delete()
        data = {
            'success': True,
            'message': 'Successfully deleted',
        }
    except Flight.DoesNotExist:
        data = {
            'success': False,
            'message': 'Flight does not exist',
        }
    return JsonResponse(data, safe=False)

