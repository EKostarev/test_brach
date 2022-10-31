from pyspark.sql import SparkSession
import os
import sys
import pandas as pd

# os.environ['PYSPARK_PYTHON'] = sys.executable
# os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

spark = SparkSession.builder.master("local[*]").appName("Word Count").getOrCreate()
df = spark.read.csv('C:/Users/Fudo/Downloads/archive/netflix_titles.csv')
df.show()