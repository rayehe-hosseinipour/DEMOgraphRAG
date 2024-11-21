import networkx as nx
import matplotlib.pyplot as plt
from falkordb import FalkorDB
import os
class GraphVisualizer:
    """
    This class connects to the FalkorDB database and visualizes the knowledge graph.

    Attributes:
        db (FalkorDB): Instance of the FalkorDB database client.
        graph_name (str): Name of the knowledge graph to retrieve.
    """
    def __init__(self, host: str, port: int, username: str, password: str, graph_name: str):
        self.db = FalkorDB(
            host=host,
            port=port,
            username=username,
            password=password
        )
        self.graph_name = graph_name

    def display_graph(self,image_dir,image_name, query: str = "MATCH (n)-[r]->(m) RETURN n, r, m"):
        """
        Displays the knowledge graph by querying the database and rendering it with NetworkX.

        Args:
            query (str): Cypher query to retrieve graph relationships. Defaults to a basic MATCH query.
        """
        # Retrieve the graph from FalkorDB
        graph = self.db.select_graph(self.graph_name)
        graph_ret = graph.query(query).result_set

        # Build a directed graph using NetworkX
        G = nx.DiGraph()

        for record in graph_ret:
            # Extract node names
            source = record[0].properties.get('name', 'Unnamed Node')
            target = record[2].properties.get('name', 'Unnamed Node')

            # Extract relationship
            relationship = str(record[1].relation)  # Convert relationship to a string

            # Add nodes and edges to the graph
            G.add_node(source)
            G.add_node(target)
            G.add_edge(source, target, label=relationship)

        # Generate the layout and display the graph
        pos = nx.spring_layout(G, k=2, iterations=50)
        plt.figure(figsize=(20, 15))
        node_size = max(1000, len(G.nodes) * 50)
        font_size = min(12, 300 // len(G.nodes))
        nx.draw(
            G, pos, with_labels=True,
            node_color="skyblue", node_size=node_size,
            font_size=font_size, font_weight="bold"
        )
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

        plt.title("Graph Visualization")
        file_path = os.path.join(image_dir, f'{image_name}.png')
        plt.savefig(file_path)
        print(f"Graph saved as {file_path}")
        plt.show()
