# import sys
# import os
# import time
# import schedule
# import shutil
# import hashlib
# import zipfile
# import smtplib
# from email.message import EmailMessage 

# # 1. Logging System
# # Create a Logs/folder
# # Store:
#     # Backup start time
#     # Files copied
#     # Zip file name
#     # Errors (if any)
# def LogDetailFolderFile(BackupStartTime,FileCopies,Zipfilename, error=None):
    
#     logFolderName = "Logfile_Backup_Info"
#     logPath =""
#     ret = os.path.exists(logFolderName)
#     if ret == True:
#             timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
#             logfilename = "Logfile" 
#             createlogfile = logfilename + "_"+timestamp +".log"
            
#             logPath = os.path.join(logFolderName,createlogfile)
#             fobj = open(logPath,"w")
            
#             fobj.write("Backup Start time is : "+BackupStartTime+"\n")
#             fobj.write("FileCopies name : "+ str(FileCopies) + "\n")
#             fobj.write("Zip File name :"+ Zipfilename +" \n")
#             fobj.close()
#             # fobj.write(f"{error}")
#     else:
#         print("Logfile_Backup_Info is created now....")
        
#         ret = os.makedirs(logFolderName, exist_ok= True)

#         print(f"{logFolderName} is created successfully ")
        
#         timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
#         logfilename = "Logfile" 
#         createlogfile = logfilename + "_"+timestamp +".log"
        
#         logPath = os.path.join(logFolderName,createlogfile)
#         fobj = open(logPath,"w")
        
#         fobj.write("Backup Start time is : \n"+BackupStartTime)
#         fobj.write("FileCopies name : \n"+ str(FileCopies))
#         fobj.write("Zip File name : \n"+ Zipfilename)
#         fobj.write(f"{error}")
#         fobj.close()
#     return createlogfile,logFolderName
            



# # 2. Email Notification
# # Send an email after backup completion
# # Attach:
# # Log file
# # Zip file name
# def send_mail(logfile,logfolder ,zip_file) :
    
        
#     sender_email = "ravirajade2@gmail.com"

#     app_passward = "XXXX ebld XXXX XXXX"  # use your own  google app Passward  
    
    
#     # receive_email ="rushikeshchavhan23@gmail.com"
    
#     subject = "Test mail from python script" 
#     body = """Jay Ganesh, 
#         This is a test email sent using  Python.
#         Regards,
#         Raviraj Aade
#     """
    
#     Border = "-" * 60
#     print("FFFFFFF:   --- 11",logfile)
    
#     for FolderName , SubFolderName , FileName in os.walk(logfolder):
#         for file in FileName:
#             fullpath = os.path.join(FolderName,file)
    
#     # create Email Object 
#     msg = EmailMessage()
    
#     # Set mail header
#     msg["From"] = sender_email
#     msg["To"] = "ravirajaade15@gmail.com"
#     msg["Subject"] = subject
    
#     # Add mail body
#     msg.set_content(body)
    
#     fobj = open(fullpath,"rb") # type: ignore
#     data = fobj.read()
#     zipfileobj = open(zip_file,"rb")
#     file2 = zipfileobj.read()
#     print(data)
#     print("FFFFFFF:   ---",logfile)
#     msg.add_attachment(data,maintype = "text",subtype ="plain", filename =f"{fullpath}.log") # type: ignore
    
#     msg.add_attachment(file2,maintype = "text",subtype ="plain", filename =f"{zip_file}.log")
    
#     # Create SMTP SSL Connection Manually
#     smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    
#     # Login using Gmail + App Password
#     smtp.login(sender_email,app_passward)
    
#     # Send the email
#     smtp.send_message(msg)
#     print("Mail send successfully")
#     fobj.close()
#     # Close Connection Manually
#     smtp.quit()






# def Make_Zip(Folder):
#     timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
#     Zip_name = Folder + "_" + timestamp  + ".zip"
    
