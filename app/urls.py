from django.urls import path, include
from rest_framework.routers import DefaultRouter
import app.views as appView

# Create a router
router = DefaultRouter()

# Register your viewsets with the router
router.register(r'items', appView.ItemViewSet)

# Define your custom API views
urlpatterns = [
    path('', include(router.urls)),  # Include the viewsets from the router
    path('items/<int:pk>/', appView.ItemDetail.as_view(), name='item-detail'),  # Detail view for a single item
    path('InjuryPredict/', appView.InjuryPredict, name='InjuryPredict'),
]
