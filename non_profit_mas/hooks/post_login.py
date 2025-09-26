import frappe
from frappe import _

def on_login(login_manager):
    # Skip for Administrator
    if frappe.session.user == "Administrator":
        return
        
    # Check if user has access to multiple companies
    companies = frappe.get_list("Company", 
        filters={},
        fields=["name"],
        ignore_permissions=True
    )
    
    # If more than one company exists, redirect to selection page
    if len(companies) > 1 and not frappe.local.request.path.startswith("/select-company"):
        default_company = frappe.defaults.get_user_default("company")
        if not default_company:
            frappe.local.response["redirect_to"] = "/select-company"