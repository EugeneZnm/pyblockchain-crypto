# declaring blockchain variable

blockchain = []


def get_last_blockchain_value():
    """ Returning latest value of current blockchain """
    return blockchain[-1]


def add_value(coins, last_transaction=[1]):
    """ Appending new value of blockchain as well as last value of blockchain to blockchain

    coins =  amount added into blockchain after every transacion
    last-transaction = added to blockchain after
    """
    blockchain.append([last_transaction, coins])


def get_transaction_value():
    """
    function to get transaction value
    :return:
    """
    user_input = float(input('Input amount: '))
    return user_input

def get_user_choice():
    """
    user choosing course of action
    :return:
    """
    user_input = input('your choice')
    return user_input

def print_blockchain_elements():
    """
    output blockchain elements
    :return:
    """
    for block in blockchain:
        print('Outputting Block')
        print(block)

tx_amount = get_transaction_value()
add_value(tx_amount)

# tx_amount = get_user_input()
# add_value(last_transaction=get_last_blockchain_value(), coins=tx_amount)
#
# # get transaction input and add value ot the blockchain
# tx_amount = get_user_input()
# add_value(tx_amount, get_last_blockchain_value())

while True:
    print('please choose')
    print('1: Add new transaction value')
    print('2: Output the blockchain blocks')

    # getting choice form user
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_elements()


    print('Done!')