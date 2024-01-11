#!usr/bin/python3

#project objective
#create automation to display the operating system information with the follwing requirements:

#please write a python script in linux with the following requirements:
#1) display the OS version - if windows, display the windows details; if executed on linux, display the linux details
#2) display the private ip address, public ip address, and the default gateway
#3) display the hard disk size; free and used space
#4) display the top five directories and their size
#5) display the cpu usage; refresh every 10 seconds

import platform
import subprocess
import psutil
import socket
import time

#1) display the OS version - if windows, display the windows details; if executed on linux, display the linux details
print('The OS Version is:') 
version=(platform.platform())
print(version)

#2) display the private ip address, public ip address, and the default gateway 

hostname = socket.gethostname()  
ip_address=socket.gethostbyname(hostname)
   
print("The Private IP Address is:")
print(ip_address) 


import requests 
url = 'https://checkip.amazonaws.com'
request = requests.get(url)
ip = request.text
print("The Public IP Address is:" )
print(ip)

gateway_output = subprocess.check_output(['ip', 'route'])
default_gateway = gateway_output.split()[2]
print('The Default Gateway is:')
print(default_gateway)

#3) display the hard disk size; free and used space
disk = psutil.disk_usage('/')
total_size = disk.total
used_size = disk.used
free_size = disk.free


print("Total Disk Size: " + str(total_size) + " bytes")
print("Total Used Size: " + str(used_size) + " bytes")
print("Total Free Size: " + str(free_size) + " bytes")



#4) display the top five directories and their size

import os

#the directory path will be root folder
directory_path = "/"

# Initialize an empty dictionary to store directory sizes
directory_sizes = {}

# Iterate over directories using os.walk()
for root, dirs, files in os.walk(directory_path):
# Check if the current item is a directory
    if os.path.isdir(root):
# Initialize the size variable for the current directory
        size = 0
        
# Iterate over files in the current directory
        for file in files:
# Get the absolute path of the file
            file_path = os.path.join(root, file)
            
# Check if the current item is a file
            if os.path.isfile(file_path):
                # Get the size of the file and add it to the directory's size
                size += os.path.getsize(file_path)
        
# Add the directory path and its size to the dictionary
        directory_sizes[root] = size

# Sort directories by size
sorted_dirs = sorted(directory_sizes, key=directory_sizes.get, reverse=True)[:5]

# Print the top 5 directories and their sizes
print("Top 5 Directories and their Sizes:")
print("---------------------------------")

for directory in sorted_dirs:
    size = directory_sizes[directory]
    print("Directory:", directory)
    print("Size:", size, "bytes")
    print("---------------------------------")
    
#5) display the cpu usage; refresh every 10 seconds    
# Get the current CPU usage

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# Main function to display the CPU usage
def display_cpu_usage():
    while True:
        cpu_usage = get_cpu_usage()
        print("CPU Usage: " + str(cpu_usage) + "%")

        time.sleep(10)

# Call the main function
display_cpu_usage()
