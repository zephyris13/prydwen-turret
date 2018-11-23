import omegaMotors

class cameraControl:
    def __init__(self, panChannel, tiltChannel, inputRange):
        self.panChannel     = panChannel
        self.tiltChannel    = tiltChannel

        self.inputRange     = inputRange

        # calculate degree change for each input step
        self.step   = float(inputRange)/180.0

        # instantiate a Servo object for both pan and tilt
        self.panServo = omegaMotors.Servo(self.panChannel, omegaMotors.SERVO_MIN_PULSE, omegaMotors.SERVO_MAX_PULSE)
        self.tiltServo = omegaMotors.Servo(self.tiltChannel, omegaMotors.SERVO_MIN_PULSE, omegaMotors.SERVO_MAX_PULSE)

		# center the servos
        self.panAngle = 90
        self.tiltAngle = 90
        self.panServo.setAngle(self.panAngle)
        self.tiltServo.setAngle(self.tiltAngle)

    # pan and tilt angles set directly based on input values
    def move(self, panValue, tiltValue):
        self.panAngle = self.calculateAngle(panValue)
        print "Setting pan servo to %d"%self.panAngle
        self.panServo.setAngle(self.panAngle)

        # tilt - invert the measurement
        self.tiltAngle = self.calculateAngle(self.inputRange - tiltValue)
        print "Setting tilt servo %d"%self.tiltAngle
        self.tiltServo.setAngle(self.tiltAngle)

    def calculateAngle(self, inputValue):
        angle = int(round(float(inputValue)/self.step))
        return angle



class cameraControlRelative(cameraControl):
    def __init__(self, panChannel, tiltChannel, inputRange, maxAngleChange):
        cameraControl.__init__(self, panChannel, tiltChannel, inputRange)
        self.maxAngleChange = float(maxAngleChange)
        self.midInputRange = int(round(float(self.inputRange)/2.0))

    # pan and tilt angles changed based on input values
    def move(self, panValue, tiltValue):
        # update and set the pan angle
        self.panAngle = self.panAngle + self.normalize(panValue)
        print "Setting pan servo to %d"%self.panAngle
        self.panServo.setAngle(self.panAngle)

        # update and set the tilt angle
        self.tiltAngle = self.tiltAngle + self.normalize(tiltValue)
        print "Setting tilt servo %d"%self.tiltAngle
        self.tiltServo.setAngle(self.tiltAngle)

    # an input of self.midInputRange means there is no change
    def normalize(self, inputValue):
        # separate the input into a magnitude and a direction
        inputMagnitude = inputValue - self.midInputRange

        inputDirection = 1  # positive
        if inputMagnitude < 0:

            inputMagnitude = self.midInputRange - inputValue
            inputDirection = -1;

        # return the normalized input
        normalizedValue = float(inputDirection) * float(inputMagnitude)
        print "normalizedValue = %f"%normalizedValue
        angleValue = self.calculateAngle(normalizedValue)
        print "angleValue = %f"%angleValue
        # the angle can only change by a defined max amount
        angleChange = (float(angleValue) / 90) * float(self.maxAngleChange)
        print "angleChange = %f"%angleChange
        return int(round(angleChange))
