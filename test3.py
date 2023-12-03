from solana.rpc.api import Client
from solders.pubkey import Pubkey
import base58

all_addresses = [
    '2AQdpHJ2JpcEgPiATUXjQxA8QmafFegfQwSLWSprPicm',
    'LeiZNZYj56ZQjveMM7NgLAaDPM9QtGHv2qocSy6teAV',
]

#endpoint = 'https://api.devnet.solana.com'    # probably for `developing`
#endpoint = 'https://api.testnet.solana.com'   # probably for `testing`
endpoint = 'https://api.mainnet-beta.solana.com'
#endpoint = 'https://solana-api.projectserum.com'

solana_client = Client(endpoint)

# Open a file named 'data.txt' in write mode
with open('data.txt', 'w') as file:
    for address in all_addresses:
        print('address:', address)
        file.write('address: ' + address + '\n')

        try:
            decoded_address = base58.b58decode(address)
            if len(decoded_address) != 32:
                raise ValueError("Address must be 32 bytes long when decoded.")
            sol_addr = Pubkey(decoded_address)
        except (ValueError, base58.Base58Error) as e:
            print("Invalid address:", address)
            print("Error:", e)
            file.write("Invalid address: " + address + "\n")
            file.write("Error: " + str(e) + "\n")
            continue

        response = solana_client.get_signatures_for_address(sol_addr)

        if response.value:
            print('len:', len(response.value))
            file.write('len: ' + str(len(response.value)) + '\n')
            for number, item in enumerate(response.value, 1):
                signature_str = str(item.signature)
                print(number, 'signature:', signature_str)
                file.write(str(number) + ' signature: ' + signature_str + '\n')

            for number, item in enumerate(response.value, 1):
                signature_str = str(item.signature)
                if signature_str.startswith('4SN'):
                    print('found at', number, '>>>', signature_str)
                    file.write('found at ' + str(number) + ' >>> ' + signature_str + '\n')
        else:
            print("No results or error in response")
            file.write("No results or error in response\n")

        print('---')
        file.write('---\n')