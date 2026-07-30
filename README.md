# 🐳 Docker Quest

**An interactive terminal-based Docker learning game built in Python. Complete missions, manage containers, earn XP, level up your engineer, and master Docker commands through a gamified CLI simulator.**

![Docker Quest](https://img.shields.io/badge/Docker-Quest-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge)

---

## 🎮 About

Docker Quest is a beginner-friendly Docker training simulator that turns learning container management into a game.

Instead of memorizing commands, you complete missions, solve incidents, and gain experience while practicing common Docker workflows in a safe simulated environment.

Train your skills as a container engineer:

* 🐳 Manage images
* 📦 Create and run containers
* 📜 Inspect container logs
* 🛑 Stop and remove containers
* 🔑 Access simulated container shells
* 🏗 Build images
* 🎯 Complete engineering missions
* ⭐ Earn XP and level up

---

## 🚀 Features

### Container Simulator

Practice Docker-style commands:

```bash
docker images
docker pull <image>
docker run <image>
docker ps
docker ps -a
docker logs <container>
docker stop <container>
docker rm <container>
docker exec <container>
docker build <name>
```

### 🎯 Mission System

Take on simulated DevOps incidents:

Examples:

```
🚨 INCIDENT

Website is broken.

Hint:
Check logs.
```

```
🚨 INCIDENT

Deploy nginx.
```

```
🚨 INCIDENT

Developer needs shell access.
```

Complete missions to earn:

* ⭐ XP
* 🔥 Streak bonuses
* 🎖 Engineer levels

---

## 📊 Progress System

Your engineer improves over time:

```
📊 STATUS

Level: 3
XP: 75/300
🔥 Streak: 5
🎯 Missions: 12
```

Level up as you complete more challenges.

---

## 🕹 Gameplay

Start the simulator:

```
🐳 DOCKER QUEST
Container Training Lab

Welcome Engineer 🐳

Type:
docker help
```

Example:

```
docker@quest:~$ docker pull nginx

⬇ Pulling image...
🐳 Pull complete


docker@quest:~$ docker run nginx

🚀 Created

nginx-1
```

---

## 🧠 Learning Goals

Docker Quest helps you practice:

* Container lifecycle management
* Image workflows
* Docker CLI concepts
* Debugging with logs
* Basic DevOps thinking
* Incident response workflows

---

## 🛠 Built With

* Python 3
* Dataclasses
* Enums
* Terminal UI
* Object-oriented programming


## 🐳 Become a Container Engineer

Learn Docker by doing.

**Complete missions. Fix incidents. Level up. Master containers.**
