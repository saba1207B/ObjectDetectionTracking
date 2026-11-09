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
CodeAlpha_ObjectDetectionTracking
================================
A real-time AI computer vision application for Multi-Object Detection and
Deep Tracking using pretrained YOLO models and ByteTrack/BoT-SORT.

CodeAlpha Artificial Intelligence Internship - Task 4
"""

from .detector import YOLODetector
from .tracker import ObjectTracker

__version__ = "1.0.0"
__author__ = "CodeAlpha AI Intern"
__all__ = ["YOLODetector", "ObjectTracker"]
