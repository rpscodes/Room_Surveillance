
import time
 

from seeed_dht import DHT
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from picamera import PiCamera
from time import sleep
from datetime import datetime
from twilio.rest import Client



def main():
    lightsensor = GroveLightSensor(0)
    i=0
    while lightsensor.light > 200:
        i=i+1
        camera = PiCamera()
                
        now1 = datetime.now()
        camera.capture('Your_File_Location/image{}.jpg'.format(now1))
                
        camera.close()
        sleep(5)
                #Twilio SMS notification
        if i == 1:
            account_sid = 'Enter Account Dis Here' 
            auth_token = 'Enter Auth token here' 
            client = Client(account_sid, auth_token) 
 
            message = client.messages.create( 
                                        messaging_service_sid='Enter Messaging Sid here',  
                                        body='Suspicious Activity in Study at {}'.format(now1),      
                                        to='+Enter the phone number to send the message to' 
                                        ) 
            i=2
if __name__ == '__main__':
    main()
