#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

class Employee(models.Model):
	emp_number = models.CharField(max_length=12, blank=False, null=False, unique=True)
	phone_number = models.CharField(max_length=10, blank=True, null=True)
	first_name = models.CharField(max_length=25, blank=True, null=True)
	last_name = models.CharField(max_length=35, blank=True, null=True)

	class Meta:
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'

	def __unicode__(self):

		return self.emp_number


def daysOfLeave(is_valid_period):
	if is_valid_period <= 0:
		
		raise ValidationError('Leave time period is invalid')
	else:
		return is_valid_period


class Leave(models.Model):
	LEAVE_STATUS = ((0, 'New'), (1, 'Approved'), (2, 'Declined'))
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave', blank=True, null=True)
	start_date = models.DateField()
	end_date = models.DateField()
	days_of_leave = models.SmallIntegerField(blank=True, null=True, validators=[daysOfLeave])
	status = models.SmallIntegerField(choices=LEAVE_STATUS)

	class Meta:
		verbose_name = 'Leave'
		verbose_name_plural = 'Leaves'

	def __unicode__(self):

		return '%s: %s' % (self.employee.emp_number, self.status) 

	def save(self, *args, **kwargs):
		self.days_of_leave = (self.end_date - self.start_date).days
		super(Leave, self).save(*args, **kwargs)
