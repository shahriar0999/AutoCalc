FROM python:3.12.8-alpine3.20

# set the working directory
WORKDIR /app
 
# copy the current directory content into the container at /app
COPY . .

# install all packages
RUN pip install -r requirements.txt

# expose the port
EXPOSE 8000

# run the app.py when the container lunches
CMD ["python", "main.py"]