#     # Open the zip file     
#     zobj = zipfile.ZipFile(Zip_name, "w", zipfile.ZIP_DEFLATED)
    
#     for root , dirs , files in os.walk(Folder):
#         for file in files:
#             full_path = os.path.join(root,file)
#             relative_path = os.path.realpath(full_path)
#             zobj.write(full_path,relative_path)
#     zobj.close()
#     return Zip_name

# def Calculate_hash(path):
#     hobj = hashlib.md5()
    
#     fobj = open(path, "rb")
    
#     while True:
#         data = fobj.read(1024)
#         if not data:
#             break
#         else:
#             hobj.update(data)
    
#     fobj.close()
#     return hobj.hexdigest()
    
# def BackupFiles(Source , Destination):
    
#     copied_files = []
    
#     print("Creating the backup folder for backup process ")
    
#     os.makedirs(Destination, exist_ok=True)
    
    
#     for root , dirs, files in os.walk(Source):
#         for fname in files :
#             src_path = os.path.join(root,fname)
            
#             relative = os.path.relpath(src_path,Source)
#             dest_path = os.path.join(Destination,relative)
            
#             os.makedirs(os.path.dirname(dest_path),exist_ok= True)
            
#             # Copy the files if its new 
            
#             if((not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path)) ):
#                 shutil.copy2(src_path,dest_path)
#                 copied_files.append(relative)
                
            
#     return copied_files

# def MarvellousDataShieldStart(Source = "Data"):
#     Border = "-" * 60
#     print(Border)
#     BackupName = "LogFileBackup"
#     print(Border)
#     backup_starttime = time.ctime()
#     print("Backup process started successfully at ", time.ctime())
#     print(Border)
    
    
    
    
#     files = BackupFiles(Source, BackupName)
#     print("File name : ", files)
#     zip_file = Make_Zip(BackupName)
#     print("Zip file nae ", zip_file)
#     print(Border)
#     print("Backup Completed Successfully")
    
#     print(Border)
#     print("-----------------Log File Info ----------")
    
#     logfile,logfolder = LogDetailFolderFile(backup_starttime,files,zip_file)
#     print("file log",logfile)
    
#     print(Border)
    
#     print(Border)
#     print("-------------------------- Send Mail-----------------")
    
#     send_mail(logfile,logfolder,zip_file)
    
#     print("file send successfully through email ")
    
#     print(Border)
#     print("Files copied : ", len(files))
#     print("Zip file gets created : ", zip_file)
#     print(Border)
    
    

# def main():
    
#     Border = "-" * 60
#     print(Border)
#     print("--------------------- Data Shield System -------------------")
#     print(Border)
    
#     if(len(sys.argv ) == 2):
#         if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
#             print("This Script is used to  : ")
#             print("1 : Takes auto backup at given time ")
#             print("2 : Backup only new and updated files ")
#             print("3 : Create an archive of the backup periodically")

            
#         elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
#             print("Use the automation script as ")
#             print("ScriptName.py TimeInterval SourceDirectory")
#             print("TimeInterval: The time in minutes for periodic scheduling ")
#             print("SourceDirectory : Name of directory to backed up ")
            
#         else:
#             print("Unable tto Proceed as there is no such option ")
#             print("Please use --h or --u get more details")
            
#     # python demo.py 5 Data
#     elif (len(sys.argv) == 3):
#         print("Inside projects logic")        
#         print("Time interval : ", sys.argv[1])
#         print("Directory name : ", sys.argv[2])
        
#         # Apply the scheduler
#         schedule.every(int(sys.argv[1]) ).minutes.do(MarvellousDataShieldStart, sys.argv[2])
#         # res = LogDetailFolderFile("10","a","6")
#         # print("File name ---",res)
#         print(Border)
#         print("Data Shield  System started successfully")
#         print("Time Interval in minutes : ", sys.argv[1])
#         print("Press Ctrl + C to stop the execution")
#         print(Border)
        
#         # wait till abort
#         while True:
#             schedule.run_pending()
#             time.sleep(1)
            
