import psutil
from boltiot import Bolt

api_key = "a1d04b0c-01e4-4542-bafa-116090c8f0ae"
device_id = "BOLT293335"

cpu_Threshold = 0.4
clientId = Bolt(api_key, device_id)

interval = 5

def control_green_color(pin, value):
  response = clientId.digitalWrite(pin, value)

def control_red_color(pin, value):
  response = clientId.digitalWrite(pin,value)


while True:

  cpu_usage = psutil.cpu_percent( interval = interval )
  print("CPU usage :  ", cpu_usage)

  if cpu_usage > cpu_Threshold:
   control_green_color('0','LOW')
   control_red_color('1', 'HIGH')
   control_red_color('2', 'LOW') 

  else:
    control_green_color('0', 'HIGH')
    control_red_color('1', 'LOW')
  
  
