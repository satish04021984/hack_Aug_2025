# Technologies Used in Natural Language to SQL Banking Assistant

This project is a Natural Language to SQL Banking Assistant, which allows users to interact with a banking database using natural language queries. It leverages several technologies to achieve this, broadly categorized into Python Libraries and other key technologies:

### Python Libraries:

The application is primarily built using **Python**, and relies on a set of powerful libraries for its functionality:

*   **`Streamlit`**: This is the framework used to create the interactive web application interface. It allows users to input natural language queries and visualize the generated SQL and its results directly in their browser.
*   **`Langchain`**: This acts as the overarching framework for building applications powered by large language models. It helps orchestrate the different components involved in processing natural language and generating SQL.
*   **`langchain-google-genai`**: This specific integration within Langchain is crucial for connecting to and utilizing Google's Generative AI models. In this project, it's used to access the `gemini-1.5-flash` model, which performs the core task of converting natural language into SQL.
*   **`python-dotenv`**: This library is used for securely managing environment variables, such as API keys for the AI models, by loading them from a `.env` file.
*   **`langchain-community`**: This package provides various community-contributed LangChain integrations, including tools and utilities. While some database functionalities might be commented out, its presence indicates the project's adherence to Langchain's modular approach.

### Other Key Technologies:

Beyond the Python libraries, the project utilizes fundamental technologies for data management and AI capabilities:

*   **Google Gemini (`gemini-1.5-flash`)**: This is the Artificial Intelligence model at the heart of the application. Provided by Google AI and accessed via `langchain-google-genai`, it's responsible for understanding the user's natural language input and intelligently generating the corresponding SQL queries.
*   **SQLite**: This is the lightweight, file-based relational database management system (`banking.db`) that stores all the banking information, including details about customers, accounts, and transactions.
*   **Pandas**: This powerful Python library is used for data manipulation and analysis. In the Streamlit application, it takes the raw results from the SQL queries and transforms them into a more user-friendly tabular format (DataFrame) for display.

**How they all work together:**

The user interacts with the **Streamlit** web application by typing a natural language query. This query is then passed to the **Langchain** framework, which uses the **`langchain-google-genai`** integration to send it to the **Google Gemini** model. Gemini processes the natural language and generates an appropriate **SQL** query. This generated SQL query is then executed against the **SQLite** database using Python's `sqlite3` module (within `app/database.py`). Finally, the results from the SQLite database are fetched, processed by **Pandas** for better formatting, and displayed back to the user in the **Streamlit** application. Environment variables, including API keys, are securely managed by **`python-dotenv`**.

This combination of technologies creates a robust and user-friendly system for natural language interaction with a banking database.
