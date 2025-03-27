import os
from lxml import etree as ET
from datetime import datetime
from tqdm import tqdm
import gzip


def sanitize_comment_text(comment_text):
    """Helper function to sanitize comment text for XML"""
    # Replace '--' with '-'
    comment_text = comment_text.replace('--', '-')
    # Ensure the comment does not end with '-'
    if comment_text.endswith('-'):
        comment_text = comment_text[:-1]  # Remove the trailing '-'
    return comment_text


def add_comment_to_xml(writer, comment_text):
    """Helper function to add comments into the XML"""
    # Sanitize the comment text
    comment_text = sanitize_comment_text(comment_text)
    # Create the comment and write it to the file
    comment = ET.Comment(comment_text)
    writer.write(ET.tostring(comment, encoding='unicode'))


def parse_and_concatenate_xml(org_folder_path, writer, org_name):
    """Function to parse and concatenate XML files from an organization folder"""
    # Get a list of all XML files in the folder
    xml_files = [f for f in os.listdir(org_folder_path) if f.endswith(".xml")]

    # Use tqdm to add a progress bar
    for filename in tqdm(xml_files, desc=f"Processing {org_name}", unit="file"):
        xml_file_path = os.path.join(org_folder_path, filename)
        try:
            # Add a comment indicating which file is being processed
            add_comment_to_xml(writer, f"Processing file: {filename} from Organization: {org_name}")

            # Parse the XML file
            for _, element in ET.iterparse(xml_file_path, events=("end",), tag="iati-activity"):
                # Write each activity element to the master XML
                writer.write(ET.tostring(element, encoding='unicode', pretty_print=True))
                element.clear()  # Free memory

        except ET.ParseError:
            # Silently ignore parsing errors
            pass


def main():
    main_folder_path = './data/iati-data-main/data/'  # Path to the main folder containing all organizations
    output_file_path = './output.xml.gz'  # Compressed output file

    # Open a gzip file for writing
    with gzip.open(output_file_path, 'wt', encoding='utf-8') as f:
        # Write the XML declaration and root element
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<root>\n')

        # Add a timestamp to the master file to track the date it was generated
        add_comment_to_xml(f, f"Master XML file generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Get a list of all organization folders
        org_folders = [f for f in os.listdir(main_folder_path) if os.path.isdir(os.path.join(main_folder_path, f))]

        # Use tqdm to add a progress bar for organization folders
        for org_folder in tqdm(org_folders, desc="Processing Organizations", unit="org"):
            org_folder_path = os.path.join(main_folder_path, org_folder)

            # Add a comment to separate organizations in the master XML
            add_comment_to_xml(f, f"Start of Organization: {org_folder}")

            # Parse and concatenate XML files for the current organization
            parse_and_concatenate_xml(org_folder_path, f, org_folder)

            # Add a comment to indicate the end of the organization
            add_comment_to_xml(f, f"End of Organization: {org_folder}")

        # Close the root element
        f.write('</root>')

    print(f"Master XML file saved to {output_file_path}")


if __name__ == "__main__":
    main()
