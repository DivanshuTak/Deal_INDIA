from common_models.models import *
from rest_framework import serializers

class CustomersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta :
		model = Customers
		fields = ( 'customerName', 'contactLastName' )			

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta :
		model = Employees
		fields = ('employeeNumber', 'lastName', 'firstName', 'extension', 'email', 'officeCode', 'reportsTo', 'jobTitle', 'employeeNumber', 'lastName', 'firstName', 'extension', 'email', 'officeCode', 'reportsTo', 'jobTitle' )			

class OfficesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta :
		model = Offices
		fields = ( 'officeCode', 'city', 'phone', 'addressLine1', 'addressLine2', 'state', 'country' , 'postalCode', 'territory' )			

class OrderdetailsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta :
		model = Orderdetails
		fields = ('orderNumber', 'productCode', 'quantityOrdered', 'priceEach', 'orderLineNumber', 'orderNumber', 'productCode', 'quantityOrdered', 'priceEach', 'orderLineNumber')			

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
	class Meta :
		model = Orders
		fields = ('orderNumber', 'orderDate', 'requiredDate', 'shippedDate', 'status', 'comments', 'customerNumber', 'orderNumber', 'orderDate', 'requiredDate', 'shippedDate', 'status', 'comments', 'customerNumber')			

class PaymentsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta :
		model = Payments
		fields = ('customerNumber', 'checkNumber', 'paymentDate', 'amount', 'customerNumber', 'checkNumber', 'paymentDate', 'amount')			

class ProductlinesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta :
		model = Productlines
		fields = ('product_line', 'text_desc', 'html_desc', 'image' )			

class ProductsSerializer():
	class Meta : 
		model = Products
		fields = ('productCode', 'productName', 'productLine', 'productScale', 'productVendor', 'productDescription', 'quantityInStock', 'buyPrice', 'MSRP', 'productCode', 'productName', 'productLine', 'productScale', 'productVendor', 'productDescription', 'quantityInStock', 'buyPrice', 'MSRP' )		