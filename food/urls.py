from django.urls import path
from . import views

app_name='food'

urlpatterns = [
    path("",views.index,name='index'),
    path("<int:item_id>/",views.details,name="details"),
    path("add/",views.create_item,name="add"),
    path("update/<int:id>/",views.update_item,name="update"),
    path("delete/<int:id>/",views.delete_item,name="delete")
]