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

## Amazon Athena

AWS Athena is an interactive query service provided by Amazon web services that allows you to analyze and query data stored in amazon s3 using sql. It provides a serverless and on-demand approach to query data without the need to setup and manage infrastructure or data warehouses. 

*  **Creating Table in Athena** : To query S3 file data, you must have an external table associated with the file structure. We can create external tables in two ways:
  

	* Manually.

	* Using AWS Glue Crawler.

*  **Price** : 

    * Amazon calculates the bytes and then rounds them to the nearest megabyte, 10MB being the minimum amount per Query.
    * You will not be charged for failed queries, statements for managing partitions, as well as Data Definition Language (DDL) statements.


Amazon s3 ----> AWS Glue Crawler ----> AWS Glue Data Catalog ----> Amazon Athena ----> Amazon quick-sight 

* githublink for reference:
    * https://github.com/johnny-chivers/sql-for-athena
    * https://www.youtube.com/watch?v=f_FUwGF-Ip8&ab_channel=Intellipaat 

## Amazon RDS

* Amazon RDS is relational dabase management service which manages relational databases for users. You can either manually create a backup via snapshot or can have an automated backup performed. MySQL, PostgresSQL, Oracle, SQLServers are available under RDS.
* Amazon RDS is a manged databse service that supports multiple database engine
* Amazon RDS Supports two types of storage. General purpose(SSD) and Provisioned IOPS(SSD). General purpose storage is suitable for most workloads, while provisoned iops storage provides higher I/O performance for intensive application.
* IOPS : input output operations per second

*  **DB Instances** : 

    * Database instance is a set of memory structure that manages the database
    * Each DB instance runs on DB engine
    * By default a customer can have 40 RDS instances

*  **DB Instance class** :
    
    * It supports mainly three types of storages: Magnestic, General purpose and Provisioned IOPS
    * Standard Instance class : db.m4, db.m3, db.m1
    * Memory optimized: db.r4 and db.r3
    * Burstable performance: db.t2
