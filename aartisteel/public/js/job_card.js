frappe.ui.form.on('Job Card', {
	refresh(frm) {
        // your code here
        console.log('refresh')
		if (frm.doc.operation == 'CRM') {
		    frappe.call({
		        method: 'aartisteel.stock.get_serial_nos',
		        args: {
		            work_order: frm.doc.work_order
		        }
		    })
		    .success(success => {
		        console.log(success.message)
		        frm.fields_dict['job_card_process'].grid.get_field("input_coil_no").get_query = function(doc, cdt, cdn) {
                	return {
                		filters: [
                			['Serial No', 'name', 'in', success.message]
                		]
                	}
                }
                frm.fields_dict['job_card_process'].grid.get_field("output_coil_no").get_query = function(doc, cdt, cdn) {
                	return {
                		filters: [
                			['Serial No', 'name', '=', '']
                		]
                	}
                }
		    })
		}
		else if (frm.doc.operation == 'Trimming') {
		     frappe.call({
		        method: 'aartisteel.stock.get_serial_nos_from_crm',
		        args: {
		            work_order: frm.doc.work_order
		        }
		    })
		    .success(success => {
		        console.log(success.message)
		        frm.fields_dict['job_card_process'].grid.get_field("input_coil_no").get_query = function(doc, cdt, cdn) {
                	return {
                		filters: [
                			['Serial No', 'name', 'in', success.message]
                		]
                	}
                }
		    })
		}
		
	}
})