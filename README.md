# Bitcoin Price Tracker: Using Serverless Compute and Cloud Database to Capture and Store Bitcoin Pricing

# Ingesting Web Data Using Cloud Technologies
- Web data ingestion and storage is critical for business intelligence.  In this project I wanted to create a simple pipeline to reach out to a web API capture JSON payload via a python script that was held and running in a serverless environment, store the data in a cloud SQL database that could be accessed via dashboard and reporting tools.

# The Goal and Plan
- I created a whiteboard diagram of the pipeline to get a plan of how to build it and what tools I would need to incorporate.

![alt text](https://github.com/ANelson82/btc_azure_function/blob/master/btc_whiteboard%20crop.jpg "Whiteboard")

# The Data Set
- The web data comes from www.coindesk.com via their API that generates JSON data.
- This data is a good representation of the type of critical streaming web data that would benefit many business intelligence groups whether that be financial, inventory, or IOT data. 

# Used Tools
- Python, Azure Functions, Azure SQL, Power BI
- These tools sets have good integration and documentation.  There's a lot of flexibility in terms of data ingestion and storage.  They are affordable and have large potential for scaling.

# Connect
- Within a python script file connection to the website was utilized by a the request library.
- The JSON data was read using the JSON library and the payload was extracted into variables.
- A connection to the Azure SQL database was made via pyodbc library. 
- A SQL query was executed to insert the payload variables into the SQL database.

# Processing
- The entire code was within a Azure timer trigger function.  The timer was set with a CRON function to run every 5 minutes.

# Storage
The function triggered a commit of the JSON payload into an Azure SQL cloud database.
![alt text](https://github.com/ANelson82/btc_azure_function/blob/master/btc_sql_50.png "SQL Storage")

# Visualization
- PowerBI was used to create a connection to the Azure SQL server and ingest data and display it for visualization.

![alt text](https://github.com/ANelson82/btc_azure_function/blob/master/powerBI_BTC.png "Power BI Visualization")

# Challenges
- A hit a challenge trying to use SQLalchemy to connect to Azure SQL.  Microsoft supports pyodbc drivers to connect to their SQL server, they don't support SQLalchemy.   I had to rewrite my code to utilize the pyodbc library.

# Conclusion
This pipeline project demonstrates a way to automate web data ingestion and storage using new serverless processing tools and well-established SQL database that can be accessed by stakeholders within an organization.

# Follow Me On
https://www.linkedin.com/in/andynelson1982/
