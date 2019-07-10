#!/bin/bash

echo "Staring apache server ..."
exec apache2 -DFOREGROUND "$@"
