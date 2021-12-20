// Copyright (c) 2021, Alcazas and contributors
// For license information, please see license.txt

frappe.ui.form.on('EODR', {
	setup: function(frm) {
		frm.set_query("job_code", "job_logs", function(doc, cdt, cdn) {
			if(!doc.eodr_requirements){
				frappe.throw(__("No EODR Requirements found for the employee."));
			}
			return {
				"query": "alcazas.utils.job_code_search",
				filters: {
					eodr_requirements: doc.eodr_requirements
				}
			}
		});
	},
	refresh: function(frm) {
		if(frm.doc.__islocal){
			frappe.call({
				method: "alcazas.eod.doctype.eodr.eodr.get_employee",
				callback: function(r){
					if(!r.message){
						frappe.set_route('List', 'EODR');
						frappe.throw(__("No Employee is attached with the user."));
					}
					frm.set_value("employee", r.message['employee'].name);
					frm.set_value("employee_name", r.message['employee'].employee_name);
					if(r.message['jc_assignment'] != 0){
						var jc_assignment = r.message['jc_assignment'];
						frm.set_value("eodr_requirements", jc_assignment.name);
						/*frm.set_value("department", jc_assignment.department);
						frm.set_value("job_scope", jc_assignment.job_scope);
						frm.set_value("job_tier", jc_assignment.job_tier);
						frm.set_value("job_description", jc_assignment.job_description);*/
						frm.set_value("supervisor", jc_assignment.supervisor);
						frm.refresh_fields();
					}
				}
			})
		}
	}
});