#     else:
#         print("Invalid No of command line arguments")
#         print("Unable tto Proceed as there is no such option ")
#         print("Please use --h or --u get more detail")
        

    
    
    
#     print(Border)
#     print("--------------- Thank You for using Our script -------------")
#     print(Border)

# if __name__ == "__main__":
#     main()



import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage 


##############################################################################################
# Project      : Automated DataShield
# Description  : An automation script that monitors a source folder, backs up only
#                new or modified files, compresses them into a timestamped ZIP archive,
#                generates a detailed log file, and sends an email notification with
#                the log and ZIP file attached — all on a scheduled time interval.
# Author       : Raviraj Aade
# Date         : 17/02/2026
##############################################################################################


Border = "-" * 60


#-----------------------------------------------------------------------------------------------------
#   Function name :  LogDetailFolderFile
#   Description :    Creates a log file inside the 'Logfile_Backup_Info' folder.
#                    Records the backup start time, list of files copied, and the
#                    ZIP file name for every backup run.
#                    If the log folder does not exist, it creates it automatically.
#   Parameter :      BackupStartTime  -> Timestamp when backup started (string)
#                    FileCopies       -> List of files that were backed up
#                    Zipfilename      -> Name of the ZIP file created
#                    error            -> Optional error message (default: None)
#   Return :         (createlogfile, logFolderName) -> log file name and folder name
#   Date :           17/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def LogDetailFolderFile(BackupStartTime, FileCopies, Zipfilename, error=None):

    logFolderName = "Logfile_Backup_Info"
    logPath = ""

    # Check if the log folder already exists
    ret = os.path.exists(logFolderName)

    if ret == True:
        # Folder exists — create a new timestamped log file inside it
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        logfilename = "Logfile"
        createlogfile = logfilename + "_" + timestamp + ".log"

        logPath = os.path.join(logFolderName, createlogfile)
        fobj = open(logPath, "w")

        fobj.write("Backup Start time is : " + BackupStartTime + "\n")
        fobj.write("FileCopies name : " + str(FileCopies) + "\n")
        fobj.write("Zip File name :" + Zipfilename + " \n")
        fobj.close()

    else:
        # Folder does not exist — create the log folder first, then write the log
        print("Logfile_Backup_Info folder not found. Creating now....")

        os.makedirs(logFolderName, exist_ok=True)
        print(f"{logFolderName} created successfully.")

        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        logfilename = "Logfile"
        createlogfile = logfilename + "_" + timestamp + ".log"

        logPath = os.path.join(logFolderName, createlogfile)
        fobj = open(logPath, "w")

        fobj.write("Backup Start time is : \n" + BackupStartTime)
        fobj.write("FileCopies name : \n" + str(FileCopies))
        fobj.write("Zip File name : \n" + Zipfilename)
        fobj.write(f"{error}")
        fobj.close()

    return createlogfile, logFolderName


