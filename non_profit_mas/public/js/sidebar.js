frappe.provide("frappe.ui");

frappe.ui.Sidebar = class CustomSidebar extends frappe.ui.Sidebar {
    make() {
        super.make();
        this.wrapper.html(`
            {% include "non_profit_mas/templates/includes/sidebar.html" %}
        `);
    }
}