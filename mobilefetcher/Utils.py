import instaloader

class InstaInteractor:
    username = "instantcodelearn"
    password = "passwordbaka"

    def get_list_of_suggestions(username, password):
        L = instaloader.Instaloader()
        ##username = "instantcodelearn"
        ##password = "passwordbaka"
        # Login or load session
        L.login(username, password)
        profile = instaloader.Profile.from_username(L.context, username)
        l = []
        # Print list of followees
        for x in profile.get_similar_accounts():
            l.append(x.username)
        return l

    def get_list_of_suggestions(username, password, anotherusername):
        L = instaloader.Instaloader()
        ##username = "instantcodelearn"
        ##password = "passwordbaka"
        # Login or load session
        L.login(username, password)
        profile = instaloader.Profile.from_username(L.context, anotherusername)
        l = []
        # Print list of followees
        for x in profile.get_similar_accounts():
            l.append(x.username)
        return l

    def get_phone_number_last_digits(username):
        url = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'
        data = {
            'email_or_username': username,
            'recaptcha_challenge_field': ''
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Password reset email sent successfully.")
        else:
            print("Failed to initiate password reset.")

    def get_list_of_followers(anotherusername):
        L = instaloader.Instaloader()
        L.login(username, password)
        profile = instaloader.Profile.from_username(L.context, anotherusername)
        return profile.get_follower()

    def get_list_of_followings(anotherusername):
        L = instaloader.Instaloader()
        L.login(username, password)
        profile = instaloader.Profile.from_username(L.context, anotherusername)
        return profile.get_followee()