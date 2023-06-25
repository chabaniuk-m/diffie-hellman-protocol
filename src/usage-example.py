from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

# Generate parameters for Diffie-Hellman key exchange
parameters = dh.generate_parameters(generator=2, key_size=2048)
private_key = parameters.generate_private_key()

# Get public key to share with the other party
public_key = private_key.public_key()
serialized_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Simulate the other party receiving the public key
# and generating their own private key
received_public_key = serialization.load_pem_public_key(
    serialized_public_key,
    backend=default_backend()
)
received_private_key = parameters.generate_private_key()

# Perform the key exchange
shared_key = private_key.exchange(received_public_key)
received_shared_key = received_private_key.exchange(public_key)

# Verify that the shared keys are equal
assert shared_key == received_shared_key

print("Shared key:", shared_key)
