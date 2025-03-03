import os
import xml.etree.ElementTree as ET

def parse_xml_filename(xml_file_path):
    """
    Parses the XML file name from the given path.

    Args:
        xml_file_path (str): The path to the XML file.

    Returns:
        str: The name of the XML file without the extension, or None if an error occurs.
    """
    try:
        tree = ET.parse(xml_file_path)
        return os.path.splitext(os.path.basename(xml_file_path))[0]
    except ET.ParseError:
        print(f"Error: Could not parse XML file: {xml_file_path}")
        return None
    except FileNotFoundError:
         print(f"Error: File not found: {xml_file_path}")
         return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
file_path = "example.xml"
# Create a dummy xml file for testing
with open(file_path, 'w') as f:
    f.write("<root><element>text</element></root>")
file_name = parse_xml_filename(file_path)

if file_name:
    print(f"The XML file name is: {file_name}")
else:
    print("Failed to parse the XML file name.")

os.remove(file_path) # Remove the dummy file
