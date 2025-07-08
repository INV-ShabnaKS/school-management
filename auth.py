import json
from datetime import datetime,timedelta
ATTEMPTS_FILE="data/login_attempts.json"
USERNAME ="admin"
PASSWORD = "admin"

def load_attempts():
    with open(ATTEMPTS_FILE,"r") as f:
        return json.load(f)

def save_attempts(data):
    with open(ATTEMPTS_FILE,"w") as f:
        json.dump(data,f)

def isblocked(data):
    if data["attempts"]<3:
        return False
    if not data["last_attempt_time"]:
        return False
    last_time= datetime.fromisoformat(data["last_attempt_time"])
    elapsed = datetime.now() - last_time

    if elapsed < timedelta(minutes=5):
        return True 
    data["attempts"] = 0
    data["last_attempt_time"] = None
    save_attempts(data)  
    return False

def login():
    data=load_attempts()
    if isblocked(data):
        print("3 Login attempts Failed...please try again after 5 minutes")
        return False
    username=input("Username:")
    password=input("Passsword:")
    if username == USERNAME and password == PASSWORD:
        print("Login Successful")
        data["attempts"]=0
        data["last_attempt_time"]=None
        save_attempts(data)
        return True
    else:
        print("Invalid Credentials")
        data["attempts"]+=1
        remaining = max(0, 3 - data["attempts"])
        print(f"Attempt {data['attempts']} of 3 failed. {remaining} attempts remaining.")

        data["last_attempt_time"]=datetime.now().isoformat()
        save_attempts(data)
        return False

    