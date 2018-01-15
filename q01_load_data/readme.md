# Loading data

This assignment comprises of loading the structured data and applying some operations to it.

## Write a function `q01_load_data` that :
- Reads CSV file and convert CSV data to dataframe.
- Skip first row.
- Extract the first row for the header, rename it to "country name" and append it as a header row in dataframe.

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path of the csv file location |

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable | pandas.Dataframe | Dataframe with above operations inculcated |
