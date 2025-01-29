FROM runpod/pytorch:2.1.1-py3.10-cuda12.1.1-devel-ubuntu22.04

COPY . .
RUN pip install --ignore-installed -r requirements.txt

CMD ["python3", "app.py"]