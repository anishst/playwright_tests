# Build Environment: Playwright
FROM mcr.microsoft.com/playwright/python:v1.21.0-focal

WORKDIR /mytests
COPY /requirements.txt /mytests/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /mytests/requirements.txt
# Add python script to Docker
COPY test_simple.py /mytests/

# Run Python script
CMD [ "pytest", "test_simple.py" ]