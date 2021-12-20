# -*- coding: utf-8 -*-
# Copyright (c) 2021, Alcazas and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class JobCode(Document):
	def autoname(self):
		description_code = frappe.db.get_value("Job Description", self.job_description, "code")
		self.name = description_code;
