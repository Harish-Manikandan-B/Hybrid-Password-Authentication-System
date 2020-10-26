import hashlib
import base64
import os
import string
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from qm import qm

print("\n\t\t\t\t CREATE NEW USER")
print("--------------------------------------------------------------------------------")


def long_enough(pw):
    'Password must be at least 10 characters'
    return len(pw) >= 10


def short_enough(pw):
    'Password cannot be more than 30 characters'
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
            print("\n", test.__doc__)
            return False
    return True

# PART 1


def proceed():
    h = hashlib.md5(password.encode())
    h2 = h.hexdigest()  # print("Hash value is\n",h2,"\n\n")

    # HASH PART 1
    # print("First half of hashing is\n",hash1,"\n\n")
    hash1 = h2[0:len(h2)//2]

    # HASH PART 2
    # print("Second half of hashing is\n",hash2,"\n\n")
    hash2 = h2[len(h2)//2 if len(h2) % 2 == 0 else ((len(h2)//2)+1):]

    # HASH PART 1 TO BINARY
    binary = bin(int(hash1, 16))
    binary = binary[2:]  # print("Printing the binary\n",binary,"\n\n")
    binary = binary[2:]

    # TO DO Padding
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
        final_bin = final_bin+"0"

    # PART 2 AES ENCRYPTION(ENCRYPTING HASH 2 USING HASH1 AS KEY)
    passw = bytes(hash1, encoding='utf-8')  # b"password"   hash1 is the key
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(passw))
    f = Fernet(key)
    # hash2 is the input to be encoded
    token = f.encrypt(bytes(hash2, encoding='utf-8'))
    temporary = token.decode()

    # CODE TO WRITE AES VALUE OF USER TO A TEXT FILE
    os.chdir(username)
    filename1 = "encrypt.txt"
    f = open(filename1, "w")
    f.write(token.decode())  # BYTES TO STRING
    f.close()
    fills = open("key.txt", "w")
    fills.write(key.decode())  # BYTES TO STRING
    fills.close()

    # PART 3
    ip = int(final_bin, 2)  # binary to hexa
    mt = []
    for i in range(0, 65536):
        mt.append(i)
    mt.remove(ip)
    n = 128
    a = [mt[i*n:(i+1)*n] for i in range((len(mt) + n - 1))]
    patterns = []
    dt = []
    dt.append(0)
    dt.append(65535)
    count = 0
    for i in range(0, 512):
        print("\niteration--> ", count)
        count = count+1
        patterns.extend(qm(a[i], dt))

    filename2 = "pattern.txt"
    with open(filename2, 'w') as f:
        for item in patterns:
            f.write("%s\n" % item)
            print("\nwriting file\n")
            print(os.getcwd())

    location = os.getcwd()

    # MYSQL CODE
    import string
    import mysql
    import mysql.connector
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'semester-8',
        'raise_on_warnings': True,
    }

    link = mysql.connector.connect(**config)
    mycursor = link.cursor(buffered=True)
    sql = "INSERT INTO manage_users(username,encrypted_string,path)VALUES(%s,%s,%s)"
    val = (username, temporary, location)
    mycursor.execute(sql, val)
    print(mycursor.rowcount, "record inserted")
    mycursor.execute("SELECT * FROM manage_users ")
    name = mycursor.fetchall()
    print(name, end="\n\n")
    mycursor.execute("SELECT * FROM manage_users")
    name2 = mycursor.fetchall()
    for i in range(len(name2)):
        print(name2[i], end="\n\n")
    link.commit()


# Get_user_inputs
username = input('\n\nEnter the username:\n\n')
password = input('\n\nPlease enter a password:\n\n')
if test_password(password):
    print("\nThat is a good password!")
    dir = os.getcwd()
    path = dir + "\\"+username
    try:
        os.mkdir(path)
    except OSError as error:
        print(error)
    proceed()
os.system("pause")
