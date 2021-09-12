import frappe

def set_serial_no_in_job_card(doc, method):
    if doc.items[0].serial_no:
        serial_nos = doc.items[0].serial_no.split('\n')
        
        get_crm_job_card = frappe.db.get_value('Job Card', {'work_order':doc.work_order, 'operation': 'CRM'}, 'name')
        job_card = frappe.get_doc('Job Card', get_crm_job_card)

        for serial_no in serial_nos:
            print(serial_no)
            if serial_no != '':
                job_card.append('job_card_process', {
                    'input_coil_no': serial_no
                })
        job_card.save()
        frappe.db.commit()

def set_output_coil_no(doc, method):
    if doc.operation == 'CRM':
        get_trimming_job_card = frappe.db.get_value('Job Card', {'work_order':doc.work_order, 'operation': 'Trimming'}, 'name')
        trimming_job_card_process = frappe.db.get_all('Job Card Process', {'parent': doc.name}, ['input_coil_no'])
        if not trimming_job_card_process:
            job_card_process = frappe.db.get_all('Job Card Process', {'parent': doc.name}, ['input_coil_no', 'output_coil_no'])
            
            job_card = frappe.get_doc('Job Card', get_trimming_job_card)
            for i in job_card_process:
                if i['output_coil_no'] == None:
                    frappe.throw('Please add output coil no')
                else:
                    job_card.append('job_card_process', {
                        'input_coil_no': i['output_coil_no']
                    })
            job_card.save()
            frappe.db.commit()  

@frappe.whitelist()
def get_serial_nos(work_order):
    print(work_order)
    stock_entry = frappe.db.get_value('Stock Entry', {'work_order': work_order}, 'name')
    stock_entry_items = frappe.db.get_all('Stock Entry Detail', {'parent': stock_entry}, ['serial_no']) 
    if stock_entry_items:
        for i in stock_entry_items:
            if i['serial_no']:
                return i['serial_no'].split('\n')

@frappe.whitelist()
def get_serial_nos_from_crm(work_order):
    get_crm_job_card = frappe.db.get_value('Job Card', {'work_order':work_order, 'operation': 'CRM'}, 'name')
    job_card_process = frappe.db.get_all('Job Card Process', {'parent': get_crm_job_card}, ['output_coil_no'])
    if job_card_process:
        items = []
        for i in job_card_process:
            items.append(i['output_coil_no'])
        return items    