// Copyright (c) 2016, Alcazas and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["EODR Summary"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"reqd": 1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1
		},
		{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee"
		},
		{
			"fieldname":"department",
			"label": __("Department"),
			"fieldtype": "Link",
			"options": "Department"
		},
		{
			"fieldname":"job_scope",
			"label": __("Job Scope"),
			"fieldtype": "Link",
			"options": "Job Scope"
		},
		{
			"fieldname":"job_tier",
			"label": __("Job Tier"),
			"fieldtype": "Link",
			"options": "Job Tier"
		},
		{
			"fieldname":"job_description",
			"label": __("Job Description"),
			"fieldtype": "Link",
			"options": "Job Description"
		},
		{
			"fieldname":"job_classification",
			"label": __("Job Classification"),
			"fieldtype": "Select",
			"options": "\nStatic Job\nDynamic Job\nRoutine Job"
		}
	]
};
