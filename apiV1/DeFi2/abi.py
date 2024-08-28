# -*- coding: utf-8 -*-
"""  1
Created on Sun Aug 29 10:11:13 2021

@author: Zain
"""

from bs4 import BeautifulSoup as bsp
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent


ABI_Path=BASE_DIR / 'data/'
# ABI_Path='/root/pypro/djangotokens/apiV1/DeFi2/data/'

def tokenAbi(address, driver=None):
    try:
        filename = f'ABI_{address}.txt'
        with open(f"{ABI_Path}/{filename}") as f:
            abi = f.readlines()
            return abi[0]
    except IOError:
        # abi = findAbi(address, driver)
        abi = get_abi_from_bscscan(address)
        return abi


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def findAbi(address, driver):
    url = f'https://bscscan.com/address/{address}#code' 
    
    if not driver:
        chrome_options = Options()
        chrome_options.headless = True
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    driver.get(url)
    page_soup = bsp(driver.page_source, features="lxml")
    abi = page_soup.find_all("pre", {"class": "wordwrap js-copytextarea2"})
    
    # with open(f'/root/pypro/djangotokens/apiV1/DeFi2/data/ABI_{address}.txt', 'w') as f:
    with open(f'{ABI_Path}/ABI_{address}.txt', 'w') as f:    
        f.write(abi[0].text)

    driver.delete_all_cookies()
    driver.get("chrome://settings/clearBrowserData");
    # driver.close()
    return abi[0].text

 

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
        
        # with open(f'/root/pypro/djangotokens/apiV1/DeFi2/data/ABI_{contract_address}.txt', 'w') as f:
        with open(f'{ABI_Path}/ABI_{contract_address}.txt', 'w') as f:
            f.write(abi_pre_tag.text)
        return abi_pre_tag.text
    
    else:
        print("Failed to find ABI on the page.")
        return None

