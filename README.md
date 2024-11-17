# FrontStory
FrontStory ServerSide - TEST

## Overview
Transform your campaign data into actionable insights with automated processing of cost and revenue metrics. Built with Python and Pandas for efficient data handling and timezone-aware calculations.

## Key Features
- Automated data processing pipeline
- Timezone handling (EST to UTC conversion)
- Advanced metric calculations
- Multiple report formats (CSV/JSON)
- Campaign performance tracking

## Installation
```bash
git clone https://github.com/DatobyWS/FrontStory.git

pip install -r requirements.txt
```

##Usage
from data_processor import DataProcessor
from report_generator import ReportGenerator

processor = DataProcessor(
    cost_url="data/costs.csv",
    revenue_url="data/revenue.csv"
)

generator = ReportGenerator(processor)
report = generator.generate(output_format='csv')

Feel free to contact me if you have any questions or need further clarifications about the implementation.
Best regards,  
Shahar Migris 
linkedin - https://www.linkedin.com/in/shahar-migris/
