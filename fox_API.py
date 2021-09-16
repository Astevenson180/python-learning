import requests
import json

data = requests.get("https://randomfox.ca/floof/").json()


writeFile = open('fox_saved.json', 'w')

writeFile.write(str(data))
writeFile.close()

print(data)
