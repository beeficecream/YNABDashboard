import json

import ynab_client
import ynab_resources

from requests import get
from requests.exceptions import HTTPError

class connect:
    def __init__(self,config):
        self.headers = {"Authorization":"Bearer {}".format(config.api_key)}
        self.service_uri = config.api_uri
        self.budget_id = config.budget_id
        self.get_user_info()

    def submit(self,endpoint_url):
        try:
            response = get(endpoint_url, headers=self.headers)
            if response.status_code != 200:
                raise response.raise_for_status()
            else:
                return response.content
        except HTTPError as e:
            print(e.args[0])
            return False
    
    def get_accounts(self):
        endpoint_url = "{}/budgets/{}/accounts".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            accounts = []
            for account in json_data["accounts"]:
                accounts.append(ynab_resources.Account(account))
            return accounts

    def get_account_by_id(self,account_id):
        endpoint_url = "{}/budgets/{}/accounts/{}".format(self.service_uri,self.budget_id,account_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            account = ynab_resources.Account(json_data["account"])
            return account

    def get_budgets(self):
        endpoint_url = "{}/budgets".format(self.service_uri)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            budgets = []
            for budget in json_data["budgets"]:
                budgets.append(ynab_resources.Budget(budget))
            return budgets

    def get_budget_by_id(self,budget_id):
        endpoint_url = "{}/budgets/{}".format(self.service_uri,budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            budget = ynab_resources.Budget(json_data["budget"])
            return budget

    def get_budget_by_id_detailed(self,budget_id):
        endpoint_url = "{}/budgets/{}".format(self.service_uri,budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            budget = ynab_resources.Budget(json_data["budget"],details=True)
            return budget

    def get_budget_by_name(self,budget_name):
        endpoint_url = "{}/budgets".format(self.service_uri)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            budget = None
            for budg in json_data["budgets"]:
                if budg["name"] == budget_name:
                    budget = ynab_resources.Budget(budg)
            return budget

    def get_budget_by_name_detailed(self,budget_name):
        budget_id = self.get_budget_by_name(budget_name).id
        endpoint_url = "{}/budgets/{}".format(self.service_uri,budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            budget = ynab_resources.Budget(json_data["budget"],details=True)
            return budget

    def get_budget_settings(self,budget_id):
        endpoint_url = "{}/budgets/{}/settings".format(self.service_uri,budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            settings = ynab_resources.Budget_Settings(json_data["settings"])
            return settings

    def get_categories(self):
        endpoint_url = "{}/budgets/{}/categories".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            categories = []
            for category_group in json_data["category_groups"]:
                for category in category_group["categories"]:
                    categories.append(ynab_resources.Category(category))
            return categories

    def get_category_by_id(self,category_id):
        endpoint_url = "{}/budgets/{}/categories/{}".format(self.service_uri,self.budget_id,category_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            category = ynab_resources.Category(json_data["category"])
            return category

    def get_categories_by_group_id(self,category_group_id):
        endpoint_url = "{}/budgets/{}/categories".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            categories = []
            for category_group in json_data["category_groups"]:
                if category_group["id"] == category_group_id:
                    for category in category_group["categories"]:
                        categories.append(ynab_resources.Category(category))
            return categories

    def get_category_groups(self):
        endpoint_url = "{}/budgets/{}/categories".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            category_groups = []
            for category_group in json_data["category_groups"]:
                category_groups.append(ynab_resources.Category_Group(category_group))
            return category_groups

    def get_category_group_by_id(self,category_group_id):
        endpoint_url = "{}/budgets/{}/categories".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            category_group = None
            for cat_group in json_data["category_groups"]:
                if cat_group["id"] == category_group_id:
                    category_group = ynab_resources.Category_Group(cat_group)
            return category_group

    def get_category_groups_detailed(self):
        endpoint_url = "{}/budgets/{}/categories".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            category_groups = []
            for category_group in json_data["category_groups"]:
                category_groups.append(ynab_resources.Category_Group(category_group,details=True))
            return category_groups

    def get_category_group_by_id_detailed(self,category_group_id):
        endpoint_url = "{}/budgets/{}/categories".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            category_group = None
            for cat_group in json_data["category_groups"]:
                if cat_group["id"] == category_group_id:
                    category_group = ynab_resources.Category_Group(cat_group,details=True)
            return category_group

    def get_months(self):
        endpoint_url = "{}/budgets/{}/months".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            months = []
            for month in json_data["months"]:
                months.append(ynab_resources.Month(month))
            return months

    def get_payees(self):
        endpoint_url = "{}/budgets/{}/payees".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            payees = []
            for payee in json_data["payees"]:
                payees.append(ynab_resources.Payee(payee))
            return payees

    def get_payee_by_id(self,payee_id):
        endpoint_url = "{}/budgets/{}/payees/{}".format(self.service_uri,self.budget_id,payee_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            payee = ynab_resources.Payee(json_data["payee"])
            return payee

    def get_transactions(self):
        endpoint_url = "{}/budgets/{}/transactions".format(self.service_uri,self.budget_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            transactions = []
            for transaction in json_data["transactions"]:
                transactions.append(ynab_resources.Transaction(transaction))
            return transactions

    def get_transaction_by_id(self,transaction_id):
        endpoint_url = "{}/budgets/{}/transaction/{}".format(self.service_uri,self.budget_id,transaction_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            transaction = ynab_resources.Transaction(json_data["transaction"])
            return transaction

    def get_transactions_by_account_id(self,account_id):
        endpoint_url = "{}/budgets/{}/accounts/{}/transactions".format(self.service_uri,self.budget_id,account_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            transactions = []
            for transaction in json_data["transactions"]:
                transactions.append(ynab_resources.Transaction(transaction))
            return transactions

    def get_transactions_by_category_id(self,category_id):
        endpoint_url = "{}/budgets/{}/categories/{}/transactions".format(self.service_uri,self.budget_id,category_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            transactions = []
            for transaction in json_data["transactions"]:
                transactions.append(ynab_resources.Transaction(transaction))
            return transactions

    def get_transactions_by_payee_id(self,payee_id):
        endpoint_url = "{}/budgets/{}/payees/{}/transactions".format(self.service_uri,self.budget_id,payee_id)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            transactions = []
            for transaction in json_data["transactions"]:
                transactions.append(ynab_resources.Transaction(transaction))
            return transactions

    def get_user_info(self):
        endpoint_url = "{}/user".format(self.service_uri)
        response = self.submit(endpoint_url=endpoint_url)
        if not response:
            raise Exception()
        else:
            json_data = json.loads(response)["data"]
            user = ynab_resources.User(json_data["user"])
            return user

## Classes
class configuration:
    def __init__(self,config_path=None,api_key=None,budget_id=None):
        self.api_uri = "https://api.youneedabudget.com/v1/"
        self.api_key_prefix = "Bearer"

        try:
            if config_path is None:
                self.api_key = api_key
                self.budget_id = budget_id
            else:
                with open(config_path) as json_file:
                    creds = json.load(json_file)
                self.api_key = creds["YNAB_APIKEY"]
                self.budget_id = creds["YNAB_BUDGETID"] if "YNAB_BUDGETID" in creds else None
        except:
            pass