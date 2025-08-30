# NL-to-SQL Banking AI System

This project aims to develop an AI-powered system that translates natural language banking requests into accurate SQL queries. This will enable non-technical staff to efficiently access and analyze financial transaction data stored in an SQLite database.

## Core Requirements

- Understand and process natural language banking queries and convert them into correct, executable SQL statements for an SQLite database.
- Support common SQL operations (SELECT, WHERE, JOIN, GROUP BY, aggregation).
- Robust error handling and ambiguity detection.
- Request clarifications in ambiguous cases and handle multi-turn conversations.

## Technical Stack

- Python 3.10+ (backend)
- SQLite (database)
- AI/ML frameworks: LangChain or LangGraph (powered by OpenAI or local models)
- Frontend: Streamlit or Gradio
- Dependency Management: `uv` or `requirements.txt`

## Setup and Usage

Follow these steps to set up and run the NL-to-SQL Banking AI System locally.

### 1. Clone the repository (if not already done)

```bash
git clone <your-repository-url>
cd nl_to_sql_banking
```

### 2. Create and Activate a Python Virtual Environment

It's recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Set up Google Gemini API Key

This project uses Google Gemini models. You need to provide your Google API key.

1.  Create a file named `.env` in the root directory of the project (`D:\Projects\nl_to_sql_banking\`).
2.  Add your Google API key to this file in the following format:
    ```
    GOOGLE_API_KEY='YOUR_GOOGLE_API_KEY'
    ```
    Replace `YOUR_GOOGLE_API_KEY` with your actual API key from [Google AI Studio](https://makersuite.google.com/app/apikey) or Google Cloud Console.

### 5. Initialize the Database

Run the database setup script to create the SQLite database and populate it with initial banking data:

```bash
python database_setup.py
```

This will create a `banking.db` file and a `schema.sql` file in the project root.

### 6. Run the Streamlit Application

Start the Streamlit frontend. Once the application launches, it will typically open in your web browser at `http://localhost:8501`.

```bash
python -m streamlit run app/main.py --server.address 0.0.0.0 --server.port 8501 --server.runOnSave true
```

If you encounter a prompt for an email address in the terminal, you can usually just press `Enter` to proceed. Alternatively, ensure your Python environment is correctly configured.

## Project Structure

```
nl_to_sql_banking/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── llm_agent.py
│   └── ... (other application modules)
├── tests/
│   ├── __init__.py
│   ├── test_sql_generation.py
│   └── ... (other test files)
├── docs/
│   ├── design_document.md
│   └── ... (other documentation)
├── README.md
├── requirements.txt
├── database_setup.py
├── schema.sql
└── .env (for environment variables)
```

## Automated Testing

To run the automated tests, ensure you have `pytest` installed (it's included in `requirements.txt`). Then, execute:

```bash
python -m pytest tests/test_sql_generation.py
```

## Security Practices

- Protection against SQL injection is implemented using parameterized queries in `app/database.py`.
- Sensitive data (like API keys) are managed via environment variables (`.env`).
- The system is designed for local execution only.

## Design/Architectural Document

A detailed design and architectural overview is available in `docs/design_document.md`.

## Evaluation Criteria

- **Functional:** Accuracy of SQL translation, support for complex queries, effective ambiguity resolution, contextual conversation handling.
- **Technical:** Agent design, SQL generation efficiency, code quality, error handling, test coverage, security measures.
- **User Experience:** Frontend usability, clarity of results (including visualizations), and quality of documentation.

## Bonus Features

- Novel agent architecture
- Extra tool/API integrations
- Use of `uv` for dependency management
- Outstanding performance on edge cases
