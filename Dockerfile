# python image
FROM python:3.12-slim
# working directory
WORKDIR /app
# copy all files to /app
COPY . /app
# install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt
# check if the code is working
RUN python manage.py check
# set dummy variables only for building the image
ENV SECRET_KEY="dummy_secret_key"
ENV DJANGO_SETTINGS_MODULE="hardboiledegg.settings.production"
# collect static files
RUN python manage.py collectstatic --noinput
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]