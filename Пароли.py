import simplecrypt
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "r") as pw:
    for password in pw:
        password = password[:-1]
        try:
            print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
        except simplecrypt.DecryptionException:
            print(password, 'is wrong')
        else:
            print(password, 'is correct')
