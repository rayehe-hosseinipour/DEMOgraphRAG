from GraphPipline.Retrieve_and_display_graph import GraphDisplayPipeline

if __name__ == "__main__":
    # Run the Graph Display Pipeline
    print("Running Graph Display Pipeline...")
    graph_display = GraphDisplayPipeline(graph_name="justTest3")
    graph_display.display_graph(image_dir="Data/graph_Image")
