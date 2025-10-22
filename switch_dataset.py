#!/usr/bin/env python3
"""
Dataset Switcher Script
Allows easy switching between movies and stocks datasets
"""

import subprocess
import sys
import os

def switch_dataset(dataset):
    """Switch between movies and stocks datasets"""
    
    if dataset not in ['movies', 'stocks']:
        print("❌ Invalid dataset. Use 'movies' or 'stocks'")
        return False
    
    print(f"🔄 Switching to {dataset} dataset...")
    
    # Change to docker directory
    docker_dir = os.path.join(os.path.dirname(__file__), 'docker')
    os.chdir(docker_dir)
    
    # Update .env file
    with open('.env', 'r') as f:
        content = f.read()
    
    content = content.replace(f'SAMPLE_SCHEMA={dataset}', f'SAMPLE_SCHEMA={dataset}')
    if f'SAMPLE_SCHEMA={dataset}' not in content:
        content = content.replace('SAMPLE_SCHEMA=movies', f'SAMPLE_SCHEMA={dataset}')
        content = content.replace('SAMPLE_SCHEMA=stocks', f'SAMPLE_SCHEMA={dataset}')
    
    with open('.env', 'w') as f:
        f.write(content)
    
    print(f"✅ Updated .env to use {dataset} schema")
    
    # Stop existing container
    print("🛑 Stopping existing container...")
    try:
        subprocess.run(['docker', 'stop', '$(docker ps | grep vanna-postgres-demo | awk \'{print $1}\')'], 
                      shell=True, capture_output=True)
    except:
        pass
    
    # Build new image
    print(f"🔨 Building Docker image with {dataset} data...")
    result = subprocess.run(['./build.sh'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Build failed: {result.stderr}")
        return False
    
    # Start container
    print(f"🚀 Starting container with {dataset} data...")
    subprocess.run(['./run.sh'], check=True)
    
    print(f"✅ Successfully switched to {dataset} dataset!")
    print(f"📊 Database is running on port 5433")
    print(f"🔗 Connection: postgresql://postgres:password@localhost:5433/postgres")
    
    return True

def show_status():
    """Show current dataset status"""
    docker_dir = os.path.join(os.path.dirname(__file__), 'docker')
    env_file = os.path.join(docker_dir, '.env')
    
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            content = f.read()
            for line in content.split('\n'):
                if line.startswith('SAMPLE_SCHEMA='):
                    current_dataset = line.split('=')[1]
                    print(f"📊 Current dataset: {current_dataset}")
                    break
    else:
        print("❌ .env file not found")
    
    # Check if container is running
    try:
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        if 'vanna-postgres-demo' in result.stdout:
            print("✅ Container is running")
        else:
            print("❌ Container is not running")
    except:
        print("❌ Could not check container status")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 switch_dataset.py [movies|stocks|status]")
        print("\nExamples:")
        print("  python3 switch_dataset.py movies    # Switch to movies dataset")
        print("  python3 switch_dataset.py stocks     # Switch to stocks dataset")
        print("  python3 switch_dataset.py status     # Show current status")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'status':
        show_status()
    elif command in ['movies', 'stocks']:
        switch_dataset(command)
    else:
        print("❌ Invalid command. Use 'movies', 'stocks', or 'status'")
        sys.exit(1)
