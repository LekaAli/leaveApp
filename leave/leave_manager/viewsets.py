#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.forms import model_to_dict
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
				ex = str(ex)
				results.update({'success': False, 'reason': ex, 'payload': ex})
		return Response(results)

	def post(self, request):
		results = dict()
		request_query_params = self.request.data
		try:
			employee = Employee.objects.create(**request_query_params)
			employee.save()
			results.update({'success': True, 'payload': model_to_dict(employee)})
		except Exception as ex:
			ex = str(ex)
			results.update({'success': False, 'reason': ex, 'payload': ex})

		return Response(results)


class LeaveViewset(APIView):

	serializer_classes = (LeaveSerializer, )
	permission_classes = (IsAuthenticated, )

	def get(self, request):
		request_query_params = self.request.query_params
		results = {'success': False, 'payload': 'Employee Number is Required', 'reason': 'Employee Number is Required'}
		if 'emp_number' in request_query_params:
			try:
				employee = Leave.objects.get(employee__emp_number=request_query_params['emp_number'])
				results = {'success': True, 'payload': model_to_dict(employee)}
			except Exception as ex:
				ex = str(ex)
				results.update({'success': False, 'reason': ex, 'payload': ex})
		return Response(results)

	def post(self, request, *args, **kwargs):
		request_query_params = self.request.data
		results = dict()
		try:
			emp_number = request_query_params['emp_number']
			employee = Employee.objects.get(emp_number=emp_number)
			leave_kwargs = {
				'employee': employee,
				'start_date': request_query_params.get('start_date'),
				'end_date': request_query_params.get('end_date'),
				'status': 0
			}
			leave = Leave.objects.create(**leave_kwargs)
			leave.save()
			results.update({'success': True, 'payload': model_to_dict(leave)})
		except Exception as ex:
			ex = str(ex)
			results.update({'success': False, 'payload': ex, 'reason': ex})

		return Response(results)
