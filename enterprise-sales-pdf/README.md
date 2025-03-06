# Enterprise Sales PDF

A project integrating CrewAI flows into the Enterprise Sales PDF solution.

## Setup

Ensure you have Python 3.11+ installed.

Install dependencies:

    pip install -r requirements.txt

## Available Commands (as defined in pyproject.toml)

- enterprise-sales-pdf: Runs the main function from enterprise_sales_pdf module.
- run_crew: Runs the crew portion using enterprise_sales_pdf.main:run.
- train: Runs the training function using enterprise_sales_pdf.main:train.
- replay: Runs the replay function using enterprise_sales_pdf.main:replay.
- test: Runs the tests using enterprise_sales_pdf.main:test.
- run_flow: Runs the CrewAI flow using flow.main:run_flow.

## Running CrewAI Flows

To run the CrewAI flow, you can either:

1. Run directly via the script command:

       enterprise-sales-pdf run_flow

2. Or run the module directly:

       python -m flow.main

## CrewAI Planning

Update this section with additional planning and usage details for integrating CrewAI flows as needed.
