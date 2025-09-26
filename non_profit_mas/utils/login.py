import frappe

def on_login(login_manager):
    """Post login handler for company selection"""
    if frappe.session.user == "Administrator":
        return
        
    # Skip if already on selection page
    if hasattr(frappe.local, 'request') and frappe.local.request \
       and frappe.local.request.path.startswith("/select-company"):
        return
    
    # Check if user has a default company
    default_company = frappe.defaults.get_user_default("company")
    if default_company:
        return
        
    # Check how many companies exist
    companies = frappe.get_all("Company", limit=2)
    
    # Redirect if multiple companies exist
    if len(companies) > 1:
        frappe.local.response["redirect_to"] = "/select-company"
    elif len(companies) == 1:
        # Auto-set if only one company exists
        frappe.defaults.set_user_default("company", companies[0].name)