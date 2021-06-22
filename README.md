# Data Engineer Challenge

How you implement the challenge is up to you. The only requirement is that all code must run in Docker containers.

1. Create an ingestion system for two data streams. It must accept HTTP messages. Example files are provided for both streams. The first stream named 'metrics.json' is an example of machine data from. The second, 'workorder.json', defines what product ran when and how much output was produced. You may use the provided files to test but your ingestion system will be tested on a different set of files.

2. Persist the data from step 1.

3. Create an ETL pipeline that reads the data from step 2, and find the top three parameters that co-relate to the production output of each product, and plot them in a static report as an output.

Document any design considerations and how to run your code.