import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile



def Make_Zip(Folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    Zip_name = Folder + "_" + timestamp  + ".zip"
    # Open the zip file 
    
    zobj = zipfile.ZipFile(Zip_name, "w", zipfile.ZIP_DEFLATED)
    
    for root , dirs , files in os.walk(Folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative_path = os.path.realpath(full_path)
            zobj.write(full_path,relative_path)
    zobj.close()
    return Zip_name

def Calculate_hash(path):
    hobj = hashlib.md5()
    
    fobj = open(path, "rb")
    
    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    
    fobj.close()
    return hobj.hexdigest()
    
def BackupFiles(Source , Destination):
    
    copied_files = []
    
    print("CReating the backup folder for backup process ")
    
    os.makedirs(Destination, exist_ok=True)
    
    
    for root , dirs, files in os.walk(Source):
        for fname in files :
            src_path = os.path.join(root,fname)
            
            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)
            
            os.makedirs(os.path.dirname(dest_path),exist_ok= True)
            
            # Copy the files if its new 
            
            if((not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path)) ):
                shutil.copy2(src_path,dest_path)
                copied_files.append(relative)
                
            
    return copied_files

def MarvellousDataShieldStart(Source = "Data"):
    Border = "-" * 60
    print(Border)
    BackupName = "LogFileBackup"
    print(Border)
    print("Backup process started successfully at ", time.ctime())
    print(Border)
    
    
    files = BackupFiles(Source, BackupName)
    
    zip_file = Make_Zip(BackupName)
    
    print(Border)
    print("Backup Completed Successfully")
    
    print("Files copied : ", len(files))
    print("Zip file gets created : ", zip_file)
    print(Border)
    
    

def main():
    
    Border = "-" * 60
    print(Border)
    print("--------------------- Data Shield System -------------------")
    print(Border)
    
    if(len(sys.argv ) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to  : ")
            print("1 : Takes auto backup at given time ")
            print("2 : Backup only new and updated files ")
            print("3 : Create an archive of the backup periodically")

            
        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as ")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval: The time in minutes for periodic scheduling ")
            print("SourceDirectory : Name of directory to backed up ")
            
        else:
            print("Unable tto Proceed as there is no such option ")
            print("Please use --h or --u get more details")
            
    # python demo.py 5 Data
    elif (len(sys.argv) == 3):
        print("Inside projects logic")        
        print("Time interval : ", sys.argv[1])
        print("Directory name : ", sys.argv[2])
        
        # Apply the scheduler
        schedule.every(int(sys.argv[1]) ).minutes.do(MarvellousDataShieldStart, sys.argv[2])
        
        print(Border)
        print("Data Shield  System started successfully")
        print("Time Interval in minutes : ", sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)
        
        # wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    else:
        print("Invalid No of command line arguments")
        print("Unable tto Proceed as there is no such option ")
        print("Please use --h or --u get more detail")
        

    
    
    
    print(Border)
    print("--------------- Thank You for using Our script -------------")
    print(Border)

if __name__ == "__main__":
    main()