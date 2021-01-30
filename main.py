import requests
import json
import os

LIMIT = 100


def main():
    after = 0
    HAPI_KEY = os.environ.get("HAPI_KEY")
    url = f"https://api.hubapi.com/crm/v3/objects/companies/search?hapikey={HAPI_KEY}"
    headers = {"Content-Type": "application/json"}
    count = 1
    companies = []
    while count > after:
        data = {
            "limit": LIMIT,
            "after": after
        }

        response = requests.post(url, headers=headers, json=data)
        result = json.loads(response.content)
        count = result['total']
        after += LIMIT

        for company in result['results']:
            if company['properties']['name']:
                companies.append(company['properties']['name'])
    print(companies)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
