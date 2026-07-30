from __future__ import annotations

import os
import time

from dataclasses import dataclass
from enum import Enum


class State(Enum):
    RUNNING="running"
    STOPPED="stopped"


@dataclass
class Engineer:
    level:int=1
    xp:int=0
    streak:int=0
    missions:int=0

    @property
    def needed(self):
        return self.level*100


@dataclass
class Container:
    image:str
    status:State=State.RUNNING


engineer=Engineer()
images=set()
containers={}
logs={}


def clear():
    os.system("cls" if os.name=="nt" else "clear")


def slow(text):
    for c in text:
        print(c,end="",flush=True)
        time.sleep(.01)
    print()


def pause():
    input("\nPress ENTER...")


def banner():
    print("""
╔══════════════════════════════╗
       🐳 DOCKER QUEST
    Container Training Lab
╚══════════════════════════════╝
""")


def gain(amount):
    engineer.xp+=amount

    if engineer.xp>=engineer.needed:
        engineer.level+=1
        engineer.xp=0
        print(f"""
🎉 LEVEL UP!

🐳 Engineer Level {engineer.level}
""")
        time.sleep(1)


def reward():
    engineer.missions+=1
    engineer.streak+=1
    amount=25+engineer.streak*5

    print(f"""
✅ SUCCESS
🔥 Streak {engineer.streak}
⭐ +{amount} XP
""")

    gain(amount)


def help_cmd():
    print("""
🐳 DOCKER COMMANDS

docker images
docker pull <image>
docker run <image>
docker ps
docker ps -a
docker logs <name>
docker stop <name>
docker rm <name>
docker exec <name>
docker build <name>

status
clear
exit
""")


def images_cmd():
    print("\n📦 IMAGES")

    if not images:
        print("No images")
        return

    for img in images:
        print(" └─",img)


def pull(p):
    if len(p)<3:
        print("Usage: docker pull <image>")
        return

    img=p[2]

    if img in images:
        print("Already exists")
        return

    images.add(img)

    print("""
⬇ Pulling image...
🐳 Pull complete
""")


def build(p):
    if len(p)<3:
        print("Usage: docker build <name>")
        return

    name=p[2]
    images.add(name)

    print(f"""
🏗 Building...

[1/3] Dependencies
[2/3] Files
[3/3] Image

✅ Built {name}
""")


def run(p):
    if len(p)<3:
        print("Usage: docker run <image>")
        return

    img=p[2]

    if img not in images:
        print("""
❌ Image missing

Use:
docker pull <image>
""")
        return

    name=f"{img.replace(':','-')}-{len(containers)+1}"

    containers[name]=Container(img)

    logs[name]=[
        "Container started",
        "Application loading",
        "Service healthy"
    ]

    print(f"""
🚀 Created

{name}
""")


def ps(all=False):
    print("\n🐳 CONTAINERS")

    if not containers:
        print("No containers")
        return

    for name,c in containers.items():
        if all or c.status==State.RUNNING:
            print(f"{name} | {c.image} | {c.status.value}")


def stop(p):
    if len(p)<3:
        return

    name=p[2]

    if c:=containers.get(name):
        c.status=State.STOPPED
        print("🛑 Stopped",name)
    else:
        print("Container not found")


def remove(p):
    if len(p)<3:
        return

    name=p[2]

    if containers.pop(name,None):
        print("🗑 Removed",name)
    else:
        print("Container not found")


def logs_cmd(p):
    if len(p)<3:
        return

    print("\n📜 LOGS")

    for line in logs.get(p[2],["No logs"]):
        print(line)


def exec_cmd(p):
    if len(p)<3:
        return

    if p[2] in containers:
        print("""
🔑 Container shell

root@container:/#

ls
cat app.py
exit
""")
    else:
        print("Container not found")


def status():
    print(f"""
📊 STATUS

Level: {engineer.level}
XP: {engineer.xp}/{engineer.needed}
🔥 Streak: {engineer.streak}
🎯 Missions: {engineer.missions}
""")


def terminal():
    clear()
    banner()

    print("""
Welcome Engineer 🐳

Type:
docker help
""")

    simple={
        "docker help":help_cmd,
        "docker images":images_cmd,
        "docker ps":lambda:ps(),
        "docker ps -a":lambda:ps(True),
        "status":status
    }

    while True:

        cmd=input("docker@quest:~$ ").strip()

        if not cmd:
            continue

        if cmd=="exit":
            break

        if cmd=="clear":
            clear()
            continue

        if cmd in simple:
            simple[cmd]()
            continue

        p=cmd.split()

        match p[:2]:
            case ["docker","pull"]: pull(p)
            case ["docker","run"]: run(p)
            case ["docker","logs"]: logs_cmd(p)
            case ["docker","stop"]: stop(p)
            case ["docker","rm"]: remove(p)
            case ["docker","exec"]: exec_cmd(p)
            case ["docker","build"]: build(p)
            case _:
                print("❓ Unknown command")


def mission():
    clear()
    banner()

    slow(random.choice([
"""
🚨 INCIDENT

Website is broken.

Hint:
Check logs.
""",
"""
🚨 INCIDENT

Deploy nginx.
""",
"""
🚨 INCIDENT

Developer needs shell access.
"""
]))

    pause()
    terminal()
    reward()


def menu():
    while True:
        clear()
        banner()

        print("""
1️⃣ Simulator
2️⃣ Missions
3️⃣ Status
4️⃣ Exit
""")

        match input("> "):
            case "1": terminal()
            case "2": mission()
            case "3":
                clear()
                banner()
                status()
                pause()
            case "4":
                print("🐳 Goodbye Engineer")
                break


if __name__=="__main__":
    menu()