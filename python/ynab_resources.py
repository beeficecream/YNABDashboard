## Functions
def convert_currency(self,currency):
    output = round(currency/1000,2)
    return output

def convert_date(self,date_str):
    import dateutil.parser as parser
    return parser.parse(date_str).isoformat()

## Classes
class Account:
    def __init__(self,json_data):
        self.id = json_data["id"]
        self.name = json_data["name"]
        self.type = json_data["type"]
        self.balance = convert_currency(self=None,currency=json_data["balance"])
        self.cleared_balance = convert_currency(self=None,currency=json_data["cleared_balance"])
        self.uncleared_balance = convert_currency(self=None,currency=json_data["uncleared_balance"])
        self.closed = json_data["closed"]
        self.deleted = json_data["deleted"]
        self.note = json_data["note"]
        self.on_budget = json_data["on_budget"]
        self.transfer_payee_id = json_data["transfer_payee_id"]

class Budget():
    def __init__(self,json_data,details=False):
        self.id = json_data["id"]
        self.name = json_data["name"]
        self.last_modified_on = json_data["last_modified_on"]
        self.first_month = json_data["first_month"]
        self.last_month = json_data["last_month"]
        self.date_format = json_data["date_format"]
        self.currency_format = json_data["currency_format"]
        if details:
            self.get_details(json_data)

    def get_details(self,json_data):
        self.accounts = [Account(data) for data in json_data["accounts"]]
        self.categories = [Category(data) for data in json_data["categories"]]
        self.category_groups = [Category_Group(data) for data in json_data["category_groups"]]
        self.months = [Month(data) for data in json_data["months"]]
        self.payees = [Payee(data) for data in json_data["payees"]]
        self.transactions = [Transaction(data) for data in json_data["transactions"]]
        ## Set additional properties on all categories
        for c in self.categories:
            category_group_name = [cg.name for cg in self.category_groups if not c.deleted and cg.id == c.category_group_id]
            if category_group_name:
                c.category_group_name = category_group_name[0]
        ## Set additional properties on all transactions
        for t in self.transactions:
            t.account_name =  [a.name for a in self.accounts if a.id == t.account_id][0]
            t.account_type = [a.type for a in self.accounts if a.id == t.account_id][0]
            t.payee_name = [p.name for p in self.payees if p.id == t.payee_id][0]
            if t.category_id is not None:
                category_name = [c.name for c in self.categories if c.id == t.category_id]
                if category_name:
                    t.category_name = category_name[0]
            if t.transfer_account_id is not None:
                transfer_account = [a.name for a in self.accounts if a.id == t.transfer_account_id]
                if transfer_account:
                    t.transfer_account_name = transfer_account[0]
        print("")

class Budget_Settings():
    def __init__(self,json_data):
        self.date_format = json_data["date_format"]
        self.currency_format = json_data["currency_format"]

class Category():
    def __init__(self,json_data):
        self.id = json_data["id"]
        self.name = json_data["name"]
        self.category_group_id = json_data["category_group_id"]        
        self.original_category_group_id = json_data["original_category_group_id"]
        self.budgeted = convert_currency(self=None,currency=json_data["budgeted"])
        self.activity = convert_currency(self=None,currency=json_data["activity"])
        self.balance = convert_currency(self=None,currency=json_data["balance"])
        self.goal_type = json_data["goal_type"]
        self.goal_creation_month = json_data["goal_creation_month"]
        self.goal_target = convert_currency(self=None,currency=json_data["goal_target"])
        self.goal_target_month = json_data["goal_target_month"]
        self.goal_percentage_complete = json_data["goal_percentage_complete"]
        self.note = json_data["note"]
        self.hidden = json_data["hidden"]
        self.deleted = json_data["deleted"]
        self.category_group_name = None

class Category_Group():
    def __init__(self,json_data,details=False):
        self.id = json_data["id"]
        self.name = json_data["name"]
        self.hidden = json_data["hidden"]
        self.deleted = json_data["deleted"]
        if details:
            self.get_details(json_data)
    
    def get_details(self,json_data):
        self.categories = [Category(data) for data in json_data["categories"]]

class Month():
    def __init__(self,json_data):
        self.month = json_data["month"]
        self.note = json_data["month"]
        self.income = json_data["month"]
        self.budgeted = json_data["month"]
        self.activity = json_data["month"]
        self.to_be_budgeted = json_data["month"]
        self.age_of_money = json_data["month"]
        self.deleted = json_data["month"]

class Payee():
    def __init__(self,json_data):
        self.id = json_data["id"]
        self.deleted = json_data["deleted"]
        self.name = json_data["name"]
        self.transfer_account_id = json_data["transfer_account_id"]

class Transaction():
    def __init__(self,json_data):
        self.id = json_data["id"]
        self.date = convert_date(self=None,date_str=json_data["date"])
        self.account_id = json_data["account_id"]
        self.category_id = json_data["category_id"]
        self.payee_id = json_data["payee_id"]
        self.amount = convert_currency(self=None,currency=json_data["amount"])
        self.approved = json_data["approved"]
        self.cleared = json_data["cleared"]
        self.deleted = json_data["deleted"]
        self.memo = json_data["memo"]
        self.flag_color = json_data["flag_color"]
        self.import_id = json_data["import_id"]
        self.transfer_account_id = json_data["transfer_account_id"]
        self.transfer_transaction_id = json_data["transfer_transaction_id"]
        self.matched_transaction_id = json_data["matched_transaction_id"]
        self.account_name = None
        self.account_type = None
        self.category_name = None
        self.category_group_name = None
        self.payee_name = None
        self.transfer_account_name = None

class User():
    def __init__(self,json_data):
        self.id = json_data["id"]
