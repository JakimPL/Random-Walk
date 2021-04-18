def progress_bar(current, total, bar_length=50):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * bar_length - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))
    percent = int(percent)
    print("Progress: [{2}{3}] frame: {0}/{1} ({4}%)".format(current, total, arrow, spaces, percent), end='\r')
