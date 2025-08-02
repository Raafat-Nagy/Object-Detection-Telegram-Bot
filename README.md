# Object Detection Telegram Bot using YOLO

![YOLO](https://img.shields.io/badge/YOLO-Object%20Detection-green?logo=openai&logoColor=white)
![python-telegram-bot](https://img.shields.io/badge/Telegram%20Bot-Async%20Python-blue?logo=telegram)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-blueviolet?logo=opencv)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Overview

This project is a Telegram Bot that performs real-time object detection on user-submitted images using the YOLO model by Ultralytics.

When a user sends an image, the bot responds with:

- An annotated image showing detected objects
- A summary report including object classes, image size, and detection speed

---

## Features

- Accepts images via Telegram
- Detects multiple object types using YOLO
- Annotates and returns the processed image
- Provides a detailed detection summary
- Sends a startup notification to the admin
- Fully async and modular code

---

## Project Structure

```

object-detection-telegram-bot
├── bot_main.py                         
├── config.py                           
├── object_detection.py                 
├── object_detection_telegram_bot_test.ipynb  
├── requirements.txt                    
└── model/
└── yolo11n.pt                      

````

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Raafat-Nagy/Object-Detection-Telegram-Bot.git
cd Object-Detection-Telegram-Bot
````

### 2. Install dependencies

Make sure you have Python 3.8 or higher:

```bash
pip install -r requirements.txt
```

### 3. Configure the bot

Edit the `config.py` file:

```python
BOT_TOKEN = "your_bot_token"
ADMIN_CHAT_ID = 123456789
MODEL_PATH = "./model/yolo11n.pt"
```

You can get your Telegram bot token from [@BotFather](https://t.me/BotFather)

---

## Running the Bot

```bash
python bot_main.py
```

The bot will:

* Notify the admin when it starts
* Wait for users to send images
* Respond with detections and image annotations

---

## Example Output

```
Object Detection Completed!

 • Size: 640x480
 • Objects: person 2, car 1
 • Speed: 2.1ms preprocess, 12.3ms inference, 1.7ms postprocess
```

---

## Demo Video

[Watch on YouTube](https://youtu.be/0K8c3HZsd2U)

[![Watch the video](https://img.youtube.com/vi/0K8c3HZsd2U/hqdefault.jpg)](https://youtu.be/0K8c3HZsd2U)

---

## Tech Stack

* YOLO – Ultralytics
* python-telegram-bot (async version)
* OpenCV
* Python 3.8+
* Jupyter Notebook (for prototyping and testing)

---

## License

This project is licensed under the MIT License.

---

## Author

Developed by [Raafat Nagy](https://github.com/Raafat-Nagy)
GitHub Repository: [Object-Detection-Telegram-Bot](https://github.com/Raafat-Nagy/Object-Detection-Telegram-Bot)

If you found this project useful, feel free to star the repo.

