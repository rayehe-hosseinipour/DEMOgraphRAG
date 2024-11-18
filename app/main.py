from GraphPipline import graph_generating_pipeline as gf
from config import conf

if __name__ == "__main__":
    # Initialize the pipeline
    boundaries = """
Entities: Look for nouns, particularly proper nouns, technical terms, and concepts. Entities can be people, places, organizations, technologies, fields of study, systems, and tools.
Examples:

Artificial Intelligence
Machine Learning
Healthcare
AI Ethics
Quantum Computing
Alan Turing
Autonomous Systems
Key Terms and Concepts: Pay attention to specific jargon or technical terms that define the scope of AI, its subfields, and its applications. These terms typically refer to techniques, models, or theories within AI and technology.

Examples:

Supervised Learning
Unsupervised Learning
Reinforcement Learning
Big Data
IoT (Internet of Things)
Cloud Computing
Autonomous Vehicles
Predictive Analytics
Relationships (Actions, Effects, Connections): Identify verbs or phrases that describe relationships between entities. Relationships describe how one entity is connected to another, how they influence each other, or how they work together.

Examples:

is a subfield of
is impacted by
can perform
addresses
requires
supports
is related to
helps with
raises questions about
Contextual Phrases: Look for sentences or phrases that define the scope, effects, or attributes of the entities. These often clarify the type of relationship, whether it's a causal one, an influencing factor, or a dependency.

Examples:

“Machine Learning models require large volumes of data to train effectively.”
“AI ethics addresses bias in AI models.”
“Quantum computing supports AI development by providing greater computational power.”
"""
    pipeline = gf.GraphGeneratorPipeline(
        input_path="Data/Input",
        output_dir="Data/Output",
        graph_name="justTest2",
        boundaries=boundaries
    )
    
    # Run the pipeline
    pipeline.run_pipeline()
