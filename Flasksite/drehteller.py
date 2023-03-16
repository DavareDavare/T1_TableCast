import time
import sys
import json
import RPi.GPIO as GPIO

#Direkt aus den vorgegebenen Scripts genommen
LCD_RS = 14
LCD_E  = 15
LCD_DATA4 = 18
LCD_DATA5 = 23
LCD_DATA6 = 24
LCD_DATA7 = 25

LCD_WIDTH = 8 		# characters per line
LCD_LINE_1 = 0x00 	# Address of 1. Display line 
LCD_LINE_2 = 0xC0 	# Address of 2. Display line
LCD_CHR = GPIO.HIGH
LCD_CMD = GPIO.LOW
E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_send_byte(bits, mode):
	GPIO.output(LCD_RS, mode)
	GPIO.output(LCD_DATA4, GPIO.LOW)
	GPIO.output(LCD_DATA5, GPIO.LOW)
	GPIO.output(LCD_DATA6, GPIO.LOW)
	GPIO.output(LCD_DATA7, GPIO.LOW)
	if bits & 0x10 == 0x10:
	  GPIO.output(LCD_DATA4, GPIO.HIGH)
	if bits & 0x20 == 0x20:
	  GPIO.output(LCD_DATA5, GPIO.HIGH)
	if bits & 0x40 == 0x40:
	  GPIO.output(LCD_DATA6, GPIO.HIGH)
	if bits & 0x80 == 0x80:
	  GPIO.output(LCD_DATA7, GPIO.HIGH)
	time.sleep(E_DELAY)    
	GPIO.output(LCD_E, GPIO.HIGH)  
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, GPIO.LOW)  
	time.sleep(E_DELAY)      
	GPIO.output(LCD_DATA4, GPIO.LOW)
	GPIO.output(LCD_DATA5, GPIO.LOW)
	GPIO.output(LCD_DATA6, GPIO.LOW)
	GPIO.output(LCD_DATA7, GPIO.LOW)
	if bits&0x01==0x01:
	  GPIO.output(LCD_DATA4, GPIO.HIGH)
	if bits&0x02==0x02:
	  GPIO.output(LCD_DATA5, GPIO.HIGH)
	if bits&0x04==0x04:
	  GPIO.output(LCD_DATA6, GPIO.HIGH)
	if bits&0x08==0x08:
	  GPIO.output(LCD_DATA7, GPIO.HIGH)
	time.sleep(E_DELAY)    
	GPIO.output(LCD_E, GPIO.HIGH)  
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, GPIO.LOW)  
	time.sleep(E_DELAY)  

def config():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(LCD_E, GPIO.OUT)
	GPIO.setup(LCD_RS, GPIO.OUT)
	GPIO.setup(LCD_DATA4, GPIO.OUT)
	GPIO.setup(LCD_DATA5, GPIO.OUT)
	GPIO.setup(LCD_DATA6, GPIO.OUT)
	GPIO.setup(LCD_DATA7, GPIO.OUT)

def init():
	lcd_send_byte(0x33, LCD_CMD)
	lcd_send_byte(0x32, LCD_CMD)
	lcd_send_byte(0x28, LCD_CMD)
	lcd_send_byte(0x0C, LCD_CMD)  
	lcd_send_byte(0x06, LCD_CMD)
	lcd_send_byte(0x01, LCD_CMD)  

def message(message, line=1):
	if line == 1:
		lcd_send_byte(LCD_LINE_1, LCD_CMD)
	else:
		lcd_send_byte(LCD_LINE_2, LCD_CMD)

	message = message.ljust(LCD_WIDTH," ")
	for i in range(LCD_WIDTH):
	  lcd_send_byte(ord(message[i]),LCD_CHR)


if __name__ == '__main__':

	config()

	init()


if __name__ == '__main__':

    #Liest Inputs.Json
    with open("./inputs.json") as json_file:
        data = json.load(json_file)
	
    LED_GPIO = 20
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (LED_GPIO, GPIO.OUT)
    pwmLED = GPIO.PWM(LED_GPIO,100)
    #Setzt die LEDs auf Helligkeit
    pwmLED.start(int(data["Helligkeit"]))

    MOTOR_GPIO = 21
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (MOTOR_GPIO, GPIO.OUT)
    pwmMotor = GPIO.PWM(MOTOR_GPIO, 100)
    #Setzt Geschwindigkeit
    pwmMotor.start(int(data["Geschwindigkeit"]))

	#Holt den Text und speichert diesen in eine Variable
	#Und setzt ", " an das Ende, um die den letzten String mit dem ersten zu verbinden, da sonst kein Beistrich zwischen letztem und erstem String   
    input1 = data["Text"]
    input1 += ", "

	#Nimmt den langen Text String und splitted ihn in ein Array
    listZeilen = str.split(input1, ",")

    print(listZeilen)

    lst = []
    value = True

	#Für die Aufteilung auf die Displays
    for letter in input1:
        lst.append(letter)

    x = 0

	#Ist dafür da den String auf die zwei Displays aufzuteilen
    eight = ""
    
    
    while len(lst)>0:
      try:
		#setzt String mit 8 Buchstaben zusammen
        eight += lst[x]
        time.sleep(0.10)
        x += 1
		#Wenn 8 Zeichen im String sind wird der erste String auf das Display gesetzt
		#Und der "eight" String wieder zurückgesetzt um die zweite Hälfte zu speichern
        if(x==8):
           message(eight)
           eight = ""
	    #Wenn wieder neue 8 Buchstaben im String sind werden diese auf das Display gesetzt
		#Der erste Buchstabe an das Ende gesetzt und an erster Stelle gelöscht
		#"eight" wieder zurückgesetzt
        if(x==16):
            message(eight, 2)
            lst.append(lst[0])
            lst.pop(0)
            eight = ""
            x=0
	  #Strg + C
      except KeyboardInterrupt:
        print("\nbye")
        GPIO.cleanup()
        sys.exit()
