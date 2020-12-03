customer = {}
all_customer = []
customer_property = {}
request_user = []


class Bank:

    def get_number_of_customers(self, numberOfCustomers):
        self.numberOfCustomers = numberOfCustomers

    def get_customer(self):
        print('All of the customers:', all_customer)

    def add_customer(self):
        bank = Bank()
        for_bank_name = 'Permata Bank'
        print(f'Welcome to {for_bank_name}')
        customer_input = input('Dear customer, do you already have an account? (Yes/No): ')
        if customer_input == 'No':
            first_name = input('Enter your first name: ')
            last_name = input('Enter your last name: ')
            full_name = first_name + last_name
            password1 = input('Enter your password: ')
            password2 = input('Re-enter your password: ')
            if password1 != password2:
                print("Password doesn't match.")
                Bank().add_customer()
            if full_name not in customer.keys() or customer == {}:
                all_customer.append(full_name)
                customer[full_name] = password1
            else:
                customer[full_name] = []
                print('You already have an account')
            # for the amount of balance
            if full_name not in customer_property.keys():
                customer_property[full_name] = 0
            numberOfCustomers = len(all_customer)
            Bank.get_number_of_customers(self, numberOfCustomers)
            print('Current amount of customers', numberOfCustomers)
            Bank.get_customer(self)
            Customer().set_account()
        elif customer_input == 'Yes':
            print('Current amount of customers', bank.numberOfCustomers)
            Bank.get_customer(self)
            Customer().set_account()


class Customer:

    def get_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self, last_name):
        self.last_name = last_name

    def getAccount(self):
        print('Current user active is', request_user)

    def set_account(self):
        if customer == {}:
            Bank().add_customer()
        else:
            print('Welcome, Customer! Log in first')
            first_name = input('Enter your first name: ')
            Customer.get_first_name(self, first_name)
            last_name = input('Enter your last name: ')
            Customer.get_last_name(self, last_name)
            full_name = first_name + last_name
            password1 = input('Enter your password: ')
            password2 = input('Re-enter your password: ')
            if password1 != password2:
                print("Password doesn't match.")
                Customer().set_account()
            if full_name in customer.keys() or full_name in all_customer and password1 == customer[full_name]:
                print(f'You are logged in as {self.first_name} {self.last_name}')
                request_user.append(full_name)
                Customer.getAccount(self)
                Account().main()
            else:
                print('Log in failed. Check your input again!')
                answer = input('Do you wish to log in again? (Yes/No): ')
                if answer == 'Yes':
                    Customer.set_account(self)
                elif answer == 'No':
                    print('Thankyou for using this bank!')
                else:
                    print('Please type either Yes or No')
                    Customer.set_account(self)


class Account:
    def main(self):
        print('Welcome!! Choose:')
        print('1. Balance''\n''2. Deposit''\n''3. Withdraw''\n''4. Quit')
        customer_picked = input('Pick our services (1,2,3,4): ')
        if customer_picked == '1':
            Account.get_balance(self)
        if customer_picked == '2':
            Account.deposit(self)
        if customer_picked == '3':
            Account.withdraw(self)
        if customer_picked == '4':
            request_user.pop(0)
            print('Thankyou for using our servives!')

    def get_balance(self):
        for request in request_user:
            for user in customer_property.keys():
                if request == user:
                    print('Your balance: ', customer_property.get(user))
                    for_input = input('Do you want to do another service? (Yes/No): ')
                    if for_input == 'Yes':
                        Account().main()
                    if for_input == 'No':
                        request_user.pop(0)
                        Bank.add_customer(self)

    def deposit(self):
        amt = int(input('Enter the amount of deposit: '))
        for request in request_user:
            for user in customer_property.keys():
                if request == user:
                    customer_property[user] += amt
                    print('Your new balance: ', customer_property[user])
                    for_answer = input('Do you want to do another service? (Yes/No): ')
                    if for_answer == 'Yes':
                        Account().main()
                    if for_answer == 'No':
                        request_user.pop(0)
                        Bank.add_customer(self)

    def withdraw(self):
        amt = int(input('Enter the amount of money you want to withdraw: '))
        for request in request_user:
            for user in customer_property.keys():
                if request == user:
                    if amt <= customer_property[user]:
                        customer_property[user] -= amt
                        print('Your current balance became', customer_property[user])
                    for_answer2 = input('Do you want to do another service? (Yes/No): ')
                    if for_answer2 == 'Yes':
                        Account().main()
                    if for_answer2 == 'No':
                        request_user.pop(0)
                        Bank.add_customer(self)


if __name__ == '__main__':
    Bank().add_customer()
