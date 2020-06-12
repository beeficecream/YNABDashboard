# YNABDashboard.Docker

A Docker compose file that will build default deployments of the following services:

* InfluxDB - Time series database used to store YNAB data

* Grafana - Analytics and visualizations application

* Chronograf - Lightweight "admin" portal to InfluxDB
  * This is optional; removing this from the Docker compose file will not hinder functionality of the solution

## Setup

Customization, configuration, and/or deployment processes for Docker are out-of-scope for this project. Considering there are numerous different ways to deploy a container and/or stack, this is being left to the discretion of the user.

Links to each image used to create this stack...

* [Grafana](https://hub.docker.com/r/grafana/grafana)

* [InfluxDB](https://hub.docker.com/_/influxdb)

* [Chronograf](https://hub.docker.com/_/chronograf)

Test
