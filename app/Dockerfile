# Use the Debian-based Python image
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies using apt-get
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy the shell script
COPY start.sh /app/start.sh

# Make the shell script executable
RUN chmod +x /app/start.sh

# Expose the port
EXPOSE 8000

# Use the script as the entry point
CMD ["bash", "-c", "echo 'Starting main_generate' && python -m main_generate && echo 'Starting main_display' && python -m main_display"]

