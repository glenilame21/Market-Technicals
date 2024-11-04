import requests

def get_spot_data(spot_key, fields, from_date, to_date, currency):
    # Read token from file
    with open('access_token.txt', 'r') as f:
        token = f.read().strip()
    
    # headers
    headers = {
        'Authorization': f'Bearer {token}',
        'AcceptEncoding': 'deflate' 
    }

    # Construct URL
    url = f"https://api.montelnews.com/spot/getprices?SpotKey={spot_key}&Fields={fields}&FromDate={from_date}&ToDate={to_date}&Currency={currency}&SortType=ascending"
    
    # Make the request
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        data = response.json()
        if 'Elements' in data and isinstance(data['Elements'], list):
            return data['Elements']
        else:
            print("Unexpected JSON structure")
            return None
    else :
        print("Error: ", response.status_code)
        return None