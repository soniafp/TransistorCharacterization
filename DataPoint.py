#User defined data point with errors
class DataPoint:
    def __init__(self, x_value, y_value, x_error, y_error,z_value=-1.0,z_error=-1.0,w_value=-1.0,w_error=-1.0):
            self.x = x_value
            self.y = y_value
            self.z = z_value
            self.w = w_value            
            self.x_err = x_error
            self.y_err = y_error
            self.z_err = z_error            
            self.w_err = w_error            
            
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y      
    
    def get_x_error(self):
        return self.x_err
      
    def get_y_error(self):
        return self.y_err  
