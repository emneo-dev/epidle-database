from DataLoader import DataLoader
import json
from pathlib import Path
import shutil

if __name__ == "__main__":
    dl = DataLoader()
    dl.cache()

    result_dir = Path("result")
    if result_dir.exists():
        shutil.rmtree(result_dir)
    result_dir.mkdir()
    
    with open(result_dir / "pools.json", 'w', encoding='utf-8') as f:
        json.dump(dl.get_pool_days(), f, indent=4, ensure_ascii=False)
    with open(result_dir / "coding-styles.json", 'w', encoding='utf-8') as f:
        json.dump(dl.get_coding_styles(), f, indent=4, ensure_ascii=False)
    with open(result_dir / "coding-style-codes.json", 'w', encoding='utf-8') as f:
        json.dump(dl.get_coding_styles_codes(), f, indent=4, ensure_ascii=False)
    with open(result_dir / "projects.json", 'w', encoding='utf-8') as f:
        json.dump(dl.get_projects(), f, indent=4, ensure_ascii=False)
    with open(result_dir / "project-codes.json", 'w', encoding='utf-8') as f:
        json.dump(dl.get_project_codes(), f, indent=4, ensure_ascii=False)
    print("Files created in result.")
