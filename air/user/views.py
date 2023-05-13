from django.http import JsonResponse


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from datetime import datetime
import json
from .models import User

# Helper function
def get_json_field(data, field, default=None):
    try:
        return data[field]
    except KeyError:
        print(f"{field} is null")
        return default

@csrf_exempt
def save(request):
    data = json.loads(request.body)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    user = User(
        username=get_json_field(data, 'username'),
        name=get_json_field(data, 'name'),
        password=get_json_field(data, 'password'),
        role=get_json_field(data, 'role'),
        status=get_json_field(data, 'status'),
        reserve1=get_json_field(data, 'reserve1'),
        reserve2=get_json_field(data, 'reserve2'),
        reserve3=get_json_field(data, 'reserve3'),
        reserve4=get_json_field(data, 'reserve4'),
        reserve5=get_json_field(data, 'reserve5'),
        create_time=now
    )
    user.save()

    content = {
        'success': True,
        'message': '  Successfully added',
        'data': data
    }
    return HttpResponse(json.dumps(content), content_type='application/json')

@csrf_exempt
def update(request):
    data = json.loads(request.body)
    user = User.objects.get(id=data['id'])

    fields = ['username', 'name', 'password', 'role', 'status', 'reserve1', 'reserve2', 'reserve3', 'reserve4', 'reserve5']
    for field in fields:
        value = get_json_field(data, field, getattr(user, field))
        setattr(user, field, value)
    user.save()

    content = {
        'success': True,
        'message': 'Successfully modified',
        'data': data
    }
    return HttpResponse(json.dumps(content), content_type='application/json')

@csrf_exempt
def page(request):
    data = json.loads(request.body)
    search = data.get('search', None)
    users = User.objects.filter(name=search) if search else User.objects.all()

    paginator = Paginator(users, data['pageSize'])
    page = paginator.get_page(data['pageNum'])

    result = [{'id': user.id, 'username': user.username, 'name': user.name, 'password': user.password,
               'role': user.role, 'status': user.status, 'reserve1': user.reserve1, 'reserve2': user.reserve2,
               'reserve3': user.reserve3, 'reserve4': user.reserve4, 'reserve5': user.reserve5} for user in page]

    content = {
        'success': True,
        'message': 'query was successful',
        'data': result,
        'total': users.count()
    }
    return HttpResponse(json.dumps(content), content_type='application/json')

@csrf_exempt
@csrf_exempt
def login(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']

    user = User.objects.filter(username=username).first()
    if not user:
        content = {'success': False, 'message': 'user does not exist'}
    elif user.password != password:
        content = {'success': False, 'message': 'Password error'}
    else:
        content = {
            'success': True,
            'message': 'Login succeeded ',
            'data': {
                "username": user.username,
                "name": user.name,
                "role": 'airer',
            }
        }
    return HttpResponse(json.dumps(content), content_type='application/json')


def user_to_dict(user):
    return {
        'id': user.id,
        'username': user.username,
        'name': user.name,
        'password': user.password,
        'role': user.role,
        'status': user.status,
        'reserve1': user.reserve1,
        'reserve2': user.reserve2,
        'reserve3': user.reserve3,
        'reserve4': user.reserve4,
        'reserve5': user.reserve5
    }

def list(request):
    users = User.objects.all()
    user_list = [user_to_dict(user) for user in users]

    content = {
        'success': True,
        'message': 'query was successful',
        'data': user_list
    }
    return JsonResponse(content, json_dumps_params={'ensure_ascii': False})

def info(request):
    query_dict = request.GET
    id = query_dict.get('id')
    user = User.objects.get(id=id)

    content = {
        'success': True,
        'message': 'query was successful ',
        'data': user_to_dict(user)
    }
    return JsonResponse(content, json_dumps_params={'ensure_ascii': False})

def delete(request):
    query_dict = request.GET
    id = query_dict.get('id')
    User.objects.get(id=id).delete()

    content = {
        'success': True,
        'message': 'Successfully deleted',
    }
    return JsonResponse(content, json_dumps_params={'ensure_ascii': False})

