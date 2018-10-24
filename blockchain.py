# declaring blockchain variable

blockchain = []


def get_last_blockchain_value():
    """ Returning latest value of current blockchain """
    # checking length of blockchain
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(coins, last_transaction=[1]):
    """ Appending new value of blockchain as well as last value of blockchain to blockchain

    coins =  amount added into blockchain after every transacion
    last-transaction = added to blockchain after
    """

    if last_transaction == None:
        last_transaction = [1]
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
    user_input = input('your choice: ')
    return user_input


def print_blockchain_elements():
    """
    output blockchain elements
    :return:
    """
    for block in blockchain:
        print('Outputting Block')
        print(block)


def verify_chain():
    """
    chain verification
    :return:
    """
    block_index = 0
    is_valid = True
    for block in blockchain:

        if block_index == 0:
            """
            increament blockchain by 1 if empty
            
            """
            block_index += 1
            continue
        if block[0] == blockchain[block_index - 1]:
            """
            checking validity of blocks by comparing it to previous block
            """
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print('please choose')
    print('1: Add new transaction value')
    print('2: Output the blockchain blocks')
    print('h: manipulate chain')
    print('q: quit')

    # getting choice form user
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice =='2':
        # ending the transaction
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        break
    else:
        # accounting from invalid input
        print('input invalid, input value from list')
    if not verify_chain():
        print('invalid blockchain')
        break

    print('choice registered')

    print('Done!')