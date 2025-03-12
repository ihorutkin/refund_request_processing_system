# Refund Request Processing System

The goal is to develop a web application using Django for submitting and processing refund 
requests for orders. The site should allow users to register, log in, and submit refund requests, 
while administrators should be able to review and manage incoming requests.

 - Clone the repository
 - Create and activate a virtual environment
 - Install dependencies: `pip install -r requirements.txt`
 - Configure environment variables (API keys, database settings)
 - Run migrations: `python manage.py migrate`
 - Create a superuser: `python manage.py createsuperuser`
 - Start the development server: `python manage.py runserver`

### How to load test dataset

 - Run: `python manage.py generate_test_refunds`

## Functionality

### To validate IBAN you have to pass url

```djangourlpath
api/validate-iban/<iban>
```

### Registration (Built-in Django authorization)

 - Log in form for authenticate
 - Log out
 - Sign up form for creation user
 - Reset password form

### Refund request list

 - List of all refund requests
 - Detail page for each refund request

### Admin page

 - Filtering for status, create date and country for RefundRequest
 - Import and Export logic
