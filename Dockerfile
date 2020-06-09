FROM python:3.7
COPY app ./app




# Changes the Working directory to our app directory
VOLUME ["/app"]
WORKDIR /app

# Builds the environement variable
ARG buildtime_variable='["abc","bca","abc"]'
ENV SPARSE_ARRAYS_STRINGS=$buildtime_variable


# Installs requirements
RUN pip3 install -r requirements.txt
# Runs the application
ENTRYPOINT ["python3","main.py"]

