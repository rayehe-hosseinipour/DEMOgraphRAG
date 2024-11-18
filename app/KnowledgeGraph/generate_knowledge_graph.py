from graphrag_sdk import KnowledgeGraph, KnowledgeGraphModelConfig, Ontology
from graphrag_sdk.models.gemini import GeminiGenerativeModel
import json
import os
from graphrag_sdk.source import Source
from dotenv import load_dotenv
from config import conf
from Utils.helper import ifGraph_exist
class KnowledgeGraphBuilder:
    """
    This class is responsible for generating a knowledge graph based on
    structured JSON data using the 'graphrag_sdk' library.

    Attributes:
        output_dir (str): Directory containing JSON files to process.
        model_name (str): Name of the generative model for ontology creation.
        conf (module): Configuration module containing host and authentication details.
        boundaries (str or None): Optional boundaries for the ontology generation.
        graph_name (str): Name for the generated knowledge graph.
    """
    def __init__(self, output_dir: str , graph_name:str, boundaries:str=None):
        
        self.output_dir = output_dir
        self.model_name = conf.LLM_MODEL 
        self.boundaries = boundaries
        self.graph_name = graph_name
        self.sources = []  
        self.graph = ifGraph_exist(self.graph_name) if ifGraph_exist(self.graph_name) else None
        load_dotenv()  

    def reset_graph(self):
        """
        Resets the knowledge graph to a clean state.
        """
        if self.graph:
            self.graph.delete()  # Assuming 'clear()' is a method provided by your graph library
            print(f"Graph {self.graph_name} has been reset.")
        else:
            print("No graph found to reset.")

    def load_sources(self):
        """
        Loads the JSON files from the output directory and initializes
        source objects for knowledge graph processing.
        """
        for file in os.listdir(self.output_dir):
            self.sources.append(Source(os.path.join(self.output_dir, file)))
        print(f"Loaded {len(self.sources)} source(s).")

    def generate_ontology(self):
        """
        Generates the ontology based on the sources and saves it as a JSON file.
        """
        self.model = GeminiGenerativeModel(model_name=self.model_name)

        if not self.sources:
            raise ValueError("No sources loaded. Please run `load_sources()` first.")
        ontology = Ontology.from_sources(
            sources=self.sources, 
            boundaries=self.boundaries,  # Optional boundaries
            model=self.model  
        )
        # Save ontology as JSON
        with open("ontology.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(ontology.to_json(), indent=2))
        print("Ontology saved to ontology.json")

    def build_knowledge_graph(self):
        """
        Builds the knowledge graph using the ontology and processes the sources.

        Assumes that an approved ontology JSON file exists as 'ontology.json'.
        """
        # Load the ontology from a previously saved JSON file
        ontology_file = "ontology.json"
        with open(ontology_file, "r", encoding="utf-8") as file:
            ontology = Ontology.from_json(json.loads(file.read()))

        # Initialize the knowledge graph with the ontology and model
        kg = KnowledgeGraph(
            name=self.graph_name,
            model_config=KnowledgeGraphModelConfig.with_model(model=self.model),
            ontology=ontology,
            host=conf.FALKOR_HOST,
            port=conf.PORTS,
            username=conf.FALKOR_USERNAME,
            password=conf.FALKOR_PASSWORD
        )

        # Process the sources into the knowledge graph
        kg.process_sources(self.sources)
        print("Knowledge graph processed successfully.")
