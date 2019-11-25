import time
import os
import json

def load_json_file(file):
    try:
        with open(file) as f:
            data = json.load(f)
            f.close()
            return data
    except FileNotFoundError:
        return {}

def write_json_file(data, filePath):
    with open(filePath, 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)
        outfile.close()



login_activity = load_json_file("static_resources/activity/login_activity.json")
user_activity = load_json_file("static_resources/activity/user_activity.json")
page_activity = load_json_file("static_resources/activity/page_activity.json")


def add_login_activity(user):
    # Update user visits
    if user in login_activity:
        login_activity[user]["last_login"] = time.asctime(time.localtime(time.time()))
        current_logins = login_activity[user]["login_count"]
        current_logins += 1
        login_activity[user]["login_count"] = current_logins
    else:
        print("not exist")
        login_activity[user] = {}
        login_activity[user]["last_login"] = time.asctime(time.localtime(time.time()))
        login_activity[user]["login_count"] = 1
    write_json_file(login_activity, "static_resources/activity/login_activity.json")


def add_user_activity(ip, page):
    # Update user visits
    print("gogo")
    if ip in user_activity:
        current_visits = user_activity[ip]
        current_visits += 1
        user_activity[ip] = current_visits
    else:
        user_activity[ip] = 1
    # Update page visits
    if page in page_activity:
        current_visits = page_activity[page]
        current_visits += 1
        page_activity[page] = current_visits
    else:
        page_activity[page] = 1
    print("done")
    write_json_file(user_activity, "static_resources/activity/user_activity.json")
    write_json_file(page_activity, "static_resources/activity/page_activity.json")


def get_user_activity():
    return user_activity, page_activity, login_activity