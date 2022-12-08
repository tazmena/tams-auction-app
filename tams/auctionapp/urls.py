from django.urls import path

from . import views, api

app_name = 'auctionapp'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.loginUser, name='login'),
    path('signup', views.signup, name='signup'),
    path('api/products/', views.fetch_products, name='fetch_products'),
    path('api/products/<int:product_id>/', views.fetch_products_id, name='fetch_product_id'),
    path('items/<int:product_id>', views.product_details, name='product_details')
    ## path('api/search/', api.api_search, name='api_search'),
]