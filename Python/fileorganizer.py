import os
import shutil
from pathlib import Path

def organize_files(directory):
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx', '.odt'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
        'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.json'],
    }
    
    path = Path(directory)
    
    if not path.exists():
        print(f"Error: {directory} doesn't exist")
        return
    
    for category in categories.keys():
        (path / category).mkdir(exist_ok=True)
    
    (path / 'Others').mkdir(exist_ok=True)
    
    moved = 0
    for item in path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            moved_to = None
            
            for category, extensions in categories.items():
                if ext in extensions:
                    dest = path / category / item.name
                    shutil.move(str(item), str(dest))
                    moved_to = category
                    moved += 1
                    break
            
            if not moved_to and ext:
                dest = path / 'Others' / item.name
                shutil.move(str(item), str(dest))
                moved += 1
    
    print(f"organized {moved} files")

if __name__ == "__main__":
    target = str(Path.home() / "Downloads")
    print(f"organizing {target}...")
    organize_files(target)
