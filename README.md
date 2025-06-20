# 📧 Serverless Email API using AWS SES

A lightweight, scalable, and cost-effective email-sending REST API built using **AWS SES**, **AWS Lambda**, **API Gateway**, and the **Serverless Framework**. Ideal for triggering transactional emails securely via a POST request — no need to manage servers.

---

## ✨ Features

- ✅ **Serverless** architecture — no EC2 or manual provisioning
- ✅ **AWS SES integration** for reliable email delivery
- ✅ **Python-based Lambda** function
- ✅ **API Gateway POST endpoint** (`/send-email`)
- ✅ **Simple JSON payload**
- ✅ **Secure and cost-efficient** (pay per use)

---

## 🚀 Live Endpoint

> **POST** `https://3fk5epas6k.execute-api.ap-south-1.amazonaws.com/send-email`

> ⚠️ This is a **POST-only** endpoint. You **cannot open it in a browser** — use tools like Postman or `curl`.

---

## 📥 API Usage

### ✅ Request

**Method**: `POST`  
**URL**: `https://3fk5epas6k.execute-api.ap-south-1.amazonaws.com/send-email`  
**Headers**:  
```http
Content-Type: application/json
