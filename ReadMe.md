# Simple CRUD Project

This is a simple project that implements basic **CRUD (Create, Read, Update, Delete)** operations. 

A custom authentication decorator is also implemented as part of the project. While libraries could have been used for authentication, this implementation was done to gain experience in writing authentication code manually.

## How to Run

Run the project using the following command:
```bash
python app.py
```

## Caution

Before running the project, make sure to install the required libraries. Use the command:
```bash
pip install -r requirements.txt
```

## Application Execution Flow

1. **Register a New User:**
   - Use the POST API endpoint:
     ```
     http://localhost:8000/user
     ```
   - Example request body:
     ```json
     {
         "Name": "admin",
         "Password": "123",
         "Permission": "A"
     }
     ```
     - `Permission`: "A" is the highest level of authority.

2. **Get JWT Token:**
   - Use the GET API endpoint to retrieve a token:
     ```
     http://localhost:8000/user?Name=admin&Password=123
     ```

3. **Send Requests Using the Token:**
   - **Get a Specific Product:**
     ```
     http://127.0.0.1:8000/product?sno=4
     ```
   - **Get All Products:**
     ```
     http://127.0.0.1:8000/product/getall
     ```
   - **Add a Product (POST):**
     - Example POST API endpoint:
       ```
       http://127.0.0.1:8000/product
       ```
     - Example request body:
       ```json
       {
           "Name": "Coke",
           "Price": 80
       }
       ```
   - **Update a Product (PUT):**
     - Example PUT API endpoint:
       ```
       http://127.0.0.1:8000/product
       ```
     - Example request body:
       ```json
       {
           "sno": "2",
           "Name": "Coke",
           "Price": 80
       }
       ```
   - **Delete a Product:**
     - Example DELETE API endpoint:
       ```
       http://127.0.0.1:8000/product?sno=4
       ```