#-----------------------------------------------------------------------------------------------------
#   Function name :  send_mail
#   Description :    Sends an email notification after the backup is complete.
#                    Attaches the latest log file and the ZIP backup file to the email.
#                    Uses Gmail SMTP SSL (port 465) with an App Password for authentication.
#                    NOTE : Replace sender_email and app_password with your own credentials.
#                           
#   Parameter :      logfile    -> Name of the log file to attach
#                    logfolder  -> Folder where the log files are stored
#                    zip_file   -> Path of the ZIP backup file to attach
#   Return :         None
#   Date :           17/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def send_mail(logfile, logfolder, zip_file):

    # Sender Gmail address
    sender_email = "ravirajade2@gmail.com"

    # Gmail App Password — generated from Google Account > Security > App Passwords
    # NOTE : Use your own App Password here. 
    app_passward = "XXXX XXXX XXXX XXXX"

    subject = "Test mail from python script"
    body = """Jay Ganesh, 
        This is a test email sent using  Python.
        Regards,
        Raviraj Aade
    """

    # Walk through the log folder to get the full path of the latest log file
    for FolderName, SubFolderName, FileName in os.walk(logfolder):
        for file in FileName:
            fullpath = os.path.join(FolderName, file)

    # Create an EmailMessage object
    msg = EmailMessage()

    # Set the email headers
    msg["From"]    = sender_email
    msg["To"]      = "ravirajaade15@gmail.com"
    msg["Subject"] = subject

    # Set the email body text
    msg.set_content(body)

    # Read and attach the log file
    fobj = open(fullpath, "rb")   # type: ignore
    data = fobj.read()
    fobj.close()

    # Read and attach the ZIP backup file
    zipfileobj = open(zip_file, "rb")
    file2 = zipfileobj.read()
    zipfileobj.close()

    # Attach the log file to the email
    msg.add_attachment(data, maintype="text", subtype="plain", filename=f"{fullpath}.log")   # type: ignore

    # Attach the ZIP backup file to the email
    msg.add_attachment(file2, maintype="text", subtype="plain", filename=f"{zip_file}.log")

    # Create an SSL-encrypted SMTP connection to Gmail on port 465
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login using sender Gmail address and App Password
    smtp.login(sender_email, app_passward)

    # Send the composed email message
    smtp.send_message(msg)
    print("Mail sent successfully")

    # Close the SMTP connection
    smtp.quit()


#-----------------------------------------------------------------------------------------------------
#   Function name :  Make_Zip
#   Description :    Creates a compressed ZIP archive of the given folder.
#                    The ZIP file is named with the folder name and a timestamp
#                    so each backup run produces a uniquely named archive.
#                    Uses ZIP_DEFLATED compression for smaller file sizes.
#   Parameter :      Folder -> Name of the folder to compress into a ZIP
#   Return :         Zip_name -> Name of the ZIP file created (string)
#   Date :           17/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def Make_Zip(Folder):

    # Generate a unique ZIP file name using current timestamp
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    Zip_name = Folder + "_" + timestamp + ".zip"

    # Open the ZIP file in write mode with deflate compression
    zobj = zipfile.ZipFile(Zip_name, "w", zipfile.ZIP_DEFLATED)

    # Walk through all files in the folder and add each one to the ZIP
    for root, dirs, files in os.walk(Folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.realpath(full_path)
            zobj.write(full_path, relative_path)

    zobj.close()
    return Zip_name


#-----------------------------------------------------------------------------------------------------
#   Function name :  Calculate_hash
#   Description :    Calculates the MD5 hash of a given file.
#                    Used to detect whether a file has been modified since the last backup.
#                    If the hash of the source file differs from the backup copy,
#                    the file is treated as changed and is re-copied.
#                    Reads the file in 1KB chunks to handle large files efficiently.
#   Parameter :      path -> Full file path of the file to hash (string)
#   Return :         MD5 hash digest string of the file contents
#   Date :           17/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def Calculate_hash(path):

    hobj = hashlib.md5()

    fobj = open(path, "rb")

    # Read the file in 1KB chunks to avoid loading large files into memory at once
    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()
    return hobj.hexdigest()


#-----------------------------------------------------------------------------------------------------
#   Function name :  BackupFiles
#   Description :    Copies files from the Source folder to the Destination (backup) folder.
#                    Performs an incremental backup — only copies a file if :
#                      1. The file does not exist in the backup folder (new file), OR
#                      2. The MD5 hash of the source file differs from the backup copy (modified file)
#                    Unchanged files are skipped to save time and storage space.
#                    Preserves the full folder structure inside the backup destination.
#   Parameter :      Source      -> Path of the source folder to back up (string)
#                    Destination -> Path of the backup destination folder (string)
#   Return :         copied_files -> List of relative file paths that were copied
#   Date :           17/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def BackupFiles(Source, Destination):

    copied_files = []

    print("Creating the backup folder for backup process ")

    # Create the destination folder if it does not already exist
    os.makedirs(Destination, exist_ok=True)

    # Walk through every file in the source folder including subfolders
    for root, dirs, files in os.walk(Source):
        for fname in files:
            src_path = os.path.join(root, fname)

            # Preserve the original subfolder structure inside the backup destination
            relative  = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)

            # Create any missing subfolders in the destination
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy only if the file is new OR its content has changed (hash mismatch)
            if (not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path)):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)

    return copied_files


