# Window Media Player Testing Setup

## Prerequisites
Before running the tests, ensure you have the following installed:
- PyCharm preferably
- Python (version 3.x recommended)
- Behave (install using `pip install behave`)
- Pywinauto (install using `pip install pywinauto`)
- behave-html-formatter (install using `pip install behave-html-formatter`)

## Running Tests
To execute the tests, follow these commands:

1. **Run all feature files and scenarios:** behave
2. **Run scenarios with a specific tag:** behave --tags=@tag_name

## Generate Test Cases Report
To generate report, follow these commands:

1. **Run**:behave -f behave_html_formatter:HTMLFormatter -o ./report.html




