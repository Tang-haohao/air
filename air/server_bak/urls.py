from django.contrib import admin
from django.urls import path
from user import views as user
from air import views as air
from flight import views as flight


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/info',user.info,name='info'),
    path('user/delete',user.delete,name='delete'),
    path('user/list',user.list,name='list'),
    path('user/login',user.login,name='login'),#登录
    path('user/registry',user.save,name='registry'),#登录
    path('user/page',user.page,name='pag'),#登录
    path('user/update',user.update,name='update'),#登录
    path('air/info',air.info,name='info'),#详情
    path('air/delete',air.delete,name='delete'),#删除
    path('air/list',air.list,name='list'),#查询所有
    path('air/save',air.save,name='save'),#新增
    path('air/update',air.update,name='update'),#修改
    path('air/page',air.page,name='pag'),#分页条件查询
    path('flight/info',flight.info,name='info'),#详情
    path('air/info1',air.info1,name='info1'),#详情
    path('flight/delete',flight.delete,name='delete'),#删除
    path('flight/list',flight.list,name='list'),#查询所有
    path('flight/save',flight.save,name='save'),#新增
    path('flight/update',flight.update,name='update'),#修改
    path('flight/page',flight.page,name='pag'),#分页条件查询
    path('flight/page1',flight.page1,name='pag1'),#分页条件查询

]
