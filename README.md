# Faceless

Faceless is a project that generates a video from a given script and subtitles. It uses OpenAI's DALL-E for image generation and FFmpeg for video processing. The project also supports adding background music to the final video.

## Demo

This is an example video that was generated using this script:

![Demo Video](https://github.com/adwaithks/faceless/blob/master/demo/final.mp4)

## Installation

1. Install Ffmpeg:

    For mac:

    ```sh
    brew install ffmpeg
    ```

2. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/faceless.git
    cd faceless
    ```

3. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

5. Set up environment variables:
    - Create a `.env` file in the root directory.
    - Add your OpenAI API key:
        ```
        OPENAI_API_KEY=your_openai_api_key
        ```

## Usage

1. Prepare your script and subtitles:

    - Place your script in `assets/script.txt`.
    - Place your subtitles in `assets/subtitles.txt`.

2. Run the main script:

    ```sh
    python main.py
    ```

3. Follow the prompts to add background music and generate the final video.

4. Output video will be in `output/videos/final_video_with_music.mp4`

## Directory Structure

```
faceless/
├── assets/
│   ├── script.txt
│   ├── subtitles.txt
│   └── README.md
├── src/
│   ├── constants.py
│   ├── generators/
│   │   ├── audio.py
│   │   ├── image.py
│   │   ├── subtitles.py
│   │   └── video.py
│   └── main.py
├── .env
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.
