from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

def add():
    description = input("Introduce the description: ")
    user = input("Introduce the username: ")
    pwd = input("Introduce the password: ")
    url = input("Introduce the URL: ")

    with open("passwords.txt", "a") as f:
        f.write(description+ ":" + user + "|" + fernet.encrypt(pwd.encode()).decode() + "|" + url + "\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            description, rest = data.split(":")
            user, pwd, url = rest.split("|")
            print("Entry "+description+": ")
            print("Username: "+user)
            print("Password: " + fernet.decrypt(pwd.encode()).decode())
            print("URL: "+url)

# write_key()
key = load_key()
fernet = Fernet(key)


while True:
    mode = input("Would you like to add a new password or would you like to view existing one? Press q to quit (add/view/q): ").lower()
    if mode == "q":
        quit()
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid method. Try again.")
        continue