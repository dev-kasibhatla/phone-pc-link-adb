# PC ↔ Phone Game Link
Play Android phone games using a computer’s keyboard and mouse.

## Details

- Use keyboard and mouse inputs to swipe or tap at specified locations on the phone
- Multi-threaded
- Simulates actual touch input
- Easily customizable keybinds

## Pre-requisites

1. Install [platform-tools](https://developer.android.com/tools/releases/platform-tools)
2. Install [python3](https://www.python.org/downloads/)

## Steps

1. Clone the repository
    
    ```bash
    git clone https://github.com/dev-kasibhatla/ADB-Mapped-Control
    ```
    
2. Connect your phone and ensure ADB can detect it
    
    ```bash
    # This command should show your device
    adb devices
    ```
    
3. Run the script
    
    ```bash
    python3 main.py
    ```
    

## Configuration

1. Modify swipe input locations in `swipe.txt`
2. Modify tap input locations in `tap.txt`
3. Change keybinds in `keys.py`

**Note:** This is a proof-of-concept. While this project works and has been tested with games like PUBG Mobile and BombSquad, it is still rough around the edges and may not work for everyone.
