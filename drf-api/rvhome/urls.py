from django.urls import path
from .views import rvhomeList, rvhomeDetail

urlpatterns = [
    path('', rvhomeList.as_view(), name='rvhome_list'),
    path('<int:pk>/', rvhomeDetail.as_view(), name='rvhome_detail')
]
