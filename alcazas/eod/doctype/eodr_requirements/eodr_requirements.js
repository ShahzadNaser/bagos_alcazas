// Copyright (c) 2021, Alcazas and contributors
// For license information, please see license.txt

frappe.ui.form.on('EODR Requirements', {
	setup: function(frm) {
		frm.set_query("job_tier", "job_filters",function(doc, cdt, cdn) {
			var cdoc = locals[cdt][cdn];
			if (cdoc.department){
				return {
					filters: {
						"department": cdoc.department
					}
				}
			}
		});
		frm.set_query("job_scope", "job_filters",function(doc, cdt, cdn) {
			var cdoc = locals[cdt][cdn];
			if (cdoc.department || cdoc.job_tier){
				var filters = {}
				if (cdoc.department){
					filters["department"] = cdoc.department;
				}
				if(cdoc.job_tier){
					filters["job_tier"] = cdoc.job_tier;
				}
				return {
					filters: filters
				}
			}
		});

		frm.set_query("job_description", "job_filters",function(doc, cdt, cdn) {
			var cdoc = locals[cdt][cdn];
			if (cdoc.department || cdoc.job_tier || cdoc.job_scope){
				var filters = {}
				if (cdoc.department){
					filters["department"] = cdoc.department;
				}
				if(cdoc.job_tier){
					filters["job_tier"] = cdoc.job_tier;
				}
				if(cdoc.job_scope){
					filters["job_scope"] = cdoc.job_scope;
				}
				return {
					filters: filters
				}
			}
		});
	}
});

frappe.ui.form.on('Job Filters', {
	department: function(doc, cdt, cdn) {
		frappe.model.set_value(cdt, cdn, "job_tier", "");
	},
	job_tier: function(doc, cdt, cdn) {
		frappe.model.set_value(cdt, cdn, "job_scope", "");
	},
	job_scope: function(doc, cdt, cdn) {
		frappe.model.set_value(cdt, cdn, "job_description", "");
	}
});