import pandas as pd
from zenml.pipelines import pipeline
from zenml.steps import step

@step
class IngestData:
    def __init__(self) -> None:
        self.data_path = None

    def get_data(self,data_path:str) -> pd.DataFrame:
        self.data_path = data_path
        df = pd.read_csv(self.data_path)
        return df 