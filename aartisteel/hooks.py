# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "aartisteel"
app_title = "Aarti Steel PLC"
app_publisher = "Atriina Technologies"
app_description = "Steel Manufacturing"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@atriina.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aartisteel/css/aartisteel.css"
# app_include_js = "/assets/aartisteel/js/aartisteel.js"

# include js, css files in header of web template
# web_include_css = "/assets/aartisteel/css/aartisteel.css"
# web_include_js = "/assets/aartisteel/js/aartisteel.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

app_include_js = "/assets/aartisteel/js/transaction.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "aartisteel.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "aartisteel.install.before_install"
# after_install = "aartisteel.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aartisteel.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"aartisteel.tasks.all"
# 	],
# 	"daily": [
# 		"aartisteel.tasks.daily"
# 	],
# 	"hourly": [
# 		"aartisteel.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aartisteel.tasks.weekly"
# 	]
# 	"monthly": [
# 		"aartisteel.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "aartisteel.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "aartisteel.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "aartisteel.task.get_dashboard_data"
# }

doc_events = {
    'Stock Entry': {
        'before_submit': 'aartisteel.stock.set_serial_no_in_job_card'
    },
    'Job Card': {
        'on_submit': 'aartisteel.stock.set_output_coil_no'
    },
	'Customer': {
		'before_save':'aartisteel.utils.validate_tax_id'
	},
}

doctype_js = {
	'Job Card' : 'public/js/job_card.js'
}

scheduler_events = {
 	"daily": [
		"aartisteel.utils.mail_notification_of_expiry_date"
	],
}