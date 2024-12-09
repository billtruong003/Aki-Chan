Dưới đây là phiên bản tiếng Anh của README mà bạn yêu cầu (`README-en.md`), được viết một cách dễ thương và dễ hiểu giống như phiên bản tiếng Việt:

---

# Aki-Maid Chatbot
![Aki-Maid](aki-maid.webp)  
**Aki-Maid** is a chatbot application powered by the **Llama3.2** model that answers questions and processes images uploaded by users. The app is built using **Streamlit** and **Ollama API**.

## 1. **Environment Setup**

### Step 1: Install Python

The application requires **Python 3.8+**. If you haven't installed Python yet, you can download it from [python.org](https://www.python.org/downloads/).

Make sure Python and **pip** (Python package manager) are installed by running the following commands:

```bash
python --version
pip --version
```

### Step 2: Install Dependencies

Create a virtual environment and install the necessary libraries using the steps below:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**:

   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies from `requirements.txt`**:

   Ensure you have a `requirements.txt` file in your project. The content of `requirements.txt` will look like this:

   **`requirements.txt`**:
   ```txt
   streamlit==1.40.2
   ollama==0.4.4
   Pillow==11.0.0
   requests==2.32.3
   jsonschema==4.23.0
   numpy==2.2.0
   pandas==2.2.3
   ```

   Then, install all the libraries with the following command:

   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Download the **Llama3.2** Model

To use the **Llama3.2** model, you'll need to download it via the **Ollama API**. You need to install **Ollama** and use its API to download the model.

1. **Install Ollama**:

   Go to Ollama's website and follow the instructions to install Ollama for your operating system: [Ollama Installation](https://ollama.com/).

2. **Download the Llama3.2 model**:

   After installing Ollama, you can download the Llama3.2 model with the following command:

   ```bash
   ollama pull llama3.2
   ```

   This command will download the **Llama3.2** model to your computer, which will be used by the application.

### Step 4: Run the Application

Once all dependencies are installed and the model is downloaded, you can run the **Aki-Maid** application using Streamlit with the following command:

```bash
streamlit run app.py
```

This will start the Streamlit app at `http://localhost:8501`, where you can chat with Aki.

---

## 2. **Application Configuration**

### The `config_character.txt` File

The application uses a file called **`config_character.txt`** to configure Aki's personality. You can modify this file to change how Aki responds. For example:

```
I am Aki, a friendly, cute, and intelligent virtual assistant. Feel free to ask me anything!
```

### Chat History

The application will save the chat history into a **`chat_history.json`** file. This file will be read when you open the app again, keeping your past conversations.

---

## 3. **Troubleshooting Common Issues**

- **Model not downloading**: If you encounter issues when downloading the model from Ollama, make sure you installed Ollama correctly, and that the model was successfully downloaded to your machine.
  
- **API or connection errors**: If the app is unable to connect to the Ollama API, check your internet connection and make sure Ollama is running correctly.

---

## 4. **Useful Links**

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Ollama Documentation](https://ollama.com/)
- [Ollama API Docs](https://docs.ollama.com/)

---

### Wishing you great success with Aki-Maid Chatbot! 🚀

---

**Note:** Make sure everything is properly configured before running the app, including downloading the model and setting up the Ollama API.

---

Chúc bạn có những cuộc trò chuyện thật vui vẻ với Aki!