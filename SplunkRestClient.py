import http.client
from urllib.parse import urlencode, quote_plus
import sys

file_path = "./4Jan22_9am_12pm.json"
sys.stdout = open(file_path, "w")
from_date = "12/17/2021:01:00:00"
to_date = "12/17/2021:02:00:00"

conn = http.client.HTTPSConnection("mgmt.ceplog.eu.oss.volvoc3.com")
searchString = {'search' :'search "Returning list of T&C that needs consent" earliest="01/04/2022:09:00:00"  latest="01/04/2022:12:00:00"'}
payload = urlencode(searchString, quote_via=quote_plus)

headers = {
  'Authorization': 'Bearer eyJraWQiOiJzcGx1bmsuc2VjcmV0IiwiYWxnIjoiSFM1MTIiLCJ2ZXIiOiJ2MiIsInR0eXAiOiJzdGF0aWMifQ.eyJpc3MiOiJwcGVyem9uQHZvbHZvY2Fycy5jb20gZnJvbSBpcC0xMC0wLTEtMTY2Iiwic3ViIjoiX2JhdGNoLXVzZXJfY29tbWVyY2lhbC1kYXRhLXBtIiwiYXVkIjoiQ21tZXJjaWFsIERhdGEgdGVhbSBoZWxwaW5nIFZvbHZvSUQgd2l0aCBzdXBwb3J0IiwiaWRwIjoiU3BsdW5rIiwianRpIjoiZWMwMzNkZWIyNTk1OGQxNWU4OGFhNTBlMTQxMzE5MzE3OWU4YmM2NjU4Y2JkMjJkZjA0ZGZkMGE0Y2QxNDE0ZCIsImlhdCI6MTYzODI4NjE3OSwiZXhwIjoxNjY5ODIyMTc5LCJuYnIiOjE2MzgyODYyMzl9.9E-716GbXbt5QYzIZM1jZ8pW1U_nFaVGNKNBdl1wE97-UxKIcENkB7MaUg8L6FcK2R-GJy9aDPJTmYhVrZZWaw',
  'Content-Type': 'application/x-www-form-urlencoded'
}
#conn.request("POST", "/servicesNS/_batch-user_commercial-data-pm/search/search/jobs/export?output_mode=json", payload, headers)
conn.request("POST", "/servicesNS/_batch-user_commercial-data-pm/search/search/jobs/export?output_mode=json", payload, headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

