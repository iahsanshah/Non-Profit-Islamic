import frappe
from frappe.utils import get_url

def get_logged_user():
    user = frappe.session.user
    if user and user != "Guest":
        return get_url("/company-selection")
    return None
