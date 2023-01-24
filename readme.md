# **Steps Installation**


### 1. Virtual Environment Activate
```
venv\Scripts\activate
```

### 2. Install requirements.txt
```
pip install -r /path/to/requirements.txt
```

### 3. Make Migrations
```
python manage.py makemigrations
python manage.py migrate
```

### 4. Migrate Error codes

```
python manage.py makeerrors
``` 

### 5. Create Super User

```
python manage.py createsuperuser
``` 

### 6. Test 

POST http://127.0.0.1:8000/api/v1/jsonrpc
```json
{
    "jsonrpc": "2.0",
    "id": 123,
    "method": "login",
    "params": {
        "username": "Admin",
        "password": "Password"
    }
}
```

### 6. Admin Dashboard 

Open in browser http://127.0.0.1:8000/admin
