#!/usr/bin/env python3
"""
Update script to copy data from main project and validate before committing.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

# Paths
MAIN_PROJECT_DATA_DIR = "/Users/reidsterling/Desktop/Synagamy/Synagamy3.0/Data/JSON/"
REPO_DATA_DIR = Path(__file__).parent / "data"

# JSON files to sync
JSON_FILES = [
    "Education_Topics.json",
    "CommonQuestions.json", 
    "infertility_info.json",
    "Pathways.json",
    "resources.json"
]

def update_data():
    """Update the repository data from the main project."""
    
    # Copy all JSON files
    print("Copying updated JSON files from main project...")
    copied_files = []
    
    for json_file in JSON_FILES:
        source = Path(MAIN_PROJECT_DATA_DIR) / json_file
        dest = REPO_DATA_DIR / json_file
        
        if source.exists():
            shutil.copy2(source, dest)
            copied_files.append(json_file)
            print(f"  ✓ Copied {json_file}")
        else:
            print(f"  ⚠️  Warning: {json_file} not found in main project")
    
    if not copied_files:
        print("❌ No files were copied!")
        return False
    
    # Validate all JSON files
    print("\nValidating all JSON files...")
    result = subprocess.run([sys.executable, "validate_json.py"], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("❌ Validation failed!")
        print(result.stdout)
        print(result.stderr)
        return False
    
    print("✅ All validations passed!")
    
    # Check if there are changes
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if not result.stdout.strip():
        print("No changes detected.")
        return True
    
    # Show what changed
    print("\nChanges detected:")
    print(result.stdout)
    
    # Add all JSON files
    for json_file in copied_files:
        subprocess.run(["git", "add", f"data/{json_file}"])
    
    # Get commit message
    commit_msg = input("Enter commit message (or press Enter for default): ").strip()
    if not commit_msg:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        commit_msg = f"Update JSON data files - {timestamp}"
    
    subprocess.run(["git", "commit", "-m", commit_msg])
    
    # Ask about pushing
    push = input("Push to GitHub? (y/N): ").strip().lower()
    if push == 'y':
        subprocess.run(["git", "push"])
        print("✅ All data updated and pushed to GitHub!")
    else:
        print("✅ All data updated locally. Run 'git push' when ready to publish.")
    
    return True

if __name__ == "__main__":
    main_project_dir = Path(MAIN_PROJECT_DATA_DIR)
    if not main_project_dir.exists():
        print(f"❌ Main project data directory not found: {main_project_dir}")
        sys.exit(1)
    
    update_data()