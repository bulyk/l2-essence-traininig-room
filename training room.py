import serial
import time
from ahk import AHK
import pyautogui
# ahk = AHK()

# ahk.key_wait('/')





ser = serial.Serial('COM6', 9600)
time.sleep(1)



yes = pyautogui.locateOnScreen('special.png', confidence = 0.7)
yes_center = pyautogui.center(yes)
print(yes_center)


xReading = str(yes_center[0]-5)
yReading = str(yes_center[1])
xReading_byte = str.encode('m'+xReading)
yReading_byte = str.encode('n'+yReading)
# print((xReading_byte))
# print(type(xReading))


ser.write(b'o')
time.sleep(1)
ser.write(b'c')
time.sleep(1)

ser.write(xReading_byte)
time.sleep(.2)
ser.write(yReading_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(3)

train = pyautogui.locateOnScreen('training.png', confidence = 0.6)
time.sleep(1)
train_center = pyautogui.center(train)

xtrain = str(train_center[0]-5)
ytrain = str(train_center[1]+295)
xtrain_byte = str.encode('m'+xtrain)
ytrain_byte = str.encode('n'+ytrain)

ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)

ser.write(xtrain_byte)
time.sleep(.2)
ser.write(ytrain_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(3)

#OK
ok = pyautogui.locateOnScreen('ok.png', confidence = 0.7)
ok_center = pyautogui.center(ok)
xok = str(ok_center[0]-5)
yok = str(ok_center[1])
xok_byte = str.encode('m'+xok)
yok_byte = str.encode('n'+yok)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xok_byte)
time.sleep(.2)
ser.write(yok_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(3)

#Grown
grown = pyautogui.locateOnScreen('grown.png', confidence = 0.8)
grown_center = pyautogui.center(grown)
xgrown = str(grown_center[0]-5)
ygrown = str(grown_center[1])
xgrown_byte = str.encode('m'+xgrown)
ygrown_byte = str.encode('n'+ygrown)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xgrown_byte)
time.sleep(.2)
ser.write(ygrown_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(3)



#toi
toi = pyautogui.locateOnScreen('toi.png', confidence = 0.8)
toi_center = pyautogui.center(toi)
xtoi = str(toi_center[0]-5)
ytoi = str(toi_center[1])
xtoi_byte = str.encode('m'+xtoi)
ytoi_byte = str.encode('n'+ytoi)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xtoi_byte)
time.sleep(.2)
ser.write(ytoi_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(2)

# этаж1
st1 = pyautogui.locateOnScreen('st1.png', confidence = 0.7)
st1_center = pyautogui.center(st1)
xst1 = str(st1_center[0]-5)
yst1 = str(st1_center[1])
xst1_byte = str.encode('m'+xst1)
yst1_byte = str.encode('n'+yst1)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xst1_byte)
time.sleep(.2)
ser.write(yst1_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(1)

# tind
tind = pyautogui.locateOnScreen('tind.png', confidence = 0.8)
tind_center = pyautogui.center(tind)
xtind = str(tind_center[0]-5)
ytind = str(tind_center[1])
xtind_byte = str.encode('m'+xtind)
ytind_byte = str.encode('n'+ytind)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xtind_byte)
time.sleep(.2)
ser.write(ytind_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(3)

# teleport
teleport = pyautogui.locateOnScreen('teleport.png', confidence = 0.7)
teleport_center = pyautogui.center(teleport)
xteleport = str(teleport_center[0]-5)
yteleport = str(teleport_center[1])
xteleport_byte = str.encode('m'+xteleport)
yteleport_byte = str.encode('n'+yteleport)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xteleport_byte)
time.sleep(.2)
ser.write(yteleport_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(1)

# tind
toka = pyautogui.locateOnScreen('toka.png', confidence = 0.8)
toka_center = pyautogui.center(toka)
xtoka = str(toka_center[0]-5)
ytoka = str(toka_center[1])
xtoka_byte = str.encode('m'+xtoka)
ytoka_byte = str.encode('n'+ytoka)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xtoka_byte)
time.sleep(.2)
ser.write(ytoka_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(7)

# select
select = pyautogui.locateOnScreen('select.png', confidence = 0.85)
select_center = pyautogui.center(select)
xselect = str(select_center[0]-5)
yselect = str(select_center[1])
xselect_byte = str.encode('m'+xselect)
yselect_byte = str.encode('n'+yselect)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xselect_byte)
time.sleep(.2)
ser.write(yselect_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(2)

# power
power = pyautogui.locateOnScreen('power.png', confidence = 0.7)
power_center = pyautogui.center(power)
xpower= str(power_center[0]-5)
ypower = str(power_center[1])
xpower_byte = str.encode('m'+xpower)
ypower_byte = str.encode('n'+ypower)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xpower_byte)
time.sleep(.2)
ser.write(ypower_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(1)

# attack
attack = pyautogui.locateOnScreen('attack.png', confidence = 0.85)
attack_center = pyautogui.center(attack)
xattack= str(attack_center[0]-5)
yattack = str(attack_center[1])
xattack_byte = str.encode('m'+xattack)
yattack_byte = str.encode('n'+yattack)
ser.write(b'o')
time.sleep(1)
ser.write(b'o')
time.sleep(1)
ser.write(xattack_byte)
time.sleep(.2)
ser.write(yattack_byte)
time.sleep(.2)
ser.write(b'c')
time.sleep(12)

# нажать z
ser.write(b'z')
time.sleep(1)










    #   //ДВИЖЕНИЕ ПО У
    #   case 'n': y_coord = val; 
    #   for (int a = 1; a < 0.79*y_coord; a++)
    #   {
    #   Mouse.move(0, 2);
    #   }
    #   delay(500);
    #   break;
      
    #   //ДВИЖЕНИЕ ПО Х
    #   case 'm': x_coord = val; 
    #   for (int a = 1; a < 0.79*x_coord; a++)
    #   {
    #   Mouse.move(2, 0);
    #   }
    #   delay(500);
    #   break;

    #   case 'o': 
    #   for (int i = 0; i < 10; i++)
    #   {
    #   Mouse.move(nul, nul);
    #   // Serial.println(y_coord); 
    #   }
    #   delay(500);
      
    #   break;
      
    #   case 'c': Mouse.click();
    #   // Serial.println(y_coord); 
    #   delay(500);
    #   break;
    # }