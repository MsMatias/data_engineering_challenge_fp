import os
import time
import json
import redis

class BaseApi:
    def __init__(self, topic, filepath):
        """
        Initializes an instance of the BaseApi class.

        Parameters:
        - topic: The topic or channel name to publish the data to in the message broker.
        - filepath: The path to the file containing the data to be streamed.

        Initializes the Redis connection using the environment variables:
        - REDIS_HOST: The hostname or IP address of the Redis server.
        - REDIS_PORT: The port number on which Redis is listening.
        - REDIS_DB: The Redis database number to use.
        """
        self.topic = topic
        self.filepath = filepath
        self.redis = redis.StrictRedis(
            host=os.environ['REDIS_HOST'],
            port=os.environ['REDIS_PORT'],
            db=os.environ['REDIS_DB'],
        )

    def get_data(self):
        """
        Retrieves the data from the specified file.

        Returns:
        - The loaded data as a Python object.
        """
        file = open(self.filepath, 'r')
        return json.load(file)

    def send_data(self, data, delay=0.05):
        """
        Publishes the data to the message broker.

        Parameters:
        - data: The data to be sent to the message broker.
        - delay: The delay (in seconds) between publishing each item of data. Default is 0.05 seconds.

        Returns:
        - True if the data is successfully sent to the message broker.

        Raises:
        - Exception: If an error occurs while sending the data to the message broker.
        """
        for item in data:
            try:
                self.redis.publish(self.topic, json.dumps(item))
                time.sleep(delay)
            except Exception as e:
                raise Exception('An error occurred while trying to send the data to the broker.', e)
        return True
