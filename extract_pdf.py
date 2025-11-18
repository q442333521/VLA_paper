#!/usr/bin/env python3
"""Extract text from PDF file in chunks."""

import PyPDF2
import sys

def extract_pdf_text(pdf_path, output_path):
    """Extract text from PDF and save to file."""
    print(f"Opening PDF: {pdf_path}")

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        print(f"Total pages: {num_pages}")

        all_text = []

        for page_num in range(num_pages):
            if page_num % 10 == 0:
                print(f"Processing page {page_num + 1}/{num_pages}...")

            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            all_text.append(f"\n--- Page {page_num + 1} ---\n")
            all_text.append(text)

        # Write to output file
        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write(''.join(all_text))

        print(f"Extraction complete! Saved to: {output_path}")
        print(f"Total characters: {len(''.join(all_text))}")

if __name__ == "__main__":
    pdf_path = "/home/user/VLA_paper/pistar06.pdf"
    output_path = "/home/user/VLA_paper/pistar06_text.txt"
    extract_pdf_text(pdf_path, output_path)
