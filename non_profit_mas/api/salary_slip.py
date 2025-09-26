from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, get_datetime, time_diff_in_seconds

def calculate_late_minutes(doc, method):
    """
    Calculate late minutes by comparing `in_time` vs `shift_start` from Employee Checkin.
    """
    if not doc.employee or not doc.start_date or not doc.end_date:
        return

    # Fetch checkin records with late entries
    checkins = frappe.db.sql("""
        SELECT ec.name, ec.time as in_time, ec.shift_start
        FROM `tabEmployee Checkin` ec
        JOIN `tabAttendance` att ON ec.employee = att.employee 
            AND DATE(ec.time) = att.attendance_date
        WHERE 
            ec.employee = %s AND
            DATE(ec.time) BETWEEN %s AND %s AND
            att.late_entry = 1 AND
            att.docstatus = 1 AND
            ec.log_type = 'IN'
    """, (doc.employee, doc.start_date, doc.end_date), as_dict=True)

    total_late_minutes = 0.0

    for checkin in checkins:
        if checkin.in_time and checkin.shift_start:
            # Calculate seconds late and convert to minutes
            late_seconds = time_diff_in_seconds(checkin.in_time, checkin.shift_start)
            if late_seconds > 0:
                total_late_minutes += late_seconds / 60  # Convert to minutes

    # Set the custom field
    doc.custom_late_minutes = flt(total_late_minutes, precision=2)

    # Optional: Add deduction (if configured)
    if total_late_minutes > 0:
        add_late_deduction(doc, total_late_minutes)

def add_late_deduction(doc, late_minutes):
    """Add a deduction component for late minutes (optional)."""
    component_name = "Late Entry Deduction"
    deduction_per_minute = 1.0  # Adjust as needed

    # Clear existing deduction (if any)
    doc.deductions = [d for d in doc.deductions if d.salary_component != component_name]

    # Add new deduction
    doc.append("deductions", {
        "salary_component": component_name,
        "amount": flt(late_minutes * deduction_per_minute, precision=2),
        "description": f"Late entry: {late_minutes:.2f} minutes"
    })