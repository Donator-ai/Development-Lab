# IATI Data Dump - XML File Concatenation

IATI is an open data sharing framework and XML standard that's widely used across the humanitarian community by aid organization, donors and others to report aid activities. Currently over 1500 organization are using IATI's XML standard to share information on aid activities. IATI's entire corpus contains information on over 1 million aid activities.

A daily **snapshot** of IATI's entire corpus is accessible via the [IATI Data Dump](https://iati-data-dump.codeforiati.org/). The Data Dump's downloadable folder contains hundreds of sub-folders organized by organization. These contain one or more individual XML files. Likewise, each file contains information on one or more individual aid activities.

## Resources

Some initial work has been carried out looking at how to concatenate XML files stored in the IATI Data Dump. The code can be found [here](https://github.com/Partnership-on-Generative-AI/Workspace/blob/main/resources/ParsingXMLs2.py)

## Project

![XML Files](https://github.com/Partnership-on-Generative-AI/Workspace/blob/main/media/IATI_XML_Concatenate.png)

IATI Data Dump makes a zipped snapshot of IATI’s entire corpus accessible to **download**. The snapshot is refreshed on a daily basis so the snapshot can change from day-to-day based on organizations updating their individual IATI XML files or adding new ones.

As a project, we are going to work out how to download daily IATI data snapshots from the IATI Data Dump and concatenate each snapshot’s hundreds of XML files into a single large day-stamped whole IATI XML file. These files will be stored in a bucket accessible to Partnership members and others.

As a first objective, we’d like to work out and refine how to generate an initial whole IATI XML file to study from an IATI Data Dump snapshot and work out how to run the necessary code from a **Digital Ocean** workspace and how to make the file accessible to others. Next we would like to work out how to automate the file generation process and begin generating day-stamped files or weekly or monthly files depending on project needs.

## Concatenation Conventions

Individual IATI XML files typically contain multiple blocks of XML code, with each block containing information on a different aid activity. Some XML files contain information on  one or a couple of aid activities while other files can contain information on hundreds of activities.

We would like to establish conventions on how to handle the concatenation of files. Because IATI Data Dump’s downloadable folder contains hundreds of sub-folders organized by publishing organization which in turn each contain multiple files, we would like to preserve Organization folder and file tile information. Thus it will be necessary to decide how to label and nest information, enabling all the information to be stored in a single large XML file.

We'd like to experiment with separating the XML files by publishing organization and then by files stored in organization folders.

As a side project, it might be advisable for tracking and other purposes to develop an auxiliary program to collect the names of organization folders and the titles of files stored in these folders. This information can be used to support and verify proper concatenation and labeling. 
