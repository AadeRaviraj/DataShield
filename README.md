# Automated DataShield — Python Automation Project

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Type](https://img.shields.io/badge/Type-Automation%20Script-red)
![Feature](https://img.shields.io/badge/Feature-Email%20Notification-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

An automated file backup system built in Python that monitors a source folder, backs up only new or modified files, compresses them into a timestamped ZIP archive, generates a detailed log file, and sends an email notification with the log and ZIP attached — all running automatically on a scheduled time interval.

---

## Problem Statement

Manual file backups are time-consuming and easy to forget. This project solves that by fully automating the backup process. You run one command with a time interval and a folder name, and the script handles everything on its own — detecting changed files, copying them, zipping the backup, writing a log, and emailing you a confirmation — without any manual involvement.

---

## Project Structure

```
Automated_DataShield/
│
├── DataShield.py               # Main backup engine — backup, zip, log, and email
├── ExtractFile.py              # Restore feature — extract a ZIP back to a folder
├── HistoryTracker.py           # Displays backup history and file metadata
│
├── Data/                       # Source folder being monitored and backed up
├── LogFileBackup/              # Destination folder where backed up files are stored
├── Logfile_Backup_Info/        # Folder containing all log files from each backup run
│
└── LogFileBackup_<timestamp>.zip   # Timestamped ZIP archives created per backup run
```

---

## Key Features

| Feature | Description |
|---------|-------------|
| Incremental Backup | Only copies files that are new or have been modified since the last backup |
| MD5 Hash Comparison | Detects file changes using MD5 checksums — not just file names or dates |
| Timestamped ZIP Archive | Compresses the backup folder into a uniquely named ZIP after every backup run |
| Automated Log File | Creates a detailed log file for every backup run inside `Logfile_Backup_Info/` |
| Email Notification | Sends an email with the log file and ZIP archive attached after each backup |
| Scheduled Execution | Runs automatically at a user-defined time interval using the `schedule` library |
| Restore Feature | Extracts any ZIP backup back to a specified folder using `ExtractFile.py` |
| Backup History | Displays file metadata and backup history using `HistoryTracker.py` |

---

## Functions Overview

| Function | File | Description |
|----------|------|-------------|
| `LogDetailFolderFile` | DataShield.py | Creates a timestamped log file recording backup details |
| `send_mail` | DataShield.py | Sends email notification with log and ZIP attached via Gmail SMTP |
| `Make_Zip` | DataShield.py | Compresses the backup folder into a timestamped ZIP archive |
| `Calculate_hash` | DataShield.py | Calculates MD5 hash of a file to detect if it has changed |
| `BackupFiles` | DataShield.py | Copies only new or modified files from source to backup folder |
| `MarvellousDataShieldStart` | DataShield.py | Main pipeline — runs all steps in order for each backup cycle |
| `main` | DataShield.py | Entry point — handles CLI arguments and starts the scheduler |
| `ExtractZipFile` | ExtractFile.py | Extracts a ZIP backup to a given destination folder |
| `HistoryTracker` | HistoryTracker.py | Reads and displays file metadata and backup history |

---

## How It Works — Step by Step

**Step 1 — Incremental Backup**
The script walks through every file in the source folder. For each file, it calculates its MD5 hash and compares it with the backup copy. If the file is new or has changed, it is copied. Unchanged files are skipped completely.

**Step 2 — Create ZIP Archive**
After copying, the entire backup folder is compressed into a ZIP file with a timestamped name like `LogFileBackup_2026-02-17_20-59-21.zip`. Each backup run creates a new ZIP so no previous backup is ever overwritten.

**Step 3 — Generate Log File**
A log file is created inside `Logfile_Backup_Info/` recording the backup start time, the list of files copied, and the ZIP file name. This gives a complete audit trail of every backup run.

**Step 4 — Send Email Notification**
An email is sent automatically to the configured recipient with the log file and ZIP archive attached. Gmail SMTP SSL on port 465 is used with a Google App Password for secure authentication.

**Step 5 — Repeat on Schedule**
All of the above happens automatically every N minutes, where N is provided as a command-line argument when starting the script.

---

## Command Line Usage

```bash
# Show help
python DataShield.py --h

# Show usage instructions
python DataShield.py --u

# Start automated backup of 'Data' folder every 5 minutes
python DataShield.py 5 Data

# Restore a backup ZIP to a destination folder
python ExtractFile.py --restore LogFileBackup_2026-02-17_20-59-21.zip ExtractFolder

# View backup history
python HistoryTracker.py --history
```

---

## Email Configuration

The email feature uses Gmail SMTP with a Google App Password. To configure it for your own account:

1. Go to your Google Account settings
2. Enable 2-Step Verification
3. Go to Security and generate an App Password
4. Replace the `sender_email` and `app_passward` values in 

---

## Log File Format

Each log file created inside `Logfile_Backup_Info/` follows this format:

```
Backup Start time is : Tue Feb 17 20:59:21 2026
FileCopies name : ['k copy 3.txt', 'k copy 4.txt', 'k copy 5.txt']
Zip File name : LogFileBackup_2026-02-17_20-59-21.zip
```

---

## Tech Stack

- Python 3
- `os` and `shutil` — file system operations and file copying
- `hashlib` — MD5 hash calculation for detecting file changes
- `zipfile` — creating and extracting ZIP archives
- `smtplib` and `email` — sending email with attachments via Gmail SMTP SSL
- `schedule` — running the backup automatically at set time intervals
- `time` — timestamps for ZIP file names and log files
- `sys` — reading command-line arguments

---

## How to Run

1. Clone this repository
2. Install the required library:
   ```bash
   pip install schedule
   ```
3. Configure your email credentials in `DataShield.py`
4. Run the script:
   ```bash
   python DataShield.py 5 Data
   ```

---

## Key Concepts Covered

- File System Automation (`os.walk`, `shutil.copy2`)
- Incremental Backup using MD5 Hash Comparison
- ZIP File Creation with Compression (`zipfile.ZIP_DEFLATED`)
- Automated Log File Generation
- Email Automation with Attachments (`smtplib`, `EmailMessage`)
- Gmail SMTP SSL Authentication with App Password
- Task Scheduling (`schedule` library)
- Command Line Argument Handling (`sys.argv`)
- File Restore and Extraction Feature

---

## Author

**Raviraj Aade**

Built as a Python Automation Project to understand real-world file management, incremental backup strategies, email automation, and scheduled task execution using pure Python.
