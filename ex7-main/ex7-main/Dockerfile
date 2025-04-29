# Use an official Python image as a base
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Python script
COPY automl.py /app/

# Install dependencies
RUN pip install pandas scikit-learn tpot

# Run the script
CMD ["python", "automl.py"]
