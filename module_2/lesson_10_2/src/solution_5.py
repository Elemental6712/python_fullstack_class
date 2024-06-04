def analyze_ad_efficiency(clicks, impressions, views):
    if clicks / impressions < 0.01:
        print('Недооцененная')
    elif 0.05 > clicks / impressions > 0.01:
        print('Низкая')
    elif 0.1 > clicks / impressions > 0.05 and views > clicks:
        print('Средняя')
    elif clicks / impressions > 0.1:
        print('Высокая')
    else:
        print('Неопределенная')
analyze_ad_efficiency(500, 10000, 200)