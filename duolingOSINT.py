import datetime, argparse, requests, pycountry

ENDPOINT_MAIL = "https://www.duolingo.com/2017-06-30/users?email="
ENDPOINT_USERNAME = "https://www.duolingo.com/2017-06-30/users?username="

def call_by_username(username):
    return requests.get(ENDPOINT_USERNAME + username, headers={"User-Agent": "Miaou"}).json()

def call_by_mail(mail):
    return requests.get(ENDPOINT_MAIL + mail, headers={"User-Agent": "Miaou"}).json()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-m', '--mail',help="Target mail address",required=False)
    group.add_argument('-u', '--username',help="Target Duolinguo username",required=False)
    args = parser.parse_args()
    if args.mail is None:
        response = call_by_username(args.username)
    else:
        response = call_by_mail(args.mail)
    usercount = len(response["users"])
    match usercount:
        case 0:
            print("Couldn't find any users with the given information.")
            exit(0)
        case 1:
            print("Found 1 user with the given information.")
        case _:
            print("Found multiple (" + str(usercount) + ") users with the given information.")
    for user in response["users"]:
        print("Informations about     : " + user["username"])
        print("Profile picture        : " + "https:" + user["picture"] + "/xxlarge")
        if "name" in user:
            print("Name                   : " + user["name"])
        print("Account Creation Date  : " + str(datetime.datetime.fromtimestamp(user["creationDate"])))
        if user["profileCountry"] is not None:
            print("Country                : " + pycountry.countries.get(alpha_2=user["profileCountry"]).name)
        print("Streak                 : " + str(user["streak"]))
        print("Has recent activity    : " + str(user["hasRecentActivity15"]))
        if user["bio"] != "":
            print("Biography              : " + user["bio"])
        print("Languages studied      : ")
        for course in user["courses"]:
            print(" + " + course["title"])
            print("   + " + str(course["crowns"])+ " crowns")
            print("   + " + str(course["xp"]) + " xp")
