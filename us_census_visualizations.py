# Databricks notebook source
# MAGIC %md
# MAGIC Databricks Training Notebook

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT state_id AS state, COUNT(zip) as nzips
# MAGIC FROM uszips_delta_unmanaged
# MAGIC WHERE state_id NOT IN ('PR', 'AS', 'GU', 'MP', 'VI')
# MAGIC GROUP BY state
# MAGIC ORDER BY nzips;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT state_id AS state, SUM(population) as population
# MAGIC FROM uszips_delta_unmanaged
# MAGIC WHERE state_id NOT IN ('AS', 'GU', 'MP', 'PR', 'VI')
# MAGIC GROUP BY state
# MAGIC ORDER BY state;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT state_id AS state, SUM(population) as population
# MAGIC FROM uszips_delta_unmanaged
# MAGIC WHERE state_id NOT IN ('AS', 'GU', 'MP', 'PR', 'VI')
# MAGIC GROUP BY state
# MAGIC ORDER BY state;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT state_id, count(density) from uszips_delta_unmanaged WHERE density > 800 DEFAULT 0 GROUP BY state_id;
