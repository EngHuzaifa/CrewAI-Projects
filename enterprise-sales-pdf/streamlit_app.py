import streamlit as st 
import base64

from enterprise_sales_pdf.crew import SalesPdfCrew  
from markdown_pdf import MarkdownPdf, Section  


def generate_pdf_content(result_raw, lead_company):
    pdf = MarkdownPdf(toc_level=1)
    pdf.add_section(Section(result_raw))
    pdf_filename = f"{lead_company}_sales_pdf.pdf"
    pdf.save(pdf_filename)
    with open(pdf_filename, "rb") as f:
        pdf_bytes = f.read()
    return pdf_filename, pdf_bytes


def main():
    st.set_page_config(page_title="Enterprise Sales PDF Generator", layout="wide")
    st.title("Enterprise Sales PDF Generator")
    st.markdown("Generate a professional Sales PDF using our CrewAI-powered tool.")

    st.sidebar.header("Input Details")
    company_name = st.sidebar.text_input("Company Name", "PIAIC")
    product_name = st.sidebar.text_input("Product Name", "Enterprise Sales PDF")
    website = st.sidebar.text_input("Website", "https://www.piaic.org")
    sales_rep_name = st.sidebar.text_input("Sales Rep Name", "Muhammad Huzaifa")
    sales_rep_contact = st.sidebar.text_input("Sales Rep Contact", "muhammadhuzaifaai890@gmail.com")

    lead_name = st.sidebar.text_input("Lead Name", "Alice Johnson")
    lead_company = st.sidebar.text_input("Lead Company", "Innovative Solutions Inc.")
    lead_industry = st.sidebar.text_input("Lead Industry", "Information Technology")

    if st.button("Generate Sales PDF"):
        with st.spinner("Generating PDF, please wait..."):
            inputs = {
                "company_info": {
                    "name": company_name,
                    "product_name": product_name,
                    "website": website,
                    "sales_rep_name": sales_rep_name,
                    "sales_rep_contact": sales_rep_contact,
                },
                "lead_info": {
                    "name": lead_name,
                    "company": lead_company,
                    "industry": lead_industry,
                },
            }
            result = SalesPdfCrew().crew().kickoff(inputs=inputs)
            pdf_filename, pdf_bytes = generate_pdf_content(result.raw, lead_company)
            st.success("PDF Generated Successfully!")
            b64 = base64.b64encode(pdf_bytes).decode('utf-8')
            href = f'<a href="data:application/octet-stream;base64,{b64}" download="{pdf_filename}">Download PDF</a>'
            st.markdown(href, unsafe_allow_html=True)


if __name__ == "__main__":
    main() 