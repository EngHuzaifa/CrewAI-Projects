# Enterprise Sales PDF Generator

## Overview

The **Enterprise Sales PDF Generator** is a Python-based application that leverages the power of CrewAI, a multi-agent framework, to research, analyze, and generate a concise one-page sales PDF tailored to a specific lead company. This tool automates the process of gathering information about a target company and its industry, aligning your company's product offerings with the lead's needs, and creating compelling sales content. The output is a professionally formatted PDF designed to pitch your product effectively.

The application uses Streamlit for an interactive web interface, allowing users to input company and lead details, generate the PDF, and download it seamlessly. It integrates advanced tools like web scraping and search APIs to ensure accurate and up-to-date research.

## Features

- **Lead Research**: Gathers comprehensive information about the target company and its industry, including market position, challenges, and potential needs.
- **Product Alignment**: Analyzes your company's offerings and identifies how they address the lead's specific challenges.
- **Content Creation**: Generates a concise, one-page sales PDF with a structured format: an attention-grabbing headline, a brief introduction, four key features/benefits, a strong call-to-action, and contact information.
- **User-Friendly Interface**: Built with Streamlit for easy input and PDF generation directly from a web browser.
- **PDF Download**: Converts the generated Markdown content into a downloadable PDF file.


## Prerequisites

- Python 3.8+
- Git (for cloning the repository)
- A modern web browser (for the Streamlit interface)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/enterprise-sales-pdf.git
   cd enterprise-sales-pdf

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Dependencies
streamlit: Web interface framework.
crewai: Multi-agent orchestration framework.
crewai_tools: Tools for web scraping and search.
markdown-pdf: Converts Markdown to PDF.
Contributing
Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or support, contact muhammadhuzaifaai890@gmail.com.
