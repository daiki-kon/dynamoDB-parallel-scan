import random
import string
import boto3
import time


def randomname(n):
    randlst = [random.choice(string.ascii_letters + string.digits)
               for i in range(n)]
    return ''.join(randlst)


if __name__ == '__main__':

    dynamo = boto3.resource('dynamodb')

    table = dynamo.Table('parallel-scan-sample')
    with table.batch_writer() as batch:
        for i in range(10000):
            batch.put_item(
                Item={
                    'productId': i,
                    'name': randomname(8),
                    'rate': random.randint(0, 5),
                }
            )
            time.sleep(0.25)
            print('sleep:', i)
