import pyscreenshot
import time
from datetime import datetime

while True:
	image = pyscreenshot.grab()
	cur_time = datetime.now().strftime('%b-%d-time-%I-%M-%S')
	filename = cur_time + '.png'
	image.save('/YOU_DIR_NAME/' + filename)
	time.sleep(0.01)
	print ("-_- $$ -_- $$ -_-")
	print ("##################")
	print ("#     (.) (.)    #")
	print ("# Made By Cipher #")
	print ("##################")
	print ("------------------")
