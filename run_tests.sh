#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Run behave tests and generate report
behave --format behave_html_formatter:HTMLFormatter --outfile TestResults/test_report.html
