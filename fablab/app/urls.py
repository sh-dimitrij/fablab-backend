from django.urls import path
from .views import *

urlpatterns = [
    # Набор методов для услуг
    path('api/works/search/', search_works),  # GET
    path('api/works/<int:work_id>/', get_work_by_id),  # GET
    path('api/works/<int:work_id>/image/', get_work_image),  # GET
    path('api/works/<int:work_id>/update/', update_work),  # PUT
    path('api/works/<int:work_id>/update_image/', update_work_image),  # PUT
    path('api/works/<int:work_id>/delete/', delete_work),  # DELETE
    path('api/works/create/', create_work),  # POST
    path('api/works/<int:work_id>/add_to_order/', add_work_to_order),  # POST

    # Набор методов для заявок
    path('api/orders/search/', search_orders),  # GET
    path('api/orders/<int:order_id>/', get_order_by_id),  # GET
    path('api/orders/<int:order_id>/update/', update_order),  # PUT
    path('api/orders/<int:order_id>/update_status_user/', update_status_user),  # PUT
    path('api/orders/<int:order_id>/update_status_admin/', update_status_admin),  # PUT
    path('api/orders/<int:order_id>/delete/', delete_order),  # DELETE
    path('api/orders/<int:order_id>/delete_work/<int:work_id>/', delete_work_from_order), # DELETE

    # Набор методов для аутентификации и авторизации
    path("api/register/", register),
    path("api/login/", login),
    path("api/check/", check),
    path("api/logout/", logout)
]
