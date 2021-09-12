# Copyright (c) 2013, Atriina Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	columns = ['Date:Date:80']+['Process:Data:100']+['Production Item:Data:150']+['Order No:Link/Work Order:150']+['Input Coil No:Data:100']+['Input Thick(mm):Data:100']+['Input Width(mm):Data:100']+['Input Weight(mm):Data:100']+['Grade:Data:80']+['Plan Thick(mm):Data:100']+['Rolling Thick(mm):Data:100']+['Output Coil No:Data:100']+['Output Weight(mt):Data:100']+['Yeild:Data:100']
	data = get_data(filters)
	return columns, data

def get_data(filters):
	if 'production_item' in filters and not 'order_no' in filters and not 'operation' in filters:
		query= "where jc.docstatus=1 and jc.posting_date between '{0}' and '{1}' and jc.production_item = '{2}' ".format(filters['from_date'], filters['to_date'], filters['production_item'])
		return filters_condition(query)
	elif 'order_no' in filters and not 'production_item' in filters  and not 'operation' in filters:
		query =	"where jc.docstatus=1 and jc.posting_date between '{0}' and '{1}' and jc.work_order = '{2}' " .format(filters['from_date'], filters['to_date'], filters['order_no'])
		return filters_condition(query)
	elif 'order_no' in filters and 'production_item' in filters  and 'operation' in filters:
		query ="where jc.docstatus=1 and jc.operation='{4}' and jc.posting_date between '{0}' and '{1}' and jc.production_item = '{2}' and jc.work_order = '{3}' ".format(filters['from_date'], filters['to_date'], filters['production_item'], filters['order_no'], filters['operation'])
		return filters_condition(query)
	elif 'order_no' in filters and not 'production_item' in filters and 'operation' in filters:
		query =	"where jc.docstatus=1 and jc.posting_date between '{0}' and '{1}' and jc.work_order = '{2}' and jc.operation='{3}' " .format(filters['from_date'], filters['to_date'], filters['order_no'], filters['operation'])
		return filters_condition(query)
	elif not 'order_no' in filters and 'production_item' in filters and 'operation' in filters:
		query ="where jc.docstatus=1 and jc.posting_date between '{0}' and '{1}' and jc.production_item = '{2}' and jc.operation = '{3}' ".format(filters['from_date'], filters['to_date'], filters['production_item'], filters['operation'])
		return filters_condition(query)
	elif not 'order_no' in filters and not 'production_item' in filters  and 'operation' in filters:
		query = "where jc.docstatus=1 and jc.posting_date between '{0}' and '{1}' and jc.operation = '{2}' ".format(filters['from_date'], filters['to_date'], filters['operation'])
		return filters_condition(query)	
	elif 'order_no' in filters and 'production_item' in filters and not 'operation' in filters:
		query ="where jc.docstatus=1 and jc.posting_date between '{0}' and '{1}' and jc.production_item = '{2}' and jc.work_order = '{3}' ".format(filters['from_date'], filters['to_date'], filters['production_item'], filters['order_no'])
		return filters_condition(query)
	else:
		query = "where jc.docstatus=1 and jc.posting_date between '{0}' and '{1}' ".format(filters['from_date'], filters['to_date'])
		return filters_condition(query)

def filters_condition(query):
	return frappe.db.sql("""
		select jc.posting_date, jc.operation,jc.production_item, jc.work_order, jcp.input_coil_no, jcp.input_thick, jcp.input_width, jcp.input_weight,
			jcp.grade, jcp.plan_thick, jcp.rolling_thick, jcp.output_coil_no, jcp.output_weight, (jcp.output_weight/jcp.input_weight)*100
		from `tabJob Card` as jc 
			join 
		`tabJob Card Process` as jcp 
			on jc.name = jcp.parent
		{}
	""".format(query))