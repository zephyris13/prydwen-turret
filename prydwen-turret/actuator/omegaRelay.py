from OmegaExpansion import relayExp

class OmegaRelay:
	"""Base class for Relay signal"""

	def __init__(self, channel):
		self.channel 	= channel
		self.frequency 	= SERVO_FREQUENCY

		# check that relay-exp has been initialized
		bInit 	= pwmExp.checkInit()

		if (bInit == 0):
			# initialize the expansion
			ret 	= pwmExp.driverInit()
			if (ret != 0):
				print 'ERROR: relay-exp init not successful!'