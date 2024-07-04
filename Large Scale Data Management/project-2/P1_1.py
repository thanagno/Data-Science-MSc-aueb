import json
import asyncio
import random
import csv
from datetime import datetime
from aiokafka import AIOKafkaProducer
from faker import Faker

def load_spotify_tracks(file_path):
    """Load Spotify track names from a CSV file."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        return [row['name'] for row in csv.DictReader(csvfile)]

# Initialize the Faker library for generating fake names
fake_data_generator = Faker()

# Specify the Kafka topic for song streaming data
kafka_topic = 'song_stream'

async def stream_song_data():
    """Asynchronously produce song streaming data to a Kafka topic."""
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:29092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    await producer.start()

    # Generate a list of random names, including a specific name
    user_names = [fake_data_generator.name() for _ in range(15)] + ["Theodoros Anagnos"]

    while True:
        for user_name in user_names:
            # Select a random song from the list
            song = random.choice(tracks)
            # Generate a timestamp in the specified format
            timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
            record = {"user_name": user_name, "timestamp": timestamp, "song": song}

            # Send the data to the Kafka topic
            await producer.send_and_wait(kafka_topic, record)
            print(f"Sent record: {record}")

        # Wait for 60 seconds before sending the next batch of records
        await asyncio.sleep(60)

# Load song data from the CSV file
tracks = load_spotify_tracks('spotify-songs.csv')

# Execute the asynchronous song streaming function
# Run the producer
loop = asyncio.get_event_loop()
loop.run_until_complete(stream_song_data())
