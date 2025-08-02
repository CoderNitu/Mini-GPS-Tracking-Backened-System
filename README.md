# 🛰️ Mini GPS Tracking Backend System

Build a Django REST Framework-based backend system that allows authenticated devices to register, send real-time location updates, and view historical location data.

---

## 🚀 Project Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/CoderNitu/Mini-GPS-Tracking-Backened-System.git
cd Mini-GPS-Tracking-Backened-System

```

### 2. Create and activate a virtual environment

```
python -m venv env
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate
```
### 3.  Install dependencies

```
pip install -r requirements.txt
```
### 4. Configure environment variables
Create a .env file based on the .env.example:

```
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Run migrations

```
python manage.py migrate
```
### 6.  Create superuser (optional, for admin access)

```
python manage.py createsuperuser
```
### 7. Run the server

```
python manage.py runserver
```

## 🧠 Design Decisions

🔐 Used Token Authentication from DRF for device-level security.

🗺️ Device and Location models for clean tracking logic.

🧪 API tested using Postman.

🔄 Implemented throttling to limit frequent location submissions.

📦 Pagination enabled for listing devices or location history.

## 📡 API Endpoint Summary

| Method | Endpoint                  | Description                      | Auth Required |
| ------ | ------------------------- | -------------------------------- | ------------- |
| POST   | `/devices/register/`      | Register a new device            | ❌ No          |
| POST   | `/locations/`             | Submit a device's location       | ✅ Yes (Token) |
| GET    | `/locations/<device_id>/` | Get location history of a device | ✅ Yes         |
| GET    | `/devices/`               | List all registered devices      | ✅ Yes         |

## 🔐 Authentication

Use Token Authentication.

Register a device → get a token in response.

Use this token in the Authorization header for other requests:

```
Authorization: Token <your_token>
```

## 📬 Sample Payloads & Responses

### 1. Register Device (No Auth)
POST /devices/register/

```
📬 Sample Payloads & Responses
1. Register Device (No Auth)
POST /devices/register/
```
Response:

```
{
  "device_id": "DEVICE123",
  "device_name": "Truck A",
  "token": "abc123tokenvalue"
}
```
### 2. Submit Location (Token Auth)
POST /locations/

```{
  "latitude": 26.9124,
  "longitude": 75.7873
}
```
#### Header:
Authorization: Token abc123tokenvalue

Response:

```
{
  "device": "DEVICE123",
  "latitude": 26.9124,
  "longitude": 75.7873,
  "timestamp": "2025-08-02T12:00:00Z"
}
```

### 3. Get Location History
GET /locations/DEVICE123/

#### Header:
Authorization: Token abc123tokenvalue

Response:

```
[
  {
    "latitude": 26.9124,
    "longitude": 75.7873,
    "timestamp": "2025-08-02T12:00:00Z"
  },
  ...
]
```
## 📬 Postman Collection
A complete Postman collection is included to demonstrate the usage of all API endpoints.

🔗 Download & Use
You can import the collection into Postman using the following steps:

Open Postman.

Click on "Import" at the top left.

Select the file:
gps_api_collection.json (included in the project root).

The collection will appear in your workspace.

### 📁 Collection Includes:

Register Device (POST /devices/register/)

Submit Location (POST /locations/)

Get Device List (GET /devices/)

Get Location History (GET /locations/<device_id>/)

Each request includes:

Required headers (e.g., Authorization: Token ...)

Sample request bodies (JSON)

Sample responses

## 🎥 Demo Video

## ☁️ Deployment 
