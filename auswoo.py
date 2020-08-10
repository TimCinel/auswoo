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
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "AP_APP_ID": "MYPOST",
        "Origin": "https://auspost.com.au",
        "Referer": "https://auspost.com.au/auth/login?caller=ACCOUNT_GLOBAL_HEADER&product=MYPOST_CONSUMER&channel=WEB",
        "Connection": "keep-alive",
        "AP_APP_ID": "MYPOST",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
        "Content-Type": "application/json",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    }

    return session.post('https://digitalapi.auspost.com.au/cssoapi/v2/session', json=json, headers=headers)

session = requests.Session()

log_in_r = log_in(session, os.environ['AUSPOST_USERNAME'], os.environ['AUSPOST_PASSWORD'])

get_shipments_r = shipments = get_shipments(session)

print(get_shipments_r.text)
