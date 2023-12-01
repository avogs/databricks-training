# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC ## Overview
# MAGIC
# MAGIC This notebook will show you how to create an **unmanaged** Delta table originating from a file that you uploaded to DBFS. The key difference here lies in what we do after reading the CSV into a DataFrame.
# MAGIC
# MAGIC BEFORE
# MAGIC 1. Wrote out the DataFrame as a Delta table
# MAGIC
# MAGIC NOW
# MAGIC 1. Write out the DataFrame in Delta format
# MAGIC 2. Wrap that data with a Delta table

# COMMAND ----------

# File location and type
file_location = "/FileStore/tables/uszips.csv"
file_type = "csv"

#this example had an error in it

# CSV options
infer_schema = "true"
first_row_is_header = "true"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .option("escape", "\"") \
  .load(file_location)

display(df)

# COMMAND ----------

delta_file_name = "uszips_delta"

# write data out in Delta format

a = df.write.format("delta")
a.mode("overwrite").save('/mnt/delta/%s' % delta_file_name)

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS uszips_delta_unmanaged USING DELTA LOCATION '/mnt/delta/uszips_delta/';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM uszips_delta_unmanaged WHERE lat > 25 LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL uszips_delta_unmanaged
