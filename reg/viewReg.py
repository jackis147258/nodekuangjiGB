# views.py

from django.http import JsonResponse
from web3 import Web3

from decouple import config
from rest_framework.decorators import api_view, authentication_classes, permission_classes


# 连接到以太坊节点
bsc=config('BSC', default='')

web3 = Web3(Web3.HTTPProvider(bsc))
        
# web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
@api_view(["POST"])
def sign_message(request):
    try:
        # 向用户发送签名请求
        message = "Please sign this message!"
        
        # 构造 JSON 响应
        return JsonResponse({"message": message})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
from eth_account.messages import encode_defunct
 

@api_view(["POST"])
def verify_signature(request):
    try:
        if request.method == 'POST':
            # 从 POST 请求中获取签名
            signature = request.POST.get('signature') 
            
             # 创建待签名的消息
            message = "Please sign this message!"
          
              # 对消息进行编码
            signable_message = encode_defunct(text=message)

            # 验证签名 message_hash
            signer_address = web3.eth.account.recover_message(
                
                signable_message,  # 使用消息哈希作为参数

                signature=signature
            )
            
            # message = encode_defunct(text="I♥SF")
            # web3.eth.account.recover_message(message, signature=signed_message.signature)
            
            
            # 返回签名验证结果
            return JsonResponse({"success": True, "signer_address": signer_address})

             

            
            # 返回签名验证结果
            return JsonResponse({"success": True, "signer_address": signer_address})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
