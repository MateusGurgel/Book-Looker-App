FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/2.10/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip && \
    apt-get install -y chromium && \
    apt-get clean


# Set environment variables for Selenium
ENV PATH=/usr/local/bin:$PATH
ENV DISPLAY=:99

# Start a virtual display to run the browser
RUN apt-get install -y xvfb

# Streamlit

RUN mkdir -p ~/.streamlit/ \
    && echo "[general]" > ~/.streamlit/credentials.toml \
    && echo "email = \"\"" >> ~/.streamlit/credentials.toml


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5123

CMD ["streamlit", "run", "main.py", "--server.port=5123", "--server.address=0.0.0.0"]