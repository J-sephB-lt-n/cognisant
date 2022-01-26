# Cognisant

**Cognisant** is an integrated suite of python tools for automated data analysis.

## Example Usage

```
import cognisant
import numpy as np

analysis_obj = cognisant.analysis_engine()

analysis_obj.prepare_data(
							data = {
									"day":{
												"vbl_function":"time_index"
											,	"vbl_tags":None
											,	"vbl_values":list(range(100))
									}
									,
									"sales":{
												"vbl_function":"to_maximise"
											,	"vbl_tags":None
											,	"vbl_values":np.random.randint()
									}
									,
									"day_of_week":{
												"vbl_function":"covariate"
											,	"vbl_tags":None
											,	"vbl_values":[]
									}
							}
)

import json
print( "## AVAILABLE TESTS ##" )
print( json.dumps(analysis_obj.available_tests, indent=4) )

analysis_obj.generate_insight(
			insight_must_contain_AT_LEAST_ONE_of_these_variables = []
		,	insight_must_contain_ALL_of_these_variables = []
		,	
		,	test_must_have_AT_LEAST_ONE_of_these_tags = [
						"univariate"
					,	"multivariate"
					,	"correlation"
					,	"predictive_model"
			]
		,	test_must_have_ALL_of_these_tags = []
	)
```
