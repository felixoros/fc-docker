#!/bin/bash

echo " ******** -- Entrypoint script started -- ******** "
cd /var/www/html/

if [ ! -f ./composer.json ]; then
	echo " ******** -- Fetching composer dependencies -- ******** "
	exec composer require mongodb/mongodb && composer require chillerlan/php-qrcode
fi

echo " ******** -- Entrypoint script finished -- ******** "