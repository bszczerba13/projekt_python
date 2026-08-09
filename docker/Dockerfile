# --------------------------------------------------
# Base image
# --------------------------------------------------
FROM python:3.13-slim

# --------------------------------------------------
# Environment variables
# --------------------------------------------------
# Display Python logs immediately
ENV PYTHONUNBUFFERED=1

# Run browser in headless mode inside Docker
ENV HEADLESS=true

# --------------------------------------------------
# Working directory
# --------------------------------------------------
WORKDIR /app

# --------------------------------------------------
# System packages
# --------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        wget \
        gnupg && \
    rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# Google Chrome repository
# --------------------------------------------------
RUN mkdir -p /etc/apt/keyrings && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | \
    gpg --dearmor -o /etc/apt/keyrings/google-chrome.gpg

RUN echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google-chrome.gpg] \
http://dl.google.com/linux/chrome/deb/ stable main" \
> /etc/apt/sources.list.d/google-chrome.list

# --------------------------------------------------
# Microsoft Edge repository
# --------------------------------------------------
RUN wget -q -O - https://packages.microsoft.com/keys/microsoft.asc | \
    gpg --dearmor -o /etc/apt/keyrings/microsoft-edge.gpg

RUN echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft-edge.gpg] \
https://packages.microsoft.com/repos/edge stable main" \
> /etc/apt/sources.list.d/microsoft-edge.list

# --------------------------------------------------
# Browsers
# --------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        google-chrome-stable \
        firefox-esr \
        microsoft-edge-stable \
        libnss3 \
        libgbm1 \
        libasound2 \
        fonts-liberation && \
    rm -rf /var/lib/apt/lists/*

# --------------------------------------------------
# Python dependencies
# --------------------------------------------------
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# --------------------------------------------------
# Framework
# --------------------------------------------------
COPY . .

# --------------------------------------------------
# Default command
# --------------------------------------------------
CMD ["pytest", "-q", "-n", "4"]