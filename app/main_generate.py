from GraphPipline.Generate_graph_pipeline import GraphGeneratorPipeline
"""
help ::
- if you have prompt's or any text that can guide the llm to extract the entity's and relations, in this this Path : prompts/ , in file that name boundaries.txt add your prompt
- if you want to reset the graph and add the new one just set reset_graph to True.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
description :
this file is used for to run a pipeline that generate the knowledge Graph
in input_path you must add your input dir
in output_dir you must set your output dir
graph_name you must set a name for your graph or if you want to add a document's graph into the graph that exist just set the name of the graph that you know already exist
"""
if __name__ == "__main__":
    # Load boundaries from the file
    path_to_prompt = './prompts/boundaries.txt'
    with open(path_to_prompt, 'r', encoding='utf-8') as file:
        boundaries = file.read()
    
    # Run the Graph Generation Pipeline
    print("Running Graph Generation Pipeline...")
    graph_generator = GraphGeneratorPipeline(
        input_path="Data/Input",
        output_dir="Data/Output",
        graph_name="justTest1",
        #reset_graph=True,
        #boundaries=boundaries
    )
    graph_generator.run_pipeline()
