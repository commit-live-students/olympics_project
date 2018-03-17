# Points Scored

## Write a function `q06_get_points` that :
- Makes use of previously created object named as `q02_rename_columns`.
- Updates the dataframe to include a new column called "Points" for Games which is a weighted value where each gold medal counts for 3 points, silver medals for 2 points, and bronze medals for 1 point.

Note - Remove the Combined total or don't use the combined total


### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path of the csv file location |

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable | pandas.Series | dataframe with points column and index |
