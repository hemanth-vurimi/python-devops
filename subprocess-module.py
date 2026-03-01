import subprocess

# install_nginx = subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nginx'], check=True)
# if install_nginx.returncode == 0:
#     print("Nginx installed successfully.")
# elif install_nginx.returncode == 1:
#     print("Nginx is already installed.")


# check_cpu = subprocess.run(["df", "-h"], capture_output=True, text=True)

# if check_cpu.returncode == 0:
#     print("Disk usage:")
#     print(check_cpu.stdout)
# else:
#     print("Error checking disk usage:")
#     print(check_cpu.stderr)

# --------------------------------------------------------- 

## Check if nginx is installed and running if not install nginx ## 
# check_nginx =  subprocess.run(["systemctl", "status", "nginx"], capture_output=True, text=True)

# keywords = ["active (running)", "active (exited)"]

# if check_nginx.returncode == 0 and keywords[0] in check_nginx.stdout:
#     print("Nginx is running.")
# elif check_nginx.returncode == 0 and keywords[1] in check_nginx.stdout:
#     print("Nginx is installed but not running.")
# else:
#     print("Nginx is not installed proceeding to install nginx")
#     install_nginx = subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nginx'], check=True)
#     if install_nginx.returncode == 0:
#         print("Nginx installed successfully.")

## checking disk space and alerting if disk space is above 80% ##

# threshold = 80

# check_disk = subprocess.run(["df", "-h"], capture_output=True, text=True)

# if check_disk.returncode == 0:
#     lines = check_disk.stdout.splitlines()
#     print(lines)
#     if len(lines) > 1:
#         disk_info = lines[1].split()
#         print(disk_info)
#         if len(disk_info) >= 5:
#             usage_percent_str = disk_info[4]
#             usage_percent = int(usage_percent_str.strip('%'))

#             print(f"Disk usage: {usage_percent}%")
#             if usage_percent > threshold:
#                 print(f"Warning: Disk usage is at {usage_percent}%")

## Service Health Checker ## 

# import sys

# service = "nginx"

# result = subprocess.run(
#     ["systemctl", "is-active", service],
#     capture_output=True,
#     text=True
# )

# if result.returncode == 0:
#     print(f"✅ {service} service is running")
#     sys.exit(0)
# else:
#     print(f"❌ {service} service is NOT running")
#     sys.exit(1)

## Command Timeout Handling ##


# import subprocess

# try:
#     result = subprocess.run(
#         ["sleep", "10"],     # Simulating long-running command
#         timeout=5            # Timeout in seconds
#     )
#     print("Command completed successfully")

# except subprocess.TimeoutExpired:
#     print("❌ Command timed out and was terminated")


## opening a file and print the content of the file ##

import os

# file_path = "file.txt"

# if os.path.exists(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print("File content:")
#         print(content)


# with open("1.txt", 'x') as file:
#     file.write("Hello")

import json
# file = "file.json"

# with open(file, 'r') as f:
#     content = json.load(f)
#     print(content)

file = {'name': 'Ashish', 'age': 30, 'city': 'Bangalore'}

with open("file.json", 'w') as f:
    json.dump(file, f, indent=4)

