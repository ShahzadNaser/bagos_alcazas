# Copyright (c) 2013, Alcazas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)
	return columns, data

def get_columns():
	columns = [
		{"label": _("Reporting Date"), "fieldname": "eodr_date", "fieldtype": "Datetime", "width": 95},
		{"label": _("Employee"), "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 130},
		{"label": _("Employee Name"), "fieldname": "employee_name", "width": 100},
		{"label": _("EODR"), "fieldname": "eodr", "fieldtype": "Link", "options": "EODR", "width": 130},
		{"label": _("Total Expected Hours"), "fieldname": "total_expected_hours", "fieldtype": "Float", "width": 100},
		{"label": _("Total Spent Hours"), "fieldname": "total_spent_hours", "fieldtype": "Float", "width": 100},
		{"label": _("Static Job Hours"), "fieldname": "static_job_hours", "fieldtype": "Float", "width": 100},
		{"label": _("Static Job Hours %"), "fieldname": "static_job_hours_percentage", "fieldtype": "Percent", "width": 100},
		{"label": _("Dynamic Job Hours"), "fieldname": "dynamic_job_hours", "fieldtype": "Float", "width": 100},
		{"label": _("Dynamic Job Hours %"), "fieldname": "dynamic_job_hours_percentage", "fieldtype": "Percent", "width": 100},
		{"label": _("Routine Job Hours"), "fieldname": "routine_job_hours", "fieldtype": "Float", "width": 100},
		{"label": _("Routine Job Hours %"), "fieldname": "routine_job_hours_percentage", "fieldtype": "Percent", "width": 100},
	]

	return columns

def get_data(filters):
	condition = get_condition(filters)

	result = frappe.db.sql("""
			select t1.name as eodr, t1.employee, t1.employee_name, t1.eodr_date,
			t2.expected_hours, t2.hours, t2.job_classification
			from `tabEODR` as t1 inner join `tabJob Done` as t2 on t1.name = t2.parent
			inner join `tabJob Code` as t3 on t2.job_code = t3.name
			where t1.docstatus = 1 {condition} order by t1.eodr_date asc
		""".format(condition=condition), filters, as_dict=1)

	eodr = frappe._dict()
	data = []
	eodr_template = frappe._dict({
			"eodr": "",
			"employee": "",
			"employee_name": "",
			"eodr_date": "",
			"total_expected_hours": 0,
			"total_spent_hours": 0,
			"static_job_hours": 0,
			"static_job_hours_percentage": 0,
			"dynamic_job_hours": 0,
			"dynamic_job_hours_percentage": 0,
			"routine_job_hours": 0,
			"routine_job_hours_percentage": 0
		})
	for job in result:
		if not job.eodr in eodr:
			eodr[job.eodr] = []
		eodr[job.eodr].append(job)

	for key,val in eodr.items():
		result = eodr_template.copy()
		result.eodr = val[0].eodr
		result.employee = val[0].employee
		result.employee_name = val[0].employee_name
		result.eodr_date = val[0].eodr_date
		total_expected_hours = 0
		total_spent_hours = 0
		total_static_hours = 0
		total_dynamic_hours = 0
		total_routine_hours = 0
		for job in val:
			total_expected_hours += job.expected_hours
			total_spent_hours += job.hours
			if job.job_classification == 'Static Job':
				total_static_hours += job.hours
			elif job.job_classification == 'Dynamic Job':
				total_dynamic_hours += job.hours
			elif job.job_classification == 'Routine Job':
				total_routine_hours += job.hours
		result.total_expected_hours = total_expected_hours
		result.total_spent_hours = total_spent_hours
		result.static_job_hours = total_static_hours
		result.dynamic_job_hours = total_dynamic_hours
		result.routine_job_hours = total_routine_hours
		result.static_job_hours_percentage = ((result.static_job_hours * 100)/8) if result.static_job_hours else 0
		result.routine_job_hours_percentage = ((result.routine_job_hours * 100)/8) if result.routine_job_hours else 0
		result.dynamic_job_hours_percentage = ((result.dynamic_job_hours * 100)/8) if result.dynamic_job_hours else 0
		data.append(result)

	return data

def get_condition(filters):
	condition = " and t1.eodr_date between %(from_date)s and %(to_date)s "
	if filters.get("employee"):
		condition += " and t1.employee = %(employee)s "

	if filters.get("job_classification"):
		condition += " and t2.job_classification = %(job_classification)s "

	if filters.get("department"):
		condition += " and t3.department = %(department)s "
	if filters.get("job_scope"):
		condition += " and t3.job_scope = %(job_scope)s "
	if filters.get("job_tier"):
		condition += " and t3.job_tier = %(job_tier)s "
	if filters.get("job_description"):
		condition += " and t3.job_description = %(job_description)s "

	return condition