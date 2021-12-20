// Copyright (c) 2021, Alcazas and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Scope', {
	refresh: function(frm) {
		if(!frm.doc.__islocal){
			frm.toggle_enable(['job_scope', 'scope_code','job_tier'], 0);
		}
	}
});
