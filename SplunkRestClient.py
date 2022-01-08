import http.client
from urllib.parse import urlencode, quote_plus
import sys

file_path = "./output.json"
sys.stdout = open(file_path, "w")
from_date = "12/17/2021:01:00:00"
to_date = "12/17/2021:02:00:00"

conn = http.client.HTTPSConnection("BASEURL.com")
searchString = {'search' :'search "Returning list of T&C that needs consent" earliest="01/04/2022:09:00:00"  latest="01/04/2022:10:00:00"'}
payload = urlencode(searchString, quote_via=quote_plus)

headers = {
  'Authorization': 'Bearer YOUR_TOKEN',
  'Content-Type': 'application/x-www-form-urlencoded'
}
conn.request("POST", "/REL_URL/search/search/jobs/export?output_mode=json", payload, headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

