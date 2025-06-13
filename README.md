# Flask + EC2 + RDS App (LAMP Replacement)

A Python Flask application hosted on EC2, connected to an RDS MySQL database, and fronted by an AWS Application Load Balancer (ALB). This replaces a traditional LAMP stack with a modern Pythonic setup.

---

## 📄 Features

* **Visitor Tracker**: Displays a message on `/` and reads names from RDS on `/people`
* **Health Endpoint**: `/health` returns `200 OK` for load balancer health checks
* **Database Integration**: Connects securely to an RDS MySQL instance
* **Load Balanced**: Deployed behind an Application Load Balancer (ALB)
* **Auto Scaling Group**: Automatically scales EC2 instances

---

## 🛠️ Architecture Overview

```
User
  |
ALB (HTTP:80)
  |
Target Group (port 80)
  |
Auto Scaling Group
  |
EC2 Instance(s) (Flask App running on port 3000)
  |
Amazon RDS (MySQL)
```

---

## 🔄 Endpoints

| Route     | Description                        |
| --------- | ---------------------------------- |
| `/`       | Displays welcome message           |
| `/people` | Reads visitor names from MySQL     |
| `/health` | Used for ALB health check (200 OK) |

---

## 🌐 Public App URL

[http://flask-alb-1147350152.eu-west-1.elb.amazonaws.com](http://flask-alb-1147350152.eu-west-1.elb.amazonaws.com)

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

---

## 🌟 AWS Deployment Summary

* **EC2 Instance**:

  * Ubuntu or Amazon Linux 2
  * Flask app runs on port `3000`
  * Security Group: allows port `3000` from ALB only

* **RDS (MySQL)**:

  * DB name: `testdb`
  * Multi-AZ option enabled (for HA)
  * Security Group: allows port `3306` from EC2 SG only

* **Application Load Balancer**:

  * Listener: `HTTP:80`
  * Target Group: forwards to port `80`
  * Health Check: `/health`

* **Auto Scaling Group**:

  * Desired capacity: 1
  * Scaling policies (optional)
  * Lifecycle hook integrated with SNS (optional)

---

## 📈 Future Improvements

* Use Gunicorn + systemd to manage Flask process
* CI/CD pipeline for automated deployments
* Store secrets in AWS Systems Manager (SSM) or Secrets Manager
* Add HTTPS via ACM + ALB SSL listener

---

## 👀 Screenshots

Add screenshots of your:

* Target Group health checks
  <img width="1470" alt="image" src="https://github.com/user-attachments/assets/d1ef0d24-c6ac-4c73-a4ef-528b1153e47a" />

* Load Balancer listener setup
 <img width="1470" alt="Screenshot 2025-06-13 at 11 12 53 PM" src="https://github.com/user-attachments/assets/5ee59426-7f24-46b6-844d-82ba10d48df0" />
 

## 📅 Author

Jd Muhirwa

---

