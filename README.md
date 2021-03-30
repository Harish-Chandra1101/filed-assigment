# Filed-assigment

## Requirements
* Python 3.x
* MySQL database

## Setup

### Step 1:
    Clone the repostiory
### Step 2:
    - Create a virtual environment inside the /server folder
        Command: virtualenv venv
    - Activate the virtualenv (For windows: ./venv\Scripts\activate
        For linux/mac: ./venv/bin/activate)
        
### Step 3 (Install requirements):
    Run the following command
    pip install -r requirements.txt

### Step 4 (Creating config file):
    - Create a file conf.py in server/weather_reporting folder
    - Copy the variables from conf_example.py and fill the respective values

### Step 5 (Migrations):
    - In the terminal or command prompt go to the server folder
    - Run the following command to create the migrations in the database
        python manage.py migrate

### Step 6 (Run backend server)
    - Run the django server using the following command
        python manage.py runserver 127.0.0.1:8000

### Step 7 (Use the postman collection to test the APIs)
    - Open Postman application, click on File > Import and select the postman collection file
