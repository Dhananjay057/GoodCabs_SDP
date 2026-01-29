# GoodCabs_SDP
Good Cabs Transportation Data Engineering Project

Project Overview : 

This project builds an end-to-end data engineering platform for Good Cabs, a fast-growing cab service operating across multiple cities in India. The primary goal is to solve a systemic issue where regional managers lack timely, city-specific analytics for daily operations. By transitioning from traditional procedural Spark pipelines to Databricks LakeFlow Spark Declarative Pipelines (SDP), the project provides a scalable, automated, and innovative solution for regional insights.

Problem Statement :
Regional teams at Good Cabs were struggling with late data and generic dashboards that required manual rework. The existing platform relied on tightly coupled procedural Spark pipelines and manual orchestration, which slowed down innovation and lacked the stability needed for rapid scaling.
Technical Architecture

The project follows the Medallion Architecture, processing data through three distinct layers:
• Bronze: Raw data ingestion from Amazon S3 using the Autoloader feature for incremental file processing.
• Silver: Cleaned and transformed data, including a programmatically generated Calendar/Date table and validated trip records.
• Gold: Highly denormalized, business-ready views tailored for regional managers.
Key Features & Technologies
• Databricks LakeFlow SDP: A declarative framework that allows developers to define "what" the data should look like rather than "how" to process it, reducing code complexity (e.g., reducing a 135-line script to just 50 lines).
• Auto CDC (Change Data Capture): Simplifies updates and deletes using a single API, handling SCD Type 1 logic without manual "merge" statements.
• Automatic Orchestration: Dependencies and execution plans are managed automatically by the SDP framework.
• Data Governance: Implemented via Unity Catalog, using Role-Based Access Control (RBAC) to ensure regional managers only access data relevant to their specific cities.
• AI-Powered Analytics: Integrated Databricks Genie, enabling stakeholders to query data using natural language for instant insights, such as average ratings or revenue by city.
Data Pipeline Details
1. Ingestion: Data is extracted from an OLTP environment into Amazon S3 as CSV files.
2. Processing:
    ◦ Materialized Views: Used for batch-oriented dimension tables like city and calendar.
    ◦ Streaming Tables: Used for the trips fact table to handle continuous or incremental data updates.
3. Validation: Applied expectations to track and log data quality issues, such as invalid driver or passenger ratings, without halting the pipeline.
Results & Benefits
• Efficiency: Achieved incremental processing for materialized views and streaming tables, reducing reprocessing costs.
• Agility: Shifting to a declarative approach allowed the team to focus on business logic rather than manual stitching and orchestration.
• Speed: Regional views are updated faster, and stakeholders can self-serve data using AI features.

--------------------------------------------------------------------------------
Tools Used: Python, SQL, Apache Spark, Databricks (LakeFlow, Unity Catalog, Genie), Amazon S3. Domain: Transportation. Project Guidance: codebasics
