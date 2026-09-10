"""
Dataset Acquisition Script
Downloads the Zomato delivery operations dataset from Hugging Face
and preserves the raw version without modification.
"""

import os
import requests
from pathlib import Path
from tqdm import tqdm
import hashlib


def download_file(url: str, output_path: Path) -> None:
    """Download file with progress bar and verification."""
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    
    with open(output_path, 'wb') as f:
        with tqdm(total=total_size, unit='iB', unit_scale=True) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                size = f.write(chunk)
                pbar.update(size)


def calculate_md5(file_path: Path) -> str:
    """Calculate MD5 hash of file for verification."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def main():
    """Main download function."""
    # Create data directories
    raw_dir = Path("data/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    # Correct Dataset URL (Hugging Face mirror)
    dataset_url = "https://huggingface.co/datasets/allenborochin/zomato_delivery_EDA/resolve/main/zomato_cleaned.csv"
    
    output_path = raw_dir / "zomato_delivery_raw.csv"
    
    print("=" * 70)
    print("Zomato Delivery Dataset Acquisition")
    print("=" * 70)
    print(f"\nSource: {dataset_url}")
    print(f"Destination: {output_path}")
    
    if output_path.exists():
        print(f"\nFile already exists: {output_path}")
        print("Skipping download to preserve raw data integrity.")
        print(f"File size: {output_path.stat().st_size / (1024*1024):.2f} MB")
        return
    
    print("\nDownloading dataset...")
    try:
        download_file(dataset_url, output_path)
        
        # Calculate and display file hash
        file_hash = calculate_md5(output_path)
        file_size = output_path.stat().st_size
        
        print("\n" + "=" * 70)
        print("Download Complete")
        print("=" * 70)
        print(f"File: {output_path}")
        print(f"Size: {file_size / (1024*1024):.2f} MB")
        print(f"MD5: {file_hash}")
        print("\nRaw data preserved without modification.")
        
    except Exception as e:
        print(f"\nError downloading dataset: {e}")
        print("\nAlternative download methods:")
        print("1. Download manually from: https://huggingface.co/datasets/allenborochin/zomato_delivery_EDA/resolve/main/zomato_cleaned.csv")
        print("2. Place the CSV file in: data/raw/zomato_delivery_raw.csv")
        raise


if __name__ == "__main__":
    main()