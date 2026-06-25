import subprocess
import time
import pyautogui

# Give time to make sure the app window is focused
time.sleep(2)

# # Hold the Alt key and press 'F'
pyautogui.hotkey('alt', 'L')
time.sleep(2)
pyautogui.press('j')	
time.sleep(2)
pyautogui.hotkey('alt', 'N')	#Opens New Procedure
time.sleep(2)
import ImportCPT

##pyautogui.write ('ProcNew2')
##pyautogui.press('tab')81002Urinalysis non-automateda1105a
##pyautogui.write ('Bot Code')
pyautogui.press('tab')
###Decides code type
pyautogui.press('tab')
pyautogui.write ('a') #account code
pyautogui.press('tab')
pyautogui.write ('1') #Type of service
pyautogui.press('tab')
pyautogui.write ('10') #POS
pyautogui.press('tab')
pyautogui.write ('5') #TTDproc
pyautogui.press('tab')
pyautogui.write ('a') #
pyautogui.press('tab')
pyautogui.write ('Aetna') #Dont bill
pyautogui.press('tab')
pyautogui.write ('Cigna') #only bill
pyautogui.press('tab')
pyautogui.write ('MM') # mod 1
time.sleep(.5)
pyautogui.press('tab')
time.sleep(.5)
pyautogui.write ('MM') # mod 2
pyautogui.press('tab')
time.sleep(.5)
pyautogui.write ('Mb')
time.sleep(.5)# mod 3
pyautogui.press('tab')
time.sleep(.5)
pyautogui.write ('MM') # mod 4
pyautogui.press('tab')
###----------create new revenue code
##import pyautogui
##
##pyautogui.press('f8')
##time.sleep(3)
##pyautogui.write ('bck') #Rev code
##pyautogui.press('tab')
##pyautogui.press('tab')
##time.sleep(1)
##pyautogui.write ('bitcoin') # Rev desc
##time.sleep(1)
##pyautogui.hotkey('alt', 's')
pyautogui.press('tab')
pyautogui.write ('2') # Default unit
pyautogui.press('tab')
pyautogui.write ('3') # NDC
pyautogui.press('tab')
pyautogui.write ('10') # NDC uit price
pyautogui.press('tab')
pyautogui.write ('G') # ndc measur
time.sleep(2)
pyautogui.press('tab')
pyautogui.write ('a') # 
pyautogui.press('tab')
pyautogui.write ('100') # PSA
pyautogui.press('tab')
time.sleep(2)
##import random
##
##def get_fun_quote():
##    quotes = [
##        "Created by Kane — automation wizardry in action",
##        "Powered by Kane’s unstoppable Python energy",
##        "Another flawless execution courtesy of Kane",
##        "Kane coded this… and yes, it’s awesome",
##        "Automation level: Kane-tier excellence",
##        "Running smoother than Kane’s morning coffee",
##        "If this works, thank Kane. If not… still thank Kane",
##        "Kane’s script strikes again",
##        "Precision brought to you by Kane",
##        "Kane: turning chaos into clean data since forever"
##    ]
##    return random.choice(quotes)
##pyautogui.write(get_fun_quote())

##pyautogui.press('tab')
##import pyautogui
##import time
##
### Optional: small delay for the app to catch up
##time.sleep(2)

##for _ in range(7):
##    pyautogui.press('tab')
##    time.sleep(0.5)  # Slight pause between tabs (optional)
##import pyautogui
time.sleep(2)
import random
import pyautogui
import time

def get_fun_quote():
    quotes = [
        "Created by Kane — automation wizardry in action",
        "Powered by Kane’s unstoppable Python energy",
        "Another flawless execution courtesy of Kane",
        "Kane coded this… and yes, it’s awesome",
        "Automation level: Kane-tier excellence",
        "Running smoother than Kane’s morning coffee",
        "If this works, thank Kane. If not… still thank Kane",
        "Kane’s script strikes again",
        "Precision brought to you by Kane",
        "Kane: turning chaos into clean data since forever"
    ]
    return random.choice(quotes)

print("Script started")
# time.sleep(5)
quote = get_fun_quote()
print("Quote to type:", quote)
pyautogui.write(quote)
print("Done typing")

#pyautogui.press('space')

