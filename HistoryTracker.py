# 5. Backup History Tracker
# Maintain a file:
# Date
# Number of files
# Zip size
# Display history using:
# python Script.py-history


import schedule
import time
import sys
import zipfile
import os
import datetime


def HistoryTracker():
    ZipFileName ="D:\Projects\Python_Automation_Projects\Automated_DataShield"
    abspath = os.path.dirname (os.path.abspath(__file__))
    Zip_path = os.path.join(abspath, ZipFileName)
    
    zipfilesize = os.path.getsize(Zip_path)
    print("Looking for zip file at:", Zip_path)
    print("Zip File Size : ",zipfilesize)
    file_details = ""
    for file_name in os.listdir(abspath):
        file_path = os.path.join(abspath, file_name)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            file_created = os.path.getctime(file_path)
            file_created = datetime.datetime.fromtimestamp(file_created).strftime('%Y-%m-%d %H:%M:%S')
            file_details += f"File Name: {file_name}\n"
            file_details += f"File Size: {file_size} bytes\n"
            file_details += f"Date Created: {file_created}\n\n"
    return file_details



def main():
    
    Border = "-" * 60
    print(Border)
    print("--------------------- History Tracker  -------------------")
    print(Border)
    

    # # python Script.py --history
    if (len(sys.argv) == 2):
        print("Inside projects logic")        
        
        if sys.argv[1] == "--history":
            res = HistoryTracker()
            print(res)

        print(Border)
        print("Data Shield  System started successfully")
        # print("Time Interval in minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)
        
        # wait till abort
        # while True:
        #     schedule.run_pending()
        #     time.sleep(1)
            
    else:
        print("Invalid No of command line arguments")
        print("Unable tto Proceed as there is no such option ")
        print("Please use --h or --u get more detail")
        

    
    
    
    print(Border)
    print("--------------- Thank You for using Our script -------------")
    print(Border)

if __name__ == "__main__":
    main()