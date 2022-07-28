'''
# Filtering against the current user

from .serializers import *
from rest_framework.generics import ListAPIView

class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    # queryset = Employee.objects.filter(manager_name='Naveen Chaudhary')
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(manager_name=user)


# DjangoFilterBackend

from .serializers import *
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['city', ]


# SearchFilter

from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter


class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [SearchFilter]
    # search_fields = ['city', ]
    # search_fields = ['name', 'employee_no', 'city', 'manager_name', ]

    # Notes :-
    # The search behavior may be restricted by prepending various characters to the search_fields.
    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search
    
    search_fields = ['name', ]
'''

# OrderingFilter

from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter


class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'city', ]
