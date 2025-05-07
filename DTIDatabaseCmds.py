#Install MySQL on your computer and set a Password for it
#Also install Python MySQL Connector using the command  -   ' python -m pip install mysql-connector-python '
#Then run the code

import mysql.connector as mysqltor

HOST="localhost"
USER="root"
PASSWD="12345678" #Before Running the code update the PASSWD variable to your MySQL Password.


myDB = mysqltor.connect(
  host=HOST,
  user=USER,
  password=PASSWD
)
cur=myDB.cursor()
cur.execute("DROP DATABASE IF EXISTS DTI") #Drops the previously existing DTI Database
cur.execute("CREATE DATABASE IF NOT EXISTS DTI")
cur.execute("USE DTI")

#CREATE TABLES
cur.execute("CREATE TABLE IF NOT EXISTS Syllabus (SEMESTER INT NOT NULL, BRANCH VARCHAR(50) NOT NULL, SUBJECTS VARCHAR(4000) NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS Students (REG_NO CHAR(9) PRIMARY KEY, NAME VARCHAR(100) NOT NULL, EmailAddress VARCHAR(100) NOT NULL, DateOfBirth DATE NOT NULL, BRANCH VARCHAR(50) NOT NULL, YEAR INT NOT NULL, CGPA FLOAT(4,2), BloodGrp Varchar(4) NOT NULL, PASSWORD VARCHAR(100) NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS faculty (NAME VARCHAR(50) PRIMARY KEY, USERNAME VARCHAR(100) NOT NULL, PASSWORD VARCHAR(100) NOT NULL,EmailAddress VARCHAR(100) NOT NULL, SUBJECTS VARCHAR(200) NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS ENGINEERING_MECHANICS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS CHEMISTRY (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS BASIC_ELECTRONICS_FOR_ELECTRICAL_ENGINEERS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS BIOSCIENCE_FOR_ELECTRICAL_ENGINEERS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULl, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS INDIAN_KNOWLEDGE_SYSTEM (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS ENGINEERING_MATHEMATICS_1 (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS ENGINEERING_MATHEMATICS_2 (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULl, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS ENGINEERING_GRAPHICS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS BASIC_ELECTRONICS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS NUMERICAL_TECHNIQUES (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS PHYSICS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_1 (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS SIGNALS_AND_SYSTEMS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS NETWORK_ANALYSIS_AND_SYNTHESIS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS ELECTRONICS_CIRCUIT_ANALYSIS_AND_DESIGN (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS ANALOG_COMMUNICATION (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS DIGITAL_LOGIC_DESIGN (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS MICROPROCESSOR_AND_MICROCONTROLLER (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS PYTHON_PROGRAMMING (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS INTEGRATED_CIRCUITS_AND_APPLICATIONS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_2 (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

cur.execute("CREATE TABLE IF NOT EXISTS PRINCIPLE_OF_COMMUNICATION_SYSTEMS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS PROBABILITY_AND_STATISTICS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS POWER_ELECTRONICS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS COMPUTER_ORGANIZATION (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS DIGITAL_COMMUNICATION (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS FILTER_THEORY (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS DATA_COMMUNICATIONS_AND_NETWORKING (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS EMBEDDED_SYSTEMS (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS WIRELESS_COMMUNICATION (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS BASICS_OF_VLSI (REG_NO INT PRIMARY KEY, NAME VARCHAR(100) NOT NULL, FACULTY VARCHAR(100) NOT NULL,BRANCH VARCHAR(50) NOT NULL, SEM INT NOT NULL, GRADE CHAR(2), Attendance INT NOT NULL, CREDIT INT NOT NULL)")

#INSERT DATA INTO THE TABLE
try:
    cur.execute("INSERT INTO Syllabus (SEMESTER, BRANCH, SUBJECTS) VALUES\
(2, 'EC', 'ENGINEERING_MATHEMATICS_2|ENGINEERING_GRAPHICS|PHYSICS|BASIC_ELECTRONICS|NUMERICAL_TECHNIQUES'),\
(1, 'EC', 'ENGINEERING_MATHEMATICS_1|ENGINEERING_MECHANICS|CHEMISTRY|BASIC_ELECTRONICS_FOR_ELECTRICAL_ENGINEERS|BIOSCIENCE_FOR_ELECTRICAL_ENGINEERS|INDIAN_KNOWLEDGE_SYSTEM'),\
(2, 'ExTC', 'ENGINEERING_MATHEMATICS_2|ENGINEERING_GRAPHICS|PHYSICS|BASIC_ELECTRONICS|NUMERICAL_TECHNIQUES'),\
(1, 'ExTC', 'ENGINEERING_MATHEMATICS_1|ENGINEERING_MECHANICS|CHEMISTRY|BASIC_ELECTRONICS_FOR_ELECTRICAL_ENGINEERS|BIOSCIENCE_FOR_ELECTRICAL_ENGINEERS|INDIAN_KNOWLEDGE_SYSTEM'),\
(3, 'ExTC', 'MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_1|SIGNALS_AND_SYSTEMS|NETWORK_ANALYSIS_AND_SYNTHESIS|ELECTRONICS_CIRCUIT_ANALYSIS_AND_DESIGN|ANALOG_COMMUNICATION|DIGITAL_LOGIC_DESIGN'),\
(4, 'ExTC', 'MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_2|INTEGRATED_CIRCUITS_AND_APPLICATIONS|MICROPROCESSOR_AND_MICROCONTROLLER|PYTHON_PROGRAMMING'),\
(3, 'EC', 'MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_1|SIGNALS_AND_SYSTEMS|NETWORK_ANALYSIS_AND_SYNTHESIS|ELECTRONICS_CIRCUIT_ANALYSIS_AND_DESIGN|ANALOG_COMMUNICATION|DIGITAL_LOGIC_DESIGN'),\
(4, 'EC', 'MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_2|INTEGRATED_CIRCUITS_AND_APPLICATIONS|MICROPROCESSOR_AND_MICROCONTROLLER|PYTHON_PROGRAMMING'),\
(5, 'ExTC', 'PRINCIPLE_OF_COMMUNICATION_SYSTEMS|PROBABILITY_AND_STATISTICS|POWER_ELECTRONICS'),\
(5, 'EC', 'PRINCIPLE_OF_COMMUNICATION_SYSTEMS|PROBABILITY_AND_STATISTICS|POWER_ELECTRONICS'),\
(6, 'ExTC', 'COMPUTER_ORGANIZATION|DIGITAL_COMMUNICATION|FILTER_THEORY'),\
(6, 'EC', 'COMPUTER_ORGANIZATION|DIGITAL_COMMUNICATION|FILTER_THEORY'),\
(7, 'ExTC', 'DATA_COMMUNICATIONS_AND_NETWORKING|EMBEDDED_SYSTEMS'),\
(7, 'EC', 'DATA_COMMUNICATIONS_AND_NETWORKING|EMBEDDED_SYSTEMS'),\
(8, 'ExTC', 'WIRELESS_COMMUNICATION|BASICS_OF_VLSI'),\
(8, 'EC', 'WIRELESS_COMMUNICATION|BASICS_OF_VLSI')")
    print('Syllabus table Created!')
except:
    print('Error while creating Syllabus Table!')
try:
    cur.execute("INSERT INTO Students (REG_NO, NAME, EmailAddress, DateOfBirth, BRANCH, YEAR, CGPA, BloodGrp, PASSWORD) VALUES('211090001', 'Aarav Sharma', 'aarav_s24@et.vjti.ac.in', '2005-03-12', 'ExTC', 4, 8.45,'A-','20050312'),\
('221090002', 'Ishaan Mehta', 'ishaan_m23@ee.vjti.ac.in', '2006-07-25', 'EC', 3, 7.89,'A+','20060725'),\
('241090003', 'Meera Iyer', 'meera_i24@et.vjti.ac.in', '2005-11-08', 'ExTC', 1, 9.12,'O+','20051108'),\
('211090004', 'Sanya Patel', 'sanya_p23@ee.vjti.ac.in', '2007-02-14', 'EC', 4, 8.76,'B+','20070214'),\
('231090005', 'Rohan Joshi', 'rohan_j24@et.vjti.ac.in', '2006-05-21', 'ExTC', 2, 7.95,'O-','20060521'),\
('221090006', 'Neha Kulkarni', 'neha_k23@ee.vjti.ac.in', '2005-08-30', 'EC', 3, 8.30,'AB+','20050830'),\
('241090007', 'Ananya Rao', 'ananya_r24@et.vjti.ac.in', '2007-01-18', 'ExTC', 1, 6.50,'B-','20070118'),\
('211090008', 'Vikram Nair', 'vikram_n23@ee.vjti.ac.in', '2006-04-05', 'EC', 4, 7.60,'A+','20060405'),\
('231090009', 'Kiran Shah', 'kiran_s24@et.vjti.ac.in', '2005-09-14', 'ExTC', 2, 7.00,'B+','20050914'),\
('221090010', 'Sneha Verma', 'sneha_v23@ee.vjti.ac.in', '2007-03-25', 'EC', 3, 8.55,'O+','20070325')")
    print('Students table Created!')
except:
    print('Error while creating Students Table!')
try:
    cur.execute("INSERT INTO Faculty (NAME, USERNAME, PASSWORD, EmailAddress, SUBJECTS) VALUES\
('Dr. Anil Mehta', 'anmehta', 'anil@123', 'anil@gmail.com', 'CHEMISTRY'),\
('Prof. Sujata Mishra', 'sumishra', 'sujata@123', 'sujata@gmail.com', 'CHEMISTRY|PHYSICS|MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_1|MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_2'),\
('Dr. Rajeshwari Menon', 'ramenon', 'rajeshwari@123', 'rajeshwari@gmail.com', 'ENGINEERING_MATHEMATICS_1|ENGINEERING_MATHEMATICS_2'),\
('Dr. Suresh Nambiar', 'sunambiar', 'suresh@123', 'suresh@gmail.com', 'ENGINEERING_MATHEMATICS_1'),\
('Prof. Arvind Kumar', 'arkumar', 'arvind@123', 'arvind@gmail.com', 'ENGINEERING_MECHANICS'),\
('Prof. Kavita Deshpande', 'kadeshpande', 'kavita@123', 'kavita@gmail.com', 'ENGINEERING_MECHANICS'),\
('Dr. Neelam Choudhury', 'nechoudhury', 'neelam@123', 'neelam@gmail.com', 'BASIC_ELECTRONICS_FOR_ELECTRICAL_ENGINEERS'),\
('Prof. Vikram Bhattacharya', 'vibhattacharya', 'vikram@123', 'vikram@gmail.com', 'BASIC_ELECTRONICS_FOR_ELECTRICAL_ENGINEERS'),\
('Dr. Sunita Bansal', 'subansal', 'sunita@123', 'sunita@gmail.com', 'BIOSCIENCE_FOR_ELECTRICAL_ENGINEERS'),\
('Prof. Prakash Joshi', 'prjoshi', 'prakash@123', 'prakash@gmail.com', 'BIOSCIENCE_FOR_ELECTRICAL_ENGINEERS'),\
('Dr. Sneha Rao', 'snrao', 'sneha@123', 'sneha@gmail.com', 'INDIAN_KNOWLEDGE_SYSTEM'),\
('Prof. Mohan Srinivasan', 'mosrinivasan', 'mohan@123', 'mohan@gmail.com', 'INDIAN_KNOWLEDGE_SYSTEM'),\
('Dr. Divya Kapoor', 'dikapoor', 'divya@123', 'divya@gmail.com', 'ENGINEERING_MATHEMATICS_2'),\
('Prof. Ashok Verma', 'asverma', 'ashok@123', 'ashok@gmail.com', 'ENGINEERING_GRAPHICS'),\
('Prof. Sanjay Kulkarni', 'sakulkarni', 'sanjay@123', 'sanjay@gmail.com', 'ENGINEERING_GRAPHICS|ELECTRONICS_CIRCUIT_ANALYSIS_AND_DESIGN|MICROPROCESSOR_AND_MICROCONTROLLER'),\
('Dr. Nitin Saxena', 'nisaxena', 'nitin@123', 'nitin@gmail.com', 'BASIC_ELECTRONICS'),\
('Prof. Lata Banerjee', 'labanerjee', 'lata@123', 'lata@gmail.com', 'BASIC_ELECTRONICS'),\
('Dr. Gopal Narayanan', 'gonarayanan', 'gopal@123', 'gopal@gmail.com', 'NUMERICAL_TECHNIQUES'),\
('Prof. Meenakshi Sharma', 'mesharma', 'meenakshi@123', 'meenakshi@gmail.com', 'NUMERICAL_TECHNIQUES'),\
('Dr. Amitabh Reddy', 'amreddy', 'amitabh@123', 'amitabh@gmail.com', 'PHYSICS'),\
('Dr. Rajesh Deshmukh', 'radeshmukh', 'rajesh@123', 'rajesh@gmail.com', 'MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_1'),\
('Dr. Pankaj Mehta', 'pamehta', 'pankaj@123', 'pankaj@gmail.com', 'SIGNALS_AND_SYSTEMS'),\
('Dr. Anita Kapoor', 'ankapoor', 'anita@123', 'anita@gmail.com', 'SIGNALS_AND_SYSTEMS'),\
('Dr. Vinod Menon', 'vimenon', 'vinod@123', 'vinod@gmail.com', 'NETWORK_ANALYSIS_AND_SYNTHESIS'),\
('Dr. Anita Desai', 'andesai', 'anita@123', 'anita@gmail.com', 'NETWORK_ANALYSIS_AND_SYNTHESIS'),\
('Dr. Lata Krishnan', 'lakrishnan', 'lata@123', 'lata@gmail.com', 'ELECTRONICS_CIRCUIT_ANALYSIS_AND_DESIGN'),\
('Dr. Ramesh Kulkarni', 'rakulkarni', 'ramesh@123', 'ramesh@gmail.com', 'ANALOG_COMMUNICATION'),\
('Dr. Meera Sen', 'mesen', 'meera@123', 'meera@gmail.com', 'ANALOG_COMMUNICATION'),\
('Dr. Nikhil Patil', 'nipatil', 'nikhil@123', 'nikhil@gmail.com', 'DIGITAL_LOGIC_DESIGN'),\
('Dr. Kavita Menon', 'kamenon', 'kavita@123', 'kavita@gmail.com', 'DIGITAL_LOGIC_DESIGN'),\
('Dr. Anjali Verma', 'anverma', 'anjali@123', 'anjali@gmail.com', 'PYTHON_PROGRAMMING'),\
('Dr. Ramesh Gupta', 'ragupta', 'ramesh@123', 'ramesh@gmail.com', 'PYTHON_PROGRAMMING'),\
('Dr. Pooja Sharma', 'posharma', 'pooja@123', 'pooja@gmail.com', 'INTEGRATED_CIRCUITS_AND_APPLICATIONS'),\
('Dr. Vikas Menon', 'vimenon2', 'vikas@123', 'vikas@gmail.com', 'INTEGRATED_CIRCUITS_AND_APPLICATIONS'),\
('Dr. Kiran Desai', 'kidesai', 'kiran@123', 'kiran@gmail.com', 'MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_2'),\
('Prof. Alok Mishra', 'almishra', 'alok@123', 'alok@gmail.com', 'COMPUTER_ORGANIZATION'),\
('Dr. Neeta Desai', 'nedesai', 'neeta@123', 'neeta@gmail.com', 'COMPUTER_ORGANIZATION'),\
('Prof. Rakesh Tiwari', 'ratiwari', 'rakesh@123', 'rakesh@gmail.com', 'DIGITAL_COMMUNICATION'),\
('Dr. Priya Nanda', 'prnanda', 'priya@123', 'priya@gmail.com', 'DIGITAL_COMMUNICATION|FILTER_THEORY'),\
('Dr. Sameer Jadhav', 'sajadhav', 'sameer@123', 'sameer@gmail.com', 'FILTER_THEORY'),\
('Dr. Kamal Batra', 'kbatra', 'kamal@123', 'kamal@gmail.com', 'PROBABILITY_AND_STATISTICS'),\
('Prof. Aruna Singh', 'arsingh', 'aruna@123', 'aruna@gmail.com', 'PROBABILITY_AND_STATISTICS'),\
('Prof. Nilesh Rane', 'nirane', 'nilesh@123', 'nilesh@gmail.com', 'POWER_ELECTRONICS'),\
('Dr. Shruti Nair', 'shnair', 'shruti@123', 'shruti@gmail.com', 'POWER_ELECTRONICS'),\
('Dr. Ritu Sinha', 'risinha', 'ritu@123', 'ritu@gmail.com', 'PRINCIPLE_OF_COMMUNICATION_SYSTEMS'),\
('Prof. Tarun Malhotra', 'tamalhotra', 'tarun@123', 'tarun@gmail.com', 'PRINCIPLE_OF_COMMUNICATION_SYSTEMS'),\
('Dr. Meenal Rathi', 'mralathi', 'meenal@123', 'meenal@gmail.com', 'WIRELESS_COMMUNICATION'),\
('Dr. Harshita Bansal', 'harbansal', 'harshita@123', 'harshita@gmail.com', 'WIRELESS_COMMUNICATION'),\
('Prof. Reena Kamat', 'reena.kamat', 'reena@123', 'reena@gmail.com', 'BASICS_OF_VLSI'),\
('Prof. Meeta Sharma', 'meeta.sharma', 'meeta@123', 'meeta@gmail.com', 'BASICS_OF_VLSI')")
    print('FACULTY table Created!')
except:
    print('Error while creating FACULTY Table!')


try:
    cur.execute("INSERT INTO CHEMISTRY (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Anil Mehta', 'ExTC', 1, 'AA', 18, 3),\
    ('221090002', 'Ishaan Mehta', 'Prof. Sujata Mishra', 'EC', 1, 'BB', 15, 3),\
    ('241090003', 'Meera Iyer', 'Dr. Anil Mehta', 'ExTC', 1, 'AB', 18, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Sujata Mishra', 'EC', 1, 'BC', 16, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Anil Mehta', 'ExTC', 1, 'AA', 18, 3),\
    ('221090006', 'Neha Kulkarni', 'Prof. Sujata Mishra', 'EC', 1, 'BB', 15, 3),\
    ('241090007', 'Ananya Rao', 'Dr. Anil Mehta', 'ExTC', 1, 'AB', 18, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Sujata Mishra', 'EC', 1, 'BC', 16, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Anil Mehta', 'ExTC', 1, 'AA', 17, 3),\
    ('221090010', 'Sneha Verma', 'Prof. Sujata Mishra', 'EC', 1, 'BB', 15, 3)")
except:
    print('Error while creating CHEMISTRY Table!')
try:
    cur.execute("INSERT INTO ENGINEERING_MATHEMATICS_1 (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'AA', 25, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Suresh Nambiar', 'EC', 1, 'BB', 23, 3),\
    ('241090003', 'Meera Iyer', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'AB', 27, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Suresh Nambiar', 'EC', 1, 'BC', 22, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'AA', 26, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Suresh Nambiar', 'EC', 1, 'BB', 24, 3),\
    ('241090007', 'Ananya Rao', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'AB', 27, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Suresh Nambiar', 'EC', 1, 'BC', 23, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'CC', 25, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Suresh Nambiar', 'EC', 1, 'AA', 26, 3)")
    print('ENGINEERING_MATHEMATICS_1 table Created!')
except:
    print('Error while creating ENGINEERING_MATHEMATICS_1 Table!')
try:
    cur.execute("INSERT INTO ENGINEERING_MECHANICS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'AA', 25, 2),\
    ('221090002', 'Ishaan Mehta', 'Dr. Suresh Nambiar', 'EC', 1, 'BB', 23, 2),\
    ('241090003', 'Meera Iyer', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'AB', 27, 2),\
    ('211090004', 'Sanya Patel', 'Dr. Suresh Nambiar', 'EC', 1, 'BC', 22, 2),\
    ('231090005', 'Rohan Joshi', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'AA', 26, 2),\
    ('221090006', 'Neha Kulkarni', 'Dr. Suresh Nambiar', 'EC', 1, 'BB', 24, 2),\
    ('241090007', 'Ananya Rao', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'AB', 27, 2),\
    ('211090008', 'Vikram Nair', 'Dr. Suresh Nambiar', 'EC', 1, 'BC', 23, 2),\
    ('231090009', 'Kiran Shah', 'Dr. Rajeshwari Menon', 'ExTC', 1, 'CC', 25, 2),\
    ('221090010', 'Sneha Verma', 'Dr. Suresh Nambiar', 'EC', 1, 'AA', 26, 2)")
    print('ENGINEERING_MECHANICS table Created!')
except:
    print('Error while creating ENGINEERING_MECHANICS Table!')

try:
    cur.execute("INSERT INTO BASIC_ELECTRONICS_FOR_ELECTRICAL_ENGINEERS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Neelam Choudhury', 'ExTC', 1, 'AA', 30, 2),\
    ('221090002', 'Ishaan Mehta', 'Prof. Vikram Bhattacharya', 'EC', 1, 'BB', 27, 2),\
    ('241090003', 'Meera Iyer', 'Dr. Neelam Choudhury', 'ExTC', 1, 'AB', 32, 2),\
    ('211090004', 'Sanya Patel', 'Prof. Vikram Bhattacharya', 'EC', 1, 'BC', 26, 2),\
    ('231090005', 'Rohan Joshi', 'Dr. Neelam Choudhury', 'ExTC', 1, 'CC', 28, 2),\
    ('221090006', 'Neha Kulkarni', 'Prof. Vikram Bhattacharya', 'EC', 1, 'AA', 31, 2),\
    ('241090007', 'Ananya Rao', 'Dr. Neelam Choudhury', 'ExTC', 1, 'BB', 27, 2),\
    ('211090008', 'Vikram Nair', 'Prof. Vikram Bhattacharya', 'EC', 1, 'AB', 32, 2),\
    ('231090009', 'Kiran Shah', 'Dr. Neelam Choudhury', 'ExTC', 1, 'BC', 25, 2),\
    ('221090010', 'Sneha Verma', 'Prof. Vikram Bhattacharya', 'EC', 1, 'AA', 33, 2)")
    print('BASIC_ELECTRONICS_FOR_ELECTRICAL_ENGINEERS table Created!')
except:
    print('Error while creating BASIC_ELECTRONICS_FOR_ELECTRICAL_ENGINEERS Table!')

try:
    cur.execute("INSERT INTO BIOSCIENCE_FOR_ELECTRICAL_ENGINEERS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Sunita Bansal', 'ExTC', 1, 'AA', 21, 2),\
    ('221090002', 'Ishaan Mehta', 'Prof. Prakash Joshi', 'EC', 1, 'BB', 19, 2),\
    ('241090003', 'Meera Iyer', 'Dr. Sunita Bansal', 'ExTC', 1, 'AB', 23, 2),\
    ('211090004', 'Sanya Patel', 'Prof. Prakash Joshi', 'EC', 1, 'BC', 19, 2),\
    ('231090005', 'Rohan Joshi', 'Dr. Sunita Bansal', 'ExTC', 1, 'CC', 20, 2),\
    ('221090006', 'Neha Kulkarni', 'Prof. Prakash Joshi', 'EC', 1, 'AA', 22, 2),\
    ('241090007', 'Ananya Rao', 'Dr. Sunita Bansal', 'ExTC', 1, 'BB', 19, 2),\
    ('211090008', 'Vikram Nair', 'Prof. Prakash Joshi', 'EC', 1, 'AB', 23, 2),\
    ('231090009', 'Kiran Shah', 'Dr. Sunita Bansal', 'ExTC', 1, 'BC', 18, 2),\
    ('221090010', 'Sneha Verma', 'Prof. Prakash Joshi', 'EC', 1, 'AA', 24, 2)")
    print('BIOSCIENCE_FOR_ELECTRICAL_ENGINEERS table Created!')
except:
    print('Error while creating BIOSCIENCE_FOR_ELECTRICAL_ENGINEERS Table!')

try:
    cur.execute("INSERT INTO INDIAN_KNOWLEDGE_SYSTEM (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Sneha Rao', 'ExTC', 1, 'AA', 22, 2),\
    ('221090002', 'Ishaan Mehta', 'Prof. Mohan Srinivasan', 'EC', 1, 'AB', 19, 2),\
    ('241090003', 'Meera Iyer', 'Dr. Sneha Rao', 'ExTC', 1, 'BB', 23, 2),\
    ('211090004', 'Sanya Patel', 'Prof. Mohan Srinivasan', 'EC', 1, 'BC', 18, 2),\
    ('231090005', 'Rohan Joshi', 'Dr. Sneha Rao', 'ExTC', 1, 'CC', 21, 2),\
    ('221090006', 'Neha Kulkarni', 'Prof. Mohan Srinivasan', 'EC', 1, 'CD', 19, 2),\
    ('241090007', 'Ananya Rao', 'Dr. Sneha Rao', 'ExTC', 1, 'DD', 21, 2),\
    ('211090008', 'Vikram Nair', 'Prof. Mohan Srinivasan', 'EC', 1, 'AA', 20, 2),\
    ('231090009', 'Kiran Shah', 'Dr. Sneha Rao', 'ExTC', 1, 'AB', 18, 2),\
    ('221090010', 'Sneha Verma', 'Prof. Mohan Srinivasan', 'EC', 1, 'BB', 22, 2)")
    print('INDIAN_KNOWLEDGE_SYSTEM table Created!')
except:
    print('Error while creating INDIAN_KNOWLEDGE_SYSTEM Table!')
try:
    cur.execute("INSERT INTO ENGINEERING_MATHEMATICS_2 (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Rajeshwari Menon', 'ExTC', 2, 'AA', 21, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Divya Kapoor', 'EC', 2, 'AB', 19, 3),\
    ('241090003', 'Meera Iyer', 'Dr. Rajeshwari Menon', 'ExTC', 2, 'BB', 23, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Divya Kapoor', 'EC', 2, 'BC', 19, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Rajeshwari Menon', 'ExTC', 2, 'CC', 20, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Divya Kapoor', 'EC', 2, 'CD', 20, 3),\
    ('241090007', 'Ananya Rao', 'Dr. Rajeshwari Menon', 'ExTC', 2, 'DD', 22, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Divya Kapoor', 'EC', 2, 'AA', 21, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Rajeshwari Menon', 'ExTC', 2, 'AB', 19, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Divya Kapoor', 'EC', 2, 'BB', 23, 3)")
    print('ENGINEERING_MATHEMATICS_2 table Created!')
except:
    print('Error while creating ENGINEERING_MATHEMATICS_2 Table!')

try:
    cur.execute("INSERT INTO ENGINEERING_GRAPHICS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Ashok Verma', 'ExTC', 2, 'AA', 22, 3),\
    ('221090002', 'Ishaan Mehta', 'Prof. Sanjay Kulkarni', 'EC', 2, 'AB', 19, 3),\
    ('241090003', 'Meera Iyer', 'Prof. Ashok Verma', 'ExTC', 2, 'BB', 23, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Sanjay Kulkarni', 'EC', 2, 'BC', 18, 3),\
    ('231090005', 'Rohan Joshi', 'Prof. Ashok Verma', 'ExTC', 2, 'CC', 21, 3),\
    ('221090006', 'Neha Kulkarni', 'Prof. Sanjay Kulkarni', 'EC', 2, 'CD', 19, 3),\
    ('241090007', 'Ananya Rao', 'Prof. Ashok Verma', 'ExTC', 2, 'DD', 21, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Sanjay Kulkarni', 'EC', 2, 'AA', 20, 3),\
    ('231090009', 'Kiran Shah', 'Prof. Ashok Verma', 'ExTC', 2, 'AB', 18, 3),\
    ('221090010', 'Sneha Verma', 'Prof. Sanjay Kulkarni', 'EC', 2, 'BB', 22, 3)")
    print('ENGINEERING_GRAPHICS table Created!')
except:
    print('Error while creating ENGINEERING_GRAPHICS Table!')

try:
    cur.execute("INSERT INTO BASIC_ELECTRONICS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Nitin Saxena', 'ExTC', 2, 'AA', 22, 3),\
    ('221090002', 'Ishaan Mehta', 'Prof. Lata Banerjee', 'EC', 2, 'AB', 19, 3),\
    ('241090003', 'Meera Iyer', 'Dr. Nitin Saxena', 'ExTC', 2, 'BB', 22, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Lata Banerjee', 'EC', 2, 'BC', 18, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Nitin Saxena', 'ExTC', 2, 'CC', 20, 3),\
    ('221090006', 'Neha Kulkarni', 'Prof. Lata Banerjee', 'EC', 2, 'CD', 19, 3),\
    ('241090007', 'Ananya Rao', 'Dr. Nitin Saxena', 'ExTC', 2, 'DD', 21, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Lata Banerjee', 'EC', 2, 'AA', 20, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Nitin Saxena', 'ExTC', 2, 'AB', 18, 3),\
    ('221090010', 'Sneha Verma', 'Prof. Lata Banerjee', 'EC', 2, 'BB', 22, 3)")
    print('BASIC_ELECTRONICS table Created!')
except:
    print('Error while creating BASIC_ELECTRONICS Table!')

try:
    cur.execute("INSERT INTO NUMERICAL_TECHNIQUES (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Gopal Narayanan', 'ExTC', 2, 'AA', 21, 3),\
    ('221090002', 'Ishaan Mehta', 'Prof. Meenakshi Sharma', 'EC', 2, 'BB', 20, 3),\
    ('241090003', 'Meera Iyer', 'Dr. Gopal Narayanan', 'ExTC', 2, 'AB', 23, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Meenakshi Sharma', 'EC', 2, 'BC', 19, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Gopal Narayanan', 'ExTC', 2, 'CC', 22, 3),\
    ('221090006', 'Neha Kulkarni', 'Prof. Meenakshi Sharma', 'EC', 2, 'CD', 20, 3),\
    ('241090007', 'Ananya Rao', 'Dr. Gopal Narayanan', 'ExTC', 2, 'DD', 17, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Meenakshi Sharma', 'EC', 2, 'AA', 23, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Gopal Narayanan', 'ExTC', 2, 'BB', 19, 3),\
    ('221090010', 'Sneha Verma', 'Prof. Meenakshi Sharma', 'EC', 2, 'AB', 22, 3)")
    print('NUMERICAL_TECHNIQUES table Created!')
except:
    print('Error while creating NUMERICAL_TECHNIQUES Table!')

try:
    cur.execute("INSERT INTO PHYSICS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Amitabh Reddy', 'ExTC', 2, 'AB', 22, 3),\
    ('221090002', 'Ishaan Mehta', 'Prof. Sujata Mishra', 'EC', 2, 'BB', 20, 3),\
    ('241090003', 'Meera Iyer', 'Dr. Amitabh Reddy', 'ExTC', 2, 'AA', 23, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Sujata Mishra', 'EC', 2, 'BC', 19, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Amitabh Reddy', 'ExTC', 2, 'CC', 21, 3),\
    ('221090006', 'Neha Kulkarni', 'Prof. Sujata Mishra', 'EC', 2, 'CD', 21, 3),\
    ('241090007', 'Ananya Rao', 'Dr. Amitabh Reddy', 'ExTC', 2, 'DD', 17, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Sujata Mishra', 'EC', 2, 'AA', 23, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Amitabh Reddy', 'ExTC', 2, 'BB', 19, 3),\
    ('221090010', 'Sneha Verma', 'Prof. Sujata Mishra', 'EC', 2, 'AB', 22, 3)")
    print('PHYSICS table Created!')
except:
    print('Error while creating PHYSICS Table!')

try:
    cur.execute("INSERT INTO MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_1 (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Rajesh Deshmukh', 'ExTC', 3, 'AA', 28, 3),\
    ('221090002', 'Ishaan Mehta', 'Prof. Sujata Mishra', 'EC', 3, 'BB', 26, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Rajesh Deshmukh', 'ExTC', 3, 'AB', 31, 3),\
    ('221090006', 'Neha Kulkarni', 'Prof. Sujata Mishra', 'EC', 3, 'BC', 25, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Rajesh Deshmukh', 'ExTC', 3, 'BB', 28, 3),\
    ('221090010', 'Sneha Verma', 'Prof. Sujata Mishra', 'EC', 3, 'AA', 22, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Sujata Mishra', 'EC', 3, 'CC', 19, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Sujata Mishra', 'EC', 3, 'DD', 16, 3)")
    print('MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_1 table Created!')
except:
    print('Error while creating MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_1 Table!')
try:
    cur.execute("INSERT INTO SIGNALS_AND_SYSTEMS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Pankaj Mehta', 'ExTC', 3, 'AB', 29, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Anita Kapoor', 'EC', 3, 'BC', 27, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Pankaj Mehta', 'ExTC', 3, 'AA', 31, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Anita Kapoor', 'EC', 3, 'BB', 28, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Pankaj Mehta', 'ExTC', 3, 'CC', 27, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Anita Kapoor', 'EC', 3, 'AA', 22, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Anita Kapoor', 'EC', 3, 'DD', 17, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Anita Kapoor', 'EC', 3, 'BB', 18, 3)")
    print('SIGNALS_AND_SYSTEMS table Created!')
except:
    print('Error while creating SIGNALS_AND_SYSTEMS Table!')
try:
    cur.execute("INSERT INTO NETWORK_ANALYSIS_AND_SYNTHESIS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Vinod Menon', 'ExTC', 3, 'AA', 30, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Anita Desai', 'EC', 3, 'BB', 27, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Vinod Menon', 'ExTC', 3, 'AB', 31, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Anita Desai', 'EC', 3, 'BC', 25, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Vinod Menon', 'ExTC', 3, 'BB', 29, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Anita Desai', 'EC', 3, 'AA', 22, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Anita Desai', 'EC', 3, 'CC', 19, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Anita Desai', 'EC', 3, 'DD', 16, 3)")
    print('NETWORK_ANALYSIS_AND_SYNTHESIS table Created!')
except:
    print('Error while creating NETWORK_ANALYSIS_AND_SYNTHESIS Table!')
try:
    cur.execute("INSERT INTO ELECTRONICS_CIRCUIT_ANALYSIS_AND_DESIGN (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Sanjay Kulkarni', 'ExTC', 3, 'AA', 28, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Lata Krishnan', 'EC', 3, 'BB', 26, 3),\
    ('231090005', 'Rohan Joshi', 'Prof. Sanjay Kulkarni', 'ExTC', 3, 'AB', 30, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Lata Krishnan', 'EC', 3, 'BC', 25, 3),\
    ('231090009', 'Kiran Shah', 'Prof. Sanjay Kulkarni', 'ExTC', 3, 'BB', 28, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Lata Krishnan', 'EC', 3, 'AA', 22, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Lata Krishnan', 'EC', 3, 'CC', 19, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Lata Krishnan', 'EC', 3, 'DD', 16, 3)")
    print('ELECTRONICS_CIRCUIT_ANALYSIS_AND_DESIGN table Created!')
except:
    print('Error while creating ELECTRONICS_CIRCUIT_ANALYSIS_AND_DESIGN Table!')
try:
    cur.execute("INSERT INTO ANALOG_COMMUNICATION (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Ramesh Kulkarni', 'ExTC', 3, 'AA', 29, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Meera Sen', 'EC', 3, 'BB', 27, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Ramesh Kulkarni', 'ExTC', 3, 'AB', 31, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Meera Sen', 'EC', 3, 'BC', 25, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Ramesh Kulkarni', 'ExTC', 3, 'BB', 28, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Meera Sen', 'EC', 3, 'AA', 22, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Meera Sen', 'EC', 3, 'CC', 19, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Meera Sen', 'EC', 3, 'DD', 16, 3)")
    print('ANALOG_COMMUNICATION table Created!')
except:
    print('Error while creating ANALOG_COMMUNICATION Table!')
try:
    cur.execute("INSERT INTO DIGITAL_LOGIC_DESIGN (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Priya Singh', 'ExTC', 3, 'AA', 16, 2),\
    ('221090002', 'Ishaan Mehta', 'Prof. Rohit Sharma', 'EC', 3, 'BB', 15, 2),\
    ('231090005', 'Rohan Joshi', 'Prof. Priya Singh', 'ExTC', 3, 'AB', 17, 2),\
    ('221090006', 'Neha Kulkarni', 'Prof. Rohit Sharma', 'EC', 3, 'BC', 14, 2),\
    ('231090009', 'Kiran Shah', 'Prof. Priya Singh', 'ExTC', 3, 'BB', 16, 2),\
    ('221090010', 'Sneha Verma', 'Prof. Rohit Sharma', 'EC', 3, 'AA', 12, 2),\
    ('211090004', 'Sanya Patel', 'Prof. Rohit Sharma', 'EC', 3, 'CC', 10, 2),\
    ('211090008', 'Vikram Nair', 'Prof. Rohit Sharma', 'EC', 3, 'DD', 8, 2)")
    print('DIGITAL_LOGIC_DESIGN table Created!')
except:
    print('Error while creating DIGITAL_LOGIC_DESIGN Table!')
try:
    cur.execute("INSERT INTO MICROPROCESSOR_AND_MICROCONTROLLER (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Deepak Malhotra', 'ExTC', 4, 'AA', 16, 3),\
    ('221090002', 'Ishaan Mehta', 'Prof. Manish Kumar', 'EC', 4, 'BB', 15, 3),\
    ('231090005', 'Rohan Joshi', 'Prof. Deepak Malhotra', 'ExTC', 4, 'AB', 17, 3),\
    ('221090006', 'Neha Kulkarni', 'Prof. Manish Kumar', 'EC', 4, 'BC', 14, 3),\
    ('231090009', 'Kiran Shah', 'Prof. Deepak Malhotra', 'ExTC', 4, 'BB', 16, 3),\
    ('221090010', 'Sneha Verma', 'Prof. Manish Kumar', 'EC', 4, 'AA', 12, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Manish Kumar', 'EC', 4, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Manish Kumar', 'EC', 4, 'DD', 8, 3)")
    print('MICROPROCESSOR_AND_MICROCONTROLLER table Created!')
except:
    print('Error while creating MICROPROCESSOR_AND_MICROCONTROLLER Table!')
try:
    cur.execute("INSERT INTO PYTHON_PROGRAMMING (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Sameer Kulkarni', 'ExTC', 4, 'AA', 16, 3),\
    ('221090002', 'Ishaan Mehta', 'Prof. Pooja Sharma', 'EC', 4, 'BB', 15, 3),\
    ('231090005', 'Rohan Joshi', 'Prof. Sameer Kulkarni', 'ExTC', 4, 'AB', 17, 3),\
    ('221090006', 'Neha Kulkarni', 'Prof. Pooja Sharma', 'EC', 4, 'BC', 14, 3),\
    ('231090009', 'Kiran Shah', 'Prof. Sameer Kulkarni', 'ExTC', 4, 'BB', 16, 3),\
    ('221090010', 'Sneha Verma', 'Prof. Pooja Sharma', 'EC', 4, 'AA', 12, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Pooja Sharma', 'EC', 4, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Pooja Sharma', 'EC', 4, 'DD', 8, 3)")
    print('PYTHON_PROGRAMMING table Created!')
except:
    print('Error while creating PYTHON_PROGRAMMING Table!')
try:
    cur.execute("INSERT INTO INTEGRATED_CIRCUITS_AND_APPLICATIONS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Kunal Deshmukh', 'ExTC', 4, 'AA', 16, 2),\
    ('221090002', 'Ishaan Mehta', 'Dr. Aarti Rajput', 'EC', 4, 'BB', 15, 2),\
    ('231090005', 'Rohan Joshi', 'Dr. Kunal Deshmukh', 'ExTC', 4, 'AB', 17, 2),\
    ('221090006', 'Neha Kulkarni', 'Dr. Aarti Rajput', 'EC', 4, 'BC', 14, 2),\
    ('231090009', 'Kiran Shah', 'Dr. Kunal Deshmukh', 'ExTC', 4, 'BB', 16, 2),\
    ('221090010', 'Sneha Verma', 'Dr. Aarti Rajput', 'EC', 4, 'AA', 12, 2),\
    ('211090004', 'Sanya Patel', 'Dr. Aarti Rajput', 'EC', 4, 'CC', 10, 2),\
    ('211090008', 'Vikram Nair', 'Dr. Aarti Rajput', 'EC', 4, 'DD', 8, 2)")
    print('INTEGRATED_CIRCUITS_AND_APPLICATIONS table Created!')
except:
    print('Error while creating INTEGRATED_CIRCUITS_AND_APPLICATIONS Table!')
try:
    cur.execute("INSERT INTO MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_2 (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Sunil Mehta', 'ExTC', 4, 'AA', 16, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Rina Kumari', 'EC', 4, 'BB', 15, 3),\
    ('231090005', 'Rohan Joshi', 'Dr. Sunil Mehta', 'ExTC', 4, 'AB', 17, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Rina Kumari', 'EC', 4, 'BC', 14, 3),\
    ('231090009', 'Kiran Shah', 'Dr. Sunil Mehta', 'ExTC', 4, 'BB', 16, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Rina Kumari', 'EC', 4, 'AA', 12, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Rina Kumari', 'EC', 4, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Rina Kumari', 'EC', 4, 'DD', 8, 3)")
    print('MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_2 table Created!')
except:
    print('Error while creating MATHEMATICS_FOR_ELECTRICAL_ENGINEERS_2 Table!')
try:
    cur.execute("INSERT INTO PRINCIPLE_OF_COMMUNICATION_SYSTEMS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Rajeev Sinha', 'ExTC', 5, 'AB', 14, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Neelima Reddy', 'EC', 5, 'BB', 15, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Neelima Reddy', 'EC', 5, 'CC', 11, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Neelima Reddy', 'EC', 5, 'AA', 16, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Neelima Reddy', 'EC', 5, 'BC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Neelima Reddy', 'EC', 5, 'DD', 7, 3)")
    print('PRINCIPLE_OF_COMMUNICATION_SYSTEMS table Created!')
except:
    print('Error while creating PRINCIPLE_OF_COMMUNICATION_SYSTEMS Table!')
try:
    cur.execute("INSERT INTO PROBABILITY_AND_STATISTICS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Meera Kapoor', 'ExTC', 5, 'BB', 17, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Anil Joshi', 'EC', 5, 'AB', 13, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Anil Joshi', 'EC', 5, 'BC', 15, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Anil Joshi', 'EC', 5, 'AA', 12, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Anil Joshi', 'EC', 5, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Anil Joshi', 'EC', 5, 'BB', 14, 3)")
    print('PROBABILITY_AND_STATISTICS table Created!')
except:
    print('Error while creating PROBABILITY_AND_STATISTICS Table!')
try:
    cur.execute("INSERT INTO POWER_ELECTRONICS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Nikhil Bansal', 'ExTC', 5, 'AA', 16, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Kavita Rao', 'EC', 5, 'AB', 11, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Kavita Rao', 'EC', 5, 'BB', 14, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Kavita Rao', 'EC', 5, 'BC', 9, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Kavita Rao', 'EC', 5, 'DD', 8, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Kavita Rao', 'EC', 5, 'CC', 13, 3)")
    print('POWER_ELECTRONICS table Created!')
except:
    print('Error while creating POWER_ELECTRONICS Table!')
try:
    cur.execute("INSERT INTO COMPUTER_ORGANIZATION (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Alok Mishra', 'ExTC', 6, 'AB', 15, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Neeta Desai', 'EC', 6, 'BB', 12, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Neeta Desai', 'EC', 6, 'BC', 14, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Neeta Desai', 'EC', 6, 'AA', 11, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Neeta Desai', 'EC', 6, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Neeta Desai', 'EC', 6, 'DD', 9, 3)")
    print('COMPUTER_ORGANIZATION table Created!')
except:
    print('Error while creating COMPUTER_ORGANIZATION Table!')
try:
    cur.execute("INSERT INTO DIGITAL_COMMUNICATION (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Rakesh Tiwari', 'ExTC', 6, 'AA', 17, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Priya Nanda', 'EC', 6, 'AB', 13, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Priya Nanda', 'EC', 6, 'BB', 14, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Priya Nanda', 'EC', 6, 'BC', 12, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Priya Nanda', 'EC', 6, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Priya Nanda', 'EC', 6, 'DD', 11, 3)")
    print('DIGITAL_COMMUNICATION table Created!')
except:
    print('Error while creating DIGITAL_COMMUNICATION Table!')
try:
    cur.execute("INSERT INTO FILTER_THEORY (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Sameer Jadhav', 'ExTC', 6, 'BB', 14, 3),\
    ('221090002', 'Ishaan Mehta', 'Dr. Komal Dixit', 'EC', 6, 'AB', 15, 3),\
    ('221090006', 'Neha Kulkarni', 'Dr. Komal Dixit', 'EC', 6, 'BC', 13, 3),\
    ('221090010', 'Sneha Verma', 'Dr. Komal Dixit', 'EC', 6, 'AA', 16, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Komal Dixit', 'EC', 6, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Komal Dixit', 'EC', 6, 'DD', 12, 3)")
    print('FILTER_THEORY table Created!')
except:
    print('Error while creating FILTER_THEORY Table!')
try:
    cur.execute("INSERT INTO DATA_COMMUNICATIONS_AND_NETWORKING (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Sanjeev Batra', 'ExTC', 7, 'AA', 17, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Neeta Agarwal', 'EC', 7, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Neeta Agarwal', 'EC', 7, 'DD', 8, 3)")
    print('DATA_COMMUNICATIONS_AND_NETWORKING table Created!')
except:
    print('Error while creating DATA_COMMUNICATIONS_AND_NETWORKING Table!')
try:
    cur.execute("INSERT INTO EMBEDDED_SYSTEMS (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Anuja Menon', 'ExTC', 7, 'AB', 16, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Rekha Srinivas', 'EC', 7, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Rekha Srinivas', 'EC', 7, 'CD', 9, 3)")
    print('EMBEDDED_SYSTEMS table Created!')
except:
    print('Error while creating EMBEDDED_SYSTEMS Table!')
try:
    cur.execute("INSERT INTO WIRELESS_COMMUNICATION (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Dr. Meenal Rathi', 'ExTC', 8, 'AA', 17, 3),\
    ('211090004', 'Sanya Patel', 'Dr. Harshita Bansal', 'EC', 8, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Dr. Harshita Bansal', 'EC', 8, 'DD', 8, 3)")
    print('WIRELESS_COMMUNICATION table Created!')
except:
    print('Error while creating WIRELESS_COMMUNICATION Table!')
try:
    cur.execute("INSERT INTO BASICS_OF_VLSI (REG_NO, NAME, FACULTY, BRANCH, SEM, GRADE, Attendance, CREDIT) VALUES\
    ('211090001', 'Aarav Sharma', 'Prof. Reena Kamat', 'ExTC', 8, 'AB', 16, 3),\
    ('211090004', 'Sanya Patel', 'Prof. Meeta Sharma', 'EC', 8, 'CC', 10, 3),\
    ('211090008', 'Vikram Nair', 'Prof. Meeta Sharma', 'EC', 8, 'CD', 9, 3)")
    print('BASICS_OF_VLSI table Created!')
except:
    print('Error while creating BASICS_OF_VLSI Table!')






myDB.commit()
myDB.close()

'''INSERT INTO STUDENTS (REG_NO, NAME, BRANCH, SEMESTER) VALUES
(211090001, 'DHRUV GUPTA', 'Electronics and Telecommunications', 2),
(221090002, 'ABHISHEK TANDON', 'Electronics and Telecommunications', 2),
(241091003, 'AARADHANA CHAUDHARY', 'Electronics and Telecommunications', 2),
(211090004, 'ABDULSUBHAN SHAHNAWAZ CHIMAOKAR', 'Electronics and Telecommunications', 2),
(231090005, 'AGRAWAL AADITYA PRADEEP', 'Electronics and Telecommunications', 2),
(241091006, 'ANANYA SIBU MATHEW', 'Electronics and Telecommunications', 2),
(241090007, 'ANISH ANANT THENGRE', 'Electronics and Telecommunications', 2),
(241091008, 'ANUSHREE SANTOSH BOBADE', 'Electronics and Telecommunications', 2),
(231090009, 'APAGE SAHIL SHRIDHAR', 'Electronics and Telecommunications', 2),
(241091010, 'ARYA VISHAL SHIRKE', 'Electronics and Telecommunications', 2),
(241091011, 'ASSAR BHAKTI BHAVESH', 'Electronics and Telecommunications', 2),
(241090012, 'AYAAN NASIR AHMED SHAIKH', 'Electronics and Telecommunications', 2),
(241090013, 'AYUSH ANAND KHADSE', 'Electronics and Telecommunications', 2),
(241090014, 'BHALANI HARSHIT VINOD', 'Electronics and Telecommunications', 2),
(241091015, 'BHURKE KHUSHI RAJENDRA', 'Electronics and Telecommunications', 2),
(241090016, 'BISWAS RAYON SAIKAT', 'Electronics and Telecommunications', 2),
(241090017, 'CHAVARE ARHAN ABHIJIT', 'Electronics and Telecommunications', 2),
(241091018, 'CHOUGULE KSHITIJA VILAS', 'Electronics and Telecommunications', 2),
(241090019, 'DHATRAK TEJAS MANOJ', 'Electronics and Telecommunications', 2),
(241090020, 'DHENGRE YASH NAVNIT', 'Electronics and Telecommunications', 2),
(241091021, 'DISHAL MIRCHANDANI', 'Electronics and Telecommunications', 2),
(241091022, 'DONGRE SHRAVANI MILIND', 'Electronics and Telecommunications', 2),
(241090023, 'DURGE ATHARVA MANOJ', 'Electronics and Telecommunications', 2),
(241090024, 'FARUQUI ZAID ABRAR', 'Electronics and Telecommunications', 2),
(241091025, 'GADE ARNIKA ATUL', 'Electronics and Telecommunications', 2),
(241090026, 'GANGAL SHARDUL SANDEEP', 'Electronics and Telecommunications', 2),
(241091027, 'GHARDE SANYUKTA UTTAM', 'Electronics and Telecommunications', 2),
(241090028, 'GHOTKAR RUDRA SUNIL', 'Electronics and Telecommunications', 2),
(241091029, 'GODE BHAGYASHREE SATISH', 'Electronics and Telecommunications', 2),
(241090030, 'GOSAVI PARTH RAJENDRA', 'Electronics and Telecommunications', 2),
(241090031, 'HIMANSHU GOPAL PUROHIT', 'Electronics and Telecommunications', 2),
(241091032, 'JADHAV NIDHI BUDHDIMAN', 'Electronics and Telecommunications', 2),
(241090033, 'JADHAV OM MADHUKAR', 'Electronics and Telecommunications', 2),
(241090034, 'JADHAV OM RAVINDRA', 'Electronics and Telecommunications', 2),
(241090035, 'JAGTAP RAOSAHEB SURESH', 'Electronics and Telecommunications', 2),
(241090036, 'JAVALE ARYAN DATTATRAY', 'Electronics and Telecommunications', 2),
(241090037, 'JONDHALE KANISHK SIDDHARTH', 'Electronics and Telecommunications', 2),
(241090038, 'KANOJE NAYAN DEVIDAS', 'Electronics and Telecommunications', 2),
(241091039, 'KIM SATYAJIT MOHITE', 'Electronics and Telecommunications', 2),
(241090040, 'LALWANI LAKSHYA DEEPAK', 'Electronics and Telecommunications', 2),
(241091041, 'MADAVI RAKSHA GANGADHAR', 'Electronics and Telecommunications', 2),
(241091042, 'MESHRAM PALAK SANJAYKUMAR', 'Electronics and Telecommunications', 2),
(241090043, 'MESTRY ATHARVA NANDKUMAR', 'Electronics and Telecommunications', 2),
(241090044, 'MIRJI SHLOK HEMANT', 'Electronics and Telecommunications', 2),
(241090045, 'MUDIT BENGANI', 'Electronics and Telecommunications', 2),
(241091046, 'MUSKAAN SACHIN KARWA', 'Electronics and Telecommunications', 2),
(241090047, 'NANAJKAR OMKAR KALIDAS', 'Electronics and Telecommunications', 2),
(241091048, 'NEVREKAR TANISHA SHIVANAND', 'Electronics and Telecommunications', 2),
(241090049, 'PADALKAR ARYAN JAGANNATH', 'Electronics and Telecommunications', 2),
(241090050, 'PANDEY SARVESH DINESH', 'Electronics and Telecommunications', 2),
(241090051, 'PARAB ARYAN JAYANT', 'Electronics and Telecommunications', 2),
(241090052, 'PATIL ATHARV SAGAR', 'Electronics and Telecommunications', 2),
(241090053, 'PATIL PIYUSH SHIVAJI', 'Electronics and Telecommunications', 2),
(241091054, 'PATIL SAKSHI CHANDRAKANT', 'Electronics and Telecommunications', 2),
(241090055, 'PATIL SOHAM UMESH', 'Electronics and Telecommunications', 2),
(241090056, 'PAWAR OMKAR RAMCHANDRA', 'Electronics and Telecommunications', 2),
(241090057, 'POPERE HITESH KRISHNA', 'Electronics and Telecommunications', 2),
(241090058, 'PRANAV YOGESH PATIL', 'Electronics and Telecommunications', 2),
(241090059, 'PRATYUSH RAO', 'Electronics and Telecommunications', 2),
(241091060, 'PURVASHA SINGH', 'Electronics and Telecommunications', 2),
(241090061, 'PUSHKAR PRAKASH DUBE', 'Electronics and Telecommunications', 2),
(241091062, 'RANE ANANYA AJAY', 'Electronics and Telecommunications', 2),
(241090063, 'RANGARI SAHIL KAILASH', 'Electronics and Telecommunications', 2),
(241090064, 'SAHIL VILAS DESAI', 'Electronics and Telecommunications', 2),
(241090065, 'SALUNKE YASHRAJ RAMESHCHANDRA', 'Electronics and Telecommunications', 2),
(241090066, 'SARODE GANESH ASHOK', 'Electronics and Telecommunications', 2),
(241090067, 'SARVAARTH NARANG', 'Electronics and Telecommunications', 2),
(241090068, 'SHAH NIHAR KUNAL', 'Electronics and Telecommunications', 2),
(241090069, 'SHAIKH AYAZ HOOD FAROOQUE', 'Electronics and Telecommunications', 2),
(241090070, 'SHELKE ARNAV SACHIN', 'Electronics and Telecommunications', 2),
(241090071, 'SHINDE PRAN BALKRISHNA', 'Electronics and Telecommunications', 2),
(241090072, 'SHIRSAT PAARTH ASHOK', 'Electronics and Telecommunications', 2),
(241091073, 'SHRAVANI GAJANAN HIWASE', 'Electronics and Telecommunications', 2),
(241090074, 'SITAFALE KRISH RAVINDRA', 'Electronics and Telecommunications', 2),
(241090075, 'SONAWANE SAURABH SANJAY', 'Electronics and Telecommunications', 2),
(241090076, 'SURVE MAYURESH ANIL', 'Electronics and Telecommunications', 2),
(241091077, 'SWAMINI KAILASH JADHAV', 'Electronics and Telecommunications', 2),
(241090078, 'THAKRE PIYUSH SHANKAR', 'Electronics and Telecommunications', 2),
(241090079, 'VARUN ADINATH PATIL', 'Electronics and Telecommunications', 2),
(241090080, 'VEDANT MAHESH MALKAR', 'Electronics and Telecommunications', 2);
'''