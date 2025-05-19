#!/usr/bin/env python3
"""
Regex Data Extraction Tool

This program extracts various data types from text using regular expressions.
"""

import re
import sys

# Define regex patterns
patterns = {
    "email": r"\b[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9.-]+\.)[a-zA-Z]{2,}\b",
    "url": r"https?://[^\s/$.?#].[^\s]*",
    "phone": r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b",
    "credit_card": r"\b(?:\d{4}[-.\s]?){3}\d{4}\b",
    "currency": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?",
    "time": r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b",
    "html_tag": r"<[a-z]+(?:\s+[a-z-]+(?:=(?:\"[^\"]*\"|\'[^\']*\'|[^>\s]+))?)*\s*/?>"
}

def extract_data(patterns, text):
    """
    Extract various data types from text using regex patterns.
    
    Args:
        patterns: Dictionary of regex patterns
        text: Text to extract data from
        
    Returns:
        Dictionary with data types as keys and lists of matches as values
    """
    results = {}
    
    for label, regex in patterns.items():
        matches = re.findall(regex, text, re.IGNORECASE)
        results[label] = matches
    
    return results

def display_results(results):
    """
    Display extraction results in a formatted way.
    
    Args:
        results: Dictionary with extraction results
    """
    print("\n=== EXTRACTION RESULTS ===\n")
    
    total_matches = sum(len(matches) for matches in results.values())
    print(f"Total items found: {total_matches}\n")
    
    for data_type, matches in results.items():
        print(f"{data_type.upper()} matches ({len(matches)} found):")
        print("-" * 40)
        
        if matches:
            for match in matches:
                print(f"  • {match}")
        else:
            print("  No matches found.")
        
        print()  # Empty line between sections

def process_file(file_path):
    """
    Extract data from a file.
    
    Args:
        file_path: Path to the file to process
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        
        results = extract_data(patterns, text)
        display_results(results)
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

def main():
    """Main function to process arguments and run extraction."""
    
    # Sample data for demonstration
    sample_data = """
    Email: user@example.com
    Another Email: firstname.lastname@company.co.uk
    
    Website: https://www.example.com
    Subdomain URL: https://subdomain.example.org/page
    
    Phone1: (123) 456-7890
    Phone2: 123-456-7890
    Phone3: 123.456.7890
    
    Price: $19.99 and $1,234.56
    
    Card1: 1234 5678 9012 3456
    Card2: 1234-5678-9012-3456
    
    Time1: 14:30
    Time2: 2:30 PM
    
    HTML: <p>This is a paragraph</p>
    More HTML: <div class="example">Example</div>
    Image: <img src="image.jpg" alt="description">
    """
    
    # Check if a file path was provided
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        process_file(file_path)
    else:
        # No file provided, use sample data
        print("No file provided. Using sample data for demonstration.")
        results = extract_data(patterns, sample_data)
        display_results(results)
        print("To process a file, run: python regex_extractor.py filename.txt")

if __name__ == "__main__":
    main()


