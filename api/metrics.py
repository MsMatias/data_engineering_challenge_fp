from utils.base import BaseApi

class Metrics(BaseApi):
    def __init__(self):
        """
        Initializes an instance of the Metrics class.
        Calls the __init__ method of the parent class (BaseApi) with the appropriate parameters.
        """
        super().__init__('metrics', './data/metrics.json')

    def process_metrics(self):
        """
        Retrieves the work order data and sends it to the message broker.
        Calls the get_data() method inherited from the BaseApi class to retrieve the data.
        Calls the send_data() method inherited from the BaseApi class to send the data to the message broker.
        """
        data = self.get_data()
        self.send_data(data)
    
# Create an instance of the Metrics class
producer = Metrics()

# Process the work order
producer.process_metrics()
