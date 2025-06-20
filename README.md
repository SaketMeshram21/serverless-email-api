# 📧 Serverless Email API using AWS SES

This project implements a **serverless email-sending API** using **AWS SES**, **AWS Lambda**, **API Gateway**, and the **Serverless Framework**. It provides a POST API endpoint to send emails using a verified SES identity.

---

## 🚀 Features

- 🔐 Secure Email Sending using AWS SES
- ⚙️ Built on AWS Lambda and API Gateway
- 🐍 Written in Python using Boto3
- ☁️ Easily deployable via Serverless Framework
- 🔁 Stateless and Scalable Architecture

---

## 🌐 Hosted Endpoint

> **POST** `https://3fk5epas6k.execute-api.ap-south-1.amazonaws.com/send-email`

⚠️ **Note:** You cannot open this link in a browser directly — it only accepts **POST** requests with JSON data.

---

## 📥 Sample API Request

### ✅ Endpoint

```
POST https://3fk5epas6k.execute-api.ap-south-1.amazonaws.com/send-email
```

### ✅ Headers

```
Content-Type: application/json
```

### ✅ JSON Body

```json
{
  "to": "recipient@example.com",
  "subject": "Test Email",
  "body": "Hello! This is a test email sent from my serverless project."
}
```

---

## 🧾 File Structure

```
serverless-email-api/
├── handler.py
├── serverless.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. A `POST` request is sent to the API Gateway endpoint.
2. Lambda function (from `handler.py`) is invoked.
3. Email parameters are extracted from the request.
4. AWS SES sends the email using verified email addresses.
5. A response is returned indicating success or failure.

---

## 🧪 Testing with curl

```bash
curl -X POST https://3fk5epas6k.execute-api.ap-south-1.amazonaws.com/send-email \
  -H "Content-Type: application/json" \
  -d '{
    "to": "recipient@example.com",
    "subject": "Test Email",
    "body": "This is a test email"
  }'
```

---

## 🛠 Tech Stack

- Python (Boto3)
- AWS Lambda
- AWS SES (Simple Email Service)
- API Gateway
- Serverless Framework

---

## 📌 Notes

- Your "To" and "From" emails **must be verified in SES** if using in sandbox mode.
- You can exit sandbox mode by applying for AWS SES production access.

---

## 📎 Author

**Saket Meshram**  
GitHub: [SaketMeshram21](https://github.com/SaketMeshram21)