# Flask + EC2 + RDS App (LAMP Replacement) + NGINX Reverse Proxy + CloudWatch

A Python Flask application hosted on EC2, connected to an RDS MySQL database, fronted by an NGINX reverse proxy **or** an AWS Application Load Balancer (ALB), with monitoring and logging integrated using Amazon CloudWatch. This setup replaces a traditional LAMP stack with a modern, observable Pythonic infrastructure.

---

## 📄 Features

* **Visitor Tracker**: Displays a message on `/` and reads names from RDS on `/people`
* **Health Endpoint**: `/health` returns `200 OK` for ALB/NGINX health checks
* **Database Integration**: Connects securely to an RDS MySQL instance
* **Reverse Proxy**: NGINX forwards traffic from port 80 to Flask app on port 3000
* **Load Balanced (Optional)**: Integrated with AWS ALB
* **Auto Scaling Group**: Automatically scales EC2 instances
* **CloudWatch Logs**: Collects NGINX access/error logs and Flask logs
* **CloudWatch Metrics**: Monitors CPU, RAM, and Disk usage
* **CloudWatch Alarms**: Alerts for high CPU usage and EC2 failures

---

## 🛠️ Architecture Overview

```
User
  |
[EC2 Public IP / ALB DNS]
  |
NGINX (port 80)
  |
Flask App (port 3000)
  |
Amazon RDS (MySQL)
```

OR with ALB:

```
User
  |
ALB (HTTP:80)
  |
Target Group (port 80)
  |
NGINX (Reverse Proxy on EC2)
  |
Flask App (port 3000)
  |
Amazon RDS (MySQL)
```

---

## 🔄 Endpoints

| Route     | Description                    |
| --------- | ------------------------------ |
| `/`       | Displays welcome message       |
| `/people` | Reads visitor names from MySQL |
| `/health` | Used for health check (200 OK) |

---

## 🌐 Public App URL

[http://flask-alb-1147350152.eu-west-1.elb.amazonaws.com](http://flask-alb-1147350152.eu-west-1.elb.amazonaws.com) OR `http://<EC2-IP>`

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone git@github.com:yourname/lamp-stack.git
cd lamp-stack
```

### 2. Configure Environment Variables

Create a `.env` file:

```env
DB_HOST=<your-rds-endpoint>
DB_NAME=testdb
DB_USER=admin
DB_PASSWORD=yourpassword
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Up Database (Optional)

Run this only once to create the `visitors` table:

```bash
python db_setup.py
```

### 5. Run App

```bash
python app.py
```

The app will be available at `http://<your-ec2-public-ip>:3000`

### 6. Set Up NGINX Reverse Proxy

Configure `/etc/nginx/nginx.conf`:

```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Restart NGINX:

```bash
sudo systemctl restart nginx
```

### 7. Register Flask as a Service (optional)

```bash
sudo nano /etc/systemd/system/flaskapp.service
```

```ini
[Unit]
Description=Flask Application
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/home/ec2-user/lamp-stack
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reexec
sudo systemctl start flaskapp
sudo systemctl enable flaskapp
```

---

## ☁️ CloudWatch Monitoring & Logging

### ✅ CloudWatch Agent Configured to Collect:

* CPU, RAM, Disk usage
* NGINX access & error logs
* Flask app logs

### 📤 Log Groups

* `nginx-access-log`
* `nginx-error-log`
* `flask-app-log`

### 🔔 Alarms

* `CPUUsage > 80%`
* `EC2 StatusCheckFailed > 0`
* Notifications sent via SNS (email subscription confirmed)

---

## 📈 Future Improvements

* Use Gunicorn + systemd to manage Flask process
* CI/CD pipeline for automated deployments
* Store secrets in AWS Systems Manager (SSM) or Secrets Manager
* Add HTTPS via ACM + ALB SSL listener
* Set up Fluent Bit or FireLens for enhanced logging

---

## 👀 Screenshots

Add screenshots of your:

* Target Group health checks
* Load Balancer listener setup
* NGINX Logs in CloudWatch
* CloudWatch metrics dashboard
* CloudWatch Alarms (CPU and EC2 Status Check)

---

## 📅 Author

Jd Muhirwa
