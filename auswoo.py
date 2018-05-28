#!/bin/env python2.7

import requests
import os

def get_shipments(session):
    headers = {
        "Accept": "application/json", 
        "Referer": "https://auspost.com.au/mypost/track/", 
        "Origin": "https://auspost.com.au", 
    }
    return session.get('https://digitalapi.auspost.com.au/watchlist/shipments' )

def log_in(session, username, password):
    json = {
        "username": username,
        "password": password,
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "AP_APP_ID": "MYPOST",
        "Origin": "https://auspost.com.au",
    }

    return session.post('https://digitalapi.auspost.com.au/cssoapi/v2/session', json=json, headers=headers)

session = requests.Session()

log_in_r = log_in(session, os.environ['AUSPOST_USERNAME'], os.environ['AUSPOST_PASSWORD'])

get_shipments_r = shipments = get_shipments(session)

print(get_shipments_r.text)
