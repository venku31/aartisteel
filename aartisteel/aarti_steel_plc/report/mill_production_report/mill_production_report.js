// Copyright (c) 2016, Atriina Technologies and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Mill Production Report"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"default": frappe.datetime.month_start()
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"default": frappe.datetime.month_end()
		},
		{
			"fieldname":"operation",
			"label": __("Operation"),
			"fieldtype": "Link",
			"options": "Operation",
			"default": "CRM"
		},
		{
			"fieldname":"production_item",
			"label": __("Product Item"),
			"fieldtype": "Data",
		},
		{
			"fieldname":"order_no",
			"label": __("Order No"),
			"fieldtype": "Link",
			"options": "Work Order"
		}
	]
};
