# Auto Drawer 🎨🤖

Auto Drawer is a Python project that automatically redraws an image on screen using mouse automation.

You load an image, the program dynamically finds the best edge-detection settings, scales the image to your drawing area, and then draws it pixel by pixel.

⚠️ **Learning-focused project not production-ready**

---

## How it works

1. You choose the image you want to draw
2. The program dynamically searches for the best parameters to detect image edges
3. A message **"Setup emulator"** appears  
   (I used **BlueStacks**, but any drawing environment works)
4. Place the mouse on the **top-left corner** of your drawing area and keep it still
5. Place the mouse on the **bottom-right corner** of the drawing area and keep it still
6. The image is automatically scaled to fit the selected area
7. The program starts drawing the image on screen

🚫 **Do not touch the mouse while drawing**

---

## Safety & Controls

- If something goes wrong, **quickly drag the mouse to a screen corner** to stop the program
- Recommended brush size: **minimum or just slightly bigger**
- Simple images work best
- ⚡ **Note:** The demo video is sped up; in real time, drawing may take several minutes

---

## Technologies used

- Python
- OpenCV (edge detection)
- PyAutoGUI (mouse automation)
- NumPy

---

## How to run

```bash
pip install -r requirements.txt
python main.py
```

---

## Demo

Download and watch the demo video: [Demo Video](Demo/demo.mp4)

