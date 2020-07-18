# Sqreen interview
This code is here to address the Sqreen technical exercise

# Pre-requisites
## Host reachable on the internet
You need to deploy this code on a host that is reachable by Sqreen.

### Tip 
You can run it on your localhost and open a specific port on your Internet Service Provider box.   
Then you can check your public IP on <a href="https://www.whatismyip.com/" target="_blank">https://www.whatismyip.com/</a>

## Email server (SMTP)
You need to know the configuration of your email provider.
### Tip 
For Gmail:
```
EMAIL_SMTP_HOST="smtp.gmail.com"
EMAIL_SMTP_TLS_PORT=587
```

## Sqreen Account
1) Create an account at <a href="https://my.sqreen.com/" target="_blank">https://my.sqreen.com/</a>   
2) Fetch your organization token. From the Sqreen Dashboard, access Account Settings > Environments & Tokens.   
Your token begins with env_org_. Take note of the token.   
3) Configure sqreen.ini
````
# Replace the values for app_name and token with your own
cat > sqreen.ini <<EOF
[sqreen]
app_name: YOUR_APPLICATION_NAME
token: SQREEN_TOKEN
EOF
````

more info: <a href="https://docs.sqreen.com/python/installation/" target="_blank">https://docs.sqreen.com/python/installation/</a>

## Sqreen Webhooks
1) In the Sqreen Dashboard, from the application to connect, navigate to Settings > Integrations.   
2) In the Webhook pane, enter the URL. It's the public HOST of this app aka the destination to which you wish to POST messages from Sqreen (<b>http://<your_ip>:8000/api/notifications</b>).   
Retrieve the secret. This secret will be used to validate the message was emitted by Sqreen.  
<b>You will add this to your .env file as SQREEN_NOTIFICATIONS_KEY.</b>   
3) Test, then Save the configuration.   

more info: <a href="https://docs.sqreen.com/integrations/webhooks/" target="_blank">https://docs.sqreen.com/integrations/webhooks/</a>

## Environment variables
Copy .env.example to .env
Configure your .env file with the necessary information
````
SQREEN_NOTIFICATIONS_KEY="GET FROM SQREEN"
EMAIL_PASSWORD="TBD"
EMAIL_SMTP_HOST="TBD"
EMAIL_SMTP_TLS_PORT=587
EMAIL_SENDER="your@email.com"
EMAIL_RECEIVER="your@email.com"
````

# Backend for Sqreen notifications
## Build & Run with Docker
````
docker build . -t sqreen_backend
docker run -d -p 8000:8000 sqreen_backend
````

## From source
### Requirements
- python3.8
- pip

````
curl https://bootstrap.pypa.io/get-pip.py | python3
````

### Virtual Env (optional)
#### Install virtualenv
````
pip3 install virtualenv
python3 -m virtualenv venv
````
#### Activate virtual env
````
source venv/bin/activate
````
#### Deactivate virtual env
````
deactivate
````

### Install Libraries
````
pip3 install -r requirements.txt
````

### Tests
#### pytest
````
pytest
pytest -s # with debugging output
````

#### Coverage
````
pytest --cov=myproj test/  # check code coverage of the tests
coverage html
````

#### Watch mode
````
ptw
ptw -- -s # with debugging output
````

### Install
````
python3 setup.py install
````

### Run DEV
````
python3 run.py
````

### Run PROD
````
gunicorn wsgi:app -w 4 -b 0.0.0.0:8000
````