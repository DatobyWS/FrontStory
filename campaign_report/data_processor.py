import pandas as pd
import pytz
from typing import Tuple, Optional
from datetime import datetime

class DataProcessor:
    def __init__(self, cost_url: str, revenue_url: str):
        self.cost_url = cost_url
        self.revenue_url = revenue_url
        self.est_tz = pytz.timezone('US/Eastern')
        self.utc_tz = pytz.UTC

    def load_and_process(self, date_from: Optional[str] = None, date_to: Optional[str] = None) -> pd.DataFrame:
        print("Starting data processing...")
        cost_df, revenue_df = self._load_data()
        merged_data = self._merge_data(cost_df, revenue_df)
        return self._calculate_metrics(merged_data)

    def _load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        cost_df = pd.read_csv(self.cost_url)
        revenue_df = pd.read_csv(self.revenue_url)  

        for df in [cost_df, revenue_df]:
            df['data_date'] = pd.to_datetime(df['data_date'], format='%m/%d/%y %H:%M')
            df['data_date'] = df['data_date'].apply(
                lambda x: self.est_tz.localize(x).astimezone(self.utc_tz)
            )
        
        print("Sample data loaded:")
        print("Cost columns:", cost_df.columns.tolist())
        print("Revenue columns:", revenue_df.columns.tolist())
        
        return cost_df, revenue_df

    def _merge_data(self, cost_df: pd.DataFrame, revenue_df: pd.DataFrame) -> pd.DataFrame:
        # Merge on matching columns
        merged_df = pd.merge(
            cost_df,
            revenue_df,
            on=['data_date', 'campaign_id']
        )
        print("Merged columns:", merged_df.columns.tolist())
        return merged_df

    def _calculate_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        # Convert date format
        df['date'] = pd.to_datetime(df['data_date'], format='%m/%d/%y %H:%M').dt.strftime('%Y/%m/%d')
        
        metrics = {
            'total_revenue': df['revenue'],
            'total_cost': df['cost'],
            'total_profit': df['revenue'] - df['cost'],
            'total_clicks': df['clicks'],
            'avg_cpc': df['cost'] / df['clicks'],
            'total_roi': (df['revenue'] / df['cost']).replace([float('inf'), -float('inf')], 0),
            'hourly_avg_revenue': df['revenue'] / 24,
            'positive_profit_hours': ((df['revenue'] - df['cost']) > 0).astype(int) * 24
        }
        
        result_df = df.assign(**metrics)
        
        final_columns = [
            'date',
            'campaign_id',
            'campaign_name',
            'total_revenue',
            'total_cost',
            'total_profit',
            'total_clicks',
            'total_roi',
            'avg_cpc',
            'hourly_avg_revenue',
            'positive_profit_hours'
        ]
        
        return result_df[final_columns]