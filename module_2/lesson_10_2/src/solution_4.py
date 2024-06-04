def choose_ad_platform(budget):
    if budget < 1000:
        print("Google")
    elif 1000 <= budget <= 5000:
        print('Facebook')
    else:
        print('Instagram')
