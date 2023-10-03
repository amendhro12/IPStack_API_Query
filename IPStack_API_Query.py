import argparse
import urllib.request
import json

def get_api_key_from_file(secret_file_path):
    with open(secret_file_path, 'r') as file:
        return file.read().strip()

def query_api(ip, api_key):
    base_url = f"http://api.ipstack.com/{ip}"
    query_string = urllib.parse.urlencode({'access_key': api_key})
    full_url = f"{base_url}?{query_string}"

    request = urllib.request.Request(full_url)

    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode('utf-8'))
        return data

def arg_parse():
    parser = argparse.ArgumentParser(description="Query the IPStack API")
    parser.add_argument("-i", "--ip_address", help="ip address to query")
    parser.add_argument("-s", "--secret_file", help="Path to file containing the API Key")
    args = parser.parse_args()
    return args

def main():
    args = arg_parse()
    api_key = None
    if args.secret_file:
        api_key = get_api_key_from_file(args.secret_file)

    try:
        result = query_api(args.ip_address, api_key)
        print(f"Latitude is {result['latitude']}, Longitude is {result['longitude']}")
    except Exception as e:
        print(f"Error querying the API: {e}")

if __name__ == "__main__":
    main()