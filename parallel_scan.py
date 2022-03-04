import boto3
import time
from concurrent import futures


def parallel_scan(segment):
    response = table.scan(
        TotalSegments=4,
        Segment=segment,
        ReturnConsumedCapacity='TOTAL'
    )

    return {
        'Count': response['Count'],
        'ScannedCount': response['ScannedCount'],
        'ConsumedCapacity': response['ConsumedCapacity']
    }


dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('parallel-scan-sample')

futures_list = []

start_time = time.time()
with futures.ThreadPoolExecutor() as executor:
    for segment in range(0, 4):
        future = executor.submit(parallel_scan, segment)
        futures_list.append(future)

elapsed_time = time.time() - start_time


print('ElapsedTime:', elapsed_time)

print('Segment0:', futures_list[0].result())
print('Segment1:', futures_list[1].result())
print('Segment2:', futures_list[2].result())
print('Segment3:', futures_list[3].result())
