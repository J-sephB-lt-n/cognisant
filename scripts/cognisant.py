
class analysis_engine():
    def __init__(self):
        self.available_tests = {
                "autocorrelation":{ 
                                        "tags":["correlation","linear","predictive","time_series","univariate"] 
                                    ,   "description":"describes the strength of the linear relationship (correlation) between a variable and a lagged version of itself"
                }
            ,   "single_linear_leading_indicator":{ 
                                        "tags":["bivariate","correlation","linear","predictive","time_series"]
                                    ,   "description":"measures the significance of the linear relationship between 2 variables, where one measurement precedes the other in time" 
                }
            ,   "single_nonlinear_leading_indicator_using_cubic_splines":{ 
                                        "tags":["bivariate","non_linear","predictive","splines","time_series"]
                                    ,   "description":"measures the significance of a non-linear relationship (modelled with cubic splines) between 2 variables, where one measurement precedes the other in time" 
                }                
        }
    
    def load_dataset( 
                self
            ):
        pass
        # define self.available_tests list based on the types of data available


