
import wpilib
import wpilib.drive
import ctre

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.front_right = ctre.WPI_TalonSRX(3)
        self.front_left = ctre.WPI_TalonSRX(2)    
        self.back_right = ctre.WPI_TalonSRX(4)
        self.back_left = ctre.WPI_TalonSRX(1)

        self.drive = wpilib.drive.MecanumDrive(
            self.front_left, self.back_left,
            self.front_right, self.back_right)

        self.stick = wpilib.XboxController(0)

        self.solenoid = wpilib.Solenoid(0, wpilib.PneumaticsModuleType.CTREPCM, 0)
        self.gyro = wpilib.ADIS16448_IMU()
        self.timer = wpilib.Timer()
        self.timer.start()

        self.first = True

        self.first_again = True
    
    def robotPeriodic(self):
        print(self.gyro.getGyroAngleX(), self.gyro.getAngle())

    def autonomousPeriodic(self):
        if self.timer.get() > 2 and self.first:
            self.solenoid.toggle()
            self.first = False

    def teleopPeriodic(self):
        self.drive.driveCartesian(self.stick.getRightX()*0.75, self.stick.getLeftX()*0.75, -self.stick.getLeftY()*0.75)

        if self.stick.getYButton() and self.first_again:
            self.solenoid.toggle()
            self.first_again = False
        if not self.stick.getYButton():
            self.first_again = True


    
                
       
wpilib.run(Robot)