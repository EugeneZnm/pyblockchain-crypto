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
    else:
        print('-' * 20)


def verify_chain():
    """
    chain verification
    :return:
    """
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        """
        looping through list allows automatic increament of blocks
        """
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            """
            checking for index in block list inside blockchain list
            validity of blocks by comparing it to previous block
            """
            is_valid = True
        else:
            is_valid = False
    #         break
    #     block_index += 1
    return is_valid


waiting_for_input = True

while waiting_for_input:
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
        print_blockchain_elements()
        print('invalid blockchain')
        break
else:
    print('user left!')

    print('choice registered')

print('Done!')