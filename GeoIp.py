import socket
from ip2geotools.databases.noncommercial import DbIpCity

url = input("inserisci un'url:  ")
ip = socket.gethostbyname(url)
response = DbIpCity.get(ip, api_key='free' )
print("IP: ", ip)
print("CITTA: ", response.city)
print("Regione: ", response.region)
print("Nazione", response.country)