#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

def load_config():
    """لود کردن تنظیمات از فایل config.txt"""
    config_path = Path("config/config.txt")
    if config_path.exists():
        print("📁 Loading config from: config/config.txt")
        with open(config_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and '=' in line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
                    print(f"   ✅ {key.strip()} = {value.strip()}")
    else:
        print("❌ config/config.txt not found!")
        config_path.parent.mkdir(exist_ok=True)
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write("MINER_IP=192.168.1.100\n")
            f.write("PORT=8000\n")
            f.write("MINER_PASSWORD=your_password_here\n")
        print("📝 Created default config/config.txt")

# لود کردن تنظیمات قبل از ایمپورت
load_config()

from main import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    miner_ip = os.environ.get("MINER_IP", "NOT_SET")
    
    print("=" * 50)
    print(f"🚀 Miner Panel Starting...")
    print(f"📁 Config: config/config.txt")
    print(f"🌐 Port: {port}")
    print(f"⛏️  Miner IP: {miner_ip}")
    print(f"📊 URL: http://localhost:{port}")
    print("=" * 50)
    
    app.run(host="0.0.0.0", port=port, debug=False)