## Using Boto3 with AWS

Boto3 is the official **AWS SDK for Python** that enables developers to interact with various **Amazon Web Services (AWS)** using Python programming language. It provides a convenient and efficient way to programmatically interact with AWS services such as Amazon S3 (Simple Storage Service), Amazon EC2 (Elastic Compute Cloud), Amazon DynamoDB (NoSQL database), Amazon SNS (Simple Notification Service), and many others

## Amazon S3 (Simple Storage Service)

Amazon S3 is a cloud-based **object storage service** offered by Amazon Web Services (AWS). It provides a scalable and reliable solution for storing and retrieving diverse types of data, including documents, images, videos, and more.

## AWS Lambda

**AWS Lambda** is a serverless compute service provided by Amazon Web Services (AWS). It allows you to run code without provisioning or managing servers. Lambda automatically scales your applications in response to incoming traffic, ensuring that you pay only for the compute time you consume.

## AWS Step Function

AWS Step Functions allows you to create and manage complex workflows using a visual interface or Amazon States Language. Workflows are represented as state machines composed of states and transitions, enabling you to coordinate and automate various tasks and services seamlessly.

## AWS Glue

AWS Glue is simply a serverless ETL tool
1. we define a crawler to populate our AWS data catalog with metadata and table definitions. we use this metadata when we define a job to transform our data in the second step. 

2. AWS Glue can generate a script to transform our data or we can also provide the script in the AWS Glue console

3. we can run our job on demand or we can set it up to start when a specified trigger occurs. The trigger can be a time-based schedule or an event. Finally, when our job runs, a script extracts data from our data source, transforms the data, and loads it into our target.

4. The data source is the place where raw data resides before any transformation, and the data store is where the processed data is stored after transformation.


The term "data target" is commonly used in the context of ETL (Extract, Transform, Load) processes to refer to the destination where transformed and processed data is loaded after undergoing transformations. It's essentially synonymous with the concept of a "data store" in AWS Glue.

5. In the ETL process:

* **Data Source**: The origin of the raw data that needs to be processed and transformed.
* **Data Transformation**: The process of applying various operations to the raw data to clean, reshape, aggregate, or otherwise prepare it for analysis or reporting.
* **Data Target (Data Store)**: The destination where the transformed data is loaded after the transformations are applied.
* **Data catalog**: It is a persistent meta data store in AWS Glue. It contains table definations, job definations and etc. AWS Glue has one data catalog per region
* **Database**: It is a set of data catalog table definations organized into a logical group in the AWS group
* **Crawler**: It is a program that connects to our data store. May be a source or a target progress through a prioritized list of classifiers to determine the schema for our data and then it creates metadata tables in the data catalog
* **Connection**: It determines the schema of our data. Aws glue provides classifiers for common file types such as csv.json , etc. It also provides classifiers for common relaltional database management systems using JDBC connection.
