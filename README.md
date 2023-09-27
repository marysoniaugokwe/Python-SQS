<h1>SQS Queue Message Totals</h1>

This Python script allows you to fetch and display the current number of items in one or more Amazon Simple Queue Service (SQS) queues and their corresponding dead letter queues.

Prerequisites

Boto3 1.16+: The script utilizes the Boto3 library to interact with AWS services.

Python 3.8+: Ensure you have Python 3.8 or a later version installed.

AWS Credentials: You need valid AWS credentials to access SQS. Make sure to set up region name, AWS access key ID and secret access key. You can configure them using one of the following methods:

- AWS CLI: Use the aws configure command to set up your credentials.
- Environment Variables: Set the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and REGION_NAME environment variables.

Installation
Install Boto3 using pip if it's not already installed:

pip install boto3
Download the script sqs_queues.py to your local machine.

Usage
You can run the script from the command line, and it also supports output in JSON format. Use the following syntax:

python sqs_queues.py [OPTIONS] queue1 queue2 ...

Options:

--json: Output the results in JSON format.
Example Usage:

To fetch message counts from specific SQS queues and display them in a tabular format:

python sqs_queues.py queue-1 queue-2 queue-3
Output:

Queue Name | Message Count
--------------------------
queue-1 | 10
queue-2 | 5
queue-3 | Error: Queue not found

To output the results in JSON format:

python sqs_queues.py --json queue-1 queue-2 queue-3

Output:

[
    {
        "QueueName": "queue-1",
        "MessageCount": "10"
    },
    {
        "QueueName": "queue-2",
        "MessageCount": "5"
    },
    {
        "QueueName": "queue-3",
        "Error": "Queue not found"
    }
]

Command-Line Options
queues: A list of one or more queue names that you want to fetch message counts for.
--json: Output the results in JSON format. Use this option to parse the results programmatically.

AWS Credentials
To use this script, ensure that you have configured your AWS credentials properly:

Access Key ID: Set the AWS_ACCESS_KEY_ID environment variable or configure it using the AWS CLI.
Secret Access Key: Set the AWS_SECRET_ACCESS_KEY environment variable or configure it using the AWS CLI.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This script utilizes the Boto3 library to interact with AWS services.

Additional Information
For more information on SQS, refer to the Amazon SQS Documentation.
