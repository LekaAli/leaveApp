#!/usr/bin/python3
# -*- coding: utf-8 -*-

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer, LeaveSerializer
from .models import Leave, Employee
from rest_framework.views import APIView
from rest_framework.response import Response


class EmployeeViewset(APIView):
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		request_query_params = self.request.query_params
		results = {'success': False, 'payload': 'Employee Number is Required', 'reason': 'Employee Number is Required'}
		if 'emp_number' in request_query_params:
			try:
				employee = Employee.objects.get(emp_number=request_query_params['emp_number'])
				serializer = EmployeeSerializer(employee)
				results = {'success': True, 'payload': serializer.data}
			except Exception as ex:
				results.update({'success': False, 'reason': ex, 'payload': ex})
		return Response(results)

	def post(self, request, *args, **kwargs):
		request_query_params = self.request.data
		# if
		return Response({})


class LeaveViewset(APIView):

	serializer_classes = (LeaveSerializer, )
	# authentication_classes = (SessionAuthentication, BasicAuthentication)
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		request_query_params = self.request.query_params
		results = {'success': False, 'payload': 'Employee Number is Required', 'reason': 'Employee Number is Required'}
		if 'emp_number' in request_query_params:
			try:
				employee = Employee.objects.get(emp_number=request_query_params['emp_number'])
				serializer = LeaveSerializer(employee.leave)
				results = {'success': True, 'payload': serializer.data}
			except Exception as ex:
				results.update({'success': False, 'reason': ex, 'payload': ex})
		return Response(results)

	def post(self, request, *args, **kwargs):

		return Response({})