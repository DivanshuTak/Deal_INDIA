from django.conf.urls import url, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'customers', views.CustomersViewsets)
router.register(r'employees',views.EmployeesViewsets)
router.register(r'offices',views.OfficesViewsets)
router.register(r'order-details',views.OrderdetailsViewsets)
router.register(r'orders',views.OrdersViewsets)
router.register(r'payments',views.PaymentsViewsets)
router.register(r'product-lines',views.ProductlinesViewsets)
router.register(r'products',views.ProductsViewsets)

urlpatterns = [
	url(r'^' , include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


