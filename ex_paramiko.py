from paramiko import SSHClient
import paramiko

client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.56.101', username='vagrant', password='vagrant')

stdin, stdout, stderr = client.exec_command('df -h') 
print(f'STDOUT: {stdout.read().decode("utf8")}')