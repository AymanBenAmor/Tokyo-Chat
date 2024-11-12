Here is a `README.md` for your project:

```markdown
# Tokyo Store Voice Assistant

This project is a voice-activated assistant for a store application named "Tokyo Store". It interacts with users through voice commands, listens for specific phrases, and responds in French. Additionally, it enables adding, listing, and removing store items through a graphical interface built with Tkinter.

## Features

- **Voice Interaction**: Uses speech recognition to listen to Arabic commands and responds in French.
- **Item Management**: Allows users to add, delete, and list store items saved in a CSV file.
- **Text Translation**: Translates recognized speech from Arabic to French for further processing.
- **Sound Playback**: Plays specific audio responses based on recognized commands or responses from the assistant.
- **Graphical User Interface (GUI)**: Includes an interactive dashboard for managing store items and starting/stopping conversations.

## Technologies Used

- **Python Libraries**:
  - `tkinter`: For the graphical interface.
  - `speech_recognition`: For voice recognition.
  - `pyttsx3`: For text-to-speech responses.
  - `googletrans`: For translating Arabic speech to French.
  - `pygame`: For playing sound files.
  - `csv`: For reading and writing item data.

## Prerequisites

Make sure the following Python packages are installed:

```bash
pip install pyttsx3 speechrecognition googletrans pygame pillow
```

## Files and Folders

- **`dashboard.py`**: Main file containing the source code for the assistant.
- **`data.csv`**: CSV file containing store items and their associated sound files.
- **`sounds` folder**: Contains MP3 sound files for responses.
- **`images` folder**: Contains images for the background and icon.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   ```
2. **Navigate to the project directory**:
   ```bash
   cd tokyo-store-assistant
   ```
3. **Run the program**:
   ```bash
   python dashboard.py
   ```

## Functionality

- **Voice Commands**: Users can interact with the assistant through Arabic voice commands. The assistant responds based on specific keywords in the commands.
- **Add New Items**: Type a new item name in the input box and click "Ajouter l'article" to add it to the list.
- **Remove Items**: Type the name of an item to delete and click "Supprimer l'article" to remove it from the list.
- **List Items**: Click "afficher tout les articles" to display all items in the inventory.

## GUI Overview

- **Add/Remove Items**: Input boxes and buttons allow the addition and removal of items.
- **Start/Stop Discussion**: Buttons to start or stop the assistant’s voice recognition.
- **Text Area**: Displays the assistant's responses and translations.

## Packaging the Project

To package the project as a standalone executable:

```bash
pyinstaller dashboard.py --onefile --noconsole --icon=images/icon.ico
```

This will create an executable in the `dist` folder.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.



## Acknowledgments

This project was developed as a store assistant for Tokyo Store, utilizing multilingual capabilities and real-time voice recognition.
```
