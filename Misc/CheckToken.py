import requests

def is_token_valid(token):
    url = f"https://api.montelnews.com/spot/getprices?SpotKey=1&Fields=hours,base,peak&FromDate=2023-10-01&ToDate=2023-10-31&Currency=EUR&SortType=ascending"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code == 200:
        print("Token is valid.")
        return True
    else:
        print("Token is invalid.")
        return False