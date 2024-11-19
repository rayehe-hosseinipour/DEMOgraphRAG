import os
from dotenv import load_dotenv
from unstructured_ingest.v2.pipeline.pipeline import Pipeline
from unstructured_ingest.v2.interfaces import ProcessorConfig
from unstructured_ingest.v2.processes.connectors.local import (
    LocalIndexerConfig,
    LocalDownloaderConfig,
    LocalConnectionConfig,
    LocalUploaderConfig
)
from unstructured_ingest.v2.processes.partitioner import PartitionerConfig

class UnstructuredDataProcessor:
    """
    This class handles the conversion of unstructured data (PDF, XML, etc.) 
    into JSON format using the 'unstructured_ingest' library.

    Attributes:
        input_path (str): Directory containing the unstructured data files.
        output_dir (str): Directory where processed JSON files will be saved.
    """
    def __init__(self, input_path: str, output_dir: str):
        self.input_path = input_path
        self.output_dir = output_dir
        load_dotenv()  # Load environment variables from .env file

    def run_pipeline(self):
        """
        Executes the data processing pipeline to convert unstructured data
        into JSON format and store the results in the output directory.
        """
        pipeline = Pipeline.from_configs(
            context=ProcessorConfig(),
            indexer_config=LocalIndexerConfig(input_path=self.input_path),
            downloader_config=LocalDownloaderConfig(),
            source_connection_config=LocalConnectionConfig(),
            partitioner_config=PartitionerConfig(
                partition_by_api=True,
                api_key=os.getenv("UNSTRUCTURED_API_KEY"),
                partition_endpoint=os.getenv("UNSTRUCTURED_API_URL"),
                strategy="hi_res",
                additional_partition_args={
                    "split_pdf_page": True,
                    "split_pdf_allow_failed": True,
                    "split_pdf_concurrency_level": 15,
                }
            ),
            uploader_config=LocalUploaderConfig(output_dir=self.output_dir),
        )
        pipeline.run()
