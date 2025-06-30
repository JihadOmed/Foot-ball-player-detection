# ⚽ Football Player Detection and Tracking System

## 📌 Project Overview

This project is an end-to-end deep learning system for **real-time football player detection, tracking, and team classification** using video footage. Built using **YOLOv8**, **ByteTrack**, **OpenCV**, and clustering algorithms, the system distinguishes players from referees, assigns teams by jersey color, tracks players across frames, and interpolates ball positions with visual overlays.


---

## 🎯 Key Objectives

- Detect and track football players frame by frame from video.
- Distinguish between referees and players using bounding box filtering.
- Assign players to their respective teams based on jersey color clustering.
- Track ball movement and interpolate missing positions for smoother trajectory.
- Visualize player IDs, movement directions, and team assignments on video.

---

## 🧠 Core Features

| Feature                       | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 🎯 Player Detection           | YOLOv8 detects players and ball in real-time.                              |
| 🧠 Tracking                   | ByteTrack maintains consistent player IDs across frames.                   |
| 🎨 Team Assignment            | KMeans clusters jersey colors to identify team membership.                |
| 🚫 Referee Filtering          | Excludes referees using color-based and bounding box heuristics.           |
| 🟠 Ball Tracking              | Tracks the ball and fills missing positions using interpolation.           |
| 🎥 Frame Overlay              | Draws bounding boxes, team colors, player IDs, and ball arrows with OpenCV.|

---

## 🛠️ Tech Stack

| Tool/Library     | Role                                |
|------------------|-------------------------------------|
| Python           | Programming language                |
| OpenCV           | Image processing and video rendering|
| YOLOv8 (Ultralytics) | Object detection (players & ball)|
| ByteTrack        | Multi-object tracking algorithm     |
| NumPy / Pandas   | Data handling and manipulation      |
| Scikit-Learn     | KMeans clustering for team grouping |
