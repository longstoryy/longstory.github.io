import secrets

# Generate a new random secret key
new_secret_key = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for _ in range(50))

print(new_secret_key)
