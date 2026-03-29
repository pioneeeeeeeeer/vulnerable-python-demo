import os
import pickle
import subprocess

password = "admin123"

def run_command():
    cmd = input("Enter command: ")
    os.system(cmd)

def execute_code():
    code = input("Enter python code: ")
    eval(code)

def load_data():
    data = input("Enter serialized data: ")
    obj = pickle.loads(data.encode())

def sql_query():
    user_id = input("Enter user id: ")
    query = "SELECT * FROM users WHERE id=" + user_id
    print(query)

def subprocess_example():
    command = input("Command: ")
    subprocess.Popen(command, shell=True)

if __name__ == "__main__":
    run_command()