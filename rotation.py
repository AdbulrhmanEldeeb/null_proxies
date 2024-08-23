import requests
from tqdm import tqdm

# List of proxies
ip_port_list = [
    "194.182.187.78:3128",
    "72.167.133.167:8082",
    "188.166.197.129:3128",
    "82.102.10.253:80",
    "219.65.73.81:80",
    "154.236.177.100:1977",
    "81.200.149.178:80",
    "207.148.71.74:80",
    "198.49.68.80:80",
    "83.68.136.236:80",
    "35.209.198.222:80",
    "37.27.6.46:80",
    "172.232.180.108:80",
    "181.188.27.162:8080",
    "217.160.99.39:80",
    "162.223.90.130:80",
    "162.223.89.34:80",
    "165.232.129.150:80",
    "107.175.179.52:80",
    "23.247.136.245:80"
]

# Test URL to check the proxy
test_url = "http://httpbin.org/ip"

# Define headers (optional)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}

# List to hold valid proxies
valid_proxies = []

print("Checking proxies...")

for ip_port in tqdm(ip_port_list):
    proxy = {"http": f"http://{ip_port}", "https": f"http://{ip_port}"}

    try:
        response = requests.get(test_url, headers=headers, proxies=proxy, timeout=5)
        if response.status_code == 200:
            valid_proxies.append(ip_port)
            print(f"Proxy {ip_port} is valid.")
        else:
            print(f"Proxy {ip_port} returned status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Proxy {ip_port} failed. Error: {e}")

print("\nValid proxies:")
for valid_proxy in valid_proxies:
    print(valid_proxy)
