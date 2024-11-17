import pandas as pd
from .data_processor import DataProcessor
from typing import Optional

class ReportGenerator:
    def __init__(self, processor: DataProcessor):
        self.processor = processor

    def generate(self, date_from: Optional[str] = None, date_to: Optional[str] = None, output_format: str = 'csv') -> str:
        df = self.processor.load_and_process(date_from, date_to)
        
        if output_format == 'csv':
            return self._to_csv(df)
        return self._to_json(df)

    def _to_csv(self, df: pd.DataFrame) -> str:
        return df.to_csv(index=False)

    def _to_json(self, df: pd.DataFrame) -> str:
        return df.to_json(orient='records')
