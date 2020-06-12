# YNABDashboard.Grafana

This is the full JSON for the Financial Health dashboard in Grafana.

## Setup

### Importing

1. Log into your Grafana installation and navigate to **Dashboards > Manage**
2. On the right of the page, find and click the **Import** button.
3. Copy the contents of the *dash_financial_health.json* file and paste them in the **Import via panel json** text box.
4. Name the dashboard whatever you wish, save the dashboard in whichever folder you wish.  Make sure the UID does not match any of your existing dashboards (change if necessary) and click **Import**.

### Configuration

Once imported there are two visualizations you must reconfigure to match your specific use case.

Accessing the settings for a visualization can be achieved by click the title of the visualization, then **Edit**.

#### Savings Objectives

This bar gauge is configured to track the "goalPercentageComplete" value for any Category you specify.  The value stored for "goalPercentageComplete" is an aggregate value available through the YNAB API and pulled over hourly by the Python script.  

Review each of the queries listed, replacing the placeholder Category names with the names of any Categories currently configured with a Goal.

There are four savings sources provided by default, more can be added by duplicating one of the provided queries and modifying the new query's targeted Category.

#### Income

This pie chart is configured to measure the sum of all transactions from target Payees within the interval currently selected for operation.  The interval can be changed by using the dropdown menu near the top right of the visualization preview pane.

Review all queries listed, replacing the placeholder Payee names with the names of the your income Payees.

There are two income sources provided by default, more can be added by duplicating one of the provided queries and modifying the new query's targeted Payee.
