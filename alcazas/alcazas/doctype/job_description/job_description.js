// Copyright (c) 2021, Alcazas and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Description', {
	refresh: function(frm) {
		if(!frm.doc.__islocal){
			frm.toggle_enable(['job_description', 'description_code', 'job_scope'], 0);
		}
	}
});
