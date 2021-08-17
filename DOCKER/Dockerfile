FROM python:3.8.11-alpine
COPY . /Mitya/
WORKDIR /Mitya/
RUN chmod +x trtr_mitya/driver/geckodriver && apk update && apk add firefox-esr && apk add xvfb && pip install -r requirements.txt
# ENTRYPOINT ["entrypoint.sh"]
VOLUME /dev/shm /dev/shm
ENV PYTHONPATH="/Mitya/:/Mitya/trtr_mitya/driver/"
CMD ["python3", "bin/run_test.py"]