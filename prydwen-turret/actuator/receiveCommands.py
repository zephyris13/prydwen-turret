import os, sys, json, getopt
import paho.mqtt.client as mqtt

import cameraControl
import omegaRelay


# variables
configFile = 'config.json'
bCameraMemory = False

# find the directory of the script
dirName = os.path.dirname(os.path.abspath(__file__))

# read the command line arguments
try:
	opts, args = getopt.getopt(sys.argv[1:], "hc:r", ["help", "config=", "relative"])
except getopt.GetoptError:
	printUsage()
	sys.exit(2)
for opt, arg, in opts:
	if opt in ("-h", "--help"):
		printUsage()
		sys.exit()
	elif opt in ("-c", "--config"):
		configFile = arg
	elif opt in ("-r", "--relative"):
		bCameraMemory = True


### MAIN PROGRAM ###
def __main__():
	# read the config file
	configPath = '/'.join([dirName, configFile])
	with open( configPath ) as f:
		try:
			config = json.load(f)
		except:
			print("ERROR: expecting JSON file at '%s'"%configPath)
			sys.exit()


	## setup mqtt
	mqttc = mqtt.Client()
	if not bCameraMemory:
		try:
			camera = cameraControl.cameraControl(config['panChannel'], config['tiltChannel'], config['inputRange'])
		except:
			print("ERROR: config file must contain settings for 'panChannel', 'tiltChannel', and 'inputRange'")
			sys.exit(2)
	else:
		try:
			camera = cameraControl.cameraControlRelative(config['panChannel'], config['tiltChannel'], config['inputRange'], config['maxAngleChange'])
		except:
			print("ERROR: config file must contain settings for 'panChannel', 'tiltChannel', 'inputRange', and 'maxAngleChange'")
			sys.exit(2)

	#try:
	relaySpool = omegaRelay.Relay(config['spoolupChannel'], config['relayAddr'])
    	relayFire = omegaRelay.Relay(config['fireChannel'], config['relayAddr'])
  	#except:
    		#print("ERROR: config file must contain settings for 'spoolupChannel', 'fireChannel'")
   		#sys.exit(2)

	## define the mqtt callbacks
	# when connection is made
	def on_connect(client, userdata, flags, rc):
	    print("Connection result: " + str(rc))
	    # subscribe to topic specified by config file
	    mqttc.subscribe(config['topicA'], 0)
	    mqttc.subscribe(config['topicB'], 0)
	    mqttc.subscribe(config['topicC'], 0)

	def on_message(client, userdata, msg):
	    if msg.payload:
	        print(msg.topic + ":: payload is " + str(msg.payload))
	        handleMessage(msg.topic, msg.payload)

	def on_subscribe(client, userdata, mid, granted_qos):
	    print("Subscribed: " + str(mid) + " " + str(granted_qos))

	def on_disconnect(client, userdata, rc):
	    print("Disconnected from Server")
	## end of mqtt callbacks

	## other functions
	def handleMessage(topic, payload):
	    if topic == config['topicA']:
          # this is for pan and tilt
	        # split payload contents
	        positions = payload.split()
	        if len(positions) == 2:
	            # double check which value is which! might have been switched!
	            print "Received positions (%d, %d)"%(int(positions[0]), int(positions[1]))
	            camera.move(int(positions[0]), int(positions[1]) )
	        else:
	            print("Invalid number of arguments received")

            if topic == config['topicB']:
          # this is for spool up
      	        spoolup = bool(int(payload))
          	if (spoolup):
              # call relay channel 0 on
	            print ("Spooling up")
		    relaySpool.set(1)
          	else:
              # call relay channel 0 off
		    print ("Spooling down")
		    relaySpool.set(0)

      	    if topic == config['topicC']:
          # this if for firing
                firing = bool(int(payload))
          	if (firing):
              # call relay channel 1 on
		    print ("Firing!")
		    relayFire.set(1)
          	else:
              # call relay channel 1 off
		    print ("Stopping")
		    relayFire.set(0)


	## Assign event callbacks
	mqttc.on_message = on_message
	mqttc.on_connect = on_connect
	mqttc.on_subscribe = on_subscribe
	mqttc.on_disconnect = on_disconnect
	# Connect
	mqttc.connect(config['server'], config['port'], 60)


	# Continue the network loop
	mqttc.loop_forever()



if __name__ == '__main__':
    __main__()
