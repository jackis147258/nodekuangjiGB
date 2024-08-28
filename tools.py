# config.py

from decimal import Decimal,ROUND_DOWN

def blockchain_number_to_decimal(blockchain_number):
    # 将区块链数字转换为Decimal，假设blockchain_number是字符串类型
    decimal_number = Decimal(blockchain_number)

    # 将区块链数字转换为具体的数值，例如将Wei转换为ETH
    converted_number = decimal_number / Decimal('1000000000000000000')
    
    # 保留3位小数，采用四舍五入的方式
    converted_number = converted_number.quantize(Decimal('0.000'), rounding=ROUND_DOWN)

    return converted_number

 
def decimal_to_blockchain_number(decimal_number):
    # 将Python数字乘以10^18，以将ETH转换为Wei
    blockchain_number = Decimal(decimal_number) * Decimal('1000000000000000000')

    # 将Decimal对象转换为字符串，以表示18位的区块链数字
    blockchain_number_str = str(int(blockchain_number))

    return blockchain_number_str



def blockchain_number_to_float(blockchain_number):
    # 将区块链数字转换为float，假设blockchain_number是字符串类型
    float_number = float(blockchain_number) / 1000000000000000000.0
    
    # 保留3位小数，采用四舍五入的方式
    float_number = round(float_number, 3)

    return float_number