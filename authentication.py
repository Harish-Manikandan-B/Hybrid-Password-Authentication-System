import mysql.connector
import mysql
import hashlib
import base64
import os
import time
import string
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
print("\n--------------------------------------------------------------------------------")
print("\n\t\t\t\t USER LOGIN PAGE")
print("--------------------------------------------------------------------------------")


def long_enough(pw):
    'Password must be at least 6 characters'
    return len(pw) >= 10


def short_enough(pw):
    'Password cannot be more than 12 characters'
    return len(pw) <= 30


def has_lowercase(pw):
    'Password must contain a lowercase letter'
    return len(set(string.ascii_lowercase).intersection(pw)) > 0


def has_uppercase(pw):
    'Password must contain an uppercase letter'
    return len(set(string.ascii_uppercase).intersection(pw)) > 0


def has_numeric(pw):
    'Password must contain a digit'
    return len(set(string.digits).intersection(pw)) > 0


def has_special(pw):
    'Password must contain a special character'
    return len(set(string.punctuation).intersection(pw)) > 0


def test_password(pw, tests=[long_enough, short_enough, has_lowercase, has_uppercase, has_numeric, has_special]):
    for test in tests:
        if not test(pw):
            print(test.__doc__)
            return False
    return True


# Count_variable
count = 0


# READ PASSWORDS FROM LIST AND PASS IT TO FUNCTION VIA LOOP
# COMPUTE TIME FROM START TO END

# DIRECTORY_TRAVERSAL_PART
username = input('\n\nEnter the username:\n\n')
password = input('\n\nEnter the password:\n\n')
useruser = username

# DATABASE AUTHENTICATION CODE HERE [To check username entered with DB]
# config based on local machine
config = {
    'user': '',
    'password': '',
    'host': 'localhost',
    'database': 'semester-8',
    'raise_on_warnings': True,
}
link = mysql.connector.connect(**config)
mycursor = link.cursor(buffered=True)
sql = "SELECT username FROM manage_users WHERE username=%s"
adr = (useruser,)
mycursor.execute(sql, adr)
name = mycursor.fetchall()  # print(name)
hello = name[0][0]  # print(hello)

if name[0][0] == username:
    start = time.time()
# Directoy_traversal
    dir = os.getcwd()
    path = dir + "\\"+username
    dirc = r"C:/Users/ABISEK/Downloads/code/CODE_FINAL/"+username
    # dirc=r"path"
    os.chdir(dirc)
    print("\n\n--------------------------------------------------------------------------------")
    print("AUTHENTICATION RESULT")
    print("--------------------------------------------------------------------------------")

    # ALSO RUN LOOP HERE
    h = hashlib.md5(password.encode())
    # print("Hash value is\n",h2,"\n")#print("hash value lenght is",len(h2),"\n\n")
    h2 = h.hexdigest()

    # HASH_PART 1
    hash1 = h2[0:len(h2)//2]  # print("First half of hashing is\n",hash1,"\n")

    # HASH_PART 2
    # print("Second half of hashing is\n",hash2,"\n")
    hash2 = h2[len(h2)//2 if len(h2) % 2 == 0 else ((len(h2)//2)+1):]

    # HASH_PART 1 TO BINARY
    binary = bin(int(hash1, 16))
    binary = binary[2:]
    binary = binary[2:]

    # To_do_Padding
    n = 4
    splits = [(binary[i:i+n]) for i in range(0, len(binary), n)]
    pos = ["2", "3", "1", "3", "2", "3", "1", "3", "2", "2", "3", "2", "1",
           "3", "2", "0"]  # static for now,It will be dynamic for each user
    final_bin = ""
    for i in range(0, len(splits)):
        temp1 = int(pos[i])
        temp2 = str(splits[i])
        f = temp2[temp1]
        final_bin = final_bin+f
    if len(final_bin) != 16:
        # print("Printing the postion values from the split\n",final_bin,"\n\n\n")
        final_bin = final_bin+"0"

    # AES_Decryption
    filename1 = "encrypt.txt"
    f = open(filename1, "r")
    temp1 = f.read().replace('\n', '')
    f.close()
    token1 = str.encode(temp1)  # String converted back to bytes
    # Key_file
    fill = open("key.txt", "r")
    temp2 = fill.read().replace('\n', '')
    fill.close()
    key = temp2
    f = Fernet(key)
    token2 = f.decrypt(token1)  # print("token2:",token2)
    # Converting token2 to string for comparing#print("\n\nhash_temp :",hash_temp)
    hash_temp = token2.decode()
    if hash2 == hash_temp:
        count = count + 1  # Authentication_1

    # Pattern_file
    file1 = open('pattern.txt', 'r')
    Lines = file1.readlines()
    ip = final_bin
    time.sleep(4)
    fin = time.time()
    temps = fin-start
    timer_timer = temps
    #print("runtime is:",temps)
else:
    print("USER DOES NOT EXIST")
link.commit()


def checker(x, y):
    match = 0
    nm = 0
    if len(x) == len(y):
        p = 0
        f = 0
        for i in range(0, 16):
            #print(x[i],end=" ")
            if x[i] == "-":
                p = p + 1
            elif x[i] != y[i]:
                f = f + 1
            elif x[i] == y[i]:
                p = p + 1
        # print(p)
        if p == 16:
            match = 4
            print("match")
            return(match)
        elif p != 16:
            nm = 0
            print("nm")
            return(nm)


sum = 1+count  # print("\n\nsum before:",sum)
for line in Lines:
    temp = line.strip()
    # print(temp)
    c = checker(temp, ip)
    sum = sum+c  # print("sum :",sum)
if sum > 2 or sum < 2:
    print("AUTHENTICATION FAILED\n")
    #print("WRONG USERNAME OR PASSWORD")
elif sum == 2:
    print("USER EXISTS\n")
    print("AUTHENTICATION SUCCESS\n")
    print("RUNTIME IS:", timer_timer)
    print("\n")
    #import webbrowser
    # time.sleep(4)
    # webbrowser.open("http://127.0.0.1/e-commerce/")

os.system("pause")
