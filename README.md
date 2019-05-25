# LeaveApp
Leave application that allows an employee to apply for a leave

# How to Install Dependencies
pip3 install virtualenv <br/>
mkdir -p ~/.virtualenvs <br/>
pip3 install virtualenvwrapper <br/>
mkvirtualenv leave_env <br/>
If the virtual environment is not activated, type "workon leave_env" <br/> 
pip3 install -r requirements.txt

# Setup the application
To create DB model: python manage.py makemigrations leave_manager <br/>
python manage.py migrate <br/>
python manage.py createsuperuser <br/>
Follows the prompts to create the user account up until it is successfully created <br/>

# How to Run Application
cd leaveApp <br/>
cd leave <br/>
workon leave_env <br/>
python manage.py runserver

# Creating access token to use to access the services
Open browser or api testing application: http://127.0.0.1:8000/api/auth/access-token/ <br/>
Prompted for username and password <br/>
When successfully created, an access-token and refresh-token will be created <br/>

# Accessing the web services

Open api testing application(i.e. Postman)
Type the following address in the request url section: http://127.0.0.1:8000/api <br/>
Set request authorisation using the generated access-token
available services: <br/>
1. /api/employee/ - accept both get and post request <br/>
  - GET: retrieve employee given the emp_number.<br/>
  - POST: create/update employee account.<br/>
2. /api/leave/ - accept both get and post request <br/>
  - GET: retrieve employee leave request. <br/>
  - POST: create/update employee leave request. <br/>
# Running test cases using coverage
coverage run manage.py test <app_name> -v 2



