#data = {"kornbot380@hotmail.com": {"category": [{"items": [{"title": "face_recog_7  ======> 127.0.0.1,0,5080,5081,Non"}, {"title": "Servo_control_12  ======> 127.0.0.1,5081,I2C,2"}, {"title": "Speech_recognition_13  ======> 127.0.0.1,1.04,th"}, {"title": "Stepper_motor_control_15  ======> 127.0.0.1,50,90"}, {"title": "BLDC_motor_control_16  ======> 127.0.0.1,20,45"}], "title": "Roboreactor_devian_14"}]}}
import json 
#data2 = {'kornbot380@hotmail.com': {'category': [{'title': 'Roboreactor_devian_14', 'items': [{'title': 'face_recog_8  ======> 127.0.0.1,0,5080,5081,Non'}, {'title': 'Servo_control_15  ======> 127.0.0.1,5081,I2C,2'}, {'title': 'Speech_recognition_13  ======> 127.0.0.1,1.04,th'}, {'title': 'Stepper_motor_control_15  ======> 127.0.0.1,50,90'}, {'title': 'BLDC_motor_control_16  ======> 127.0.0.1,20,45'}]}]}}
#{'category': [{'items': [{'title': 'face_recog_7  ======> 127.0.0.1,0,5080,5081,Non'}, {'title': 'Servo_control_12  ======> 127.0.0.1,5081,I2C,2'}, {'title': 'Speech_recognition_13  ======> 127.0.0.1,1.04,th'}, {'title': 'Stepper_motor_control_15  ======> 127.0.0.1,50,90'}, {'title': 'BLDC_motor_control_16  ======> 127.0.0.1,20,45'}], 'title': 'Roboreactor_devian_14'}]}

data2 = {"kornbot380@hotmail.com":{"category":[{'title': 'Roboreactor_devian_15', 'items': [{'title': 'face_recog_7  ======> 127.0.0.1,0,5080,5081,Non'}, {'title': 'Servo_control_12  ======> 127.0.0.1,5081,I2C,2'}, {'title': 'Speech_recognition_13  ======> 127.0.0.1,1.04,th'}, {'title': 'Stepper_motor_control_15  ======> 127.0.0.1,50,90'}, {'title': 'BLDC_motor_control_16  ======> 127.0.0.1,20,45'}]}]}}
data = {"kornbot380@hotmail.com": {"category": [{"items": [{"title": "face_recog_7  ======> 127.0.0.1,0,5080,5081,Non"}, {"title": "Servo_control_12  ======> 127.0.0.1,5081,I2C,2"}, {"title": "Speech_recognition_13  ======> 127.0.0.1,1.04,th"}, {"title": "Stepper_motor_control_15  ======> 127.0.0.1,50,90"}, {"title": "BLDC_motor_control_16  ======> 127.0.0.1,20,45"}], "title": "Roboreactor_devian_14"}, {"items": [{"title": "face_recog_7  ======> 127.0.0.1,0,5080,5081,Non"}, {"title": "Servo_control_12  ======> 127.0.0.1,5081,I2C,2"}, {"title": "Speech_recognition_13  ======> 127.0.0.1,1.04,th"}, {"title": "Stepper_motor_control_15  ======> 127.0.0.1,50,90"}, {"title": "BLDC_motor_control_16  ======> 127.0.0.1,20,45"}], "title": "Roboreactor_devian_12"}]}}
output2 = data2.get('kornbot380@hotmail.com').get('category')
print(output2)
output1 = data.get('kornbot380@hotmail.com').get('category') # main database of the machine 
project_name = "Roboreactor_devian_15"
if output2[0] in output1:

       print("Found matched info inside the list now checking the project element data")

if output2[0] not in output1:
       print("Checking new data inserting")       
       project_data = {}
       for p in output1:
                   print(p.get('title'),p.get('items')) 
                   project_data[p.get('title')] = p.get('items')
       print(project_data)         
       # Add the project if found inside the list of new dictionary data    
       if project_name not in list(project_data):
                        
                     data['kornbot380@hotmail.com'].get('category').append(data2.get('kornbot380@hotmail.com').get('category')[0])
                     print("New project append",data)
                     output1 = data.get('kornbot380@hotmail.com').get('category')
                     for rt in list(output1):
                        print("Data_elem",rt.get('title'),rt.get('items'))
                           
                        #if rt == 'items':
                        #      for rf in  output1.get(rt):
                        #            print(rf.get('title').split(" ")[0])   
       if project_name in list(project_data):              
       
                   if project_name == p.get('title'):
                                  p.get('items').clear() 
                                  for t in output2:
                                         elem = t.get('items')
                                         for data in elem:
                                                   p.get('items').append(data)
                   print("Output result change",output1)
                   output1.append(output1[0])
                   print("Data manipulator",output1)
                   print("Seeking element")  
                   print(len(output1))
                   print("Complete list",output1[0])
                   for rt in list(output1[0]):
                        print(output1[0].get(rt))
                        if rt == 'items':
                              for rf in  output1[0].get(rt):
                                    print(rf.get('title').split(" ")[0])     
                
  
                   print(data)
       
