from django.urls import path
from app.api.views import api_detail_item_view

app_name = 'app'

urlpatterns = [
    path('<slug>/', api_detail_item_view, name= 'detail')
]
