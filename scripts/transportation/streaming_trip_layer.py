from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Inisialisasi Spark Session
spark = SparkSession.builder \
    .appName("SmartTransportationStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# 1. Definisi Schema (Harus sesuai dengan JSON dari generator)
schema = StructType([
    StructField("trip_id", StringType()),
    StructField("vehicle_type", StringType()),
    StructField("location", StringType()),
    StructField("distance", DoubleType()),
    StructField("fare", IntegerType()),
    StructField("timestamp", StringType())
])

# 2. Membaca Stream dari folder JSON
print("🚀 Reading Stream from stream_data/transportation...")
raw_stream = spark.readStream \
    .schema(schema) \
    .json("stream_data/transportation")

# 3. Transformasi Data (Konversi timestamp string ke format waktu)
processed_stream = raw_stream.withColumn("timestamp", to_timestamp("timestamp"))

# 4. Menulis hasil ke format Parquet (Data Lake Layer)
query = processed_stream.writeStream \
    .format("parquet") \
    .option("path", "data/serving/transportation") \
    .option("checkpointLocation", "logs/checkpoints/transportation") \
    .outputMode("append") \
    .start()

print("✅ Streaming Layer is Running and saving to Parquet...")
query.awaitTermination()
