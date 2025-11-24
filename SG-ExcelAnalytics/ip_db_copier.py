import pandas as pd
import csv
import os
import glob
import openpyxl
from pathlib import Path
import paramiko as pmk
import socket

BASE_DIR = Path(__file__).resolve().parent


class IP_DB_Copier:
    def __init__(self, device_name_list, device_ip_list):
        self.device_name_list = device_name_list
        self.device_ip_list = device_ip_list

    def copy_db(self):
        local_dir = r"C:\\Users\\user\Desktop\\Yakir Avner\\SG_Devices"
        if not os.path.exists(local_dir):
            os.mkdir(local_dir)
            print("This folder doesn't exist!!!")

    def connect_to_SGPhone(self):
        for phone_name, ip in zip(self.device_name_list, self.device_ip_list):
            # Connecting to each DB in the list.
            # Define the database connector from the given IP
            try:
                hostname, port = ip.split(":")
                port = int(port)
            except ValueError:
                print(f"Invalid IP format: {ip}")
                continue
            port = int(port)
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            phone_source_folder = r"/Documents"

            client = pmk.SSHClient()
            client.set_missing_host_key_policy(pmk.AutoAddPolicy())

            try:
                client.connect(hostname=hostname, port=port,
                               username=username, password=password)
                sftp = client.open_sftp()
                remote_dir = sftp.listdir(phone_source_folder)
                for db_date in phone_source_folder:
                    print(db_date)

            except (pmk.SSHException, socket.timeout, TimeoutError, OSError) as e:
                print(
                    f"Failed to connect to device at IP: {hostname} with an {e} error")
