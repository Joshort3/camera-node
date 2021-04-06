from picamera import PiCamera
from time import sleep
import connect
import client

masked = 0
maskless = 0

while True:
    camera = PiCamera()
    #camera.start_preview()
    camera.capture('image.jpg')
    
    # Mask detection algorithm goes here
    
    connect.db_connect(masked, maskless)
    print("Database Connection Finished!!")
    client.server_connect('image.jpg')
    #sleep(3)
    #camera.stop_preview()
    break
    

