# Use an image that includes Chrome
FROM python:3.11.4-slim-bullseye

# Install Chrome and required dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set up working directory
WORKDIR /app

# Copy the script
COPY scrape.py .

# Set environment variables for Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

CMD ["python", "scrape.py"]
