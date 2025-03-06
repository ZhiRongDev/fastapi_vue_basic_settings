sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout snakeoil.key -out snakeoil.crt \
    -subj "/C=TW/ST=Taiwan/L=Taipei/O=hti/OU=IT"

sudo chmod 644 snakeoil.key
sudo chmod 644 snakeoil.crt