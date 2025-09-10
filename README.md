# Fertility Education Data

This repository contains the JSON data files for the Synagamy fertility education app.

## Files

- `data/Education_Topics.json` - Main education topics database containing 189 fertility-related topics with lay explanations, references, and related topics.

## Usage

The JSON files can be accessed directly via GitHub's raw content URLs:

```
https://raw.githubusercontent.com/YOUR_USERNAME/fertility-data/main/data/Education_Topics.json
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