milestone1.py:  
- EDA on uncleaned training set
- counting number of missing values
- visualization of outliers
- removed some outliers and replot the histograms
- count the number of words in description

histogram generator:  
- generate histograms of 1.1 with outliers removed, reads trainning data as input, outputs 3 png files to the hist - outliers file

missing outlier handler:  
- count missing values in each variables and save the result (agression) to file mssing_count_result  
- a) count outliers for each reasonable variables and then print the result  
- b) for those outliers in a), actually delete those outliers.  
note: the algorithm uses 3 stds to determine the outliers