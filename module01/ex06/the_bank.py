class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    def __init__(self):
        self.account = []
    def add(sef, account):
        self.account.append(account)
    @staticmethod
    def check_Account(obj:Account):
        if not isinstance(obj, Account):
            print("Not a Account")
            return False
        idx_dir = dir(obj)
        if len(idx_dir) % 2 == 0:
            print("Not a Even")
            return False 
        if "name" not in idx_dir:
            print("Not name")
            return False
        if hasattr(obj, 'value') is False:
            print("Not value")
            return False
        if len(list(filter(lambda x: (x.startswith('b')), idx_dir))) != 0:
            print("not 'b' attribute")
            return False
        if len(list(filter(lambda x: (x.startswith('zip')), idx_dir)))  == 0 or \
            len(list(filter(lambda x: (x.startswith('addr')), idx_dir))) == 0:
            print("not zip or addr" )
            return False
        return True

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:   int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return  True if success, False if an error occured
        """
        if check_Account(origin) is False or \
            check_Account(dest) is False:
            return False
        if not isinstance(origin.name, str) or \
            not isinstance(dest.name, str):
            return False
        if amount > origin.amount or amount < 0:
            return False
        origin.transfer(-amount)
        dest.transfer(amount)
        
    def fix_account( account):
        idx_dir = dir(account)
        if hasattr(account, 'value') is False:
            setattr(account, 'value', 1)
        if "name" not in idx_dir:
            setattr(account, 'name', None)
        lst_b = list(filter(lambda x :  x.startswith('value'), idx_dir))
        print(lst_b)
        print(idx_dir)
        for l in lst_b:
            delattr (idx_dir, l)
        print(idx_dir)

   
        

a = Account("A", zip=None, addr = None, value = 10)
b = Bank
b.fix_account(a)
        