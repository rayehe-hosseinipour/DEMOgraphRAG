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
cd DEMOgraphRAG
```

### Install Dependencies
```bash
pip install -r requirements.txt
cd app
```

### Set Environment Variables
Create a `.env` file with:
```
GOOGLE_API_KEY=<Your Gemini Token>
UNSTRUCTURED_API_KEY=<Your UNSTRUCTURED-IO KEY>
UNSTRUCTURED_API_URL= <Your UNSTRUCTURED-IO URL>
FALKOR_HOST_URL=<Your FalkorDB endpoint>
FALKOR_USERNAME=<Your FalkorDB username>
FALKOR_PASSWORD=<Your FalkorDB password>
PORTS=<Your FalkorDB PORT>
```

---

## **Usage**

### Run Locally
1. Place files in the `Data/Input` directory (supported: `.pdf`, `.docx`, `.pptx`).
2. Generate the Knowledge Graph:
```bash
python -m main.py 
```

### Run with Docker
- Build and run the container:
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
├── app/                                  # Main application folder
│   ├── config/                           # Configuration files
│   │   ├── .env                          # Environment variables
│   │   └── conf.py                       # Configuration settings
│   ├── Data/                             # Data handling folder
│   │   ├── Input/                        # Input data processing
│   │   └── Output/                       # Output data processing
│   ├── GraphPipeline/                    # Graph pipeline for generating graphs
│   │   └── graph_generating_pipeline.py  # Script to generate graphs from data
│   ├── KnowledgeGraph/                   # Knowledge graph generation and display
│   │   ├── __init__.py                 
│   │   ├── Display_graph.py              # Script to display generated graphs
│   │   └── generate_knowledge_graph.py   # Script to generate knowledge graph
│   ├── logs/                             # Logs folder for storing logs
│   ├── Test/                             # Test files for unit testing and validation
│   ├── Unstructured_IO/                  # Folder for handling unstructured data
│   │   ├── __init__.py                 
│   │   └── Pre_processing.py             # Pre-processing of unstructured data
│   ├── Utils/                            # Utility functions
│   │    └── helper.py                    # Helper functions used across the app
│   └── main.py                           # Main script to run the application
├── .gitignore                            # Git ignore file to exclude certain files from version control
├── README.md                             # Readme file for project information and setup
└── requirements.txt                      # List of dependencies required to run the project
```

---
