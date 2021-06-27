import webiopi

GPIO = webiopi.GPIO

P_ANO = [20, 21, 22, 23, 24]
P_CAT = [6, 7, 2, 8, 3, 4, 5]
cnt = 0
num = 0

DT = [ [1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1] ]

def setup():
	for ano in range(5):
		GPIO.setFunction( P_ANO[ano], GPIO.OUT )
		GPIO.digitalWrite( P_ANO[ano], False )

	for cat in range(7):
		GPIO.setFunction( P_CAT[cat], GPIO.OUT )
		GPIO.digitalWrite( P_CAT[cat], True )

def loop():
	for cat in range(7):
		GPIO.digitalWrite( P_CAT[cat], False )
		for ano in range(5):
			GPIO.digitalWrite( P_ANO[ano], DT[cat][ano] ) 
			webiopi.sleep( 0.0001 )
			GPIO.digitalWrite( P_ANO[ano], False ) 
		GPIO.digitalWrite( P_CAT[cat], True )
