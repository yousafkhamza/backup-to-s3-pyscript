# Directory Backup Moved to S3 (Pyscript)
[![Build](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

---
## Description
Here it's a python script that needs to use this script simply create a directory backup and moved that compressed backup file to a configured S3 bucket with the help of python script and AWS IAM User with S3 full access. So, let's roll down.

----
## Feature
- Easy to configure for anyone 
- It generates the directory compressed format
- Which one we entered directory converted to a backup/compressed form to S3
- All the steps I have provided including AWS IAM User and S3 Bucket Creation 

---
## Modules used
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [os](https://docs.python.org/3/library/os.html)
- [posixpath](https://www.oreilly.com/library/view/python-standard-library/0596000960/ch13s04.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [tarfile](https://docs.python.org/3/library/tarfile.html)


----
## Pre-Requests
- Basic Knowledge of python 
- Basic Knowledge of AWS IAM, S3 service
- Need to change your IAM user creds and bucket name at var.py

### IAM User Creation steps (_with screenshot_)
1. _log into your AWS account as a root user and go to IAM user_
2. _goto Access Managment >> Users_
![alt_txt](https://i.ibb.co/Y7kzZmN/IAM-1.png)
3. _Click Add User_ (_top right corner_)
![alt_txt](https://i.ibb.co/wW38xvR/IAM-2.png)
4. _Enter any username as you like and Choose "Programmatic access" >> Click Next Permissions_
![alt_txt](https://i.ibb.co/TrCbpBh/IAM-3.png)
5. _Set Permissions >> Select "Attach existing policies directly" >> Choose "AmazonS3FullAccess" >> Click Next Tags_
![alt_txt](https://i.ibb.co/8BHhwmc/IAM-4.png)
6. _Add Tags(Optional)_ >> _Enter a key and value as you like either you can leave as blank_
![alt_txt](https://i.ibb.co/QQb9svy/IAM-5.png)
7. _Review your user details and click "Create User"_
![alt_txt](https://i.ibb.co/RcxL770/IAM-6.png)
8. _Store your credentials to your local_
![alt_txt](https://i.ibb.co/nPVWcXZ/IAM-7.png)

_Reference URL_:: _IAM User creation [article](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)_

----
### S3 Bucket Creation (_with screenshot_)
1. _Go to S3 >  Click Create Bucket_
![alt_txt](https://i.ibb.co/bLky3Rb/S3-1.png)
2. _Any bucket name as you wish and then please enable versioning (that you upload same file multiple times or modified versions uploaded that the S3 stored as a version bases like Git)_
![alt_txt](https://i.ibb.co/kXCQJfQ/S3-3.png)
3. _Click create bucket_

![alt_txt](https://i.ibb.co/chwztWB/S3-4.png)

> Reference URL:: Creating S3 bucket please use this [doc](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) and you can secure your bucket with IAM user using S3 [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-iam-policies.html)

----
### Pre-Requested (Dependency packages)
```sh
yum install -y git
yum install -y python3
yum install -y python3-pip
```

### How to get
```sh
git clone https://github.com/yousafkhamza/backup-to-s3-pyscript.git
cd backup-to-s3-pyscript
pip3 install -r requirements.txt
```
> Change your creds and bucket name in at var.py file

Command to run the script::
```
python3 to-S3.py Python/test
# Pyhon/test               <------------ Directory to take backup and move the backup to S3
```

----
## Output be like
```sh
$ $ python3 to-S3.py Python/httpd
Start to Upload that the httpd.tar.gz your S3 Bucket yousaf-test
Backup successfully uploaded to your S3 bucket yousaf-test
```

## View of S3 bucket
_Screenshot_
![alt_txt](https://i.ibb.co/41Cn2QC/Screenshot-67.png)

----
## Behind the code
_vim to-S3.py_
```sh
import boto3
import tarfile
import os
import sys
import posixpath
import var
from boto3.s3.transfer import S3Transfer

directory = sys.argv[1]
dirname = os.path.split(directory)[-1]
if directory.endswith ('/'):
    print ('Please remove / after the directory path you have entered')
else:
    if posixpath.isdir(directory):
        tarname = '/tmp/{}.tar.gz'.format(dirname)
        tar = tarfile.open(tarname,'w:gz')
        tar.add(directory)
        tar.close()
        print('Start to Upload that the', dirname+'.tar.gz', 'your S3 Bucket', var.BUCKET_NAME)

# S3 uploading started
        client = boto3.client('s3', aws_access_key_id=var.AWS_ACCESS_KEY_ID,aws_secret_access_key=var.AWS_SECRET_ACCESS_KEY)
        transfer = S3Transfer(client)
        transfer.upload_file(tarname, var.BUCKET_NAME, 'backup/{}.tar.gz'.format(dirname))
        print('Backup succesfully uploaded to your S3 bucket', var.BUCKET_NAME)
    
# Remove temporary backup from local
        os.remove(tarname)
    else:
        print('Please enter a valid directory path')
```
var.py
```sh
AWS_ACCESS_KEY_ID = 'AKTBRI2N5IAT3ND'             <--------------   Replace your acess key
AWS_SECRET_ACCESS_KEY = 'asUNmMPrC99HoiiQPjehetFtVsPv'          <--------- Replace your secret key
BUCKET_NAME = 'yousaf-test'                <----------- Replace your bucket name
```
----
## Conclusion
It's a simple python script to take backup of directories (compressing) then the same to move your mentioned S3 bucket with the help of AWS IAM User. this script may be helpful who had face issues moving backups to S3 so it might be useful for cloud engineers.  

### ⚙️ Connect with Me 

<p align="center">
<a href="mailto:yousaf.k.hamza@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/yousafkhamza"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a> 
<a href="https://www.instagram.com/yousafkhamza"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"/></a>
<a href="https://wa.me/%2B917736720639?text=This%20message%20from%20GitHub."><img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white"/></a><br />
