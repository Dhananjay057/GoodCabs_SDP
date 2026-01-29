from pyspark import pipelines as dp
from pyspark.sql.functions import *

source_path = "s3://goodcabs-dj047/data-store/trips"

@dp.table(
    name ='transportation.bronze.trips',
    comment = 'Streaming ingestion of raw orders data with Autoloader',
    table_properties = {
        "quality" : "bronze",
        "layer" : "bronze",
        "source_format" : "csv",
        "delta.enableChangeDataFeed" : "true",
        "pipelines.autoOptimize.optimizeWrite" : "true",
        "pipelines.autoOptimize.autoCompact" : "true"
    }
)
def trips_bronze():
    df = (spark.readStream.format('cloudFiles')
          .option('cloudFiles.format','csv')
          .option('cloudFiles.inferColumnTypes','true')
          .option('cloudFiles.schemaEvolutionMode','rescue')
          .option('cloudFiles.maxFilesPerTrigger',100)
          .load(source_path)
    )

    df = df.withColumnRenamed('distance_travelled(km)','distance_travelled_km')

    df = df.withColumn("file_name",col('_metadata.file_path')).withColumn('ingest_datetime',current_timestamp())

    return df

