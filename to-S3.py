import boto3
import tarfile
import os
import sys
import posixpath
import var
from boto3.s3.transfer import S3Transfer

directory = sys.argv[1]
dirname = os.path.split(directory)[-1]

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
    
#remove temporary backup from local
    os.remove(tarname)
else:
    print('Please enter a valid directory path')