# Cognisant

**Cognisant** is an integrated suite of python tools for automated data analysis.

## Example Usage

```
import cognisant
import numpy as np

analysis_obj = cognisant.analysis_engine()

analysis_obj.load_dataset(
							data = {
									"day":{
												"vbl_function":"time_index"
											,	"vbl_tags":None
											,	"vbl_values":list(range(35))
									}
									,
									"sales":{
												"vbl_function":"to_maximise"
											,	"vbl_tags":None
											,	"vbl_values":np.random.uniform(low=100,high=1000,size=35)
									}
									,
									"day_of_week":{
												"vbl_function":"covariate"
											,	"vbl_tags":None
											,	"vbl_values":["mon","tues","wed","thu","fri","sat","sun"]*5
									}
							}
)

import json
print( "## AVAILABLE TESTS ##" )
print( json.dumps(analysis_obj.available_tests, indent=4) )
# TODO: give ability to showed filtered list of tests by constraint (same filters as those in generate_insight() below)
# TODO: give ability to showed filtered list of variables by constraint (same filters as those in generate_insight() below)

# run a specific test:
analysis_obj.generate_insight( list_of_allowed_tests=["autocorrelation"] ) 

# generate a random insight (optionally with user-specified constraints)
analysis_obj.generate_insight(
			insight_must_contain_AT_LEAST_ONE_of_these_variables = []
		,	insight_must_contain_ALL_of_these_variables = []
		,	insight_must_NOT_contain_ANY_of_these_variables = []
		,	list_of_allowed_tests = []
		,	test_must_have_AT_LEAST_ONE_of_these_tags = [
						"univariate"
					,	"multivariate"
					,	"correlation"
					,	"predictive_model"
			]
		,	test_must_have_ALL_of_these_tags = []
		,	test_must_NOT_contain_ANY_of_these_tags = []
		,	minimum_test_significance_level = "medium"
	)

# view and edit the significance thresholds of one of the tests:


# after running many tests, free up memory by removing history of past tests:
analysis_obj.clear_test_history()

```
