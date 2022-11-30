from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

# Create your views here.
#
# Departments API
#
@api_view(["GET", "POST"])
def departments(request):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)

        return Response(departments_serializer.data, status=200)

    elif request.method == 'POST':
        department_data = request.data
        departments_serializer = DepartmentSerializer(data=department_data)
        
        if departments_serializer.is_valid():
            departments_serializer.save()

            return Response('Department added successfully', status=200)
        
        return Response('Failed to add department', status=401)

    return Response('Unknown request method', status=401)

@api_view(["GET", "PUT", "DELETE"])
def department(request, id):
    if request.method == 'GET':
        department = Departments.objects.get(DepartmentId = id)
        departments_serializer = DepartmentSerializer(department, many=False)

        return Response(departments_serializer.data, status=200)

    elif request.method == 'PUT':
        department_data = request.data
        department = Departments.objects.get(DepartmentId = id)
        departments_serializer = DepartmentSerializer(department, data=department_data)

        if departments_serializer.is_valid():
            departments_serializer.save()

            return Response('Department updated successfully', status=200)
        
        return Response('Failed to update department', status=401)

    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId = id)
        department.delete()

        return Response('Department deleted successfully', status=200)

    return Response('Unknown request method', status=401)
#
# Employees API
#
@api_view(["GET", "POST"])
def employees(request):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)

        return Response(employees_serializer.data, status=200)

    elif request.method == 'POST':
        employee_data = request.data
        employees_serializer = EmployeeSerializer(data=employee_data)
        
        if employees_serializer.is_valid():
            employees_serializer.save()

            return Response('Employee added successfully', status=200)
        
        return Response('Failed to add employee', status=401)

@api_view(["GET", "PUT", "DELETE"])
def employee(request, id):
    if request.method == 'GET':
        employee = Employees.objects.get(EmployeeId = id)
        employees_serializer = EmployeeSerializer(employee, many=False)

        return Response(employees_serializer.data, status=200)

    elif request.method == 'PUT':
        employee_data = request.data
        employee = Employees.objects.get(EmployeeId = id)
        employees_serializer = EmployeeSerializer(employee, data=employee_data)

        if employees_serializer.is_valid():
            employees_serializer.save()

            return Response('Employee updated successfully', status=200)
        
        return Response('Failed to update employee', status=401)

    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId = id)
        employee.delete()

        return Response('Employee deleted successfully', status=200)

@api_view(['POST'])
def saveFile(request, id):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)

    employee = Employees.objects.get(EmployeeId = id)
    employee.PhotoFilePath = file_name
    employee.save()

    return Response('Employee photo updated successfully', status=200)