import requests

with open('access_token.txt', 'r') as f:
    token = f.read().strip()

def get_spot_metadata(token):

    url = "https://api.montelnews.com/spot/getmetadata"
    
    headers = {
        'Authorization': f'Bearer {token}',
        'AcceptEncoding': 'deflate' 
    }
    
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code == 200:
        data = response.json()
        if 'Elements' in data and isinstance(data['Elements'], list):
            return data['Elements']
        else:
            print("Unexpected JSON structure")
            return None
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None