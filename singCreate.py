@api_view(["GET"])
def generate_key(request):
    account = Account.create()
    private_key = account.privateKey.hex()
    address = account.address
    
    result = {
        'private_key': private_key,
        'address': address
    }
    
    return JsonResponse({'valid': True, 'message': result})