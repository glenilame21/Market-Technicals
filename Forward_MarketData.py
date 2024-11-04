import requests
import Generate_New_Token
import pandas as pd

def get_OHLC(token):
    # Ask the user for the required parameters
    symbolkey = input("Enter symbol key: ")
    from_date = input("Enter from date (YYYY-MM-DD): ")
    to_date = input("Enter to date (YYYY-MM-DD): ")

    headers = {
        'Authorization': f'Bearer {token}',
        'Accept-Encoding': 'deflate'
    }

    # Construct the full URL with all specified fields
    url = (f"https://api.montelnews.com/derivatives/ohlc/get?"
           f"symbolKey={symbolkey}"
           f"&fields=TickerSymbol&fields=ContractName&fields=Date&fields=Open"
           f"&fields=High&fields=Low&fields=Close&fields=Settlement"
           f"&fields=Volume&fields=OpenInterest"
           f"&fromDate={from_date}"
           f"&toDate={to_date}"
           f"&sortType=ascending"
           f"&insertElementsWhenDataMissing=never"
           f"&continuous=true")

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 401:
        token = Generate_New_Token.generate_new_token()
        print("Token expired. Generating new token...")
        print("Fetching Data again...")
        return get_OHLC(token)
    else:
        data = response.json()
        data = data['Elements']
        df = pd.DataFrame(data)
        return df
        


