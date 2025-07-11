# 🚀 Agentic Outreach Assistant

A full-stack AI application that uses a collaborative team of agents to generate personalized sales emails. This project demonstrates a complete idea-to-deployment workflow, featuring a stateful, learning system with a persistent cloud-based vector memory.

---

### ✨ Live Demo GIF

*(This is where you should insert a GIF of your application working. A 30-second clip showing a "first run" and then an "instant cached run" is perfect.)*

![Demo GIF](link_to_your_demo.gif) 

---

### 🌟 Key Features

*   **Multi-Agent Workflow:** A `Researcher` agent analyzes a target company's website, and a `Copywriter` agent uses that research to craft a personalized email.
*   **Persistent Cloud Memory:** Utilizes **Qdrant Cloud** to store the results of agent work, creating a stateful system that learns over time.
*   **Vector-Based Caching:** Performs a vector similarity search to check for previous requests, enabling **instant recall** of cached results and saving on API costs.
*   **Full-Stack & Containerized:** Built with a Django/DRF backend and a React frontend, fully containerized with **Docker** and orchestrated with Docker Compose.
*   **Production-Ready Practices:** Served with Gunicorn and Nginx, demonstrating a modern, scalable deployment architecture.

---

### 🛠️ Tech Stack

| Backend                                                                                      | Frontend                                                                             | AI & Data                                                                                    | DevOps                                                                                     |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | ![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB) | ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white) | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white) |
| ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) | ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) | ![CrewAI](https://img.shields.io/badge/CrewAI-1A8B6F?style=for-the-badge)                      | ![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white) |
| ![DjangoREST](https://img.shields.io/badge/DRF-A30000?style=for-the-badge)                      | ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) | ![Qdrant](https://img.shields.io/badge/Qdrant-BA1F2E?style=for-the-badge)                       | ![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white) |

---

### 📂 Project Structure


---

### 🚀 Getting Started

Follow these steps to run the application locally.

#### Prerequisites

*   **Docker Desktop** installed and running.
*   **Git** installed.
*   **OpenAI API Key**.
*   **Qdrant Cloud URL and API Key**.

#### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create the environment file for the backend:**
    *   Navigate to the `agentic_project/` directory.
    *   Create a file named `.env`.
    *   Add your secret keys to this file:
    ```
    OPENAI_API_KEY="sk-YourOpenAIKeyGoesHere"
    QDRANT_URL="https://your-qdrant-cluster-url.aws.cloud.qdrant.io:6333"
    QDRANT_API_KEY="YourQdrantAPIKeyGoesHere"
    ```

3.  **Build and run the application with Docker Compose:**
    *   Navigate back to the root `AGENT_OUTREACH/` directory.
    *   Run the magic command:
    ```bash
    docker-compose up --build
    ```
    The first build will take a few minutes. Subsequent builds will be much faster.

4.  **Access the application:**
    *   Open your web browser and go to `http://localhost:3000`.

---

### 💡 The Toughest Challenge: "Dependency Hell"

The most significant challenge was resolving a series of cascading dependency conflicts within the AI library stack. Manually pinning versions of `crewai`, `langchain`, and `openai` created an impossible situation for the package manager.

**Solution:** I overcame this by adopting a modern, flexible dependency strategy. I removed all non-essential version pins for the AI libraries in `requirements.txt` and updated the Python code to be compatible with the latest stable versions. This allowed `pip`'s dependency resolver to find a valid, working combination of packages and resulted in a more robust and maintainable project.
