import requests
import sys
url=input("Enter URL: ")
if not url.endswith("/"):
    url=url+"/"
try:
    r=requests.get(url,timeout=5)
except requests.exceptions.Timeout:
    print("Site took too long")
    sys.exit()

print(f"The Status Code of {url}: ", r.status_code)
print(f"The Server of {url}: ",r.headers.get('Server'))
print(f"The Content type of {url}: ",r.headers.get('Content-Type'))
print(f"The Content Length of {url}: ",r.headers.get('Content-Length'))

try:
    print(f"JSON Format:\n",r.json())
except:
    print("JSON file was not returned")

with open("file.html","w",encoding='UTF-8') as f:
    f.write(r.text)
    print("HTML saved ")
