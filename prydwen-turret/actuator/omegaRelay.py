from OmegaExpansion import relayExp

class OmegaRelay:
	"""Base class for Relay signal"""

	def __init__(self, addr):
    self.addr = addr

		# check that relay-exp has been initialized
		bInit 	= relayExp.checkInit(self.addr)

		if (bInit == 0):
			# initialize the expansion
			ret 	= relayExp.driverInit(self.addr)
			if (ret != 0):
				print ("ERROR: relay-exp init not successful!")

class Relay:
	"""Class for relays"""

	def __init__(self, channel, addr):
		# initialize a pwm channel
		self.channel 	= channel
		self.relayDriver 	= OmegaRelay(self.addr)

  def set(self, value):
		self.relayDriver.setChannel(self.addr, self.channel, value)