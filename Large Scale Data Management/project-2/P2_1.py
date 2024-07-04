from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, LongType, IntegerType, FloatType
from pyspark.sql.functions import from_json, col

# Define the schema for messages consumed from Kafka
kafka_message_schema = StructType([
    StructField("user", StringType(), True),
    StructField("timestamp", StringType(), True),  # Use StringType for consistency with produced format
    StructField("track_name", StringType(), True)
])

# Define the schema for the Spotify tracks dataset
spotify_tracks_schema = StructType([
    StructField("name", StringType(), True),
    StructField("artist", StringType(), True),
    StructField("duration_ms", LongType(), True),
    StructField("album", StringType(), True),
    StructField("release_date", StringType(), True),
    StructField("danceability", FloatType(), True),
    StructField("energy", FloatType(), True),
    StructField("key", IntegerType(), True),
    StructField("loudness", FloatType(), True),
    StructField("mode", IntegerType(), True),
    StructField("speechiness", FloatType(), True),
    StructField("acousticness", FloatType(), True),
    StructField("instrumentalness", FloatType(), True),
    StructField("liveness", FloatType(), True),
    StructField("valence", FloatType(), True),
    StructField("tempo", FloatType(), True)
])

# Initialize a Spark session with Kafka package
spark = SparkSession.builder \
    .appName("SpotifyKafkaIntegration") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Read streaming data from Kafka
kafka_stream_df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:29092") \
    .option("subscribe", "song_stream") \
    .option("startingOffsets", "latest") \
    .load()

# Extract and parse the JSON messages from the Kafka stream
parsed_stream_df = kafka_stream_df \
    .selectExpr("CAST(value AS STRING) as json") \
    .select(from_json("json", kafka_message_schema).alias("data")) \
    .select("data.*")

# Read Spotify tracks data into a DataFrame
spotify_tracks_df = spark.read \
    .csv("spotify-songs.csv", header=True, schema=spotify_tracks_schema)

# Join the Kafka data stream with the static Spotify tracks DataFrame
joined_stream_df = parsed_stream_df \
    .join(spotify_tracks_df, parsed_stream_df.track_name == spotify_tracks_df.name) \
    .drop(spotify_tracks_df.name)

# Function to write batches of data to Cassandra
def write_to_cassandra(batch_df, batch_id):
    batch_df.write \
        .format("org.apache.spark.sql.cassandra") \
        .option("keyspace", "spotify") \
        .option("table", "streaming_records") \
        .mode("append") \
        .save()

# Write the results to Cassandra, invoking the function for each batch
streaming_query = joined_stream_df.writeStream \
    .foreachBatch(write_to_cassandra) \
    .outputMode("append") \
    .start()

# Keep the application running until terminated
streaming_query.awaitTermination()
