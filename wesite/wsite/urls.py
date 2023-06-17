from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from wsite.views import *

urlpatterns = [
    path('users/', UserCollectionView.as_view()),
    path('cities/', CityCollectionView.as_view()),
    path('subs/', SubCollectionView.as_view()),
    path('users/<str:link>', UserCollectionViewDetail.as_view()),
    path('cities/<str:name>', CityCollectionViewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)