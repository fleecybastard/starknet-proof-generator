import os
import json

files = [os.path.join('starknet', file) for file in os.listdir('starknet')]

addresses = {}

for file in files:
    with open(file, 'r') as f:
        tmp = json.load(f)['eligibles']

        for add in tmp:
            addresses[add['identity'].lower()] = add


with open('my_addresses.txt', 'r') as f:
    lines = f.readlines()
    my_addresses = [line.replace('\n', '').lower() for line in lines]


def generate_claim_data(data):
    merkle_index = data['merkle_index']
    identity = data['identity']
    amount = int(data['amount']) * (10 ** 18)
    merkle_path_len = data['merkle_path_len']
    merkle_path = ','.join(data['merkle_path'])
    claim_data = f'{identity}, {amount}, 0, {merkle_index}, {merkle_path_len}, {merkle_path}'
    return claim_data


for address in my_addresses:
    data = addresses.get(address.lower())
    if data is not None:
        output = generate_claim_data(data)
    else:
        output = 'No such address in files'
    print(address)
    print(output)



