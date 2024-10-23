from django.contrib import admin
from django.urls import path
from .views import AllProductListView, AddNewProductView, RetrieveProductByIdView, RemovedProducView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='JO API',)

urlpatterns = [

    path(r'^$', schema_view),
    path('product/', AllProductListView.as_view()),
    path('product/<int:pk>/', RetrieveProductByIdView.as_view(), name='retrieve-product'),
    path('product_create/', AddNewProductView.as_view()),
    path('product_removed/<int:pk>/', RemovedProducView.as_view(), name='removed-product'),
]