time.sleep(1)
pyautogui.hotkey('alt', 'a')	#changes to amount tab
pyautogui.write ('1200') # amount
pyautogui.hotkey('alt', 's')
#------------------------------Create an adjustment------------------------------
time.sleep(1)
pyautogui.hotkey('alt', 'N')	#Opens New Procedure
time.sleep(1)
pyautogui.write ('ADJ')
pyautogui.press('tab')
pyautogui.write ('Adjustment') #desc
time.sleep(2)
pyautogui.press('tab')
#Decides code type

pyautogui.write ('a') 
time.sleep(1)
pyautogui.press('tab')
pyautogui.write ('2')  #desc
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write ('adj') #alt code 2
pyautogui.press('tab')
pyautogui.write ('adj') #alt code 3

time.sleep(3)
pyautogui.hotkey('alt', 'a')	#changes to amount tab
pyautogui.write ('0') # amount
pyautogui.hotkey('alt', 's')

#-------------------Create a cash payment-----------------------
time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New Procedure
time.sleep(3)
pyautogui.write ('Cash')
pyautogui.press('tab')
pyautogui.write ('cash') #desc
time.sleep(2)
pyautogui.press('tab')
time.sleep(2)
import pyautogui
import time

for _ in range(12):
    pyautogui.press('down')
    time.sleep(0.5)  # Selects cash payment
pyautogui.press('tab')
pyautogui.write ('a') 
time.sleep(1)
pyautogui.press('tab')
pyautogui.write ('2')  #desc
pyautogui.press('tab')
pyautogui.press('tab')


time.sleep(3)
pyautogui.hotkey('alt', 's')

#----------------Create a Insurance payment Code----------------------

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('INSPAY')
pyautogui.press('tab')
pyautogui.write ('Insurance Payment') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('INSUrance payment')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2)   

#------------------Insurance Takeback Adjustment Code----------------------

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('TakeBack')
pyautogui.press('tab')
pyautogui.write ('Insurance Takeback Adjustment') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('INSUrance takeback')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2)   
#-------------------Insurance Withhold Adjustment Code----------------------

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('Withhold')
pyautogui.press('tab')
pyautogui.write ('Insurance Withhold Adjustment') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('INSUrance withhold')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2)   
#----------------------Comment Code

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('COMMENT')
pyautogui.press('tab')
pyautogui.write ('Comment') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('COMMENT')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2)   
#-----------------------Cash Copayment Code----------------------

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('CashCoPay')
pyautogui.press('tab')
pyautogui.write ('Cash Copayment') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('CASH copay')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2)   
#-----------------------Check Copayment Code----------------------

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('CheckCoPay')
pyautogui.press('tab')
pyautogui.write ('Check Copayment') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('CHECK copay')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2)   
#-----------------------Credit Card Copayment Code----------------------

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('CCCOPay')
pyautogui.press('tab')
pyautogui.write ('Credit Card Copayment') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('CREDIT CARD copay')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2)   
#------------------------Check Payment-------------------

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('CheckPay')
pyautogui.press('tab')
pyautogui.write ('Check Payment') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('CHECK payment')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2) 
#------------------------Credit Card Payment-------------------

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('CCPAY')
pyautogui.press('tab')
pyautogui.write ('Credit Card Payment') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('CREDIT CARD payment')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2)   
#--------------------Deductible-

time.sleep(3)
pyautogui.hotkey('alt', 'N')	#Opens New code
time.sleep(3)
pyautogui.write ('DED')
pyautogui.press('tab')
pyautogui.write ('Deductible') #desc 
pyautogui.press('tab')  
time.sleep(2)
pyautogui.write ('DEDUCTIBLE')
pyautogui.press('tab')
time.sleep(3)
pyautogui.hotkey('alt', 's')
time.sleep(2)   
#--------------------EDIT a Code-----------------
time.sleep(3)
# pyautogui.write ('d')
pyautogui.hotkey('alt', 'i')	#Opens Edit Procedure
time.sleep(3)
pyautogui.hotkey('alt', 'a')	#changes to amount tab
pyautogui.write ('500') # amount
pyautogui.hotkey('alt', 's')
time.sleep(2)   
pyautogui.hotkey('alt', 'c') #Save and close procedure window