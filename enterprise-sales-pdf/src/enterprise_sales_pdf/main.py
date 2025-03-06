#!/usr/bin/env python
import sys

from markdown_pdf import MarkdownPdf, Section

from enterprise_sales_pdf.crew import SalesPdfCrew




def run():
    """
    Run the crew.
    """
    inputs = {
        "company_info": {
            "name": "crewai",
            "product_name": "Enterprise Sales PDF Service",
            "website": "https://www.crewai.com",
            "sales_rep_name": "Muhammad Huzaifa",
            "sales_rep_contact": "muhammadhuzaifaai890@gmail.com",
        },
        "lead_info": {
            "name": "Alice Johnson",
            "company": "Innovative Solutions Inc.",
            "industry": "Information Technology",
        },
    }

    result = SalesPdfCrew().crew().kickoff(inputs=inputs)

    pdf = MarkdownPdf(toc_level=1)
    pdf.add_section(Section(result.raw))
    pdf.save(f"{inputs['lead_info']['company']}_sales_pdf.pdf")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        SalesPdfCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SalesPdfCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        SalesPdfCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
