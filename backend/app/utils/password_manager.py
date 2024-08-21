from argon2 import PasswordHasher

ph = PasswordHasher(memory_cost=19456, time_cost=2, parallelism=1)

hash = ph.hash('Testing')

print(hash)

print(ph.verify(hash, 'Testing'))

print(ph.check_needs_rehash(hash))

print(ph.verify(hash, 'testing'))
