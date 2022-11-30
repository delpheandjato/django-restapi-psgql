from django.urls import path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('departments', views.departments),   
    path('department/<int:id>', views.department),   
    path('employees', views.employees),   
    path('employee/<int:id>', views.employee), 
    path('employee/save_file/<int:id>', views.saveFile)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)