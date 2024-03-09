## Table of contents
- [Setup Instructions](#setup-instructions)
- [File Desciptions](#file-descriptions)

## Setup Instructions

Please set up a python environment then run the requirements.txt file to install all necessary python dependancies. I recommend constructing a folder called Data in the repo and formatting it as below. Change the variable base path at the beginning of each file so that the script points to the correct folder.

```
Data
├── 0_PDF
│   ├── AER (** please make subfolders similar to AER for other journals too)
│   │    ├── aer_og
│   │    ├── aer_shards
│   │    ├── aer_shards_png
│   │    └── aer_wo_cover
│   ├── ECTA 
│   ├── JPE
│   ├── QJE
│   └── RES 
├── 1_JSON
│   ├── gpt
│   ├── tesseract
│   ├── bibtex
│   └── recon_helper_files
├── 2_CSV
│   ├── masterlist
│   ├── pivots
│   ├── processed
│   ├── scopus
│   ├── indicator_files
│   └── stats
│       ├── auth_network_stats
│       └── citation_network_stats
└── 3_GEXF
    ├── author_networks
    └── citations_networks
 
```

## File Descriptions

| Prefix | File Title/s   | Description | Inputs | Outputs | Comment |
| --- | --- | ------------------------------------- | ---| --- | --- |
| 010 | /010_cleaning_masterlists | Correct spelling errors, categorize the document via JSTOR title and combine the data obtained from SCOPUS with JSTOR masterlists by matching title and year | master lists, pivot lists and SCOPUS data | processed ...m_sco_du.xlsx files of combined scopus + masterlist + jstor and figures of SCOPUS coverage | Variable descriptions |
| 020 | 020_author_name_recon.ipynb | extracts all author names from the masterlists and reconciles them. | ...m_sco_du.xlsx files from 010 | JSON reconciliation files and author names + aliases in Dictionary format | Please see this page for an output format description |
| 020 | 020_split_pdfs.ipynb    | Detect and remove the JSTOR/journal cover page of each pdf and split each page into its own .pdf file and .png file | Masterlists, .pdf files | list of all pages for each journal (.csv), split pdf files and png files and articles with the cover page removed |  |
| 021 | 021_inventory.py | Script that goes through a list of pdf file names, displays the page and records observations about each page. | split pdf files + list of all pages for each journal | csv file containing indicator field recording observation on each page. |  |
| 022 | 
| 023 |
| 024 |
| 030 |
| 031 |
| 031 |
| 032 |