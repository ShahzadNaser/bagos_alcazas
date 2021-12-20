# -*- coding: utf-8 -*-
# Copyright (c) 2021, Alcazas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import nowdate, getdate, formatdate
from frappe.model.document import Document

class EODR(Document):
	def validate(self):
		self.calculate_hours()
		self.calculate_percentage()
		self.check_future_date()
		self.check_existing_record()

	def check_future_date(self):
		if getdate(self.eodr_date) > getdate(nowdate()):
			frappe.throw(_("Reporting Date must not be greater then Current Date."))

	def check_existing_record(self):
		existing = frappe.get_list("EODR", filters={ "employee": self.employee, "eodr_date": self.eodr_date, "name": ["!=", self.name] })
		if existing:
			frappe.throw(_("Record Already exist against this Reporting Date: {0}.".format(formatdate(self.eodr_date))))

	def calculate_hours(self):
		total_expected_hours = 0
		total_spent_hours = 0
		total_static_hours = 0
		total_dynamic_hours = 0
		total_routine_hours = 0

		for job in self.job_logs:
			total_expected_hours += job.expected_hours
			total_spent_hours += job.hours

			if job.job_classification == 'Static Job':
				total_static_hours += job.hours
			elif job.job_classification == 'Dynamic Job':
				total_dynamic_hours += job.hours
			elif job.job_classification == 'Routine Job':
				total_routine_hours += job.hours

		self.total_expected_hours = total_expected_hours
		self.total_spent_hours = total_spent_hours
		self.static_job_hours = total_static_hours
		self.dynamic_job_hours = total_dynamic_hours
		self.routine_job_hours = total_routine_hours

	def calculate_percentage(self):
		self.static_job_hours_percentage = ((self.static_job_hours * 100)/8) if self.static_job_hours else 0
		self.routine_job_hours_percentage = ((self.routine_job_hours * 100)/8) if self.routine_job_hours else 0
		self.dynamic_job_hours_percentage = ((self.dynamic_job_hours * 100)/8) if self.dynamic_job_hours else 0


@frappe.whitelist()
def get_employee(user=None):
	if not user:
		user = frappe.session.user
	employee = frappe.get_all("Employee", filters={"user_id": user}, fields=['name', 'employee_name'])
	jc_assignment = 0
	if employee:
		jc_assignment_list = frappe.get_all("EODR Requirements", filters={"employee": employee[0].name}, fields=['name', 'supervisor'])
		if jc_assignment_list:
			jc_assignment = jc_assignment_list[0]
	return {"employee": employee[0], "jc_assignment": jc_assignment} if employee else 0
