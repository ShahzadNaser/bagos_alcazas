# -*- coding: utf-8 -*-
# Copyright (c) 2021, Alcazas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class JobDescription(Document):
	def validate(self):
		if len(self.description_code) != 2:
			frappe.throw(_("Description Code must be of 2 digits."))

		if not self.job_scope_code:
			frappe.throw(_("No Code found for Job Scope: {0}").format(self.job_scope))

	def autoname(self):
		self.code = self.job_scope_code+''+self.description_code
		self.name = self.code+': '+ self.job_description

