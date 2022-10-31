from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
conf = SparkConf()
conf.setMaster("local").setAppName('My app')
sc = SparkContext.getOrCreate(conf=conf)
spark = SparkSession(sc)
print('Запущен Spark версии', spark.version)