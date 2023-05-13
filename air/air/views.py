import json

from django.forms import model_to_dict

from django.core.serializers import serialize
import json
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import Air
from datetime import datetime

from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from air.models import Air
import json

@csrf_exempt
def delete(request):
    id = request.GET.get('id')
    Air.objects.get(id=id).delete()
    content = {
        'success': True,
        'message': 'Successfully deleted',
    }
    return HttpResponse(json.dumps(content), content_type='application/json')

@csrf_exempt
def update(request):
    jsonData = json.loads(request.body)
    air = Air.objects.get(id=jsonData['id'])
    for key, value in jsonData.items():
        if hasattr(air, key):
            setattr(air, key, value)
    air.save()
    content = {
        'success': True,
        'message': 'Successfully modified',
        'data': jsonData
    }
    return HttpResponse(json.dumps(content), content_type='application/json')

@csrf_exempt
def page(request):
    data = json.loads(request.body)
    pageNum, pageSize, search = data['pageNum'], data['pageSize'], data.get('search', None)
    res = Air.objects.filter(name=search) if search else Air.objects.all()
    total = res.count()
    paginator = Paginator(res, pageSize)
    page = paginator.get_page(pageNum)
    resList = [model_to_dict(item) for item in page]
    content = {
        'success': True,
        'message': 'Query was successful ',
        'data': resList,
        'total': total
    }
    return HttpResponse(json.dumps(content), content_type='application/json')


def save(request):
    jsonData = json.loads(request.body.decode())
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    fields = [
        'airCode', 'airCna', 'status', 'reserve1', 'reserve2', 'reserve3',
        'reserve4', 'reserve5', 'airC', 'airF', 'airFna', 'airTotal',
        'airY', 'airYna'
    ]

    data = {field: jsonData.get(field, None) for field in fields}
    if 'create_time' in Air._meta.fields:
        data['create_time'] = now

    air = Air(**data)
    air.save()

    # Serialize data for response
    air_data = serialize('json', [air])
    air_data = json.loads(air_data)[0]['fields']

    content = {
        'success': True,
        'message': 'query was successful',
        'data': air_data
    }

    return HttpResponse(content=json.dumps(content, ensure_ascii=False),
                        content_type='application/json;charset = utf-8')


def air_to_dict(air_obj):
    fields = ['id', 'airCode', 'airCna', 'status', 'reserve1', 'reserve2', 'reserve3',
              'reserve4', 'reserve5', 'airC', 'airF', 'airFna', 'airTotal', 'airY', 'airYna']
    return {field: getattr(air_obj, field) for field in fields}

def list(request):
    air_objects = Air.objects.all()
    air_list = [air_to_dict(air) for air in air_objects]
    content = {
        'success': True,
        'message': 'Search successful',
        'data': air_list,
    }
    return JsonResponse(content, json_dumps_params={'ensure_ascii': False}, charset='utf-8')

def info(request):
    air_id = request.GET.get('id')
    air_obj = Air.objects.get(id=air_id)
    air_dict = air_to_dict(air_obj)
    content = {
        'success': True,
        'message': 'Search successful',
        'data': air_dict,
    }
    return JsonResponse(content, json_dumps_params={'ensure_ascii': False}, charset='utf-8')

def info1(request):
    air_code = request.GET.get('airCode')
    air_obj = Air.objects.get(airCode=air_code)
    air_dict = air_to_dict(air_obj)
    content = {
        'success': True,
        'message': 'Search successful',
        'data': air_dict,
    }
    return JsonResponse(content, json_dumps_params={'ensure_ascii': False}, charset='utf-8')

