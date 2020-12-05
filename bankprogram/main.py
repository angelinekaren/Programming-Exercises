class Bank:
    numberOfCustomers = 0

    def __init__(self, bankName, customers):
        self.bankName = bankName
        self.customers = customers

    def addCustomer(self, first_name, last_name):
        self.customers.append(Customer(str(first_name), str(last_name)))
        self.numberOfCustomers += 1

    def getNumberOfCustomers(self):
        return self.numberOfCustomers

    def getCustomer(self, index):
        return self.customers[index]


class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.account = Account()

    def __repr__(self):
        return str('{} {}'.format(self.first_name, self.last_name))


    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def getAccount(self):
        return self.account

    def setAccount(self, acc):
        self.account = acc


class Account:
    # class variable
    noOfAccounts = 0

    def __init__(self, balance=0):
        self.balance = balance  # instance variable

    def getBalance(self):
        return self.balance

    def deposit(self, amt):
        if amt > 0:
            self.balance = self.balance + amt
            return True
        else:
            return False

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return True
        else:
            return False


def bank_manager_menu():
    bCa = Bank("BCA", customers)
    staffManager = {'staff': '123'}
    print('Welcome, Staff user!')
    print('Log in first')
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username in staffManager.keys() and password == staffManager[username]:
        print('Successfully login! Choose:')
        print('1. Check all customers''\n''2. Check number of customers''\n''3. Add new account')
        for_answer = input('(1/2/3): ')
        if for_answer == '1':
            print('All customers: ', bCa.customers)
            inputs = input('Do you still want to do another action? (Yes/No): ')
            if inputs == 'Yes':
                bank_manager_menu()
            if inputs == 'No':
                main()
        if for_answer == '2':
            bCa.numberOfCustomers = len(customers)
            print('Number of customers: ', bCa.getNumberOfCustomers())
            inputs = input('Do you still want to do another action? (Yes/No): ')
            if inputs == 'Yes':
                bank_manager_menu()
            if inputs == 'No':
                main()
        if for_answer == '3':
            print('Input the customer data below!')
            first_name = str(input('Enter first name: '))
            last_name = str(input('Enter last name: '))
            full_name = first_name + ' ' + last_name
            bCa.addCustomer(first_name=first_name, last_name=last_name)
            print('Customers: ', customers)
            all_customer.append(full_name)
            answer = input('Do you still want to do another action? (Yes/No): ')
            if answer == 'Yes':
                bank_manager_menu()
            if answer == 'No':
                main()
    else:
        print('You are not authenticated as a staff user')
        main()


def customer_menu():
    customer_input = input('Dear customer, do you already have an account? (Yes/No): ')
    if customer_input == 'Yes':
        print('Log in first!')
        first_name= str(input('Enter your first name: '))
        last_name = str(input('Enter your last name: '))
        full_name = first_name + ' ' + last_name
        customer = Customer(first_name=first_name, last_name=last_name)
        if full_name in all_customer:
            print('You are succesfully log in.')
            print(f'Welcome to BCA, {full_name}!')
            print('Please fill in the data below')
            customer.setAccount(Account(int(input('Enter the amount of money you would like to store: '))))
            customer_service_menu(customer)
    if customer_input == 'No':
        print('Please ask the Bank to make an account for you.')
        print('Thankyou for using BCA bank!')
        main()

def customer_service_menu(customer):
    print('Choose:''\n''1. Balance''\n''2. Deposit''\n''3. Withdraw''\n''4. Quit')
    customer_picked = input('Pick our services (1,2,3,4): ')
    if customer_picked == '1':
        print('Account balance >>', customer.getAccount().getBalance())
        answer = input('Do you want to continue? (Yes/No): ')
        if answer == 'Yes':
            customer_service_menu(customer)
        if answer == 'No':
            main()
    if customer_picked == '2':
        if customer.getAccount().deposit(int(input('Enter the amount you would like to deposit: '))):
            print("Balance updated ", customer.getAccount().getBalance())
            answer = input('Do you want to continue? (Yes/No): ')
            if answer == 'Yes':
                customer_service_menu(customer)
            if answer == 'No':
                main()
        else:
            print("Invalid transaction!!!")
            print("Balance is not updated ", customer.getAccount().getBalance())
            answer = input('Do you want to continue? (Yes/No): ')
            if answer == 'Yes':
                customer_service_menu(customer)
            if answer == 'No':
                main()
    if customer_picked == '3':
        if customer.getAccount().withdraw(int(input('Enter the amount you would like to withdraw: '))):
            print("Balance updated ", customer.getAccount().getBalance())
            answer = input('Do you want to continue? (Yes/No): ')
            if answer == 'Yes':
                customer_service_menu(customer)
            if answer == 'No':
                main()
        else:
            print("Invalid transaction!!!")
            print("Balance is not updated ", customer.getAccount().getBalance())
            answer = input('Do you want to continue? (Yes/No): ')
            if answer == 'Yes':
                customer_service_menu(customer)
            if answer == 'No':
                main()
    if customer_picked == '4':
        print('Thankyou for using our servives!')
        main()


def main():
    print('Welcome to BCA!')
    print('Login as a: ''\n''1. Staff manager''\n''2. Customer')
    answers = input('(1/2): ')
    if answers == '1':
        bank_manager_menu()
    if answers == '2':
        customer_menu()


if __name__ == "__main__":
    all_customer = []
    customers = []
    main()
