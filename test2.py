from solana.rpc.api import Client
from solders.pubkey import Pubkey
import base58

all_addresses = [
    # '2AQdpHJ2JpcEgPiATUXjQxA8QmafFegfQwSLWSprPicm',
    'LeiZNZYj56ZQjveMM7NgLAaDPM9QtGHv2qocSy6teAV',
]

#endpoint = 'https://api.devnet.solana.com'    # probably for `developing`
#endpoint = 'https://api.testnet.solana.com'   # probably for `testing`
endpoint = 'https://api.mainnet-beta.solana.com'
#endpoint = 'https://solana-api.projectserum.com'

solana_client = Client(endpoint)

for address in all_addresses:
    print('address:', address)
    
    try:
        # Decode the base-58 address to bytes
        decoded_address = base58.b58decode(address)
        
        # Check if the decoded address is 32 bytes long
        if len(decoded_address) != 32:
            raise ValueError("Address must be 32 bytes long when decoded.")

        sol_addr = Pubkey(decoded_address)
    except (ValueError, base58.Base58Error) as e:
        print("Invalid address:", address)
        print("Error:", e)
        continue
    
    #result = solana_client.get_confirmed_signature_for_address2(address, limit=1)
    response = solana_client.get_signatures_for_address(sol_addr)#, before='89Tv9s2uMGaoxB8ZF1LV9nGa72GQ9RbkeyCDvfPviWesZ6ajZBFeHsTPfgwjGEnH7mpZa7jQBXAqjAfMrPirHt2')
    
    # if 'result' in result:
        
    #     print('len:', len(result['result']))

    #     # I use `[:5]` to display only first 5 values
    #     for number, item in enumerate(result['result'][:5], 1):
    #         print(number, 'signature:', item['signature'])

    #     # check if there is `4SNQ4h1vL9GkmSnojQsf8SZyFvQsaq62RCgops2UXFYag1Jc4MoWrjTg2ELwMqM1tQbn9qUcNc4tqX19EGHBqC5u`
    #     for number, item in enumerate(result['result'], 1):
    #         if item['signature'].startswith('4SN'):
    #             print('found at', number, '>>>', item['signature'])

    # else:
    #     # error message 
    #     print(result)
    if response.value:
        print('len:', len(response.value))
        for number, item in enumerate(response.value[:5], 1):
            signature_str = str(item.signature)  # Convert Signature object to string
            print(number, 'signature:', signature_str)

        for number, item in enumerate(response.value, 1):
            signature_str = str(item.signature)  # Convert Signature object to string
            if signature_str.startswith('4SN'):
                print('found at', number, '>>>', signature_str)
    else:
        print("No results or error in response")

    print('---')

    #solana_client.get_account_info(address)