from django.urls import path
from api_app import views


urlpatterns = [
    path('employees/',views.EmployeeGerincView.as_view()),
    path('employees/<int:pk>',views.EmployeeRetrieveView.as_view()),

]