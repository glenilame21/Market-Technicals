import requests

def get_volume(token):

    symbolkey = input("Enter symbol key: ")
    fromtime = input("From: yyyy-MM-ddTHH:mm:ss")
    totime = input("To: yyyy-MM-ddTHH:mm:ss")
    Sorting = input("Sorting: ")

    url = f"https://api.montelnews.com/derivatives/trade/get?SymbolKey={symbolkey}&FromTime={fromtime}&ToTime={totime}&SortType={Sorting}"

    headers = {
        'Authorization': f'Bearer {token}',
        'AcceptEncoding': 'deflate'
    }


    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        print(response.json())
        #return response.json()
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None


    