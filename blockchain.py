# declaring blockchain variable

# reward for blockchain miner
MINING_REWARD = 10

genesis_block = {'previous_hash': '',
                 'index': 0,
                 'transactions': []
                 }
blockchain = [genesis_block]
open_transactions = []
owner = 'Nick'
participants ={'Nick'}


def hash_block(block):

    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    """ getting transaction amount for specific sender/participant """

    # getting  amount for specific transaction in transactions in a block in the blockchain if sender of transaction is a participant
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]

    # getting transaction amount in open transactions if sender is a participant in transaction
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]

    # list with all transaction amounts for sender
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received -amount_sent


def get_last_blockchain_value():
    """ Returning latest value of current blockchain """
    # checking length of blockchain
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_transaction(recipient, sender=owner,  amount=1.0):
    """
    Appending new value of blockchain as well as last value of blockchain to blockchain

    """
    transaction = {'sender': sender,
                   'recipient': recipient,
                   'amount': amount
                   }

    if verify_transaction(transaction):
        open_transactions.append(transaction)

        # management of participants
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def mine_block():
    last_block = blockchain[-1]

    # implementing list comprehension to get key in each dictionary in the block
    hashed_block = hash_block(last_block)

    # determine reward for miners
    reward_transaction ={
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD,
    }
    # appending reward of mining transaction to transaction details
    open_transactions.append(reward_transaction)
    """
    joining hashed list of dictionaries
    
    """
    # print(hashed_block)
    block = {'previous_hash': hashed_block,
             'index':len(blockchain),
             'transactions': open_transactions
             }
    blockchain.append(block)

    # resetting open transactions back to empty array
    return True


def get_transaction_value():
    """
    function to get transaction value
    :return:
    """
    tx_recipient = input('Enter recipient: ')
    tx_amount = float(input('Input amount: '))
    return tx_recipient, tx_amount


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
    # comparing stored hash in a block with recalculated hash of previous block
    for (index,block) in enumerate(blockchain):
        """ loop through blocks in blockchain """
        if index == 0:
            continue

        # comparing value stored in last key with previous block
        if block['previous_hash'] != hash_block(blockchain[index -1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('please choose')
    print('1: Add new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output Participants')
    print('h: manipulate chain')
    print('q: quit')

    # getting choice form user
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data

        # adding transaction amount to the blockchain
        if add_transaction(recipient, amount=amount):
            print('Add transaction')
        else:
            print('Transaction Failed')
        print(open_transactions)
    elif user_choice =='2':

        # resetting transactions to an empty array when mining occurs
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                 'previous_hash': '',
                 'index': 0,
                 'transactions': [{'sender': 'chris', 'recipient':'Max', 'amount':100.0}]
                             }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        # accounting for invalid input
        print('input invalid, input value from list')
    if not verify_chain():
        print_blockchain_elements()
        print('invalid blockchain')
        break
    print(get_balance('Nick'))
else:
    print('user left!')


print('Done!')