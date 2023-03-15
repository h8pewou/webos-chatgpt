# webos-chatgpt
Proof of concept ChatGPT implementation for legacy webOS devices.

## Install prerequisites on Debian 11

### Install pip:
```apt install python3-pip```

### Install Python dependencies:
```pip3 install flask_cors flask openai```

### Install nginx:
```apt install nginx```

## Development backend

### Obtain OpenAI API key
1. Sign up: https://beta.openai.com/signup
2. Open: https://beta.openai.com/account/api-keys
3. Click the "Create new secret key" button

### Add OpenAI API key to main.py
Add key to ```main.py```, look for ```openai.api_key =```

### main.py
Launch main.py as follows: ```python3 main.py```

## Web server

### nginx configuration
Edit ```/etc/nginx/sites-available/chatbot.conf``` using the contents from this github. Ensure that you dit the ```server_name``` directive to match your hostname and IP.
Create a symlink as follows:
```ln -s /etc/nginx/sites-available/chatbot.conf /etc/nginx/sites-enabled/```
Restart nginx:
```systemctl restart nginx```
Allow 80/tcp in your firewall (e.g., ```ufw allow http```).

## Frontend
### Create new directory & add files
Create /var/www/chatbot:
```mkdir /var/www/chatbot```
Download index.html and jquery-3.6.0.min.js to the directory.

## Usage
Navigate with your webOS browser to the host or IP address.
