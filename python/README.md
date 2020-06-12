# YNABDashboard.Python

The meat 'n potatoes of the whole project, the heavy lifter. Allow me to elaborate...

## Included

### main.py

All of the logic behind pulling data out of YNAB, filtering out what's not necessary for dashboarding, creating properly organized time-series points, and uploading those points to the configured InfluxDB instance and index.  Normally this script runs very quickly, there have been very few instances where full, successful execution extended beyond 5s.

### ynab_client.py and ynab_resources.py

Wrappers for working with the YNAB API

### sample_config.json

This is a template of a working config file for the python script. Rename this to config.json and fill in the required data.

### requirements.txt

Dependencies for the script and wrappers

## Setup

### Configurations

* InfluxDBHost - Hostname or IP address of InfluxDB host

* InfluxDBPort - Listening port for InfluxDB service

* InfluxDBIndex - Name of InfluxDB index holding YNAB data

* InfluxDBUser - InfluxDB user with access to YNAB index listed in 'InfluxDBIndex' configuration

* InfluxDBPass - Password for InfluxDB user listed in 'Infl

* YNAB_API_Key - API Key assigned to your YNAB account

* YNAB_Budget_ID - ID of YNAB budget to pull data from

### Execution and Scheduling

Currently, the script is purpose-built to run on an hourly basis. This can be achieved by using **cron** on linux hosts or the **Task Scheduler** on Windows hosts.

Note: Running this on a Windows host requires installation and configuration of Python 3.8 prior to execution.
