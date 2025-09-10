#!/usr/bin/env python3
"""
JSON validation script for fertility education data.
Validates JSON structure and related_to references.
"""

import json
import sys
from pathlib import Path

def validate_json_file(file_path):
    """Validate a JSON file's structure and references."""
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

if __name__ == "__main__":
    script_dir = Path(__file__).parent
    json_file = script_dir / "data" / "Education_Topics.json"
    
    if not json_file.exists():
        print(f"❌ JSON file not found: {json_file}")
        sys.exit(1)
    
    if validate_json_file(json_file):
        print("✅ All validations passed!")
        sys.exit(0)
    else:
        print("❌ Validation failed!")
        sys.exit(1)