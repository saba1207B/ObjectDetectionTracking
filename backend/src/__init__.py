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
backend/src
===========
Core vision modules: YOLO Detector and Object Tracker (ByteTrack / BoT-SORT).
Part of CodeAlpha AI Internship - Task 4: Object Detection and Tracking.
"""
from .detector import YOLODetector
from .tracker import ObjectTracker

__all__ = ["YOLODetector", "ObjectTracker"]
