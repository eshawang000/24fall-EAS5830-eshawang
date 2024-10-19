import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.providers.rpc import HTTPProvider

'''If you use one of the suggested infrastructure providers, the url will be of the form
now_url  = f"https://eth.nownodes.io/{now_token}"
alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_token}"
infura_url = f"https://mainnet.infura.io/v3/{infura_token}"
'''


def connect_to_eth():
	url = "https://eth-mainnet.g.alchemy.com/v2/gM8pULMkbSerYWUI9MgMzbYPSxcuJoRY"  # FILL THIS IN
	w3 = Web3(HTTPProvider(url))
	assert w3.is_connected(), f"Failed to connect to provider at {url}"
	return w3


def connect_with_middleware(contract_json):
	with open(contract_json, "r") as f:
		d = json.load(f)
		d = d['bsc']
		address = d['address']
		abi = d['abi']

	# TODO complete this method
	# The first section will be the same as "connect_to_eth()" but with a BNB url
	bnb_url = "https://bsc-testnet-rpc.publicnode.com"
	w3 = Web3(HTTPProvider(bnb_url))
	# The second section requires you to inject middleware into your w3 object and
	# create a contract object. Read more on the docs pages at https://web3py.readthedocs.io/en/stable/middleware.html
	# and https://web3py.readthedocs.io/en/stable/web3.contract.html
	assert w3.is_connected(), f"Failed to connect to provider at {bnb_url}"
	w3.middleware_onion.inject(geth_poa_middleware, layer=0)
	contract = w3.eth.contract(address=Web3.to_checksum_address(address), abi=abi)

	return w3, contract


if __name__ == "__main__":
	# connect_to_eth()
	eth_w3 = connect_to_eth()
	print("is_connected_eth?", eth_w3.is_connected())
	latest_block_eth = eth_w3.eth.get_block('latest')
	print("latest_block_eth:", latest_block_eth)
    
	try:
		contract_json_path = "contract_info.json"
		bnb_w3, contract = connect_with_middleware(contract_json_path)
		print("is_connected_bnb?", bnb_w3.is_connected())
        
		latest_block_bnb = bnb_w3.eth.get_block('latest')
		print("latest_block_bnb:", latest_block_bnb)
	except Exception as e:
		print(f"Error: {e}")
