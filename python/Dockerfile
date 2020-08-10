FROM python:3

# FROM https://stackoverflow.com/questions/37458287/how-to-run-a-cron-job-inside-a-docker-container
RUN apt-get update && apt-get -y install cron

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copy hello-cron file to the cron.d directory
COPY ynab-cron /etc/cron.d/ynab-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/ynab-cron

CMD ["cron", "-f"]
