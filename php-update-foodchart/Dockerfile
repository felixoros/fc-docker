FROM php:7.2-apache

RUN apt-get update && apt-get install git-core -y && apt-get install -y software-properties-common

RUN apt-get install -y python3.4 python3-pip
RUN python3 -m pip install pymongo
RUN python3 -m pip install requests

# Config apache2 server
RUN echo "ServerName localhost" >> $APACHE_CONFDIR/apache2.conf &&\
    echo "ServerName localhost" >> $APACHE_CONFDIR/httpd.conf

# Install low level mongoDB Driver && xDebug
RUN pecl install mongodb-1.5.2
RUN pecl install xdebug-2.7.0

# Install composer in order to add php extensions
COPY ./composer/composer.phar /usr/local/bin/composer

# Copy the php config file
COPY ./configs/php.ini /usr/local/etc/php/

# COPY SSL CERTIFICATION
COPY ./configs/server.crt /etc/apache2/ssl/server.crt
COPY ./configs/server.key /etc/apache2/ssl/server.key

COPY ./configs/foodchart.conf /etc/apache2/sites-enabled/foodchart.conf

RUN a2enmod rewrite
RUN a2enmod ssl

# Copy hello-cron file to the cron.d directory
COPY ./cronjobs-foodchart/updateRankings.py /etc/cron.d/updateRankings.py
COPY ./cronjobs-foodchart/updateRankings.sh /etc/cron.d/updateRankings.sh

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/updateRankings.py
RUN chmod 0644 /etc/cron.d/updateRankings.sh

# Apply cron job
RUN crontab /etc/cron.d/updateRankings.sh

RUN service cron start
# Run the command on container startup
# CMD ["sh","-c","cron -f && ./usr/sbin/apache2ctl -DFOREGROUND"]
# usr/sbin/apache2ctl -DFOREGROUND"]
# CMD ["cron", "-f", ";", "/usr/bin/apache2-foreground", "-D", "FOREGROUND"]
# CMD /usr/local/bin/ httpd-foreground && cron -f
# CMD ["cron", "-f"]

# COPY ./configs/entrypoint.sh /entrypoint.sh
# COPY ./configs/start.sh /start.sh

# ENTRYPOINT [ "/entrypoint.sh" ]
# CMD [ "/start.sh" ]
