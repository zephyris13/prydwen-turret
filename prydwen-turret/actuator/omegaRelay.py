from OmegaExpansion import relayExp

class OmegaRelay:
	"""Base class for Relay signal"""

	def __init__(self, addr):
    		self.addr = addr

		# check that relay-exp has been initialized
		bInit = relayExp.checkInit(self.addr)

		if (bInit == 0):
			# initialize the expansion
			print ("Initializing relay driver")
			ret = relayExp.driverInit(self.addr)
			if (ret != 0):
				print ("ERROR: relay-exp init not successful!")

	def setState(self, channel, addr, value):
    		"""Set relay state for relay channel"""
		print ("Setting relay state")
		ret = relayExp.setChannel(addr, channel, value)
		if (ret != 0):
			print 'ERROR: relay-exp setupDriver not successful!'

		return ret

class Relay:
	"""Class for relays"""

	def __init__(self, channel, addr):
		# initialize a relay channel
		self.channel = channel
		self.addr = addr
		self.relayDriver = OmegaRelay(self.addr)

 	def set(self, value):
		print ("Relay addr " + str(self.addr) + " - channel " + str(self.channel) + " - value " + str(value))
		ret 	= self.relayDriver.setState(self.channel, self.addr, value)
		return ret
