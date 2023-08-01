from django.urls import path
from .views import *

urlpatterns=[
    path('Items/',AddItemView.as_view(),name='Items'),
    path('Show_Items/',ItemShowView.as_view(),name='Show_Items'),
    path('Update/<int:pk>',ItemUpdateView.as_view(),name='Update_Items'),
    path('Delete/<int:pk>',ItemDeleteView.as_view(),name='Delete_Items')

]