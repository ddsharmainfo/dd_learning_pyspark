# from pyspark.sql import SparkSession
# spark = SparkSession.builder \
#     .appName("Python Spark SQL basic example") \
#     .config("spark.some.config.option", "some-value") \
#     .getOrCreate()

inputPath = './resources/users.parquet'


def read_parquet(spark):
    print('----- read_parquet method start -----')

    df = spark.read.format('parquet').load(inputPath)

    print('----- Schema -----')
    df.printSchema()

    print('Record counts: ', df.count())

    df.show(truncate=False)

    print('----- read_parquet method end -----')


# if __name__ == "__main__":
#     read_parquet()