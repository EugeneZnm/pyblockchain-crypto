# declaring blockchain variable

blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(coins, last_transaction=[1]):
    blockchain.append([last_transaction, coins])


def get_user_input():
    return float(input('Input amount: '))


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_blockchain_value(), coins=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)