import requests
import json

PINATA_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIzZjRkMDJiZS04MDQxLTRmYWYtOGQ0Ny03OWQzYmFkZWQ3ZjIiLCJlbWFpbCI6ImVzaGF3YW5nQHNlYXMudXBlbm4uZWR1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiRlJBMSJ9LHsiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6IjMxNDI5ODQxNWY2YjM2NTcyNDhjIiwic2NvcGVkS2V5U2VjcmV0IjoiOGEwODBiZWJjNmQwODVlMDNmYjE1MTBjY2U4YzA1MDFiMTZmMGVhOTFkNmQ2M2Q3NWExOGNlNTE1MDE3MWU2ZSIsImV4cCI6MTc2MDg1ODkwM30.iVjWODV2EwmU8J-G0BpREzh3L0njxTyAJxosdLBciPU"
PINATA_PIN_URL = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
PINATA_GATEWAY_URL = "https://apricot-obliged-bonobo-868.mypinata.cloud/ipfs"
PINATA_PUBLIC_GATEWAY_URL = "https://gateway.pinata.cloud/ipfs"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	payload = {
			"pinataContent": data,
			"pinataMetadata": {
					"name": "MyPinnedData",
					"keyvalues": {
							"project": "example-project"
					}
			}
	}

	headers = {
			"Authorization": f"Bearer {PINATA_JWT}",
			"Content-Type": "application/json"
	}

	response = requests.post(PINATA_PIN_URL, json=payload, headers=headers)

	if response.status_code == 200:
			cid = response.json()["IpfsHash"]
			return cid
	else:
			raise Exception("Failed to pin data to IPFS")
	# return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	response = requests.get(f"{PINATA_PUBLIC_GATEWAY_URL}/{cid}")

	if response.status_code == 200:
			data = response.json()  # Assuming the content is JSON
			assert isinstance(data, dict), "get_from_ipfs should return a dict"
			return data
	else:
			raise Exception("Failed to retrieve data from IPFS")

	# assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	# return data
