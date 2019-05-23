#!/usr/bin/python3
# -*- coding: utf-8 -*-
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer, LeaveSerializer
from .models import Leave, Employee


class EmployeeViewset(ModelViewSet):

	queryset = Employee.objects.all()
	serializer_classes = (EmployeeSerializer, )
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated, )


class LeaveViewset(ModelViewSet):
	queryset = Leave.objects.all()
	serializer_classes = (LeaveSerializer, )
	authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated, )