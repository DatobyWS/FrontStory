from campaign_report.data_processor import DataProcessor
from campaign_report.report_generator import ReportGenerator

def main():
    print("Starting application...")
    
    COST_URL = "https://s3.amazonaws.com/frontstory-test-data/server-side/cost_1.csv"
    REVENUE_URL = "https://s3.amazonaws.com/frontstory-test-data/server-side/revenue_1.csv"

    print("Loading data from URLs...")
    processor = DataProcessor(COST_URL, REVENUE_URL)
    generator = ReportGenerator(processor)

    print("Processing report...")
    report = generator.generate(
        date_from='2023-01-01',
        date_to='2023-12-31',
        output_format='csv'
    )

    print("Writing report to file...")
    with open('campaign_report.csv', 'w') as f:
        f.write(report)
    print("Report generation complete!")

if __name__ == "__main__":
    main()