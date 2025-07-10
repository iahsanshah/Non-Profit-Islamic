app_name = "non_profit_mas"
app_title = "Non Profit MAS"
app_publisher = "Ahsan Shah"
app_description = "Non-Profit MAS is a custom ERPNext app designed to streamline nonprofit management. It helps organizations efficiently manage donations, grants, volunteers, events, and financial records while integrating seamlessly with ERPNext. The app provides tailored workflows for nonprofit operations, ensuring transparency, compliance, and efficient resource management."
app_email = "iahsanshah11@gmail.com"
app_license = "mit"


app_name = "non_profit_mas"
app_title = "Non Profit MAS"

# Website route for company selection
website_route_rules = [
    {
        "from_route": "/select-company",
        "to_route": "select-company",
        "type": "page",
        "template": "templates/pages/select_company.html"
    }
]

# non_profit_mas/hooks.py
app_include_js = "/assets/non_profit_mas/js/custom_pos.js"



app_include_js = "/assets/non_profit_mas/js/buying_dashboard_extension.js"

# Post login hook - point to the correct module path
on_login = "non_profit_mas.utils.login.on_login"
# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "non_profit_mas",
# 		"logo": "/assets/non_profit_mas/logo.png",
# 		"title": "Non Profit MAS",
# 		"route": "/non_profit_mas",
# 		"has_permission": "non_profit_mas.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/non_profit_mas/css/non_profit_mas.css"
# app_include_js = "/assets/non_profit_mas/js/non_profit_mas.js"

# include js, css files in header of web template
# web_include_css = "/assets/non_profit_mas/css/non_profit_mas.css"
# web_include_js = "/assets/non_profit_mas/js/non_profit_mas.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "non_profit_mas/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "non_profit_mas/public/icons.svg"

# Home Pages
# ----------

# override_whitelisted_methods = {
#     "frappe.auth.get_logged_user": "non_profit_mas.custom_login.get_logged_user"
# }
app_include_css = [
  "/assets/non_profit_mas/css/login.css"
  "/assets/non_profit_mas/css/sidebar.css"
  "/assets/non_profit_mas/js/sidebar.js"
]



doc_events = {
    "Salary Slip": {
        "before_save": "interio_floors.customize_hr.salary_slip.calculate_late_minutes"
    }
}




# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "non_profit_mas.utils.jinja_methods",
# 	"filters": "non_profit_mas.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "non_profit_mas.install.before_install"
# after_install = "non_profit_mas.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "non_profit_mas.uninstall.before_uninstall"
# after_uninstall = "non_profit_mas.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "non_profit_mas.utils.before_app_install"
# after_app_install = "non_profit_mas.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "non_profit_mas.utils.before_app_uninstall"
# after_app_uninstall = "non_profit_mas.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "non_profit_mas.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"non_profit_mas.tasks.all"
# 	],
# 	"daily": [
# 		"non_profit_mas.tasks.daily"
# 	],
# 	"hourly": [
# 		"non_profit_mas.tasks.hourly"
# 	],
# 	"weekly": [
# 		"non_profit_mas.tasks.weekly"
# 	],
# 	"monthly": [
# 		"non_profit_mas.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "non_profit_mas.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "non_profit_mas.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "non_profit_mas.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["non_profit_mas.utils.before_request"]
# after_request = ["non_profit_mas.utils.after_request"]

# Job Events
# ----------
# before_job = ["non_profit_mas.utils.before_job"]
# after_job = ["non_profit_mas.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"non_profit_mas.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

