FROM python:3.10 

ARG PORT
ENV PORT=8080

RUN mkdir -pv /usr/src/python_echo 
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "python", "./server.py" ]