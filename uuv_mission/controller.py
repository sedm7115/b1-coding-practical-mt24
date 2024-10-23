class Controller:
    def __init__(self, Kp=int, Kd=int):
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0

    def get_control_action(self, reference, output_depth) :
        error = reference - output_depth
        #u = Kp*e + Kd*(e - prev_e)
        control_action = self.Kp*error + self.Kd*(error-self.prev_error)
        #renew previous error (step)
        self.prev_error = error
        return control_action

        

