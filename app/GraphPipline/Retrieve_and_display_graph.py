from KnowledgeGraph.Display_graph import GraphVisualizer
from config import conf

class GraphDisplayPipeline:
    """
    Pipeline for displaying a pre-existing knowledge graph.

    Attributes:
        graph_name (str): Name of the knowledge graph to be displayed.
    """
    def __init__(self, graph_name: str):
        self.graph_name = graph_name

    def display_graph(self):
        """
        Connects to and displays the knowledge graph.
        """
        print("Step 1: Displaying the knowledge graph...")
        visualizer = GraphVisualizer(
            host=conf.FALKOR_HOST,
            port=conf.PORTS,
            username=conf.FALKOR_USERNAME,
            password=conf.FALKOR_PASSWORD,
            graph_name=self.graph_name
        )
        visualizer.display_graph()
