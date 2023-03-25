# Resume Validator

This Python script validates a resume by checking for the presence of certain skills and experience in a PDF file. It uses the `pdfminer` library to extract text from the PDF and then searches for the specified keywords.

## Prerequisites

To run this script, you need to have Python installed on your system. Additionally, you'll need to install the `pdfminer` library. You can install it using pip:

```
pip install pdfminer.six
```

## Usage

To use the script, run the following command in your terminal, replacing `<filename>` with the path to the PDF file you want to validate:

```
python validate_resume.py <filename>
```

The script will print the extracted text from the PDF and then check for the presence of the required skills and experience. If any of the specified keywords are missing, the script will print a message indicating which ones were not found. If all the keywords are found, the script will print "Resume is valid."

## Customization

To customize the script to check for different skills or experience, modify the `required_skills` and `required_experience` lists in the `validate_resume()` function. Add or remove keywords as needed to match your specific requirements.
