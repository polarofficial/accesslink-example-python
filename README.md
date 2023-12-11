# Polar Open AccessLink example applications

Here you can find simple Python example applications that use the [Polar Open AccessLink] API. With the [Polar Open AccessLink] you can access different data recorded with Polar devices.

## Prerequisites

* [Polar Flow](https://flow.polar.com) account
* [Python 3](https://www.python.org/downloads/) installed
* [PIP (Python package installer)](https://pip.pypa.io/en/stable/installation/) installed

## Getting Started

AccessLink API client is required in order to access the APIs. Following steps describe how the client is created and what other steps are required to access the data. Check out [Authentication section](https://www.polar.com/accesslink-api/#authentication) of the official documentation for more information about the authentication flow.

### 1. Create new API client

Navigate to https://admin.polaraccesslink.com. Log in with your Polar Flow account and create a new API client.

When asked, use `http://localhost:5000/oauth2_callback` as the authorization redirect URL for this example. **Please note that it's important to use correct callback url** so that the example applications work correctly.

You can edit your API client later and modify and/or add new authorization redirect URLs. Just make sure that with these examples the correct redirect URL is set as the default.
  
### 2. Configure client credentials

Fill in your client id and secret in [config.yml] (example below):

```bash
client_id: 57a715f8-b7e8-11e7-abc4-cec278b6b50a
client_secret: 62c54f4a-b7e8-11e7-abc4-cec278b6b50a
```
  
### 3. Install python dependencies

```bash
pip3 install -r requirements.txt
```

## Example web app

Web application is the easiest and fastest way to get started. It does the required user account linking and user registration automatically for logged in Polar Flow user once the user has authorized the access.

### Running the web application

```bash
python example_web_app.py
```

After launching the app navigate to [http://localhost:5000/](http://localhost:5000/)

* On the site there are buttons for authorization and reading current available data.
* Click "Link to authorize" to authorize the user access using Polar Flow credentials.
* Webapp supports multible connected accounts
  * In order to connect using another account, you need to be logged out of [https://flow.polar.com/](https://flow.polar.com/), after which the authorization button will redirect to a login page.
* Clicking the authorization button multible times, while being logged in only re-logs your current account which will reveal a "Account Linked" box.

After the account has been linked a new file [usertokens.yml] will be created for user's access token.

Web application has following functionality:

1) Link to authorize
    * Authenticates Polar Flow user, logout in Polar Flow to authenticate another user.
2) Read data
   * Get user information
   * Get data from non-transactional endpoints that do not discard the data after it has been fetched.
       * Data includes: exercises, sleep and nightly recharge.

## Example console app

Console application requires a bit more manual work than the web app. User account needs to be linked to client application and the user registered before client can get any user data. User is asked for authorization in Polar Flow, after which the user is redirected back to application callback url (which was previously set when API client was created) with the authorization code.

### Linking and registering the user

First we beed to start the callback service by running:

```bash
python authorization_callback_server.py
```

When the callback service is running, navigate to `https://flow.polar.com/oauth2/authorization?response_type=code&client_id=<YOUR_CLIENT_ID>` to link the user account and register the user. You should see Polar Flow login window if not logged in already. Otherwise your browser should be redirected to the callback url and the linking should be completed.

After linking has been done you may close [authorization_callback_server.py]. Access token and user id should be automatically saved to [config.yml] and the file should look similar to following:

```bash
access_token: YOUR_ACCESS_TOKEN
client_id: YOUR_CLIENT_ID
client_secret: YOUR_CLIENT_SECRET
user_id: YOUR_POLAR_USER_ID
```

### Running the console application

```bash
python example_console_app.py
```

Console application has following functionality:

1) Get user information
    * Get information about the user, this includes gender, first name, etc.
2) Get available transactional data
    * Get data from transactional endpoints that discard the data after it has been fetched.
    * Data includes: exercises, activity summary and physical information.
3) Get available non-transactional data
    * Get data from non-transactional endpoints that do not discard the data after it has been fetched.
    * Data includes: exercises, sleep and nightly recharge.
4) Revoke access token
    * Revoke current access token after which authentication needs to be done again.
5) Exit
    * Quit the application.

Once user has linked their user account to client application and synchronizes data from Polar device to Polar Flow, the example application is able to load the data.

## Troubleshooting

If you have any trouble running these example applications check the following.

1) Make sure that you are **using the correct python and pip** if you have multiple Python versions installed.
2) Make sure that you have **created and configured the API client** with your `client_id` and `client_secret` in the [config.yml] file.
3) Make sure that you have used **correct authorization redirect URL**. You can reconfigure your API client if needed.

[authorization_callback_server.py]: ./authorization_callback_server.py

[config.yml]: ./config.yml

[usertokens.yml]: ./usertokens.yml

[Polar Open AccessLink]: https://www.polar.com/accesslink-api/
