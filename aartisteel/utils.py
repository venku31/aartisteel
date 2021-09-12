import frappe
import datetime
import smtplib

def validate_tax_id(doc,method):
    if len(doc.tax_id) == 10:
        if doc.tax_id.isnumeric():
            return
        else:
            frappe.throw("Tax id should be numeric")
    else:
        frappe.throw("Tax id should be 10 digit")

def mail_notification_of_expiry_date():
    customer_list=frappe.db.get_all("Customer",fields=['*'])
    for doc in customer_list:
        customer_details=frappe.db.get_all("Customer Document Details",filters={"parent":doc.name},fields=['document_type','expiry_date','attachment'])
        if customer_details:
            for i in customer_details:
                today = datetime.date.today()
                if isinstance(i.expiry_date, str): 
                    expiry_date = datetime.strptime(i.expiry_date, '%Y-%m-%d')
                else:
                    expiry_date = i.expiry_date    
                remaining_days_count = expiry_date - today
                if (remaining_days_count.days <= 6 and remaining_days_count.days >= 0):
                    notification = frappe.get_doc('Notification', 'Customer Expiry')
                    args={'doc': doc}
                    doc.document_type=i.document_type
                    doc.remaining_days = remaining_days_count
                    recipients,cc,bb = notification.get_list_of_recipients(doc, args)
                    frappe.enqueue(method=frappe.sendmail, cc=cc, sender=None, 
                    subject=frappe.render_template(notification.subject, args), message=frappe.render_template(notification.message, args))