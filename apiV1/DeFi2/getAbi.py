import requests
from bs4 import BeautifulSoup

def get_abi_from_bscscan(contract_address):
    url = f"https://bscscan.com/address/{contract_address}#code"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch the page. HTTP Status Code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    abi_pre_tag = soup.find("pre", {"class": "js-copytextarea2"})

    if abi_pre_tag:
        return abi_pre_tag.text
    else:
        print("Failed to find ABI on the page.")
        return None

contract_address = "0x768a62a22b187eb350637e720ebc552d905c0331"
abi = get_abi_from_bscscan(contract_address)
print(abi)
