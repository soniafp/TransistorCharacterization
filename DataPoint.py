#User defined data point with errors
class DataPoint:
    def __init__(self, x_value, y_value, x_error, y_error):
            self.x = x_value
            self.y = y_value
            self.x_err = x_error
            self.y_err = y_error
            
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y      
    
    def get_x_error(self):
        return self.x_err
      
    def get_y_error(self):
        return self.y_err  