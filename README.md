# DEMOgraphRAG

# **Knowledge Graph Generator**

## **Overview**
This project implements a **Knowledge Graph Generator** using `GraphRAG-SDK` and `Unstructured-IO`. It processes PDF, Word, and PowerPoint files, generates a Knowledge Graph, and stores it in **FalkorDB**. The solution is containerized with CI/CD automation for scalability and maintainability.

---

## **Tech Stack**
- **Programming Language**: Python 3  
- **Framework**: GraphRAG-SDK  
- **Data Parsing**: Unstructured-IO  
- **Database**: FalkorDB  
- **Containerization**: Docker  
- **CI/CD**: GitHub Actions  

---

## **Setup and Installation**

### Prerequisites
- **Python 3.8+**, **Docker**, and **Docker Compose** installed.
- FalkorDB account and credentials.

### Clone the Repository
```bash
git clone <repository-url>
cd knowledge-graph-generator
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Set Environment Variables
Create a `.env` file with:
```
FALKORDB_URL=<Your FalkorDB endpoint>
FALKORDB_API_KEY=<Your FalkorDB API Key>
```

---

## **Usage**

### Run Locally
1. Place files in the `data/` directory (supported: `.pdf`, `.docx`, `.pptx`).
2. Generate the Knowledge Graph:
   ```bash
   python generate_knowledge_graph.py --input-dir ./data
   ```

### Run with Docker
Build and run the container:
```bash
docker-compose up --build
```

---

## **Testing**
Run tests locally:
```bash
pytest tests/
```

---

## **Project Structure**
```
├── data/                  # Input files
├── src/                   # Code for ingestion, graph generation, and storage
├── tests/                 # Unit and integration tests
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---
