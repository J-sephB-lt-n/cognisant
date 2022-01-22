# Cognisant

**Cognisant** is an integrated suite of python tools for automated data analysis.

## Example Usage

```
import cognisant
import numpy as np

analysis_obj = cognisant.analysis_engine()

analysis_obj.generate_insight(
			insight_must_contain_AT_LEAST_ONE_of_these_variables = []
		,	insight_must_contain_ALL_of_these_variables = []
		,	insight_must_have_AT_LEAST_ONE_of_these_attributes = [
						"univariate"
					,	"multivariate"
					,	"correlation"
					,	"predictive_model"
			]
		,	insight_must_have_ALL_of_these_attributes = []
	)
```
