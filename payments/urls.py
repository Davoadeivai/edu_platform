from django.urls import path
from .views import StartPaymentView

urlpatterns = [
    path('start/<int:course_id>/', StartPaymentView.as_view(), name='start-payment'),
]
