
class analysis_engine():
    # TODO: implement grouping variables as a type of variable
    def __init__(self):
        self.test_history = []          # each time a test is done, the result is appended to this list
        self.available_tests = {
                "autocorrelation":{ 
                                        "tags":set( ["correlation","linear","predictive","time_series","univariate"] ) 
                                    ,   "description":"describes the strength of the linear relationship (correlation) between a variable and a lagged version of itself"
                                    ,   "significance_thresholds":{
                                                "metric":"pearson_correlation"
                                            ,   "thresholds":{"low":0.1, "medium":0.5, "high":0.8}
                                    }
                }
            ,   "single_linear_leading_indicator":{ 
                                        "tags":set( ["bivariate","correlation","linear","predictive","time_series"] )
                                    ,   "description":"measures the significance of the linear relationship between 2 variables, where one measurement precedes the other in time" 
                                    ,   "significance_thresholds":{
                                                "metric":"pearson_correlation"
                                            ,   "thresholds":{"low":0.1, "medium":0.5, "high":0.8}
                                    }                                    
                }
            ,   "single_nonlinear_leading_indicator_cubic_spline_prediction":{ 
                                        "tags":set( ["bivariate","non_linear","predictive","splines","time_series"] )
                                    ,   "description":"measures the significance of a non-linear relationship (modelled with cubic splines) between 2 variables, where one measurement precedes the other in time" 
                                    ,   "significance_thresholds":{
                                                "metric":"1 / absolute_value(mean_absolute_error/mean_observed_value)"
                                            ,   "thresholds":{"low":1/0.1, "medium":1/0.05, "high":1/0.01}
                                    }
                }                
        }
    
    def clear_test_history(self):
        # TODO: allow clearing of 
        self.test_history = []

    def load_dataset( 
                    self
                ,   dataset
            ):
        # TODO: some tests to validate format of input data
        self.data = dataset

    def run_unit_tests( self, tests_to_run=[], **kwargs ):
        pass

    def run_test( self, test_name ):
        if test_name not in self.available_tests:
            print( f"'{test_name}' is not an available test" )
        elif test_name == "autocorrelation":
            print( f"'autocorrelation' test is not implemented yet")
        elif test_name == "single_linear_leading_indicator":
            print( f"'single_linear_leading_indicator' test is not implemented yet")
        elif test_name == "single_nonlinear_leading_indicator_using_cubic_splines":
            print( f"'single_nonlinear_leading_indicator_using_cubic_splines' test is not implemented yet")
        else:
            pass
