# Test-Project---Car-Controlled-by-a-Web-Application

### Video Link:
https://www.youtube.com/embed/nhjSveXiptY

### Project Description 
- a robot car controlled using web browser. 
### Parts
   - Raspberry Pi with WiFi 
   - Chassis Rectangle 4WD with motors 
   - Motor Driver L298D
   
### Connections
Raspberry Pi controls the servos via the PWM module and the driver by setting the pins on the H-bridge and providing PWM signal
  
  #### Schematic:
   ![image_VPzvSFuoSL](https://user-images.githubusercontent.com/36682645/56653784-bd5eb300-668e-11e9-8d4a-e126cba52a18.png)
    
   controller’s outputs are connected to the H-bridge, and the PWM signal is used to set the speed of the motors. 
   The RPi-pins are also connected to the H-bridge. 
   The states on the appropriate pins will determine the direction of rotation of the motors. 
   
### below are some illustrative photos of the whole car
![image_fffiELLAn5](https://user-images.githubusercontent.com/36682645/56653607-44f7f200-668e-11e9-8ed0-24498cd4f1eb.png)    
    
    
    
### Web Page

![Untitled](https://user-images.githubusercontent.com/36682645/56653658-66f17480-668e-11e9-88ca-f29181dedd06.png)
