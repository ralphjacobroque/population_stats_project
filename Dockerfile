# 1. Use an official lightweight Python image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy your script and dataset into the container
COPY dataset.csv .
COPY analytics.py .

# 5. Declare output volume
VOLUME ["/app/output_graphs"]

# 6. Run script
CMD ["python", "analytics.py"]