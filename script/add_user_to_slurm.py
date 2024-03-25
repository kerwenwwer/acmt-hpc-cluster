import subprocess

def add_user_to_slurm_account(username, account='lab'):

    # Use sacctmgr to add user to an exist slurm account.
    command = f"sacctmgr add user {username} Account={account} --immediate"

    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        if result.stderr:
            print(f"Error {result.stderr}")
        else:
            print(f"User {username} has been added to {account}")
    except subprocess.CalledProcessError as e:
        print(f"Falt a slurm contorl: {e}")
    
if __name__ == "__main__":
    username = input("Username: ")
    add_user_to_slurm_account(username)
