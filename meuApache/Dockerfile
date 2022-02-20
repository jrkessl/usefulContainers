FROM httpd:2.4.52

RUN sed -i 's/Listen 80/Listen 9000/' /usr/local/apache2/conf/httpd.conf
RUN rm /usr/local/apache2/htdocs/index.html && echo "Voce chegou na pagina web do apache." > /usr/local/apache2/htdocs/index.html && echo "hostname: "$HOSTNAME >> /usr/local/apache2/htdocs/index.html

EXPOSE 9000
CMD ["httpd-foreground"]
