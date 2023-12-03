import requests
import pprint

headers = {
    'APIKeyId': 'nxx5cSKuNWZwd9Q',
    'APISecretKey': '3aGDtfCCdf9zMDq',
}

network = 'mainnet-beta'
mint_address = '3aGDtfCCdf9zMDq'

# --- metadata ---

url = f"https://api.blockchainapi.com/v1/solana/nft/{network}/{mint_address}"
response = requests.get(url, headers=headers)
data = response.json() 

pprint.pprint(data)

# --- owner ---

url = f"https://api.blockchainapi.com/v1/solana/nft/{network}/{mint_address}/owner"
response = requests.get(url, headers=headers)
data = response.json() 

pprint.pprint(data)