frappe.pages['buying'].on_page_load = function(wrapper) {
    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Buying Dashboard',
        single_column: true
    });

    // Add company dropdown
    let company_field = page.add_field({
        label: 'Company',
        fieldtype: 'Select',
        fieldname: 'company_filter',
        options: [],
        change() {
            render_filtered_charts(company_field.get_value());
        }
    });

    // Fetch companies
    frappe.call({
        method: "frappe.client.get_list",
        args: {
            doctype: "Company",
            fields: ["name"],
            limit_page_length: 50
        },
        callback: function(r) {
            if (r.message) {
                let options = r.message.map(row => row.name);
                company_field.df.options = options;
                company_field.refresh();
                render_filtered_charts(options[0]); // Default load
            }
        }
    });

    function render_filtered_charts(company) {
        $(page.body).empty();

        const charts = [
            "Purchase Order Amounts",
            "Supplier Count",
            "Purchase Invoices"
        ];

        charts.forEach(chart_name => {
            frappe.call({
                method: "frappe.desk.query_report.get_dashboard_chart",
                args: {
                    chart_name: chart_name,
                    filters: { company }
                },
                callback: function(res) {
                    if (res.message) {
                        frappe.dashboard_utils.render_chart(res.message, page.body, {
                            filters: { company }
                        });
                    }
                }
            });
        });
    }
};
