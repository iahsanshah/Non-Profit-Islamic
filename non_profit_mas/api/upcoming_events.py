import frappe
import datetime

@frappe.whitelist(allow_guest=True)
def get_upcoming_birthdays():
    today = datetime.date.today()
    future = today + datetime.timedelta(days=30)

    # You can also add filters like status='Active' if needed
    employees = frappe.db.sql("""
        SELECT name, employee_name, date_of_birth
        FROM `tabEmployee`
        WHERE 
            DAYOFYEAR(date_of_birth) >= DAYOFYEAR(%s)
            AND DAYOFYEAR(date_of_birth) <= DAYOFYEAR(%s)
        ORDER BY DAYOFYEAR(date_of_birth)
    """, (today, future), as_dict=True)

    return employees
