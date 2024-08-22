from dataclasses import dataclass

from argon2 import PasswordHasher, exceptions


@dataclass
class PasswordManager:

    ph: PasswordHasher = PasswordHasher(memory_cost=19456, time_cost=2, parallelism=1)

    def hasher(self, user_password: str) -> str:
        try:
            hashed_pw = self.ph.hash(password=user_password)

            while self.ph.check_needs_rehash(hashed_pw) is False:
                hashed_pw = self.ph.hash(password=user_password)
                print('Hash: Re-Hashing Password...')

            print('Hash: Success!')
            return hashed_pw

        except exceptions.HashingError as e:
            print(f'error: Hashing Process Failed... {e}')

    def verification(self, stored_hash: str, submitted_password: str,) -> bool:
        try:
            return self.ph.verify(hash=stored_hash, password=submitted_password)
        except exceptions as e:
            print(f'Verification: Failed... {e}')
