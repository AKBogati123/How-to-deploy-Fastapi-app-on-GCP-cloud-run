#Use the official Python slim image
FROM python:3.9-slim

#Set working directory in the container
WORKDIR /app

#Copy requirements first to leverage Docker cache
COPY requirements.txt .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application code
COPY . .

#Expose the port your app runs on
EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]