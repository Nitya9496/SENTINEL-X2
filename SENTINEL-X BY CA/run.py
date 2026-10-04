"""
SENTINEL-X — Launcher Script
Boots the offline supervisory analytics server and opens the web console.
"""

import os
import sys
import webbrowser
import uvicorn

def main():
    print("=" * 70)
    print("SENTINEL-X — Supervisory Analytics Tool for SOC Assessment (SAT-SA)")
    print("Air-Gapped Prototype for NCIIPC Supervisory Oversight")
    print("=" * 70)
    print("\nStarting local server on http://localhost:8000 ...")
    
    # Try to open default browser
    try:
        webbrowser.open("http://localhost:8000")
    except Exception as e:
        print(f"Notice: Browser open exception: {e}")

    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=False)

if __name__ == "__main__":
    main()
