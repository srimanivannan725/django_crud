from django.urls import path
from .import views

urlpatterns= [
    path("userreg/",views.userreg , name="userreg"),
    path("insertuser/",views.insertuser , name="insertuser"),
    path("readdata/",views.read , name="read"),
    path("update/<int:id>",views.update , name="update"),
    path("updatedatapost/<int:id>",views.updatedatapost , name="updatedatapost"),
    path("deletecrud/<str:id>",views.deletecrud,name="deletecrud"),
    
]