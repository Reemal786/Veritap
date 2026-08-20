# VeriTap — RFID Student Attendance System 

**VeriTap** is an RFID-based student attendance system designed to streamline classroom attendance and reduce the time professors spend manually recording student presence.


## Purpose 
VeriTap was developed to improve the traditional classroom attendance process by making it faster, more accurate, and less disruptive to instruction.

The system was designed to:

Reduce time spent manually taking attendance
Minimize mistakes associated with manual attendance tracking
Simplify attendance management for professors
Allow students to check themselves in quickly
Enable professors to begin teaching immediately rather than spending the beginning of class taking roll

## Features

* RFID-based student identification
* Automatic attendance recording
* Student information database
* Duplicate scan detection
* LCD feedback after RFID scans
* Graphical interface for viewing and managing attendance information
* Date and time tracking using a real-time clock (RTC)
* Support for adding and managing student RFID records

## How It Works

1. A student taps their RFID card on the reader.
2. The system reads the card's unique RFID identifier.
3. The identifier is compared against registered student records.
4. Duplicate scans are checked to prevent unintended attendance entries.
5. The student's attendance is recorded with the corresponding date and time.
6. The LCD provides feedback confirming the scan.
7. Attendance information can be accessed through the system's graphical interface.

## Technologies

**Languages**

* Java
* Python

**Hardware**

* RFID Reader
* RFID Cards/Tags
* LCD Display
* Real-Time Clock (RTC)

**Software Concepts**

* RFID communication
* Database management
* Hardware-software integration
* GUI development
* Duplicate detection
* Real-time data logging


## System Architecture

```text
       RFID Card
           │
           ▼
     RFID Reader
           │
           ▼
   Student ID Lookup
           │
           ▼
   Duplicate Check
           │
           ▼
  Attendance Database
           │
      ┌────┴────┐
      ▼         ▼
 LCD Feedback   GUI
      │
      ▼
Student Confirmation
```


## Future Improvements

* User authentication for instructors and administrators
* Web-based attendance dashboard
* Attendance analytics and reporting
* Export attendance records to CSV
* Improved database management
* Notifications for missing or duplicate attendance records
* More extensive automated testing


