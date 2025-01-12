# LangChain Image Processing Model

This repository hosts a Streamlit-based application that leverages Google's Generative AI capabilities for image processing. The application allows users to upload images and receive detailed, AI-generated descriptions of the contents of the images, including objects, actions, and context.

## Features
- **Image Upload:** Supports `.jpg`, `.png`, and `.jpeg` formats for image input.
- **Generative AI Integration:** Utilizes Google's Gemini-1.5-Pro model for content generation.
- **Detailed Descriptions:** Provides in-depth insights into the uploaded images.

## Requirements
- Python 3.8 or later
- Dependencies listed in `requirements.txt`

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alihassanml/Generative-AI-Image-Processing.git
   cd Generative-AI-Image-Processing
   ```

2. **Install Dependencies:**
   Ensure you have `pip` installed. Then, run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set API Key:**
   Replace the placeholder API key in the script with your own Google Generative AI API key:
   ```python
   api_key = 'YOUR_API_KEY_HERE'
   ```

4. **Run the Application:**
   Launch the Streamlit app with the following command:
   ```bash
   streamlit run app.py
   ```

## File Overview
- **`app.py`:** The main application script containing the Streamlit interface and image processing logic.
- **Dependencies:**
  - `Pillow` (PIL): For handling image uploads.
  - `google.generativeai`: For leveraging Google's generative AI models.
  - `gtts`: (Optional) For generating text-to-speech outputs.

## How It Works
1. The user uploads an image via the Streamlit interface.
2. The application sends the uploaded image and a predefined prompt to the Generative AI model.
3. The AI model generates a detailed textual description of the image content.
4. The result is displayed in the Streamlit interface.

## Example
1. Start the application using Streamlit.
2. Upload an image.
3. Receive a detailed AI-generated description of the image.

## Future Enhancements
- Support for additional file types.
- Enhanced prompts for better contextual understanding.
- Option to export results to text or speech formats.

## Contributing
Feel free to fork this repository and submit pull requests to improve the application or add features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

