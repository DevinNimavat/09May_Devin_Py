from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.getdata),
    path('get_data_id/<int:id>',views.get_data_id),
    path('add_data/',views.add_data),
    path('update_comment/<int:id>',views.update_comment),
    path('delete_comment/<int:id>',views.delete_comment),
]
