# Polar Open AccessLink example application

This is an example application that uses the [Polar Open AccessLink] API.
With the [Polar Open AccessLink] you can access the training and daily activity data recorded with Polar devices.

## Prerequisites

* [Polar Flow](https://flow.polar.com) account
* Python 3 and pip related to Python 3

## Getting Started
#### 1. Create new API client 
 
Navigate to https://admin.polaraccesslink.com. Log in with your Polar Flow account and create a new client.

Use `http://localhost:5000/oauth2_callback` as the authorization callback domain for this example.
  
#### 2. Configure client credentials

Fill in your client id and secret in [config.yml] (example):
 
```
client_id: 57a715f8-b7e8-11e7-abc4-cec278b6b50a
client_secret: 62c54f4a-b7e8-11e7-abc4-cec278b6b50a
```
  
#### 3. Install python dependencies

```
pip3 install -r requirements.txt
```
## To run webapp example skip rest of the steps and launch
#### (skip this step and continue on the steps 4 and 5 if you want to run console example instead)
```
python exampleapp.py
```
After launching the app navigate to [http://localhost:5000/](http://localhost:5000/)
On the site there are buttons for authorization and reading current available data.
Webapp supports multible connected accounts,
connecting multible accounts requires you to be logged out of [https://flow.polar.com/](https://flow.polar.com/),
after which the authorization button will redirect to a log in page instead.
(Clicking the authorization button multible times,
while being logged in only re-logs your current account which will reveal a "Account Linked" box)

#### 4. Link user

User account needs to be linked to client application before client can get any user data. User is asked for authorization 
in Polar Flow, and user is redirected back to application callback url with authorization code once user has accepted the request.
 
To start example callback service, run:

```
python authorization.py
```

and navigate to `https://flow.polar.com/oauth2/authorization?response_type=code&client_id=<YOUR_CLIENT_ID>` to link user account.
After linking has been done you may close [authorization.py]. Linking saves access token and user id to [config.yml]

#### 5. Run example application
    
```
python accesslink_example.py
```

Once user has linked their user account to client application and synchronizes data from Polar device to Polar Flow, 
application is able to load data. Selecting 'Check available data' option from example application menu loads the 
synchronized data from Polar Flow and prints it on the screen.

[authorization.py]: ./authorization.py

[config.yml]: ./config.yml

[Polar Open AccessLink]: https://www.polar.com/accesslink-api/
