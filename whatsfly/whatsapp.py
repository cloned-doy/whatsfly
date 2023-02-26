

class WhatsApp(object):
	def __init__(self, user: None, machine: "mac", browser: "safari"):
		"""
		user : user phone number. in the whatsmeow golang are called client.
		machine : os login info
		browser : browser login info

		import the compiled whatsmeow golang package, and setup basic client and database.
		auto run based on any database (login and chat info database), hence a user phone number are declared.
		if there is no user login assigned yet, assign a new client.
		put the database in current file whereever this class instancess are imported. database/client.db
		"""

		self.user 	 = user 
		self.user_name = None
		self.machine = machine
		self.browser = browser

	def Session(self):
		pass
	
	def send_message(self, message: str, phone: str):
		"""
		mesage : string or a list of string
		phone : string or list of string
		media : voice, images, or video
		return : status info. bool or str?
		"""

		sent = False
		status_info = None

		send_message = True

		if send_message:
			sent True
			status_info = f"a message to {phone} has been sent: {message}"

		return sent, status_info

	def send_image(self, message: str, phone: str, file_path: str):

		

		pass

	def send_video(self, message: str, phone: str, file_path: str):

		media_url = self.upload_media(phone, file_path)
		send_message = f"send video to {phone}: media url : {media_url}"

		pass

	def upload_media(self, message: str, phone: str, file_path: str) -> str:
		pass


if __name__ == '__main__':

	# main()
	client = WhatsApp()
	client.send_message(message, phone)