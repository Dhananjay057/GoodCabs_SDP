from pyspark import pipelines as dp
from pyspark.sql.functions import col, current_timestamp
from pyspark.sql.functions import md5, concat_ws, sha2

# Configuration
source_path = "s3://goodcabs-dj047/data-store/city"

@dp.materialized_view(
    name = 'transportation.bronze.city',
    comment = "City Raw Data Processing",
    table_properties = {
        "quality" : "bronze",
        "layer" : "bronze",
        "source_format" : "csv",
        "delta.enableChangeDataFeed" : "true",
        "delta.autoOptimize.optimizeWrite" : "true",
        "delta.autoOptimize.autoCompact" : "true"
    }
)

def city_bronze():
    df = spark.read.format("csv").option("header", True).option("inferSchema", True).option("mode", "PERMISSIVE").option("columnNameOfCorruptRecord", "_corrupt_record").csv(source_path)

    df = df.withColumn("file_name", col("_metadata.file_path")).withColumn("ingest_datetime", current_timestamp())

    return df