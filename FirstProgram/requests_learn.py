import requests
url = "https://mail.google.com/mail/u/0/#inbox"
r = requests.get(url)
print("Staus: ", r.status_code)

url = 'https://www.youtube.com'
r = requests.get(url)
print(r.status_code)