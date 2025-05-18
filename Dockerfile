FROM python:3.12

COPY . .

RUN chmod +x buildvllm.sh

RUN ./buildvllm.sh

RUN pip install -r requirements.txt

CMD ["python", "app.py"]