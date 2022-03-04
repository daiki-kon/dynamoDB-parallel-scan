import boto3
import time

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('parallel-scan-sample')

start_time = time.time()
response = table.scan(
    ReturnConsumedCapacity='TOTAL' 
)
elapsed_time = time.time() - start_time

print('ElapsedTime:', elapsed_time)
print('Count:', response['Count'])
print('ScannedCount:', response['ScannedCount'])
print('ConsumedCapacity:', response['ConsumedCapacity'])
