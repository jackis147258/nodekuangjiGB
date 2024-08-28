from eth_keys import keys
import secrets

def generate_private_key():
    # Generate a new private key using secrets for cryptographic randomness
    private_key_bytes = secrets.token_bytes(32)
    private_key = keys.PrivateKey(private_key_bytes)
    return private_key

def get_address_from_private_key(private_key):
    # Derive the public key and Ethereum address from the private key
    public_key = private_key.public_key
    address = public_key.to_checksum_address()
    return address

# Generate private key and signer address
private_key = generate_private_key()
signer_address = get_address_from_private_key(private_key)

# Print the private key and signer address
print(f"Private Key: {private_key}")
print(f"Signer Address: {signer_address}")
