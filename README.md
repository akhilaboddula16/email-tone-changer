📧 Email Tone Changer

This project helps you rewrite an email in a different tone (formal, polite, friendly, etc.)
The meaning of the email stays the same, only the tone changes.

It uses Generative AI with LangChain and LangGraph.

🤔 What Does This Project Do?

You give:

  * An email draft

  * A tone (example: formal)

The program:

  * Understands your email

  * Rewrites it in the given tone

  * Returns a clean and professional email


### **EXAMPLE**

**Input Email**
       
         I can’t attend the meeting today.

**Tone**
        
        Polite
        
**Output Email**

  
    I hope you are doing well. Unfortunately, I will not be able to attend today’s meeting. Thank you for your understanding.

### **Tools Used**

  * Python – programming language

  * LangChain – talks to AI models (LLMs)

  * LangGraph – controls the flow of steps

  * dotenv – keeps secret keys safe

  * LLM (AI model) – rewrites the email

### **Project Structure**



    mail_toner/
    │
    ├── .env                # API keys and environment variables
    ├── main.py             # Entry point of the application
    ├── toner.py            # Email tone rewriting logic
    ├── langgraph.json      # LangGraph configuration
    ├── pyproject.toml      # Project dependencies and settings
    ├── uv.lock             # Dependency lock file
    ├── .python-version     # Python version used
    ├── README.md           # Project documentation


### **Environment Setup (.env)**

* Create a .env file inside the mail_toner folder:

       MODEL_NAME=gemini-2.5-pro
       MODEL_PROVIDER=google_vertexai
       LANGCHAIN_TRACING_V2=true
       LANGCHAIN_API_KEY=your_langsmith_api_key
       LANGCHAIN_PROJECT=mail-toner








