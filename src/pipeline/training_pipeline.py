from src.components.data_ingestion import DataIngestion


class TrainPipeline:
    def starting_data_ingestion(self):
        
        data_ingestion: DataIngestion = DataIngestion() 
        return data_ingestion.data_ingestion_initialize()
    
    def run_pipeline(self):
        start_data_ingestion = self.starting_data_ingestion()
    