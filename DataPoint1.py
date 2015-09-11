#User defined data point with errors
class DataPoint1:
    def __init__(self, x_value, y_value, y_error, unixtime):
            self.x = x_value
            self.y = y_value
            self.y_err = y_error
            self.unixtime = unixtime
            
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y      
      
    def get_y_error(self):
        return self.y_err 
    
    def get_unixtime(self):
        return self.unixtime 