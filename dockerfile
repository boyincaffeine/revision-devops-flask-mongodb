FROM python
COPY . .
RUN pip install -r requirement.txt
CMD ["python","app.py"]
