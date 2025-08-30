The document outlines a technical challenge focused on building an AI-powered system that translates natural language banking requests into accurate SQL queries, enabling non-technical staff to access financial transaction data efficiently.

Core Requirements
The system must understand and process natural language banking queries and convert them into correct, executable SQL statements for an SQLite database.

It must support common SQL operations (SELECT, WHERE, JOIN, GROUP BY, aggregation) and be robust in handling errors and detecting ambiguity in user requests.

The AI should request clarifications in ambiguous cases and handle multi-turn conversations, maintaining context across interactions.

Technical Stack and Implementation
Python 3.10+ for backend, SQLite as the database, and AI/ML frameworks such as LangChain or LangGraph powered by OpenAI or local models.

Streamlit (or Gradio) for the frontend interface, requirement management via uv or requirements.txt.

Code must run locally only, with setup scripts initializing the database, and should include at least 60% automated test coverage (preferably with Pytest).

Proper security practices are mandated, like protecting against SQL injection and managing sensitive data carefully.

Submission and Documentation
Submissions require a GitHub repository with properly structured folders and well-documented code.

A design/architectural document is required, detailing the SQL generation approach, agent architecture, challenges faced, performance metrics, strengths and limitations.

A complete README.md should provide setup and usage instructions.

Evaluation Criteria
Functional: Accuracy of SQL translation, support for complex queries, effective ambiguity resolution, contextual conversation handling.

Technical: Agent design, SQL generation efficiency, code quality, error handling, test coverage, security measures.

User Experience: Frontend usability, clarity of results (including visualizations), and quality of documentation.

Bonus: Novel agent architecture, extra tool/API integrations, use of uv, and outstanding performance on edge cases.

Notable Reminders
Automated evaluation is strict about folder structure—misplacement may result in disqualification regardless of feature completeness.

Avoid putting all files in the root folder, deviating from the template, missing documentation, or submitting overly long demo videos.

Summary:
The document describes a banking-focused AI challenge to develop a natural language-to-SQL query system using modern Python, SQLite, and agent-based architectures, with rigorous requirements for error handling, ambiguity resolution, security, documentation, and test coverage. Proper folder structure and clear documentation are critical for successful automated evaluation
