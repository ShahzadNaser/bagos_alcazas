# -*- coding: utf-8 -*-
# Copyright (c) 2021, Alcazas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class JobScope(Document):
	def validate(self):
		if len(self.scope_code) != 2:
			frappe.throw(_("Scope Code must be of 2 digits."))

		if not self.job_tier_code:
			frappe.throw(_("No Code found for Job Tier: {0}").format(self.job_tier))

	def autoname(self):
		self.code = self.job_tier_code+''+self.scope_code
		self.name = self.code+': '+ self.job_scope
