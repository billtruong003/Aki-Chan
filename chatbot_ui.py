import streamlit as st
import ollama
import json
from PIL import Image
import os

# Đọc và lưu lịch sử trò chuyện vào file JSON
def load_chat_history(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_chat_history(file_path, chat_history):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(chat_history, file, ensure_ascii=False, indent=4)

# Cải thiện giao diện với CSS
def read_system_message(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    # Ghép các dòng lại thành 1 chuỗi duy nhất
    return ''.join(line.strip() for line in lines)


st.markdown("""
    <style>
        /* Các kiểu cho toàn bộ trang */
        body {
            background-color: #212121; /* Màu nền tối (đen) */
            color: #ffffff; /* Chữ màu trắng để nổi bật trên nền đen */
        }

        /* Container cho các tin nhắn */
        .chat-container {
            background-color: #333333; /* Màu nền container tối */
            padding: 15px;
            border-radius: 10px;
            max-width: 800px;
            margin: 0 auto;
            margin-bottom: 10px;
        }

        /* Tin nhắn của người dùng */
        .user-message {
            background-color: #ff6600; /* Màu cam cho tin nhắn của người dùng */
            color: white; /* Chữ trắng trên nền cam */
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        /* Tin nhắn của Aki */
        .aki-message {
            background-color: #ffebcc; /* Màu sáng hơn cho tin nhắn của Aki */
            color: #212121; /* Màu chữ tối cho dễ đọc */
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
        }

        /* Nút xóa lịch sử */
        .clear-button {
            background-color: #ff6600; /* Màu cam cho nút */
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }
        .clear-button:hover {
            background-color: #e65c00; /* Sắc cam tối hơn khi hover */
        }

        /* Hình ảnh của Aki */
        .aki-image {
            border-radius: 15px;
            border: 5px solid #ff6600; /* Viền cam cho ảnh */
        }

        /* Tiêu đề ứng dụng */
        .app-title {
            color: #ff6600; /* Màu cam cho tiêu đề */
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)


# Hiển thị ảnh từ file trong thư mục hiện tại
st.image("aki-maid.webp", caption="Chào chủ nhân, em là Aki!", width=400)

# Tiêu đề ứng dụng
st.title("Aki-Maid")
st.markdown("""
Chào mừng bạn đến với chatbot Aki! Bạn có thể nhập câu hỏi và/hoặc tải lên hình ảnh để nhận câu trả lời từ Aki.
""")

# Đường dẫn đến file JSON lưu lịch sử
history_file_path = 'chat_history.json'

# Khởi tạo danh sách để lưu các câu hỏi và câu trả lời, hoặc đọc từ file nếu có
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = load_chat_history(history_file_path)

# Tạo hộp nhập liệu câu hỏi
user_input = st.text_input("Nhập câu hỏi của bạn:")

# Tạo hộp tải lên hình ảnh
uploaded_image = st.file_uploader("Tải lên hình ảnh (nếu có)", type=["jpg", "jpeg", "png"])

# Xử lý câu hỏi và hình ảnh khi người dùng nhập câu hỏi hoặc tải lên ảnh
if user_input or uploaded_image:
    with st.spinner('Đang nhận phản hồi từ Aki...'):
        try:
            # Chuyển đổi hình ảnh tải lên thành đối tượng Image (PIL)
            image_data = None
            if uploaded_image is not None:
                image_data = Image.open(uploaded_image)

            # Cấu hình tên và tính cách mô hình (System message)
            system_message = read_system_message("config_character.txt")

            # Gửi câu hỏi và hình ảnh đến Ollama với mô hình llama3.2-vision
            if image_data:
                # Nếu có hình ảnh, gửi cả hình ảnh và câu hỏi
                response = ollama.chat(
                    model='llama3.2-vision',
                    messages=[{
                        'role': 'system',
                        'content': system_message  # Mô tả tính cách của mô hình
                    }, {
                        'role': 'user',
                        'content': user_input if user_input else "Không có câu hỏi",
                        'images': [uploaded_image.getvalue()]  # Gửi ảnh dưới dạng byte
                    }]
                )
            else:
                # Nếu không có hình ảnh, chỉ gửi câu hỏi
                response = ollama.chat(
                    model='llama3.2-vision',
                    messages=[{
                        'role': 'system',
                        'content': system_message  # Mô tả tính cách của mô hình
                    }, {
                        'role': 'user',
                        'content': user_input
                    }]
                )

            # Thêm câu trả lời vào lịch sử trò chuyện, đặt câu hỏi và câu trả lời mới lên đầu danh sách
            st.session_state.chat_history.insert(0, {'role': 'aki', 'content': response['message']['content']})
            st.session_state.chat_history.insert(0, {'role': 'user', 'content': user_input})

            # Lưu lại lịch sử trò chuyện vào file JSON
            save_chat_history(history_file_path, st.session_state.chat_history)

        except Exception as e:
            st.error(f"Đã có lỗi xảy ra: {e}")

# Hiển thị các câu hỏi và câu trả lời cũ
for message in st.session_state.chat_history:
    if message['role'] == 'user':
        st.markdown(f'<div class="chat-container user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-container aki-message">{message["content"]}</div>', unsafe_allow_html=True)

# Thêm nút xóa lịch sử
if st.button('Xóa lịch sử'):
    st.session_state.chat_history = []
    save_chat_history(history_file_path, st.session_state.chat_history)
    st.experimental_rerun()  # Làm mới lại trang để xóa lịch sử
