import shutil
import os
from falkordb import FalkorDB
from config import conf
def clear_output_directory(output_dir):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        os.makedirs(output_dir)
        print(f"Output directory {output_dir} cleared.")

def ifGraph_exist(graph_name):
    db = FalkorDB(
            host=conf.FALKOR_HOST,
            port=conf.PORTS,
            username=conf.FALKOR_USERNAME,
            password=conf.FALKOR_PASSWORD,
        )
    graph = db.select_graph(graph_name)
    if graph:
        print(f'graph {graph.name} found')
        return graph
    else: None


def isGraph_exist(graph_name):
    db = FalkorDB(
            host=conf.FALKOR_HOST,
            port=conf.PORTS,
            username=conf.FALKOR_USERNAME,
            password=conf.FALKOR_PASSWORD,
        )
    graph = db.select_graph(graph_name)
    query = "MATCH (n) RETURN n"
    isNodeExist=graph.query(query).result_set
    if isNodeExist:
        print(f'graph {graph.name} found')
        return graph
    else: 
        print(f'graph {graph.name} Not found')
        return None