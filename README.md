# AusWoo

Australia Post bot for WooCommerce

## Overview

Automatically processes orders that have shipments scanned in your MyPost account.

Steps:
1. Looks for WooCommerce orders in "processing" state
2. Pulls your MyPost shipment list
3. For each processing order with order ID "{order_id}:
    1. Finds shipment containing "#{order_id}" in its name
    2. Adds a note to order with the Australia Post tracking ID
    3. Marks the order as completed

## Configure

You'll need the following:

* WooCommerce WordPress base URL
* WooCommerce API keys
* Australia Post MyPost login details

Set these details in environment variabes first, here's an example:

```
$ cat /etc/auswoo.conf
export WC_BASE_URL=https://www.example.com
export WC_KEY=ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export WC_SECRET=cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
export AUSPOST_USERNAME=login@example.com
export AUSPOST_PASSWORD=hunter2
```

## Build

Just use docker:

```
$ docker build -t timcinel/auswoo .
...
```

## Run

Just run it, baby.

```
$ source /etc/auswoo.conf
$ docker run --rm -ti -e WC_BASE_URL -e WC_KEY -e WC_SECRET -e AUSPOST_USERNAME -e AUSPOST_PASSWORD timcinel/auswoo /bin/bash process.sh
Requesting orders in 'processing' state...
Requesting all shipments from AusPost...
Looking for shipment matching order #4282...
Order #4282 matches shipment 6001811096XXX
Adding note to order...
Marking order as completed...
Looking for shipment matching order #4280...
Order #4280 matches shipment 60298032XXXXXX
Adding note to order...
Marking order as completed...
```
