# Polar Open AccessLink example application

This is an example application that uses the [Polar Open AccessLink](https://www.polar.com/accesslink-api) API.
With the Polar Open AccessLink you can access the training and daily activity data recorded with Polar devices.

## Prerequisites

* [Polar Flow](https://flow.polar.com) account
* Python and pip

## Getting Started

#### 1. Create new API client 
 
Navigate to https://admin.polaraccesslink.com. Log in with your Polar Flow account and create a new client.

Use `http://localhost:5000/oauth2_callback` as the authorization callback domain for this example.
  
#### 2. Configure client credentials

Fill in your client id and secret in config.yml:

```
client_id: 57a715f8-b7e8-11e7-abc4-cec278b6b50a
client_secret: 62c54f4a-b7e8-11e7-abc4-cec278b6b50a
```
  
#### 3. Install python dependencies

```
pip install -r requirements.txt
```

#### 4. Link user 

User account needs to be linked to client application before client can get any user data. User is asked for authorization 
in Polar Flow, and user is redirected back to application callback url with authorization code once user has accepted the request.
 
To start example callback service, run:

```
python authorization.py
```

and navigate to 'https://flow.polar.com/oauth2/authorization?response_type=code&client_id=CLIENT_ID' to link user account.

#### 5. Run example application
    
```
python accesslink_example.py
```

Once user has linked their user account to client application and synchronizes data from Polar device to Polar Flow, 
application is able to load data. Selecting 'Check available data' option from example application menu loads the 
synchronized data from Polar Flow and prints it on the screen.
