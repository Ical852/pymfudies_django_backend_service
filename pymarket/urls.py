from django.urls import path
from pymarket.views import *

urlpatterns = [
    path('transaction', createTransaction),
    path('transaction/all', getAllTransactions),
]