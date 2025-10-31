# 🎨 Air Canvas: Virtual Drawing Board

### A Real-Time Computer Vision Application

**Air Canvas** is an innovative real-time computer vision application that transforms your movements into virtual brush strokes. It allows users to "paint" and control a drawing application simply by moving a brightly **colored object** (like a marker or pen cap) visible to a webcam. The application tracks the object's movement and translates it directly into drawing actions on a virtual canvas.

---

## ✨ Features

* **Real-Time Tracking:** Utilizes **HSV color masking** and contour detection to reliably and smoothly track a designated colored object in a live video stream. 
* **Virtual Canvas:** All drawing output is rendered on a separate, pristine **white canvas**, ensuring a clean slate for your creations.
* **Side-by-Side Display:** Shows the live camera feed (with the tool selection buttons) and the drawing canvas **simultaneously** for an intuitive user experience.
* **Drawing Tools:** Easily switch between different drawing modes by pointing at the on-screen buttons:
    * **Green Pen**
    * **Red Pen**
    * **Blue Pen**
    * **Eraser**
* **Utilities:**
    * **Erase All:** Clears the entire drawing canvas.
    * **Save:** Saves the current state of the canvas as `img/pic.jpg`.

---

## ⚙️ Setup and Installation

This project is built using **Python** and relies heavily on the **OpenCV** library for computer vision tasks.

### Prerequisites

* You must have **Python** installed on your system.

### Dependencies

Install the required libraries using the `pip` package manager:

```bash
pip install opencv-python numpy
```

### File Structure

The project relies on a specific file structure for **modularity** and **state management**. Ensure all the provided Python files are placed in the same directory, and create the designated output folder:

**Required Output Directory:**

You also need to create a directory named `img` at the top level of the project to store saved canvas images:

```bash
mkdir img
```

---
## 🚀 How to Run

1.  Ensure your **webcam** is connected and working correctly.
2.  Have a brightly colored object (**Green, Red, or Blue** marker cap, pen, etc.) ready to use as your pointer.
3.  Navigate to the project directory in your terminal:

    ```bash
    cd /path/to/air-canvas-project
    ```

4.  Run the main script:

    ```bash
    python main.py
    ```

---

## 🛠️ How to Use the Air Canvas

1.  **Calibration Window:** When the application starts, a window named **"Setter"** may appear with **trackbars**. These are intended for tuning the **HSV color range**  used for tracking. The current code often uses hard-coded, optimized values, but you can adjust these if your colored object isn't being tracked reliably.

2.  **Pointer:** Hold your colored object in front of the camera. The application should successfully track it, drawing a circle or **contour** around it on the live video feed (left side).

3.  **Drawing:** Move the object in the air to draw on the **right-hand canvas**. The default drawing color will be active upon startup.

4.  **Selecting Tools:** To switch tools (colors, eraser, utilities), simply move your pointer object over one of the **buttons displayed on the live camera feed** (left side) and hold it briefly.

| Tool | Action |
| :--- | :--- |
| **ERASER** | Switches the drawing mode to erase. |
| **GREEN/RED/BLUE** | Switches to the respective drawing color. |
| **ERASE ALL** | Clears the canvas and resets the mode. |
| **SAVE** | Saves the current canvas state to `img/pic.jpg`. |

> **Note:** After saving, the mode automatically switches to **ERASE ALL** to prevent unintended drawing immediately afterward.

5.  **Exit:** Press the **`Q` key** to close all application windows and safely stop the program.
