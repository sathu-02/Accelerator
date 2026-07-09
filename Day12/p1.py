## Problem 1: Industrial IoT Sensor Data Downcaster
"""
Problem Statement:
An industrial manufacturing plant monitors continuous operations through massive IoT sensors.
 The system logs raw telemetry readings to a CSV file. Because the file scales rapidly, 
 memory efficiency is critical. The engineering team needs to optimize the dataset's memory 
 usage by applying memory downcasting strategies before running downstream analytics.

The application must execute the following operations:
Load the raw telemetry logs.
Display the initial data types (dtypes) of all numeric columns.
Quantify the exact initial memory usage (in bytes) of only the numeric columns.
Downcast all integer types to their minimum possible memory subtype (e.g., int64 to int16/int32) and 
float columns to their minimum possible subtype (e.g., float64 to float32) using pd.to_numeric().
Display the optimized data types and the final minimized memory usage of the numeric columns.

Requirements:
Read telemetry.csv.
Use .memory_usage() to track changes.
Apply pd.to_numeric(..., downcast=...).

Input File:telemetry.csv
----------
Output Format:
-------------
Initial Data Types
...
Initial Memory Usage
... Bytes
Optimized Data Types
...
Optimized Memory Usage
... Bytes

telemetry.csv:
---------------
SensorID,ReadingValue,ErrorCode
1001,45.20,12
1002,12.85,0
1003,99.10,5
1004,5.00,0

Test Case:
---------

case=1
output=
Initial Data Types
ReadingValue    float64
ErrorCode         int64
dtype: object

Initial Memory Usage
64 Bytes

Optimized Data Types
ReadingValue    float32
ErrorCode          int8
dtype: object

Optimized Memory Usage
20 Bytes

"""
import pandas as pd

data=pd.read_csv("telemetry.csv")
num_cols=data[['ReadingValue','ErrorCode']]

print("Initial Data Types")
print(num_cols.dtypes)

ini_mem=num_cols.memory_usage(index=False).sum()
print("\nInitial Memory Usage")
print(f"{ini_mem} Bytes")

print("\nOptimized Data Types")
int_cols=num_cols.select_dtypes(include=["int"])
float_cols=num_cols.select_dtypes(include=["float"])

for col in int_cols.columns:
    data[col]=pd.to_numeric(data[col],downcast="integer")
    
for col in float_cols.columns:
    data[col]=pd.to_numeric(data[col],downcast="float")
    
optimized_cols=data[["ReadingValue","ErrorCode"]]
    
#print("\nOptimized Data Types")
print(optimized_cols.dtypes)

print("\nOptimized Memory Usage")
print(f"{optimized_cols.memory_usage(index=False).sum()} Bytes")
