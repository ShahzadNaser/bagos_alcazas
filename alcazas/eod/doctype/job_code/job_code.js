// Copyright (c) 2021, Alcazas and contributors
// For license information, please see license.txt

frappe.ui.form.on('Job Code', {
	refresh: function(frm) {
		if(!frm.doc.__islocal){
			frm.toggle_enable(['department','job_scope','job_tier','job_description'], 0);
		}
	}
});
