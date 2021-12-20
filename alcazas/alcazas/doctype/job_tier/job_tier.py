# -*- coding: utf-8 -*-
# Copyright (c) 2021, Alcazas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class JobTier(Document):
	def validate(self):
		if len(self.tier_code) != 2:
			frappe.throw(_("Tier/Level Code must be of 2 digits."))

		if not self.department_code:
			frappe.throw(_("No Department Code found for Department: {0}").format(self.department))

	def autoname(self):
		self.code = self.department_code+''+self.tier_code
		self.name = self.code+': '+ self.job_tier
