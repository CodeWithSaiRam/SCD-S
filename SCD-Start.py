# Databricks notebook source
# MAGIC %md # Starting Notebook
# MAGIC Initiallise Datasets and Configs

# COMMAND ----------

# MAGIC %md _C.Williams - 2021_

# COMMAND ----------

# MAGIC %md ### Setup Dataset

# COMMAND ----------

# MAGIC %md Run settings notebook

# COMMAND ----------

# MAGIC %run "./~Configs/SCD-0-Init"

# COMMAND ----------

# MAGIC %md Get sample dataset

# COMMAND ----------

# Preview Dataset
display(sql("SELECT * FROM EmployeeSample"))

# COMMAND ----------

# MAGIC %md ### Write Dataset to DB
# MAGIC For use in other notebooks

# COMMAND ----------

# Create DB if it doesn't already exist
sql("CREATE DATABASE IF NOT EXISTS scd")
# Drop table if it already exists
sql("DROP TABLE IF EXISTS scd.employees")
# Create new table (delta format) using the sample Employee dataset
sql("CREATE TABLE scd.employees USING delta AS SELECT * FROM EmployeeSample")
