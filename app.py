# Copyright (c) 2026 Sabareesh M (saba1207B). All Rights Reserved.
#
# This source code is proprietary and confidential.
#
# Unauthorized copying, redistribution, modification, or use — including
# any use for artificial intelligence / machine learning training —
# is strictly prohibited.
#
# See the LICENSE and COPYRIGHT files in the repository root for full terms.

"""
Root entry point for CodeAlpha Object Detection & Tracking.
Delegates to backend/app.py.
"""
import os
import sys

base_dir = os.path.join(os.path.dirname(__file__), "backend")
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from app import run_application

if __name__ == "__main__":
    run_application()

