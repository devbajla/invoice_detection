This project involved developing a 3 part system to automatically extract and tabulate key-field data from scans of invoices. Key field data includes invoice numbers, names, adddresses, dates etc. and this system automatically extracts this information from a scan. To do this, there are 3 steps:
1. Document Structure Detection:
   Using a custom YOLOv8 model trained on thousands of training images, this section creates bounding boxes around all the paragraphs, titles and tables in the invoice.
   Separating the document into different sections like this allows the OCR to be more accurate and to better understand which text is associated with each other.

2. Optical Character Recognition:
   By running an OCR program on each bounding box identified, we are able to extract the actual text from the document, broken up into different sections for each bounding box.

3. Key-Value Extraction:
   A trained HuggingFace NLP model is run on each text section identified. This program looks for the key field data mentioned previously, and tries to find the correct value associated with that key.
   After doing this for all the text sections in the document, it picks the value with the highest probability for each key and stores it in a CSV format to allow for further processing or logging.
