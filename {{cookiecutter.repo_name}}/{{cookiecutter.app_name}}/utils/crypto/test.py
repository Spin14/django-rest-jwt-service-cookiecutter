from os import getenv
from unittest import TestCase

from jwt import encode, decode
from cryptography.hazmat.primitives import serialization

from utils.crypto import PemKeyLoader


class TestJWTKeys(TestCase):

    ALGORITHMS = ['RS256']

    def test_private_public(self):
        private_key = PemKeyLoader.load_private_key(getenv('DJANGO_JWT_PRIVATE_KEY'))
        public_key = PemKeyLoader.load_public_key(getenv('DJANGO_JWT_PUBLIC_KEY'))

        if private_key is not None and public_key is not None:
            public_key_bytes = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.PKCS1
            )

            private_key_bytes = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )

            payload = {'user_id': 123}
            for algorithm in self.ALGORITHMS:
                token = encode(payload, private_key_bytes, algorithm=algorithm).decode('utf-8')
                decoded_payload = decode(token, public_key_bytes, algorithms=self.ALGORITHMS)

            self.assertEqual(payload, decoded_payload)
