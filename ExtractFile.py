import schedule
import time
import sys
import zipfile
import os

# 3. Restore Feature
# Add a command:
# python Script.py --restore ZipFileName
# Destination
# Extract backup to given directory





def ExtractZipFile(ZipFileName,Designation,exclude_extensions= None):
    if exclude_extensions is None:
        # Ignore:
            # .tmp..log..exe
        exclude_extensions = [".tmp", ".log", ".exe"] 
        
    fobj = os.path.exists(Designation)
    
    if fobj == True:
        ret = os.path.isdir(Designation)
        if ret == False:
            
            return "Unable to create folder"
    else:
        os.makedirs(Designation)
        print("Directory created successfully....")
    print("Outer else ")

    abspath = os.path.dirname (os.path.abspath(__file__))
    Zip_path = os.path.join(abspath, ZipFileName)
    
    print("Looking for zip file at:", Zip_path)
    print("Exists?", os.path.exists(Zip_path))

    filezip = zipfile.ZipFile(Zip_path,"r")
    for file in filezip.namelist():
        if file.endswith(tuple(exclude_extensions)):
            print(f"Skipping excluded file: {file}")
            continue
        filezip.extract(file, Designation)
        print(f"Extracted: {file}")

    filezip.close()
    # filezip.extractall(Designation)
    # filezip.close() 
    print("end...")



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
            
    # python demo.py  --restore  Data 
    elif (len(sys.argv) == 4):
        print("Inside projects logic")        
        # print("Time interval : ", sys.argv[1])
        # print("Directory name : ", sys.argv[2])
        
        if sys.argv[1] == "--restore":
            Zipfilename = sys.argv[2]
            designation = sys.argv[3]
        
        ExtractZipFile(Zipfilename,designation)
        
        # Apply the scheduler
        # schedule.every(int(sys.argv[1] ) ).minutes.do(ExtractZipFile, sys.argv[2])
        # res = LogDetailFolderFile("10","a","6")
        # print("File name ---",res)
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