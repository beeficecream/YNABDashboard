# YNABDashboard.Python
The meat 'n potatoes of the whole project, the heavy lifter. Allow me to elaborate...

### main.py
All of the logic behind pulling data out of YNAB, filtering out what's not necessary for dashboarding, creating properly organized time-series points, and uploading those points to the configured InfluxDB instance and index.  Normally this script runs very quickly, there have been very few instances where full, successful execution extended beyond 5s.

### ynab_client.py and ynab_resources.py
Wrappers for working with the YNAB API

### sample_config.json
This is a template of a working config file for the python script. Rename this to config.json and fill in the required data.

### requirements.txt
Dependencies for the script and wrappers