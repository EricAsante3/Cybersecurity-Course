import subprocess
import sys
import time
from Lab1Gen import hashF
from datetime import datetime

t0 = datetime.now()
print(f"start time: {t0}")

ExposedUsers = open('../../Vulnerable_Users/Exposed_Usernames', 'r')  # 'r' is for read mode
HashedPasswordfile = open('../../Vulnerable_Users/Salted_Common_PWs', 'r')  # 'r' is for read mode
PwnedPWs100kfile = open('../../Vulnerable_Users/Common_PWs100k', 'r')  # 'r' is for read mode

UserInfo = []
for line in ExposedUsers:
    UserInfo.append(line.strip())

UsersHashedPasswords = {}
for line in HashedPasswordfile:
    line = line.strip()   
    name, password = line.split(',')
    if name in UserInfo:
        UsersHashedPasswords.update({password:name})

for line in PwnedPWs100kfile:
    line = line.strip()   
    for i in range(10):
        for j in range(10):
            password = line + str(i) + str(j)

            hashedpassword = hashF(password)

            if hashedpassword in UsersHashedPasswords.keys():
                name = UsersHashedPasswords[hashedpassword]
                attempt = subprocess.run(["../../Vulnerable_Users/Login.pyc",name,password],capture_output=True, text = True)
                if attempt.stdout == "Login successful.\n":
                    print(f"Dum User: {name}")
                    print(f"Correct Password: {password}")

t1 = datetime.now()
print(f"end time: {t1}")

