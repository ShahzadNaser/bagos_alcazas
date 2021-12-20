# -*- coding: utf-8 -*-
# Copyright (c) 2021, Alcazas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class EODRRequirements(Document):
	def validate(self):
		total_percent = (self.static_job if self.static_job else 0) + (self.dynamic_job if self.dynamic_job else 0) + (self.routine_job if self.routine_job else 0)
		if total_percent > 100:
			frappe.throw(_("Total Percentage of Staic Job, Routine Job and Dynamic Job must not exceed 100%"))
		#self.validate_job_filters()

	def validate_job_filters(self):
		if not self.job_filters: return
		departments = []
		for jf in self.job_filters:
			if jf.department not in departments:
				departments.append(jf.department)
			else:
				frappe.throw(_("Duplicate Department: {0} ").format(jf.department))
