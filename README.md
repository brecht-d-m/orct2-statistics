# OpenRCT2 statistics
Statistics about RCT2_ADDRESS, RCT2_CALL, and RCT2_GLOBAL usage across different commits. This is plotted using the Pandas and Plotly Python libraries.

## About
This plot (in `index.html`) shows the number of occurrences of `RCT2_ADDRESS`, `RCT2_CALL`, or `RCT2_GLOBAL` per commit for the [OpenRCT2 project](http://github.com/openrct2/openrct2). This plot is created using [plot.ly](https://plot.ly/) - a data visualization tool.

You can filter in the plot by clicking on the different keys in the legend. It is also possible to zoom in and to zoom back out (double click on the plot at the top).

To start the script:

```
./count-values.sh $path_to_orct2
```

The variable `path_to_orct2` can have for example following value: `~/Documents/openrct2/`. 

## Data gathering and processing
The data for the different statistics is gathered using following command:

```
git grep -h -c $fragment $commit | numsum
```

The variable `$fragment` will have the values: `RCT2_ADDRESS`, `RCT2_CALL`, and `RCT2_GLOBAL`. The results of this commands is written to a csv file (`orct2_statistics.csv`).  The header of this file has following structure:
 - Commit id
 - Timestamp commit
 - Number of RCT2_GLOBAL occurrences
 - Number of RCT2_ADDRESS occurrences
 - Number of RCT2_CALL occurrences

A list of all the commits is retrieved using following command:

```
git rev-list --count develop
```

To process the data afterwards, a Python script was used. The data was read and transformed using the [Pandas library](http://pandas.pydata.org/) and the [Plotly library](https://plot.ly/).
