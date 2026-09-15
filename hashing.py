#Hashing: one way process. same input --> same output

import hashlib

password = "monkey100?"

data = password.encode("utf-8")
digust = hashlib.md5(data).hexdigest()

print(f"Password:{password}")
print(f"Hash: {digust}")


# Comparing Hased passwords

diff_Passwords = ["Monkey100?", "a", "George_n_Bones", "douglessJake" ]

for p in diff_Passwords:
    data = p.encode("utf-8") # converts plain text to raw bytes
    digust = hashlib.md5(data).hexdigest()  
    print(f"Password: {p}")
    print(f"Hash: {digust}", "\n")