# Data Engineer Challenge

How you implement the challenge is up to you. The only requirements are that the code must run with minimal setup on our own machines and that the code is clean and well abstracted.

1. Write two APIs that are going to stream the data (use the data in the provided files as the source.  The first stream named 'metrics.json' is an example of machine data. The second, 'workorder.json', defines what product ran when and how much output was produced ). A cousmer/producer should be implemented to consume from the API and then publish to a message broker system. Another cousmer should be implemented to presist the data from the message broker.

2. Create an ETL pipeline that reads the data from step 1, and finds the top three parameters that correlate to the production output of each product (please note that there is a relation between the metrics and the workorders data), and output them in a static report.

Document any design considerations and how to run your code.
You may use the provided files to test but your entire system will be tested on a different set of files.
