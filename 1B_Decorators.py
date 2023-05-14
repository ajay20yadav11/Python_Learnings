import pandas as pd
import numpy as np

datasource = pd.read_excel(r"D:\AJAY\CBI\Switch_Version.xlsx")
#### Reading source data using .read_excel() method
#### provide the source path in the above method
#### storing source data into an object “datasource”

#### Create Pivot table using .pivot_table() method
pivot_output = pd.pivot_table(  # Provide arguments inside the methods
    datasource,  # source data
    index=datasource.columns[0],  # set the index column
    values="Column_Value",  # values, columns, rows and aggfunc
    columns=datasource.columns[1],  # are similar to pivot table fields
    aggfunc=np.sum,
)  # use Numpy library for arithmetic
# operation

print(pivot_output)
