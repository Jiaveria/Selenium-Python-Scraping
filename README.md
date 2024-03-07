# New Zealand Migration Data Scraper

Welcome to the New Zealand Migration Data Scraper repository! This project offer Python script that automate the process of extracting data from the New Zealand migration data explorer website. The website provides various data sets related to migration, including information about students, work visitors, and population statistics. Users can apply different filters and variables to customize the data sets and visualize the data through charts and tables. The script in this repository enable users to dynamically select filters, retrieve the desired data sets, and download them as CSV files.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

This repository contains Python script that automate the process of extracting data from the New Zealand migration dataset website. By leveraging Selenium, a powerful web automation tool, the script enable users to dynamically apply filters and variables to customize the data sets according to their requirements. The scraping process includes waiting for the DOM to populate using Python's `time.sleep` to ensure the selection of filters via the dashboard occurs only when the necessary elements are available.

## Features

- **Automated Data Extraction:** Dynamically apply filters and variables to retrieve customized data sets.
- **Dynamic Selection:** Utilize Selenium to interact with the website's dashboard and select filters dynamically.
- **CSV Data Export:** Download the extracted data sets as CSV files.

## Prerequisites

Before using the scripts in this repository, ensure you have the following prerequisites installed:

- Python 
- Selenium

## Installation

1. Clone the repository:


2. Navigate to the project directory:


3. Install dependencies:


## Usage

1. Navigate to the directory containing the desired scraping script.
2. Execute the script using Python:
3. Once the scraping process is complete, the extracted data will be saved as CSV files in the specified location.


