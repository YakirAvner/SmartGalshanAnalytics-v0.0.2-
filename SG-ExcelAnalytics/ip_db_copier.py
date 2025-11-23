import pandas as pd
import csv
import os
import glob
import openpyxl
from pathlib import Path
import paramiko as pmk

BASE_DIR = Path(__file__).resolve().parent


class IP_DB_Copier:
    def __init__(self, device_name_list, device_ip_list):
        self.device_name_list = device_name_list
        self.device_ip_list = device_ip_list

    def copy_databases(self):
        for phone_name, ip in self.device_name_list, self.device_ip_list:
            # Connecting to each DB in the list.
            # Define the database connector from the given IP
            hostname = ip
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            phone_source_folder = r"/Documents"
            remote_dir = glob.glob(os.path.join(
                phone_source_folder, '**', 'Galshan.db'), recursive=True)

            client = pmk.SSHClient()
            client.set.missing_host_key_policy(pmk.AutoAddPolicy())

            try:
                client.connect(hostname=hostname,
                               username=username, password=password)
                sftp = client.open_sftp()
            except pmk.SSHException as e:
                print(f"Failed to connect to device at IP: {hostname}")
                return
