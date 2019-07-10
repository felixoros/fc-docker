FROM php:7.2-apache

RUN apt-get update && apt-get install git-core -y && apt-get install -y software-properties-common

# Install PHP GD for MPDF Lib
RUN apt-get update && \
    apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng-dev && \
    docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && \
    docker-php-ext-install gd

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

# RUN docker-php-ext-install

RUN a2enmod rewrite
RUN a2enmod ssl

# COPY ./configs/entrypoint.sh /entrypoint.sh
# COPY ./configs/start.sh /start.sh

# ENTRYPOINT [ "/entrypoint.sh" ]
# CMD [ "/start.sh" ]
