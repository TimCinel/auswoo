#!/bin/bash

set -o errexit
set -o nounset

# find all processing orders
>&2 echo "Requesting orders in 'processing' state..."
orders="$(curl --silent -X GET \
  "${WC_BASE_URL}/wp-json/wc/v2/orders?status=processing" \
  -u "${WC_KEY}:${WC_SECRET}" \
  | jq -r '.[] | .number')"

if [[ "${orders}" == "" ]]; then
    >&2 echo "No orders to process."
    exit 0
else
    >&2 echo "Orders found..."
fi

# find all shipments
>&2 echo "Requesting all shipments from AusPost..."
shipments="$(python auswoo.py \
  | jq '.[] | {"name": .nickname, "status": .trackStatus, "id": .id}'
)"

for order in ${orders}; do
    # find shipment matching order
    >&2 echo "Looking for shipment matching order #${order}..."
    match="$(echo "${shipments}" | jq -r ". | select (.name != null) | select(.name|contains(\"#${order}\")).id")"

    if [[ "${match}" == "" ]]; then
        echo "Order #${order} has no matching shipment"
    else
        echo "Order #${order} matches shipment ${match}"
        # add note to order
        >&2 echo "Adding note to order..."
        curl --silent -X POST \
          "${WC_BASE_URL}/wp-json/wc/v2/orders/${order}/notes" \
          -u "${WC_KEY}:${WC_SECRET}" \
          -H "Content-Type: application/json" \
          -d "{
          \"note\": \"Order sent. Australia Post Tracking: https://auspost.com.au/mypost/track/#/details/${match}\",
          \"customer_note\": true
        }" \
        > /dev/null

        # mark order as completed
        >&2 echo "Marking order as completed..."
        curl --silent -X PUT \
          "${WC_BASE_URL}/wp-json/wc/v2/orders/${order}" \
          -u "${WC_KEY}:${WC_SECRET}" \
          -H "Content-Type: application/json" \
          -d '{
          "status": "completed"
        }' \
        > /dev/null
    fi

done
