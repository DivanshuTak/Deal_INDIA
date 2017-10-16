# -*- coding: utf-8 -*-
from common_models.models import *
from api.serializers import *
from rest_framework import viewsets

class CustomersViewsets(viewsets.ModelViewSet):
	"""
	generate view for customer table
	"""
	queryset = Customers.objects.all()
	serializer_class = CustomersSerializer

class EmployeesViewsets(viewsets.ModelViewSet):
	"""
	generate view for employees table
	"""
	queryset = Employees.objects.all().order_by('-customers')
	serializer_class = EmployeesSerializer
	
class OfficesViewsets(viewsets.ModelViewSet):
	"""
	generate view for offices table
	"""
	queryset = Offices.objects.all().order_by('-postalCode')
	serializer_class = CustomersSerializer
	
class OrderdetailsViewsets(viewsets.ModelViewSet):
	"""
	generate view for orderdetails table
	"""
	queryset = Orderdetails.objects.all().order_by('-orderNumber')
	serializer_class = CustomersSerializer
	
class OrdersViewsets(viewsets.ModelViewSet):
	"""
	generate view for orders table
	"""
	queryset = Orders.objects.all().order_by('-orderNumber')
	serializer_class = CustomersSerializer
	
class PaymentsViewsets(viewsets.ModelViewSet):
	"""
	generate view for payments table
	"""
	queryset = Payments.objects.all().order_by('-customerNumber')
	serializer_class = CustomersSerializer
	
class ProductlinesViewsets(viewsets.ModelViewSet):
	"""
	generate view for productlines table
	"""
	queryset = Productlines.objects.all()
	serializer_class = ProductlinesSerializer
	
class ProductsViewsets(viewsets.ModelViewSet):
	"""
	generate view for products table
	"""
	queryset = Products.objects.all().order_by('-productCode')
	serializer_class = CustomersSerializer
	