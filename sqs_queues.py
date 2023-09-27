import boto3
import json
import sys
import argparse

def get_queues_message_totals(queues):
    sqs = boto3.client('sqs')
    results = []

    for queue_name in queues:
        queue_info = {'QueueName': queue_name}
        try:
            response = sqs.get_queue_attributes(
                QueueUrl=queue_name,
                AttributeNames=['ApproximateNumberOfMessages']
            )
            queue_info['MessageCount'] = response['Attributes']['ApproximateNumberOfMessages']
        except Exception as e:
            queue_info['Error'] = str(e)
        results.append(queue_info)

    return results

def print_as_json(queues):
    results = get_queues_message_totals(queues)
    print(json.dumps(results, indent=2))

def main():
    parser = argparse.ArgumentParser(description="Fetch message totals from SQS queues.")
    parser.add_argument('queues', nargs='+', help="List of queue names")
    parser.add_argument('--json', action='store_true', help="Output as JSON")

    args = parser.parse_args()

    if args.json:
        print_as_json(args.queues)
    else:
        print("Queue Name | Message Count")
        print("--------------------------")
        results = get_queues_message_totals(args.queues)
        for result in results:
            print(f"{result['QueueName']} | {result.get('MessageCount', 'Error')}")

if __name__ == "__main__":
    main()
