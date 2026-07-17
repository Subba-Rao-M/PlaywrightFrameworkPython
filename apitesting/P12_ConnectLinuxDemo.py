import paramiko as paramiko
import csv
from utilities.configurations import *

# Start Connection
username = getConfig()['Server']['username']
password = getConfig()['Server']['password']
host = getConfig()['Server']['host']
port = getConfig()['Server']['port']
ssh = paramiko.SSHClient()
#ssh is used to connect to remote server
#add the public key of the server to known host file, if not present
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,port,username,password)

# Run commands -command
#stdin - > input to the command
#stdout - > output of the command
#stderr - > error if any
#stdin,stdout,stderr = ssh.exec_command("ls -a")
stdin,stdout,stderr = ssh.exec_command("cat demofile") #cat command is used to read the file content
print(stdout.readlines()) # read all lines from output
lines = stdout.readlines()
print(lines[1])

#Upload files
#sftp is the protocol for uploading  or download the file to remote server
sftp = ssh.open_sftp()
destinationPath = "script.py"
localPath = "batchFiles/script.py"
sftp.put(localPath,destinationPath)

destinationPath = "loanasa.csv"
localPath = "batchFiles/loanasa.csv"
sftp.put(localPath,destinationPath) #take file from local path and place it in destination path
#check using ls -a for file moved in aws instance
#Trigger the Batch commands, by default python should be available in aws instance
stdin,stdout,stderr = ssh.exec_command("python script.py")

#Download the file to local system,
sftp.get("loanasa.csv","outputFiles/loanasa.csv")

#Parse Output file CSV
with open("outputFiles/loanasa.csv") as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    for row in csvReader:
        if row[0] == "32321":
           assert row[1] == "approved"


#close connection
ssh.close()