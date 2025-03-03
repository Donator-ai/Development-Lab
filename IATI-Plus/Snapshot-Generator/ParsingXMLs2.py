# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:20:04 2023

@author: user
"""

import os
import xml.etree.ElementTree as ET

def parse_and_concatenate_xml(org_folder_path, master_xml):
    for filename in os.listdir(org_folder_path):
        if filename.endswith(".xml"):
            xml_file_path = os.path.join(org_folder_path, filename)
            try:
                tree = ET.parse(xml_file_path)
                root = tree.getroot()

                # Append XML data to the master XML
                master_xml.extend(root)
            except ET.ParseError as e:
                print(f"Error parsing {xml_file_path}: {e}")

def main():
    main_folder_path = 'D:\Brent\iati-data-main\data'  # Replace with the actual path to your main folder
    master_xml = ET.Element('root')  # Create a root element for the master XML

    # Iterate through each organization folder
    for org_folder in os.listdir(main_folder_path):
        org_folder_path = os.path.join(main_folder_path, org_folder)

        if os.path.isdir(org_folder_path):
            # Parse and concatenate XML files for the current organization
            parse_and_concatenate_xml(org_folder_path, master_xml)

    # Create a new tree with the master XML and write it to a file
    master_tree = ET.ElementTree(master_xml)
    master_tree.write('D:/Brent/output/master.xml')  # Replace with the desired output file path

if __name__ == "__main__":
    main()