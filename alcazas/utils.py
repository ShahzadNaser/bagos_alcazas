# -*- coding: utf-8 -*-
# Copyright (c) 2021, Alcazas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.desk.reportview import get_match_cond, get_filters_cond
from erpnext.controllers.queries import get_fields

def check_department_code(doc, method):
	if doc.doctype == "Department":
		if len(doc.department_code) != 2:
			frappe.throw(_("Department Code must be of 2 digits."))


# searches for active employees
@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def job_code_search(doctype, txt, searchfield, start, page_len, filters):
	conditions = ""
	fields = get_fields("Job Code", ["name", "job_title"])

	if filters.get("eodr_requirements"):
		conditions += get_job_code_conditions(filters.get("eodr_requirements"))

	return frappe.db.sql("""select {fields} from `tabJob Code`
		where
			({key} like %(txt)s
				or job_title like %(txt)s)
			and {conditions}
		order by
			if(locate(%(_txt)s, name), locate(%(_txt)s, name), 99999),
			if(locate(%(_txt)s, job_title), locate(%(_txt)s, job_title), 99999),
			idx desc,
			name, job_title
		limit %(start)s, %(page_len)s""".format(**{
			'fields': ", ".join(fields),
			'key': searchfield,
			'conditions': conditions
		}), {
			'txt': "%%%s%%" % txt,
			'_txt': txt.replace("%", ""),
			'start': start,
			'page_len': page_len
		})


def get_job_code_conditions(eodr_requirements):
	edorr = frappe.get_doc("EODR Requirements", eodr_requirements)
	if not edorr.get("job_filters"):
		return " 1 = 1"
	conditions = "( "
	loop = 1
	for jb in edorr.get("job_filters"):
		conditions += "( 1 = 1 "
		if jb.get("department"):
			conditions += " and department = '{0}' ".format(jb.department)
		if jb.get("job_tier"):
			conditions += " and job_tier = '{0}' ".format(jb.job_tier)
		if jb.get("job_scope"):
			conditions += " and job_scope = '{0}' ".format(jb.job_scope)
		if jb.get("job_description"):
			conditions += " and job_description = '{0}' ".format(jb.job_description)
		conditions += " )"
		if loop != len(edorr.get("job_filters")):
			conditions += " or "
		loop += 1
	conditions += " )"
	return conditions