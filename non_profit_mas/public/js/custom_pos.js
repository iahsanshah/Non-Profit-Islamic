frappe.ready(() => {
	frappe.require("erpnext/selling/page/point_of_sale/point_of_sale.js", () => {
		const original_prepare_menu = erpnext.PointOfSale.Controller.prototype.prepare_menu;

		erpnext.PointOfSale.Controller.prototype.prepare_menu = function () {
			// Call the original menu
			original_prepare_menu.call(this);

			// Add your custom Print button
			this.page.add_menu_item(__("Print Invoice"), () => {
				if (!this.frm || !this.frm.doc.name) {
					frappe.msgprint("Invoice is not saved yet.");
					return;
				}

				const invoice_name = this.frm.doc.name;
				window.open(`/printview?doctype=POS Invoice&name=${invoice_name}&format=POS Invoice`, "_blank");
			}, false, "Ctrl+P");
		};
	});
});
