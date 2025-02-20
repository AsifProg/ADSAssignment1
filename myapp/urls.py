from django.contrib import admin
from django.urls import path
from .views import delete_record,add_record,update_record
from myapp import views
urlpatterns = [
   #path('', admin.site.urls),
    path("", views.home,name="home"),
    #path("readrecord/", views.show_record,name="showrecord"),
    path("createrecord/", add_record,name="createrecord"),
    #path("deleterecord/", record_list,name="record_list"),
    path('deleterecord/<int:id>/', delete_record, name='deleterecord'),
    path('updaterecord/<int:id>/', update_record, name='updaterecord'),
]