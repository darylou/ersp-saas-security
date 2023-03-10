# Use the Nginx image
FROM --platform=linux/amd64 nginx
#FROM nginx

COPY build/ /usr/share/nginx/html 

# Remove the default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Replace with our own nginx.conf
COPY nginx.conf /etc/nginx/conf.d/