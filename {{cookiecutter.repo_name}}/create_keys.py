from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# The public exponent of the new key.
# Usually one of the small Fermat primes 3, 5, 17, 257, 65537.
# If in doubt you should use 65537.
PUBLIC_EXPONENT = 65537

# generate private/public key pair
key = rsa.generate_private_key(
    backend=default_backend(),
    public_exponent=PUBLIC_EXPONENT,
    key_size=2048
)

# get public key (RSA PUBLIC KEY)
public_key = key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.PKCS1
)

# get private key (RSA PRIVATE KEY)
private_key = key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# to file
with open('private.key', 'wb') as fp:
    fp.write(private_key)

with open('public.key', 'wb') as fp:
    fp.write(public_key)
