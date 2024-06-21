# LLMs-chatbot-with-RAG
Thiết lập 1 chatbot trả lời các câu hỏi lịch sử Nhật Bản sử dụng kiến trúc RAG

## Kiến trúc: Gồm 5 file chính
1. File model_rag.jypynb là file xây dựng kiến trúc RAG cho mô hình
2. file model.py là file sử dụng mô hình để sinh câu trả lời.
3. app.py là file giao diện
4. data.pdf là file dữ liệu sử dụng
5. requirement.txt: Chứa các module cần cài đặt

## Công nghệ chính được sử dụng:
1. Mô hình: Sử dụng dịch vụ API miễn phí của Groq, mô hình sử dụng là gemma-7b-it
2. Xây dựng RAG: Langchain
3. UI: Streamlit

## Quy trình xây dựng hệ thống LLMs:
- Bước 1: Thiết lập kết nối với dịch vụ của Groq
- Bước 2: Load dữ liệu, chia dữ liệu thành các chunks nhỏ
- Bước 3: Embedding dữ liệu và nhét vào vector database
- Bước 4: Thiết lập Prompt Template cho mô hình
- Bước 5: Tạo chain với prompt template, vector database và model sử dụng ở trên
- Bước 6: Xây dựng UI


