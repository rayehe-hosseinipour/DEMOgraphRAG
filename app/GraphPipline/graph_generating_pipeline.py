from KnowledgeGraph.Display_graph import GraphVisualizer
from KnowledgeGraph.generate_knowledge_graph import KnowledgeGraphBuilder
from Unstructured_IO.Pre_processing import UnstructuredDataProcessor
from config import conf
from Utils.helper import clear_output_directory

class GraphGeneratorPipeline:
    """
    A unified pipeline to process unstructured data, create a knowledge graph, and display it.

    Attributes:
        input_path (str): Directory containing the unstructured data files.
        output_dir (str): Directory where processed JSON files will be saved.
        model_name (str): The name of the generative model used in the knowledge graph.
        graph_name (str): Name of the knowledge graph for visualization.
    """
    def __init__(self, input_path: str, output_dir: str, graph_name: str , boundaries:str=None,reset_graph=True):
        self.input_path = input_path
        self.output_dir = output_dir
        self.graph_name = graph_name
        self.boundaries = boundaries
        self.reset_graph = reset_graph
    def run_pipeline(self):
        """
        Executes the entire pipeline:
        1. Converts unstructured data to JSON.
        2. Generates and processes the knowledge graph.
        3. Visualizes the knowledge graph.
        """
        print("Step 0: Clearing output directory...")
        clear_output_directory(self.output_dir)


        # Step 1: Process unstructured data into JSON
        print("Step 1: Processing unstructured data...")
        processor = UnstructuredDataProcessor(input_path=self.input_path, output_dir=self.output_dir)
        processor.run_pipeline()

        # Step 2: Generate and process the knowledge graph
        print("Step 2: Generating the knowledge graph...")
        graph_builder = KnowledgeGraphBuilder(
            output_dir=self.output_dir,
            graph_name=self.graph_name,
            boundaries=self.boundaries
        )
        if self.reset_graph:
            graph_builder.reset_graph()
        graph_builder.load_sources()
        graph_builder.generate_ontology()
        graph_builder.build_knowledge_graph()

        # Step 3: Display the knowledge graph
        print("Step 3: Displaying the knowledge graph...")
        visualizer = GraphVisualizer(
            host=conf.FALKOR_HOST,
            port=conf.PORTS,
            username=conf.FALKOR_USERNAME,
            password=conf.FALKOR_PASSWORD,
            graph_name=self.graph_name
        )
        visualizer.display_graph()
