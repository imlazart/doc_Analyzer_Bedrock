# 🚀 AI Document Analyzer using AWS Bedrock

A simple **Generative AI-powered Document Analyzer** that allows users to ask questions about documents using a conversational interface.

This application uses **AWS Bedrock Knowledge Base** with **Claude 3 Haiku** and a **Streamlit UI** to retrieve relevant document information and generate accurate responses using **Retrieval Augmented Generation (RAG)**.

---

## 📌 Project Overview

Many organizations deal with large volumes of documents. Searching through them manually can be time-consuming.

This project demonstrates how **Generative AI + Retrieval Augmented Generation (RAG)** can be used to build an intelligent system that allows users to **ask questions directly from documents and receive contextual answers instantly**.

---

## 🧠 How It Works

1. Documents are indexed into an **AWS Bedrock Knowledge Base**
2. Documents are converted into **vector embeddings**
3. User asks a question through the **Streamlit chat interface**
4. The query is sent to **Bedrock Agent Runtime**
5. Relevant document chunks are retrieved
6. **Claude 3 Haiku** generates the final response using the retrieved context

---

## 🏗️ Architecture

```
User Question
      │
      ▼
Streamlit Chat UI
      │
      ▼
AWS Bedrock Agent Runtime
      │
      ▼
Bedrock Knowledge Base
(Vector Embeddings + Retrieval)
      │
      ▼
Claude 3 Haiku Model
      │
      ▼
Generated Answer
```

---

## ⚙️ Tech Stack

| Technology | Purpose |
|------------|--------|
| **Python** | Application logic |
| **Streamlit** | Web UI for chatbot |
| **AWS Bedrock** | Generative AI platform |
| **Claude 3 Haiku** | Large Language Model |
| **Bedrock Knowledge Base** | Document retrieval |
| **Boto3** | AWS SDK for Python |

---

## 📂 Project Structure

```
doc_Analyzer_Bedrock
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🔧 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/imlazart/doc_Analyzer_Bedrock.git
cd doc_Analyzer_Bedrock
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv chatbot
```

Activate the environment:

**Windows**

```bash
chatbot\Scripts\activate
```

**Mac / Linux**

```bash
source chatbot/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 AWS Configuration

Configure AWS credentials using AWS CLI.

```bash
aws configure
```

Provide the following details:

```
AWS Access Key ID
AWS Secret Access Key
Default region name (example: us-east-1)
Default output format (json)
```

Ensure your IAM user has permissions for:

- Amazon Bedrock
- Bedrock Knowledge Base
- Bedrock Agent Runtime

---

## ▶️ Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will run at:

```
http://localhost:8501
```

---

## 📌 Example Use Cases

- 📄 Enterprise document search
- 📚 Knowledge management systems
- 🏢 Internal company policy assistants
- 🔍 Research document analysis
- 💬 AI-powered support assistants

---

## 🚀 Future Enhancements

- Upload documents directly from UI
- Support multiple document sources
- Display document citations
- Deploy using Docker or AWS services
- Authentication and role-based access

---

## 🔗 GitHub Repository

Project Repository:

https://github.com/imlazart/doc_Analyzer_Bedrock

---

## 👨‍💻 Author

**Lazar Thomas**

Passionate about **Generative AI, Cloud Computing, and AI-powered applications.**

---

## ⭐ If you found this useful

Please consider giving the repository a **star ⭐** to support the project.
