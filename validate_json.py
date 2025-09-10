#!/usr/bin/env python3
"""
JSON validation script for fertility education data.
Validates JSON structure and related_to references.
"""

import json
import sys
from pathlib import Path

def validate_education_topics(file_path):
    """Validate Education_Topics.json structure and references."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return False
    
    # Collect all topics
    all_topics = set()
    required_fields = ['category', 'topic', 'lay_explanation', 'reference', 'related_to']
    
    for i, entry in enumerate(data):
        # Check required fields
        missing_fields = [field for field in required_fields if field not in entry]
        if missing_fields:
            print(f"❌ Entry {i+1} missing fields: {missing_fields}")
            return False
        
        all_topics.add(entry['topic'])
    
    # Validate related_to references
    invalid_refs = []
    for entry in data:
        for ref in entry.get('related_to', []):
            if ref not in all_topics:
                invalid_refs.append((entry['topic'], ref))
    
    if invalid_refs:
        print(f"❌ Found {len(invalid_refs)} invalid related_to references:")
        for topic, invalid_ref in invalid_refs:
            print(f"  '{topic}' -> '{invalid_ref}'")
        return False
    
    print(f"✅ {file_path} is valid!")
    print(f"  - {len(data)} total entries")
    print(f"  - {sum(len(entry.get('related_to', [])) for entry in data)} total references")
    return True

def validate_generic_json(file_path):
    """Validate any JSON file for basic syntax."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            print(f"✅ {file_path} is valid!")
            print(f"  - {len(data)} total entries")
        elif isinstance(data, dict):
            print(f"✅ {file_path} is valid!")
            print(f"  - {len(data)} total keys")
        else:
            print(f"✅ {file_path} is valid!")
            print(f"  - Contains {type(data).__name__} data")
        
        return True
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error in {file_path}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error reading {file_path}: {e}")
        return False

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    data_dir = script_dir / "data"
    
    if not data_dir.exists():
        print(f"❌ Data directory not found: {data_dir}")
        sys.exit(1)
    
    # Get all JSON files in the data directory
    json_files = list(data_dir.glob("*.json"))
    
    if not json_files:
        print(f"❌ No JSON files found in: {data_dir}")
        sys.exit(1)
    
    print(f"Validating {len(json_files)} JSON files...\n")
    
    all_valid = True
    
    for json_file in sorted(json_files):
        if json_file.name == "Education_Topics.json":
            # Special validation for Education_Topics
            if not validate_education_topics(json_file):
                all_valid = False
        else:
            # Generic JSON validation for other files
            if not validate_generic_json(json_file):
                all_valid = False
        print()  # Empty line for readability
    
    if all_valid:
        print("✅ All JSON files passed validation!")
        sys.exit(0)
    else:
        print("❌ Some validations failed!")
        sys.exit(1)