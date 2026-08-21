# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# dependencies = [
#   "databricks-vectorsearch",
# ]
# ///
# DBTITLE 1,Install required packages
# MAGIC %pip install databricks-vectorsearch

# COMMAND ----------

# DBTITLE 1,Restart Python
dbutils.library.restartPython()

# COMMAND ----------

import os
from databricks.vector_search.client import VectorSearchClient
from databricks.vector_search.reranker import DatabricksReranker

workspace_url = os.environ.get("WORKSPACE_URL")
sp_client_id = os.environ.get("SP_CLIENT_ID")
sp_client_secret = os.environ.get("SP_CLIENT_SECRET")

vsc = VectorSearchClient(
    workspace_url=workspace_url,
    service_principal_client_id=sp_client_id,
    service_principal_client_secret=sp_client_secret
)

index = vsc.get_index(endpoint_name="vectorsearch_1", index_name="agentic_catalog.agentic_schema.product_docs_index")

index.similarity_search(num_results=3, columns=["indexed_doc","product_id"], query_text="where can i find the tutorial related to AccountEase Pro product", query_type="HYBRID")

# COMMAND ----------

