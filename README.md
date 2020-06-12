# YNABDashboard

Everything required to get started on dashboarding your YNAB budget data!

![Dashboard Example](https://i.redd.it/pedwe755gd451.png)

This project leverages the following different pieces of technology to achieve the end product:

* Python 3.8
  * A python script and a couple custom modules are included that exports data from YNAB, filters it, then uploads it to a target database

* InfluxDB 1.8
  * The time-series database chosen for this project

* Grafana 7.0
  * The visualization software used to build and display dashboards

* Docker 19.03
  * Containerization software used to host both InfluxDB and Grafana

## Deployment

The order in which each module of this solution needs deployed is listed chronologically below.  Detailed instructions for deploying each module can be found in README files within provided directories.

1. Docker - There need to be services to communicate with moving forward

2. Python - Data is going to be required to visualize anything

3. Grafana - Your infrastructure and data collection are in place, time to setup the dashboard
