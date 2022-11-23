
import wpilib
import wpilib.drive
import ctre

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        self.front_left = ctre.WPI_TalonSRX(3)
        self.front_right = ctre.WPI_TalonSRX(1)    
        self.back_left = ctre.WPI_TalonSRX(4)
        self.back_right = ctre.WPI_TalonSRX(2)

        self.drive = wpilib.drive.MecanumDrive(
            self.front_left, self.back_left,
            self.front_right, self.back_right)

        self.controller = wpilib.XboxController(0)

        self.solenoid = wpilib.Solenoid(0, wpilib.PneumaticsModuleType.CTREPCM, 0)

        self.timer = wpilib.Timer()
        self.timer.start()

        self.first = True

        self.first_again = True

    def autonomousPeriodic(self):
        if self.timer.get() > 2 and self.first:
            self.solenoid.toggle()
            self.first = False

    def teleopPeriodic(self):
        move_y = -self.controller.getLeftX()
        move_x = -self.controller.getLeftY()
        rotation_z = self.controller.getRightX()
        self.drive.driveCartesian(move_x, move_y, rotation_z)

        if self.controller.getYButton() and self.first_again:
            self.solenoid.toggle()
            self.first_again = False
        if not self.controller.getYButton():
            self.first_again = True


    
                
       
wpilib.run(Robot)