import json
import boto3

sns = boto3.client("sns")
dynamodb = boto3.resource("dynamodb")

# Replace with your actual DynamoDB table name
table = dynamodb.Table("LogiHaul-Orders")

TOPIC_ARN = "arn:aws:sns:af-south-1:437619427896:LogiHaul-Notification-Topic"

def lambda_handler(event, context):

    print("EVENT RECEIVED:", event)

    for record in event["Records"]:

        body = json.loads(record["body"])

        # Read all values from the SQS message
        order_id = body.get("OrderID", "UNKNOWN")
        created_at = body.get("CreatedAt")
        customer_id = body.get("CustomerID", "UNKNOWN")
        driver_id = body.get("DriverID", "UNASSIGNED")
        delivery_status = body.get("DeliveryStatus", "Pending")
        status = body.get("Status", "Active")

        print("Processing order:", order_id)

        # Write the order to DynamoDB
        table.put_item(
            Item={
                "OrderID": order_id,
                "CreatedAt": created_at,
                "CustomerID": customer_id,
                "DriverID": driver_id,
                "DeliveryStatus": delivery_status,
                "Status": status
            }
        )

        # Send notification
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="LogiHaul Delivery Notification",
            Message=f"Order {order_id} has been processed successfully.\n"
                    f"Customer ID: {customer_id}\n"
                    f"Driver ID: {driver_id}\n"
                    f"Delivery Status: {delivery_status}\n"
                    f"Status: {status}"
        )

    return {
        "statusCode": 200,
        "body": "Processed SQS messages successfully."
    }