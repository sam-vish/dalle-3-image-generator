# DALL-E 3 Image Generator

This Streamlit application allows users to generate images using OpenAI's DALL-E 3 model. Users can input descriptions, and the model will generate corresponding images.

## Features

- Generate images based on textual descriptions.
- Adjustable number of images to generate.
- Powered by OpenAI's DALL-E 3 model.

## Installation

To run the application locally, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project-directory>
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory of the project and add your OpenAI API key:

    ```plaintext
    OPENAI_API_KEY = "your_openai_api_key_here"
    ```

5. Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

6. Access the application in your browser at `http://localhost:8501`.

## Usage

- Enter a description of the image in the text input field.
- Select the number of images to generate using the number input field.
- Click the "Generate Image" button to generate the images based on the provided description.
- Images will be displayed in a carousel format.

## Dependencies

- `streamlit`
- `openai`
- `streamlit_carousel`
- `python-dotenv`

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests to improve the application.

## License

This project is licensed under the [MIT License](LICENSE).
