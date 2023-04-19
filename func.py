# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:56:24 2023

@author: hkarayazim
"""

import socket
import portlist
import os
import time


def welcome_screen(app_name,delay_time):
    os.system("cls" if os.name == "nt" else "clear")

    # Define the variables
    
    created_by = "Created by: Hüseyin Karayazım"
    github_link = "https://github.com/BlckSoftware"
    web_site="https://www.huseyinkarayazim.com.tr"

    # Print the ASCII art with blue color
    print("\033[1;34m")
    print("""  
                           _       _           _
                          / /\    / /\        /\_\      
                         / / /   / / /       / / /  _   
                        / /_/   / / /       / / /  /\_\ 
                       / /\ \__/ / /       / / /__/ / / 
                      / /\ \___\/ /       / /\_____/ /  
                     / / /\/___/ /       / /\_______/   
                    / / /   / / /       / / /\ \ \      
                   / / /   / / /       / / /  \ \ \     
                  / / /   / / /       / / /    \ \ \    
                  \/_/    \/_/        \/_/      \_\_\   
                                      

		
""")
 
    print(f"{app_name:^75}")
    print(f"{created_by:^75}")
    print(f"{github_link:^75}")
    print(f"{web_site:^75}")
    print("\033[0m")
    time.sleep(delay_time)


def port_scan(target_host: str, start_port: int, end_port: int):
    """
    Scans the target host for open ports in the range of start_port to end_port (inclusive) and returns
    a list of lists containing the port number and its status ("open" or "closed").

    :param target_host: The target host to scan.
    :param start_port: The port number to start the scan.
    :param end_port: The port number to end the scan.
    :return: A list of lists containing the port number and its status.
    """
    open_ports = []
 
    for port in range(start_port, end_port+1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((target_host, port))
                if result == 0:
                    # open_ports.append([port,"Open"])
                    # port_info(f"{port} - Open ")
                    a=portlist.portDescription(port)
                    
                    print("\n", f"\033[1;31mPORT : {port} - !! \033[4m Open\033[0m\033[1;31m !!  ---> ",a,"\033[0m")
                    
                else:
                    # open_ports.append([port,"Closed"])
                    # port_info(f"{port} - Closed ")
                    a=portlist.portDescription(port)
                    print("\n",f"\033[0;32mPORT : {port} - Closed  ---> ",a,"\033[0m")
        except socket.gaierror:
            print(f"Hostname could not be resolved: {target_host}")
            break
        except socket.error:
            print(f"Couldn't connect to {target_host}:{port}")
            break
    return open_ports

    
   