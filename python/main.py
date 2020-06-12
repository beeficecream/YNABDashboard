# Libraries
import influxdb
import json
import logging
import requests
import sys
import time

import ynab_client
import ynab_resources

from datetime import datetime,timedelta

# Configurations
execution_datetime          = datetime.now().replace(minute=0,second=0,microsecond=0)
execution_window_days       = 7
idb_host                    = "influxdb_ip_address"
idb_port                    = 8086
idb_index                   = "name_of_influxdb_index"
idb_user                    = "influxdb_username"
idb_pass                    = "influxdb_password"
ynab_api_key                = "ynab_api_key"
ynab_budget_id              = "ynab_budget_id"

# Execution
## Setup logging
logging.basicConfig(level=logging.INFO,stream=sys.stdout, format="[%(asctime)s] %(levelname)s :: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger()

# Initiate connection to InfluxDB
influx_client = influxdb.InfluxDBClient(idb_host,idb_port,idb_user,idb_pass)

## Verify existence of required index
indices = influx_client.get_list_database()
if not any(index["name"] == idb_index for index in indices):
    influx_client.create_database(idb_index)
influx_client.switch_database(idb_index)

# Query for existing transaction data in InfluxDB
influx_query_transactions = ('SELECT * FROM "{}"."autogen"."transactions"'.format(idb_index))
influx_transactions_points = influx_client.query(influx_query_transactions).get_points(measurement='transactions')
influx_transactions_list = list(influx_transactions_points)
influx_transactions_ids = [i["id"] for i in influx_transactions_list]

## Configure and connect to YNAB
ynab_config = ynab_client.configuration(api_key=ynab_api_key,budget_id=ynab_budget_id)
ynab = ynab_client.connect(ynab_config)

## Get and parse budget data
budget = ynab.get_budget_by_id_detailed(ynab_budget_id)
accounts = [a for a in budget.accounts if not a.deleted and not a.closed]
categories = [c for c in budget.categories if not c.deleted and not c.hidden]
payees = budget.payees
all_transactions = [t for t in budget.transactions]
all_transactions_ids = [t.id for t in all_transactions]
new_transactions = [t for t in all_transactions if not any(t.id in id for id in influx_transactions_ids)]
bad_transactions = [i for i in influx_transactions_ids if not any(i in id for id in all_transactions_ids)]

## Create plot points
points = []
for account in accounts:
    account_json = {
        "measurement": "accounts",
        "time": execution_datetime.isoformat(),
        "tags": {
            "account": account.name,
            "id": account.id,
            "budget": budget.name,
            "type": account.type,
            "closed": account.closed,
            "deleted": account.deleted,
            "on_budget": account.on_budget
        },
        "fields": {
            "balance": account.balance,
            "unclearedBalance": account.cleared_balance,
            "clearedBalance": account.uncleared_balance
        }
    }
    points.append(account_json)

for category in categories:
    category_json = {
        "measurement": "categories",
        "time": execution_datetime.isoformat(),
        "tags": {
            "budget": budget.name,
            "category": category.name,
            "categoryGroup": category.category_group_name,
            "goalType": category.goal_type,
            "goalTargetMonth": category.goal_target_month,
            "id": category.id,
            "deleted": category.deleted,
            "hidden": category.hidden
        },
        "fields": {
            "budgeted": category.budgeted,
            "activity": category.activity,
            "balance": category.balance,
            "goalTarget": category.goal_target,
            "goalPercentageComplete": category.goal_percentage_complete
        }
    }
    points.append(category_json)

for transaction in new_transactions:
    transaction_json = {
        "measurement": "transactions",
        "time": transaction.date,
        "tags": {
            "account": transaction.account_name,
            "budget": budget.name,
            "category": transaction.category_name,
            "categoryGroup": transaction.category_group_name,
            "id": transaction.id,
            "payee": transaction.payee_name,
            "flagColor": transaction.flag_color
            
        },
        "fields": {
            "amount": transaction.amount
        }
    }
    points.append(transaction_json)

## Remove bad points
for b in bad_transactions:
    influx_query_delete = "DELETE FROM \"transactions\" WHERE \"id\"='{}'".format(b)
    influx_client.query(influx_query_delete)

## Write all new points
influx_client.write_points(points)