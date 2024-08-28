# config.py
from decouple import config



DEBUG = config('DEBUG', default=False, cast=bool)
EbcContractTokenAddress = config('EbcContractTokenAddress', default='')
YmiiContractTokenAddress = config('YmiiContractTokenAddress', default='')
TRADE_TOKEN_ADDRESS = config('TRADE_TOKEN_ADDRESS', default='')
USDT_TOKEN_ADDRESS = config('USDT_TOKEN_ADDRESS', default='')
WBNB_ADDRESS = config('WBNB_ADDRESS', default='')
PANCAKE_ROUTER_ADDRESS = config('PANCAKE_ROUTER_ADDRESS', default='')
LP_ymiiUsdt_ADDRESS = config('LP_ymiiUsdt_ADDRESS', default='')
Tools_lpPrice_ADDRESS = config('Tools_lpPrice_ADDRESS', default='')
EbcState_ADDRESS = config('EbcState_ADDRESS', default='')
SECRET_KEY = config('SECRET_KEY', default='')
BSC = config('BSC', default='')



# DEBUG = True
# # EbcContractTokenAddress = '0xe139A62266860BC2b5952830d6476B43c658e489'
# EbcContractTokenAddress = '0xCa73c531d0Db3A07C78Dfa45E291154313b345C0'
# YmiiContractTokenAddress = '0x768a62a22b187EB350637e720ebC552D905c0331'



# TRADE_TOKEN_ADDRESS = '0x768a62a22b187EB350637e720ebC552D905c0331'  #None  # Add token address here example : "0xc66c8b40e9712708d0b4f27c9775dc934b65f0d9"


# USDT_TOKEN_ADDRESS = '0x55d398326f99059fF775485246999027B3197955'  

# WBNB_ADDRESS = "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
# # WBNB_ADDRESS = "0x55d398326f99059fF775485246999027B3197955"

# PANCAKE_ROUTER_ADDRESS = "0x10ED43C718714eb63d5aA57B78B54704E256024E"
# LP_ymiiUsdt_ADDRESS = '0x6b6b2D8166D13b58155b8d454F239AE3691257A6'  
# Tools_lpPrice_ADDRESS = '0x02Fa571EdAd13043EE3f3676E65092c5000E3Ad0'  

# EbcState_ADDRESS='0xEd4Cf521b1Bf91Df5A1e6443D7447ddf849f78dC'

 
# SECRET_KEY = 'mysecretkey'