import json
import boto3
import os
from botocore.exceptions import ClientError

def send_email(event, context):
    """
    AWS Lambda function to send emails using Amazon SES
    
    Expected JSON body:
    {
        "receiver_email": "recipient@example.com",
        "subject": "Your subject here",
        "body_text": "Your email content here"
    }
    """
    
    # CORS headers for API Gateway
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    try:
        # Handle preflight CORS requests
        if event.get('httpMethod') == 'OPTIONS':
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'CORS preflight successful'})
            }
        
        # Parse request body
        if 'body' not in event or not event['body']:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'error': 'Missing request body',
                    'message': 'Request body is required'
                })
            }
        
        # Handle both direct invocation and API Gateway
        if isinstance(event['body'], str):
            body = json.loads(event['body'])
        else:
            body = event['body']
        
        # Validate required fields
        required_fields = ['receiver_email', 'subject', 'body_text']
        missing_fields = [field for field in required_fields if field not in body or not body[field]]
        
        if missing_fields:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'error': 'Missing required fields',
                    'missing_fields': missing_fields,
                    'required_fields': required_fields
                })
            }
        
        # Extract email parameters
        receiver_email = body['receiver_email'].strip()
        subject = body['subject'].strip()
        body_text = body['body_text'].strip()
        
        # Validate email format (basic validation)
        if '@' not in receiver_email or '.' not in receiver_email:
            return {
                'statusCode': 400,
                'headers': headers,
                'body': json.dumps({
                    'error': 'Invalid email format',
                    'message': 'Please provide a valid email address'
                })
            }
        
        # Get sender email from environment variable
        from_email = os.environ.get('FROM_EMAIL')
        if not from_email:
            return {
                'statusCode': 500,
                'headers': headers,
                'body': json.dumps({
                    'error': 'Configuration error',
                    'message': 'FROM_EMAIL environment variable not set'
                })
            }
        
        # Create SES client
        ses_client = boto3.client('ses', region_name=os.environ.get('AWS_REGION', 'region: ap-south-1'))
        
        # Send email using SES
        response = ses_client.send_email(
            Source=from_email,
            Destination={
                'ToAddresses': [receiver_email]
            },
            Message={
                'Subject': {
                    'Data': subject,
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Text': {
                        'Data': body_text,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )
        
        # Success response
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({
                'message': 'Email sent successfully',
                'messageId': response['MessageId'],
                'receiver_email': receiver_email,
                'subject': subject
            })
        }
        
    except json.JSONDecodeError as e:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({
                'error': 'Invalid JSON',
                'message': 'Request body must be valid JSON'
            })
        }
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_message = e.response['Error']['Message']
        
        # Handle specific SES errors
        if error_code == 'MessageRejected':
            status_code = 400
            message = 'Email rejected - check email addresses and content'
        elif error_code == 'MailFromDomainNotVerifiedException':
            status_code = 400
            message = 'Sender email domain not verified in SES'
        elif error_code == 'ConfigurationSetDoesNotExistException':
            status_code = 500
            message = 'SES configuration error'
        else:
            status_code = 500
            message = f'SES error: {error_message}'
        
        return {
            'statusCode': status_code,
            'headers': headers,
            'body': json.dumps({
                'error': 'Email service error',
                'message': message,
                'aws_error_code': error_code
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': headers,
            'body': json.dumps({
                'error': 'Internal server error',
                'message': str(e)
            })
        }


# Test function for local development
def test_send_email():
    """Test function to verify email sending locally"""
    test_event = {
        'body': json.dumps({
            'receiver_email': 'test@example.com',
            'subject': 'Test Email',
            'body_text': 'This is a test email from the serverless API.'
        })
    }
    
    result = send_email(test_event, {})
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    test_send_email()