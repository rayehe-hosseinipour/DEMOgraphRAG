from KnowledgeGraph.generate_knowledge_graph import KnowledgeGraphBuilder
from Unstructured_IO.Pre_processing import UnstructuredDataProcessor
from Utils.helper import clear_output_directory, isGraph_exist

class GraphGeneratorPipeline:
    """
    Pipeline for processing unstructured data and generating a knowledge graph.

    Attributes:
        input_path (str): Directory containing the unstructured data files.
        output_dir (str): Directory where processed JSON files will be saved.
        graph_name (str): Name of the knowledge graph.
    """
    def __init__(self, input_path: str, output_dir: str, graph_name: str, boundaries: str = None, reset_graph: bool = False):
        self.input_path = input_path
        self.output_dir = output_dir
        self.graph_name = graph_name
        self.boundaries = boundaries
        self.reset_graph = reset_graph
        self.isgraphexist = isGraph_exist(graph_name=self.graph_name)
    def run_pipeline(self):
        """
        Executes the pipeline:
        1. Processes unstructured data to JSON.
        2. Generates and processes the knowledge graph.
        """
        print("Step 0: Clearing output directory...")
        clear_output_directory(self.output_dir)

        print("Step 1: Processing unstructured data...")
        processor = UnstructuredDataProcessor(input_path=self.input_path, output_dir=self.output_dir)
        processor.run_pipeline()

        print("Step 2: Generating the knowledge graph...")
        if self.reset_graph:
            self.isgraphexist.delete()
            print(f"Graph {self.graph_name} has been reset.")
        else:
            print("No need to reset.")

        graph_builder = KnowledgeGraphBuilder(
            output_dir=self.output_dir,
            graph_name=self.graph_name,
            boundaries=self.boundaries
        )
        graph_builder.load_sources()
        graph_builder.generate_ontology()
        graph_builder.build_knowledge_graph()
