# Fertility Education Data

This repository contains the JSON data files for the Synagamy fertility education app.

## Files

- `data/Education_Topics.json` - Main education topics database containing 189 fertility-related topics with lay explanations, references, and related topics.
- `data/CommonQuestions.json` - Frequently asked questions and answers about fertility treatments.
- `data/infertility_info.json` - Information about different types of infertility and their causes.
- `data/Pathways.json` - Treatment pathways and decision trees for fertility care.
- `data/resources.json` - External resources, websites, and support organizations.

## Usage

The JSON files can be accessed directly via GitHub's raw content URLs:

```
https://raw.githubusercontent.com/rsterl14/fertility-data/main/data/Education_Topics.json
https://raw.githubusercontent.com/rsterl14/fertility-data/main/data/CommonQuestions.json
https://raw.githubusercontent.com/rsterl14/fertility-data/main/data/infertility_info.json
https://raw.githubusercontent.com/rsterl14/fertility-data/main/data/Pathways.json
https://raw.githubusercontent.com/rsterl14/fertility-data/main/data/resources.json
```

## Data Structure

Each topic entry contains:
- `category`: The topic category
- `topic`: The topic name
- `lay_explanation`: User-friendly explanation
- `reference`: Array of scientific reference URLs
- `related_to`: Array of related topic names

## Updates

This repository allows for real-time updates to the app's educational content without requiring App Store submissions.

## Validation

All `related_to` references are validated to ensure they correspond to existing topics in the database.

Last updated: $(date)