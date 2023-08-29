## Using Boto3 with AWS

Apache spark is written in scala programming language. To support python with spark, apache spark community released a tool, pyspark. Using pyspark, you can work with RDDs in python programming language also. 

* **SparkContext** :
SparkContext is the entry point to any spark functionality. When we run any spark functionality, a driver programs start, which has the main function and your spark context get initiated here. By default, Spark automatically creates the SparkContext object named sc, when pyspark shell gets intiated. 

* **RDD** :
RDD Stands for resilient distributed dataset. These are the elements that run and oparate on multiple nodes to do parellel processing on a cluster. RDDs are immutable elements, which means once you create you can not change it. RDDs are fault tolerant as well, hence in case of any failure, they recover automatically. 
RDD is a fundamental datastructure in pyspark that represents a distributed collection of data that can be processed in parellel. 

To apply operations on these RDD's, there are two ways -
    * **Transformation** : These are the operations, which are applied on RDD to create a new RDD. Filter, groupBy and map are the examples of transformations.
    * **Action** : These are the oprations that are applied on RDD, which instructs Spark to perform computation and send the result back to the driver. 



