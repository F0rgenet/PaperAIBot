# PaperAI - Telegram Bot for Document Generation
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
[![CodeFactor](https://www.codefactor.io/repository/github/f0rgenet/paperai/badge)](https://www.codefactor.io/repository/github/f0rgenet/paperai)

PaperAI is a Telegram bot that harnesses the power of neural networks to generate documents effortlessly. All you need to do is provide a topic, and PaperAI will deliver a document in either .docx or .pdf format.

## Table of Contents

- [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- **Topic-Based Document Generation**: PaperAI can generate documents on a wide range of topics. Just send the bot a topic, and it will do the rest.

  - **Document Formats**: You can choose to receive your document in either .docx or .pdf format, making it convenient for various use cases.

  - **User-Friendly Telegram Interface**: Interact with PaperAI through a user-friendly Telegram bot interface. No need for complex commands or setups.

## Getting Started

Follow these instructions to get PaperAI up and running on your local machine.

### Prerequisites

- Python (3.6 or higher)
  - Required Python packages (listed in requirements.txt)

### Installation

1. Clone the PaperAI repository:
   ```bash
   git clone https://github.com/yourusername/PaperAI.git
   ```

   2. Navigate to the project directory:
      ```bash
      cd PaperAI
      ```

   3. Install the required Python packages:
      ```bash
      pip install -r requirements.txt
      ```

   4. Set up your Telegram bot and obtain an API token. You can follow the [official Telegram Bot documentation](https://core.telegram.org/bots) for guidance.

   5. Create a `config.ini` file in the project directory with the following content:
      ```ini
      [Telegram]
      token = YOUR_TELEGRAM_BOT_API_TOKEN
      ```

   6. Run the PaperAI bot:
      ```bash
      python paperai.py
      ```

Now, your PaperAI bot should be up and running.

## Usage

1. Start a chat with your PaperAI bot on Telegram.

   2. Send the bot a topic you want a document about.

   3. PaperAI will process your request and generate the document.

   4. You will receive a file in the format you specified (either .docx or .pdf) in response.

Enjoy the power of automated document generation with PaperAI!

## Contributing

We welcome contributions from the community. Feel free to open issues or pull requests if you have any improvements, suggestions, or bug reports.

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa]


Attribution (BY): You are free to share and adapt the content, but you must give appropriate credit to the original author. 

Non-Commercial (NC): You may not use the content for commercial purposes without permission.

Alike (SA): If you remix, transform, or build upon the content, you must distribute your contributions under the same license as the original.

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]
