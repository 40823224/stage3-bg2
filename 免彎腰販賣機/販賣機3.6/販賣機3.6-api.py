import sim as vrep
import math
import random
import time
import keyboard

print ('Start')

# Close eventual old connections
vrep.simxFinish(-1)
# Connect to V-REP remote server
clientID = vrep.simxStart('172.20.10.2', 19997, True, True, 5000, 5)

if clientID != -1:
    print ('Connected to remote API server')
    
    res = vrep.simxAddStatusbarMessage(
        clientID, "40823217&40823210",
        vrep.simx_opmode_oneshot)
    if res not in (vrep.simx_return_ok, vrep.simx_return_novalue_flag):
        print("Could not add a message to the status bar.")

    opmode = vrep.simx_opmode_oneshot_wait
    
    vrep.simxStartSimulation(clientID, opmode)
    ret,DOOR_handle=vrep.simxGetObjectHandle(clientID,"TD",opmode)
    ret,glass2_handle=vrep.simxGetObjectHandle(clientID,"TG",opmode)
    ret,Board_handle=vrep.simxGetObjectHandle(clientID,"P1",opmode)
    ret,Worm_2_handle=vrep.simxGetObjectHandle(clientID,"C1",opmode)
    ret,SP1_handle=vrep.simxGetObjectHandle(clientID,"TP1",opmode)
    ret,SP2_handle=vrep.simxGetObjectHandle(clientID,"TP2",opmode)
    ret,SP3_handle=vrep.simxGetObjectHandle(clientID,"TP3",opmode)
    ret,SP4_handle=vrep.simxGetObjectHandle(clientID,"TP4",opmode)
    ret,SP5_handle=vrep.simxGetObjectHandle(clientID,"TP5",opmode)
    ret,SP6_handle=vrep.simxGetObjectHandle(clientID,"TP6",opmode)
    ret,SP7_handle=vrep.simxGetObjectHandle(clientID,"TP7",opmode)
    ret,SP8_handle=vrep.simxGetObjectHandle(clientID,"TP8",opmode)
    ret,SP9_handle=vrep.simxGetObjectHandle(clientID,"TP9",opmode)
    ret,RO_1_handle=vrep.simxGetObjectHandle(clientID,"TRO1",opmode)
    ret,RO_2_handle=vrep.simxGetObjectHandle(clientID,"TRO2",opmode)
    ret,RO_3_handle=vrep.simxGetObjectHandle(clientID,"TRO3",opmode)
    ret,RO_4_handle=vrep.simxGetObjectHandle(clientID,"TRO4",opmode)
    ret,RO_5_handle=vrep.simxGetObjectHandle(clientID,"TRO5",opmode)
    ret,RO_6_handle=vrep.simxGetObjectHandle(clientID,"TRO6",opmode)
    ret,RO_7_handle=vrep.simxGetObjectHandle(clientID,"TRO7",opmode)
    ret,RO_8_handle=vrep.simxGetObjectHandle(clientID,"TRO8",opmode)
    ret,RO_9_handle=vrep.simxGetObjectHandle(clientID,"TRO9",opmode)
    ret,RO_10_handle=vrep.simxGetObjectHandle(clientID,"TRO10",opmode)
    #ret,main = vrep.simxGetObjectHandle(clientID, "main", opmode)
    while True:
    
        #keyboard "1" 
        if keyboard.is_pressed("1"):
            vrep.simxSetJointTargetVelocity(clientID,SP1_handle,100,opmode)
            #keyboard "2" 
        if keyboard.is_pressed("2"):
            vrep.simxSetJointTargetVelocity(clientID,SP2_handle,100,opmode)
        #keyboard "3" 
        if keyboard.is_pressed("3"):
            vrep.simxSetJointTargetVelocity(clientID,SP3_handle,100,opmode)
        #keyboard "4" 
        if keyboard.is_pressed("4"):
            vrep.simxSetJointTargetVelocity(clientID,SP4_handle,100,opmode)
        #keyboard "5" 
        if keyboard.is_pressed("5"):
            vrep.simxSetJointTargetVelocity(clientID,SP5_handle,100,opmode)
        #keyboard "6" 
        if keyboard.is_pressed("6"):
            vrep.simxSetJointTargetVelocity(clientID,SP6_handle,100,opmode)
        #keyboard "7" 
        if keyboard.is_pressed("7"):
            vrep.simxSetJointTargetVelocity(clientID,SP7_handle,100,opmode)
        #keyboard "8" 
        if keyboard.is_pressed("8"):
            vrep.simxSetJointTargetVelocity(clientID,SP8_handle,100,opmode)
        #keyboard "9" 
        if keyboard.is_pressed("9"):
            vrep.simxSetJointTargetVelocity(clientID,SP9_handle,100,opmode)
        
        #keyboard "space" 
        if keyboard.is_pressed("space"):
            vrep.simxSetJointTargetVelocity(clientID,SP1_handle,0,opmode)
            vrep.simxSetJointTargetVelocity(clientID,SP2_handle,0,opmode)
            vrep.simxSetJointTargetVelocity(clientID,SP3_handle,0,opmode)
            vrep.simxSetJointTargetVelocity(clientID,SP4_handle,0,opmode)
            vrep.simxSetJointTargetVelocity(clientID,SP5_handle,0,opmode)
            vrep.simxSetJointTargetVelocity(clientID,SP6_handle,0,opmode)
            vrep.simxSetJointTargetVelocity(clientID,SP7_handle,0,opmode)
            vrep.simxSetJointTargetVelocity(clientID,SP8_handle,0,opmode)
            vrep.simxSetJointTargetVelocity(clientID,SP9_handle,0,opmode)
        #keyboard "O" 
        if keyboard.is_pressed("O"):
            vrep.simxSetJointTargetVelocity(clientID,RO_1_handle,100,opmode)
            vrep.simxSetJointTargetVelocity(clientID,RO_2_handle,100,opmode)
            vrep.simxSetJointTargetVelocity(clientID,RO_3_handle,100,opmode)
            vrep.simxSetJointTargetVelocity(clientID,RO_4_handle,100,opmode)
            vrep.simxSetJointTargetVelocity(clientID,RO_5_handle,100,opmode)
            vrep.simxSetJointTargetVelocity(clientID,RO_6_handle,100,opmode)
            vrep.simxSetJointTargetVelocity(clientID,RO_7_handle,100,opmode)
            vrep.simxSetJointTargetVelocity(clientID,RO_8_handle,100,opmode)
            vrep.simxSetJointTargetVelocity(clientID,RO_9_handle,100,opmode)
            vrep.simxSetJointTargetVelocity(clientID,RO_10_handle,100,opmode)
        #keyboard "W" 
        if keyboard.is_pressed("W"):
            vrep.simxSetJointTargetVelocity(clientID,Worm_2_handle,10,opmode)
            vrep.simxSetJointTargetVelocity(clientID,Board_handle,2,opmode)
         #keyboard "E" 
        if keyboard.is_pressed("E"):
            vrep.simxSetJointTargetVelocity(clientID,Worm_2_handle,0,opmode)
            vrep.simxSetJointTargetVelocity(clientID,Board_handle,0,opmode)   
        #keyboard "S" 
        if keyboard.is_pressed("S"):
            vrep.simxSetJointTargetVelocity(clientID,Worm_2_handle,-10,opmode)
            vrep.simxSetJointTargetVelocity(clientID,Board_handle,-2,opmode)
        #keyboard "Z" 
        if keyboard.is_pressed("Z"):
            vrep.simxSetJointTargetVelocity(clientID,DOOR_handle,1.5,opmode)
        #keyboard "X" 
        if keyboard.is_pressed("X"):
            vrep.simxSetJointTargetVelocity(clientID,DOOR_handle,0,opmode)
        #keyboard "C" 
        if keyboard.is_pressed("C"):
            vrep.simxSetJointTargetVelocity(clientID,DOOR_handle,-1.5,opmode)  
        #keyboard "B" 
        if keyboard.is_pressed("B"):
            vrep.simxSetJointTargetVelocity(clientID,glass2_handle,5,opmode)
        #keyboard "N" 
        if keyboard.is_pressed("N"):
            vrep.simxSetJointTargetVelocity(clientID,glass2_handle,0,opmode)
        #keyboard "M" 
        if keyboard.is_pressed("M"):
            vrep.simxSetJointTargetVelocity(clientID,glass2_handle,-5,opmode)
        #keyboard "esc" 
        if  keyboard.is_pressed("esc"):
            vrep.simxStopSimulation(clientID, opmode)
            break
        
else:
    print ('Failed connecting to remote API server')
    print ('End')