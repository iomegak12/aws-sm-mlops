!aws s3 cp s3://sagemaker-sample-files/datasets/tabular/synthetic/churn.txt ./

import boto3
import os
import sagemaker

prefix = 'sagemaker/DEMO-xgboost-churn'
region = boto3.Session().region_name
default_bucket = sagemaker.session.Session().default_bucket()
RawData = boto3.Session().resource('s3')\
.Bucket(default_bucket).Object(os.path.join(prefix, 'data/RawData.csv'))\
.upload_file('./churn.txt')

print(os.path.join("s3://",default_bucket, prefix, 'data/RawData.csv'))
