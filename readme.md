# Aki-Maid Chatbot
![Aki-Maid](aki-maid.webp)
**Aki-Chan** là một ứng dụng chatbot sử dụng mô hình **Llama3.2** để trả lời câu hỏi và xử lý hình ảnh từ người dùng. Ứng dụng được xây dựng bằng **Streamlit** và **Ollama API**.

## 1. **Cài Đặt Môi Trường**

### Bước 1: Tải và Cài Đặt Python

Ứng dụng yêu cầu **Python 3.8+**. Nếu bạn chưa cài đặt Python, bạn có thể tải từ [python.org](https://www.python.org/downloads/).

Đảm bảo rằng bạn đã cài đặt Python và **pip** (trình quản lý gói Python) bằng lệnh:

```bash
python --version
pip --version
```

### Bước 2: Cài Đặt Thư Viện

Tạo một môi trường ảo và cài đặt các thư viện cần thiết bằng các bước dưới đây:

1. **Tạo môi trường ảo**:
   ```bash
   python -m venv venv
   ```

2. **Kích hoạt môi trường ảo**:

   - Trên **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - Trên **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Cài đặt các phụ thuộc từ `requirements.txt`**:

   Đảm bảo rằng bạn đã có một file `requirements.txt` trong dự án của mình. Nội dung của file `requirements.txt` sẽ như sau:

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

   Sau đó, cài đặt tất cả các thư viện từ `requirements.txt` bằng lệnh:

   ```bash
   pip install -r requirements.txt
   ```

### Bước 3: Tải Mô Hình **Llama3.2**

Để sử dụng mô hình **Llama3.2**, bạn cần tải mô hình này thông qua **Ollama API**. Bạn cần cài đặt **Ollama** và sử dụng API để tải mô hình.

1. **Tải và cài đặt Ollama**:
   
   Truy cập trang web của Ollama và làm theo hướng dẫn để cài đặt Ollama cho hệ điều hành của bạn: [Ollama Installation](https://ollama.com/).

2. **Tải mô hình Llama3.2**:

   Sau khi cài đặt Ollama, bạn có thể tải mô hình Llama3.2 bằng lệnh sau:

   ```bash
   ollama pull llama3.2
   ```

   Lệnh này sẽ tải mô hình **Llama3.2** xuống máy tính của bạn để sử dụng trong ứng dụng.

### Bước 4: Chạy Ứng Dụng

Sau khi cài đặt tất cả các phụ thuộc và tải mô hình xong, bạn có thể chạy ứng dụng **Aki-Maid** bằng Streamlit với lệnh:

```bash
streamlit run app.py
```

Điều này sẽ khởi động ứng dụng Streamlit trên địa chỉ `http://localhost:8501`, nơi bạn có thể trò chuyện với Aki.

---

## 2. **Cấu Hình Ứng Dụng**

### File cấu hình `config_character.txt`

Ứng dụng sử dụng một file **`config_character.txt`** để cấu hình tính cách của mô hình. Bạn có thể chỉnh sửa file này để thay đổi cách trả lời của Aki. Ví dụ:

```
Em là Aki, một trợ lý ảo thân thiện, dễ thương và thông minh. Hãy hỏi em bất kỳ câu hỏi nào!
```

### Lịch Sử Trò Chuyện

Ứng dụng sẽ lưu lại lịch sử trò chuyện vào một file **`chat_history.json`**. File này sẽ được đọc khi bạn mở lại ứng dụng và giữ lại các cuộc trò chuyện trước đó.

---

## 3. **Giải Quyết Các Lỗi Phổ Biến**

- **Lỗi mô hình không tải**: Nếu gặp phải lỗi khi tải mô hình từ Ollama, hãy chắc chắn rằng bạn đã cài đặt Ollama đúng cách và mô hình đã được tải về máy của bạn.
  
- **Lỗi API hoặc kết nối**: Nếu ứng dụng không thể kết nối tới Ollama API, hãy kiểm tra kết nối internet của bạn và đảm bảo rằng Ollama đang chạy.

---

## 4. **Tài Liệu và Liên Kết Hữu Ích**

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Ollama Documentation](https://ollama.com/)
- [Ollama API Docs](https://docs.ollama.com/)

---

### Chúc bạn thành công khi sử dụng Aki-Maid Chatbot! 🚀

---

**Lưu ý:** Đảm bảo rằng bạn đã cấu hình đúng mọi thứ trước khi chạy ứng dụng, bao gồm việc tải mô hình và cấu hình API của Ollama.