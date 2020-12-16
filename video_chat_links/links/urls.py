from django.urls import path
from .views import (
    link_create_view, link_home_view, link_list_view
    )

app_name = 'links'

urlpatterns = [
    path('', link_home_view, name='link-home'),
    # path('<int:id>/', link_detail_view, name='link-detail'),
    # path('<int:id>/delete', link_delete_view, name='link-delete'),
    path('create/', link_create_view, name='link-create'), 
    path('list/', link_list_view, name='link-list')
]
