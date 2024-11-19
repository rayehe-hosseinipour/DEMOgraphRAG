from GraphPipline import graph_generating_pipeline as gf

if __name__ == "__main__":
    path_to_prompt = './prompts/boundaries.txt'
    with open(path_to_prompt, 'r', encoding='utf-8') as file:
        boundaries = file.read()   
    print(boundaries)    
    # Initialize the pipeline
    pipeline = gf.GraphGeneratorPipeline(
        input_path="Data/Input",
        output_dir="Data/Output",
        graph_name="justTest0",
        boundaries=boundaries
    )
    
    # Run the pipeline
    pipeline.run_pipeline()
