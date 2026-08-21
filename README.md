# 🤖 Agentic AI Customer Service Assistant

An end-to-end **Agentic AI application built using Databricks** that combines **Retrieval-Augmented Generation (RAG)** with **structured data querying** to create an intelligent customer-service assistant.

The system can retrieve information from product documentation, query customer-service data, and generate context-aware responses through a conversational Databricks application.



🏗️ Architecture


                    ┌───────────────────┐
                    │     End User      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Databricks App  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │     AI Agent      │
                    │    LLM + Tools    │
                    └───────┬───┬───────┘
                            │   │
                ┌───────────┘   └────────────┐
                ▼                            ▼
        ┌───────────────┐            ┌───────────────┐
        │ Vector Search │            │ UC Functions  │
        └───────┬───────┘            └───────┬───────┘
                │                            │
                ▼                            ▼
        Product PDF Docs              Delta Tables
        (Unstructured)                 (Structured)
        
🎯 Project Objective

The objective of this project is to build an AI-powered customer-service assistant that can work with both structured and unstructured data.

The system uses:

Product documentation stored as PDF files
Customer-service data stored in Delta tables
Policy information stored in structured tables
Vector Search for semantic document retrieval
Unity Catalog Functions for structured-data access
An LLM to reason over the retrieved information and generate responses


🔑 Key Concepts Implemented

1. Retrieval-Augmented Generation (RAG)

RAG allows the LLM to answer questions using information retrieved from the project's own knowledge base.

User Query
    ↓
Retrieve Relevant Information
    ↓
Add Retrieved Context
    ↓
LLM
    ↓
Generated Response

****For example, when a user asks:

Where can I find tutorials for AccountEase Pro?

the system searches the product documentation, retrieves the relevant content, and provides it to the LLM to generate the answer.

2. Unstructured Knowledge Base

The project uses 509+ product PDF documents as the unstructured knowledge source.

The documents were processed using Python/PyPDF2.

PDF Documents
      ↓
Extract Text
      ↓
Create Product Documents Table
      ↓
Combine with Product Metadata
      ↓
Create Indexed Document
      ↓
Generate Embeddings
      ↓
Vector Search Index

The indexed_doc contains relevant product metadata along with the document content, allowing the Vector Search system to retrieve useful product information.

3. Embeddings & Vector Search

The processed document text is converted into embeddings, which represent the semantic meaning of the text numerically.

These embeddings are stored in a Databricks Vector Search Index.

When a user asks a question:

User Question
     ↓
Query Embedding
     ↓
Similarity Search
     ↓
Relevant Documents

This enables semantic retrieval of relevant product documentation.

The Vector Search index is then provided to the AI Agent as a tool.

4. Structured Knowledge Base

Structured information such as:

Customer service history
Return policies
Product information

is stored using Delta Tables.

The structured data is accessed through Unity Catalog Functions.

This provides the AI Agent with controlled functions instead of requiring it to directly query the underlying tables.

5. Unity Catalog Functions

Two important functions were implemented.

get_return_policy()

Used to retrieve return-policy information.

Policy Name
     ↓
get_return_policy()
     ↓
Policies Table
     ↓
Policy Details
get_service_history()

Used to retrieve customer-specific service history.

Customer Email
      ↓
get_service_history()
      ↓
Customer Service Table
      ↓
Aggregate Service History
      ↓
Result

During testing, the function successfully returned an example showing 23 returns in the last 12 months for a queried customer.

🤖 AI Agent & Tool Calling

The AI Agent is the central component of the system.

It uses an LLM together with three tools:

                    AI Agent
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
   Vector Search   Return Policy   Service History

The agent determines which tool is required based on the user's question.

User Question	Tool
Where can I find the AccountEase Pro tutorial?	Vector Search
What is the return policy?	get_return_policy()
How many returns did this customer make?	get_service_history()

This tool-selection capability allows the LLM to work with different enterprise data sources instead of acting only as a text-generation chatbot.

🧪 Agent Testing

The agent was tested using the Databricks Playground.

The Vector Search index and Unity Catalog Functions were added as tools and tested with different types of questions.

Example:

Question
   ↓
Agent understands the request
   ↓
Selects appropriate tool
   ↓
Retrieves required information
   ↓
LLM generates final response

The tests verified that the agent could correctly use both structured and unstructured knowledge sources.

🚀 Agent Deployment

After testing the agent, a Databricks Agent Notebook was generated.

The agent was then registered in Unity Catalog and deployed using Model Serving.

Databricks Playground
        ↓
Create Agent Notebook
        ↓
Register Agent
        ↓
Unity Catalog
        ↓
Model Serving Endpoint

The registered model used in the project was:

agentic_catalog.agentic_schema.customer_service_model

🌐 Databricks Application

The deployed Model Serving endpoint was connected to a Databricks App.

The final user flow is:

User
 ↓
Databricks App
 ↓
Model Serving Endpoint
 ↓
AI Agent
 ↓
Tool Selection
 ↓
Vector Search / UC Functions
 ↓
LLM
 ↓
Final Response

The end user interacts with the system through a simple conversational interface without needing to know which underlying data source was used.

🔍 Agent Tracing

Databricks tracing was used to understand the internal execution of the agent.

A typical request can be represented as:

User Query
    ↓
LLM
    ↓
Tool Selection
    ↓
Tool Execution
    ↓
Tool Result
    ↓
LLM
    ↓
Final Response

Tracing provides visibility into:

LLM calls
Tool calls
Tool arguments
Tool outputs
Token usage
Execution flow


        
