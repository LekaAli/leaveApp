from django.test import TestCase
from .models import Leave,  Employee


class LeaveManagerTestCase(TestCase):

	def setUp(self):

		self.emp = self.create_employee()
		self.leave = self.create_leave(self.emp)

	def tearDown(self):
		self.emp = None
		self.leave = None
		
	def create_employee(self):
		employee_kwargs = {
			'emp_number': 'ABLT411',
			'phone_number': '0760426043',
			'first_name': 'Leka',
			'last_name': 'Tshoane'
			}
		return Employee(**employee_kwargs)

	def create_leave(self, emp):
		leave_kwargs = {
		'employee': emp,
		'start_date': '21/05/2019',
		'end_date': '31/05/2019',
		'days_of_leave': 2,
		'status': 0
		}
		return Leave(**leave_kwargs)

	def test_leave_start_is_less_than_end_date(self):

		self.assertTrue(self.leave.start_date < self.leave.end_date)
