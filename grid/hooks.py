# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "grid"
app_title = "Grid"
app_publisher = "Matt Lake"
app_description = "Makes a grid page"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "lake.matthew.s@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/grid/css/grid.css"
# app_include_js = "/assets/grid/js/grid.js"

# include js, css files in header of web template
# web_include_css = "/assets/grid/css/grid.css"
# web_include_js = "/assets/grid/js/grid.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "grid.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "grid.install.before_install"
# after_install = "grid.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "grid.notifications.get_notification_config"

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
# 		"grid.tasks.all"
# 	],
# 	"daily": [
# 		"grid.tasks.daily"
# 	],
# 	"hourly": [
# 		"grid.tasks.hourly"
# 	],
# 	"weekly": [
# 		"grid.tasks.weekly"
# 	]
# 	"monthly": [
# 		"grid.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "grid.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "grid.event.get_events"
# }

