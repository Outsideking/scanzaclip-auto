# ใช้ Python base image
FROM python:3.12-slim

# ตั้ง working directory
WORKDIR /app

# คัดลอกโปรเจกต์
COPY . /app

# ติดตั้ง dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# รัน workflow auto
CMD ["python", "workflow.py"]