#-----------------------------------------------------------------------------------------------------
#   Function name :  MarvellousDataShieldStart
#   Description :    Main backup pipeline controller.
#                    Orchestrates the complete backup workflow in order :
#                      1. Copy new or modified files from source to backup folder
#                      2. Compress the backup folder into a timestamped ZIP archive
#                      3. Generate a detailed log file for this backup run
#                      4. Send an email notification with log and ZIP attached
#                    This function is triggered by the scheduler at each time interval.
#   Parameter :      Source -> Name of the source folder to back up (default: "Data")
#   Return :         None
#   Date :           17/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def MarvellousDataShieldStart(Source="Data"):

    print(Border)
    BackupName = "LogFileBackup"
    print(Border)

    backup_starttime = time.ctime()
    print("Backup process started successfully at ", backup_starttime)
    print(Border)

    # Step 1 : Copy new and modified files to the backup folder
    files = BackupFiles(Source, BackupName)
    print("File name : ", files)

    # Step 2 : Compress the backup folder into a timestamped ZIP archive
    zip_file = Make_Zip(BackupName)
    print("Zip file name : ", zip_file)

    print(Border)
    print("Backup Completed Successfully")
    print(Border)

    # Step 3 : Create a log file for this backup run
    print("-----------------Log File Info ----------")
    logfile, logfolder = LogDetailFolderFile(backup_starttime, files, zip_file)
    print("Log file created : ", logfile)
    print(Border)

    # Step 4 : Send email notification with log and ZIP file attached
    print("-------------------------- Send Mail -----------------")
    send_mail(logfile, logfolder, zip_file)
    print("Email sent successfully.")

    print(Border)
    print("Files copied      : ", len(files))
    print("Zip file created  : ", zip_file)
    print(Border)


#-----------------------------------------------------------------------------------------------------
#   Function name :  main
#   Description :    Entry point of the DataShield application.
#                    Handles command-line arguments to control the script behaviour :
#                      --h or --H            -> Display help information
#                      --u or --U            -> Display usage instructions
#                      <interval> <folder>   -> Start scheduled backup every N minutes
#                    Keeps the script running using an infinite loop so the scheduler
#                    can trigger the backup automatically at the given time interval.
#   Parameter :      None (reads from sys.argv)
#   Return :         None
#   Date :           17/02/2026
#   Author:          Raviraj Aade
#----------------------------------------------------------------------------------------------------

def main():

    print(Border)
    print("--------------------- Data Shield System -------------------")
    print(Border)

    if len(sys.argv) == 2:

        # Show help information
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This Script is used to  : ")
            print("1 : Takes auto backup at given time ")
            print("2 : Backup only new and updated files ")
            print("3 : Create an archive of the backup periodically")

        # Show usage instructions
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval: The time in minutes for periodic scheduling ")
            print("SourceDirectory : Name of directory to backed up ")

        else:
            print("Unable to Proceed as there is no such option ")
            print("Please use --h or --u get more details")

    # Start scheduled backup : python DataShield.py 5 Data
    elif len(sys.argv) == 3:
        print("Inside projects logic")
        print("Time interval  : ", sys.argv[1])
        print("Directory name : ", sys.argv[2])

        # Schedule the backup to run every N minutes
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])

        print(Border)
        print("Data Shield System started successfully")
        print("Time Interval in minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)

        # Keep the script running — execute scheduled tasks as they become due
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid No of command line arguments")
        print("Unable to Proceed as there is no such option ")
        print("Please use --h or --u get more detail")

    print(Border)
    print("--------------- Thank You for using Our script -------------")
    print(Border)


if __name__ == "__main__":
    main()