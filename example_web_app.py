#!/usr/bin/env python
from __future__ import print_function
import platform
if platform.system() == 'Windows':
    from asyncio.windows_events import NULL
from genericpath import exists
from pickle import NONE

import requests
from flask import Flask, request, redirect, render_template

from utils import load_config, save_config
from accesslink import AccessLink


CALLBACK_PORT = 5000
CALLBACK_ENDPOINT = "/oauth2_callback"

CONFIG_FILENAME = "config.yml"
TOKEN_FILENAME = "usertokens.yml"

REDIRECT_URL = "http://localhost:{}{}".format(CALLBACK_PORT, CALLBACK_ENDPOINT)

config = load_config(CONFIG_FILENAME)

accesslink = AccessLink(client_id=config['client_id'],
                        client_secret=config['client_secret'],
                        redirect_url=REDIRECT_URL)
app = Flask(__name__)

@app.route("/")
def index():
    status=request.args.get("status")
    return render_template("index.html", userid = config["client_id"], redirect_url=REDIRECT_URL, status=status)

@app.route("/data")
def data():
    tokens = token_db()
    alldata = []    
    for item in tokens["tokens"]:
        if item == None:
            continue
        exercisedata = accesslink.get_exercises(access_token=item["access_token"])
        sleepdata = accesslink.get_sleep(access_token=item["access_token"])
        rechargedata = accesslink.get_recharge(access_token=item["access_token"])
        userdata = accesslink.get_userdata(user_id=item["user_id"], access_token=item["access_token"])
        alldata.append( {"exercises": exercisedata,
                           "sleepdata": sleepdata,
                           "recharge": rechargedata,
                           "userdata": userdata })
    return render_template("data.html", alldata = alldata)

@app.route(CALLBACK_ENDPOINT)
def callback():
    """Callback for OAuth2 authorization request

    Saves the user's id and access token to a file.
    """

    #
    # Get authorization from the callback request parameters
    #
    authorization_code = request.args.get("code")

    #
    # Get an access token for the user using the authorization code.
    #
    # The authorization code is only valid for 10 minutes, so the access token
    # should be fetched immediately after the authorization step.
    #
    token_response = accesslink.get_access_token(authorization_code)

    #
    # Save the user's id and access token to the configuration file.
    #

    user_id = token_response["x_user_id"]
    accesstoken = token_response["access_token"]

    usertokens = token_db()

    usertokens["tokens"] = remove_oldtokens(array = usertokens["tokens"], newuserid= user_id)
    newtoken = {"user_id": user_id, "access_token":accesstoken}
    usertokens["tokens"].append(newtoken)
    save_config(usertokens, TOKEN_FILENAME)

    #
    # Register the user as a user of the application.
    # This must be done before the user's data can be accessed through AccessLink.
    #
    try:
        accesslink.users.register(access_token=accesstoken)
    except requests.exceptions.HTTPError as err:
        # Error 409 Conflict means that the user has already been registered for this client.
        # That error can be ignored in this example.
        if err.response.status_code != 409:
            return redirect("/?status=duplicatetokens")

    return redirect("/?status=ok")  

def remove_oldtokens(array , newuserid):
    res = []
    for item in array:
        if item == None:
            del item
            continue
        useritem = item["user_id"]
        usertoken = item["access_token"]
        if useritem != newuserid:
            res.append({"user_id": useritem,
                      "access_token":usertoken})
    return res

def token_db():
    usertokens = None
    if exists(TOKEN_FILENAME):
        usertokens = load_config(TOKEN_FILENAME)
    if usertokens == None:
        usertokens = {"tokens" : []}
    return usertokens

def main():
    print("Navigate to http://localhost:{port}/ for authorization.\n".format(port=CALLBACK_PORT))
    app.run(host='localhost', port=CALLBACK_PORT)

if __name__ == "__main__":
    main()

