import json
import boto3
from datetime import datetime, timezone

sqs = boto3.client("sqs")

QUEUE_URL = "https://sqs.af-south-1.amazonaws.com/437619427896/LogiHaul-Delivery-Queue"

def lambda_handler(event, context):

    body = event.get("body")

    if body:
        try:
            body = json.loads(body)
        except Exception:
            body = {}
    else:
        body = {}

    # Read values from the API request
    order_id = body.get("OrderID", "UNKNOWN")
    customer_id = body.get("CustomerID", "UNKNOWN")
    driver_id = body.get("DriverID", "UNASSIGNED")
    delivery_status = body.get("DeliveryStatus", "Pending")
    status = body.get("Status", "Active")

    # Generate timestamp when the API request is received
    created_at = datetime.now(timezone.utc).isoformat()

    # Send message to SQS
    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps({
            "OrderID": order_id,
            "CreatedAt": created_at,
            "CustomerID": customer_id,
            "DriverID": driver_id,
            "DeliveryStatus": delivery_status,
            "Status": status
        })
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Order {order_id} has been processed successfully.",
            "OrderID": order_id,
            "CreatedAt": created_at,
            "CustomerID": customer_id,
            "DriverID": driver_id,
            "DeliveryStatus": delivery_status,
            "Status": status
        })
    }