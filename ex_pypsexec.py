from pypsexec.client import Client

host = '192.168.56.105'
user = 'vagrant'
pw = 'Winter12292021*'

c = Client(host, username=user, password=pw, encrypt=False)
c.connect()
c.create_service()
result = c.run_executable("cmd.exe",arguments="/c echo Hello World")
output = []
output = result[0]
print(result)