# Copyright (c) 2025, Ahsan Shah and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class DonationCollection(Document):
    def on_submit(self):
        self.make_journal_entry()

    def make_journal_entry(self):
        if not self.accounts:
            frappe.throw("No accounts found to create Journal Entry")

        # Create new Journal Entry
        je = frappe.new_doc("Journal Entry")
        je.posting_date = self.posting_date
        je.voucher_type = "Journal Entry"
        je.company = self.company

        # Loop over accounts table
        for row in self.accounts:
            if not row.account or not row.amount:
                continue

            # Debit - from donor account
            je.append("accounts", {
                "account": row.account,
                "debit_in_account_currency": row.amount,
                "credit_in_account_currency": 0
            })

            # Credit - donation account
            if not row.donation_account:
                frappe.throw(f"Donation Account missing in row {row.idx}")

            je.append("accounts", {
                "account": row.donation_account,
                "party_type": "Donor",
                "party":self.donor,
                "credit_in_account_currency": row.amount,
                "debit_in_account_currency": 0
            })

        # Save and submit JE
        je.save()
        je.submit()

        frappe.msgprint(f"Journal Entry <a href='/app/journal-entry/{je.name}'>{je.name}</a> created.")
