class Twitter:
    tweet_list = []
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def twitter_main(self):
        while True:
            user_name = input("Input your username, ''= quit:\n")
            if user_name == '':
                print('Quit')
                break
            else:
                while True:
                    self.print_menu()
                    user_choice = input('Choose one:\n')
                    if user_choice == '2':
                        date = input('Input date, format:(Jan 01):\n')
                        message = input('input message:\n')
                        self.add_tweet(user_name, date, message)
                    elif user_choice == '3':
                        name = input('Input name:\n')
                        self.search_by_at(name)
                    elif user_choice == '4':
                        hash_tag = input('Input a hash tag:\n')
                        self.search_by_hashtag(hash_tag)
                    elif user_choice == '5':
                        self.search_by_author(user_name)
                    elif user_choice == '6':
                        print('Logout')
                        break
                    else:
                        print("Can't understand")

    def print_menu(self):
        print('------------------------')
        print('2. Make a new Tweet')
        print('3. Search Tweets by username')
        print('4. Search Tweets by hash tag')
        print('5. See all the Tweet made by the user')
        print('6. Logout')
        print('------------------------')

    def add_tweet(self, author, date, message):
        at_list = []
        hash_list = []
        for i in range(0, len(message) - 1):
            if message[i] == '@':
                for j in range(i, len(message)):
                    if message[j] == ' ' or j == len(message) - 1:
                        at_list.append(message[i + 1: j])
                        break
            elif message[i] == '#':
                for j in range(i, len(message)):
                    if message[j] == ' ' or j == len(message) - 1:
                        hash_list.append(message[i + 1: j])
                        break
        Twitter.tweet_list.append(
            {'author': author, 'date': date, 'message': message, 'at_list': at_list, 'hash_list': hash_list})
        print('Done')

    def search_by_at(self, name):
        result = '------------------------'
        for tweet in Twitter.tweet_list:
            if (name) in tweet['at_list']:
                result += f"\nBy: {tweet['author']}\nDate: {tweet['date']}\n{tweet['message']}\n------------------------"
        if len(result) == 0:
            print('Nothing Found')
        else:
            print(result)

    def search_by_hashtag(self, hash_tag):
        result = '------------------------'
        for tweet in Twitter.tweet_list:
            if (hash_tag) in tweet['hash_list']:
                result += f"\nBy: {tweet['author']}\nDate: {tweet['date']}\n{tweet['message']}\n------------------------"
        if len(result) == 0:
            print('Nothing Found')
        else:
            print(result)

    def search_by_author(self, user_name):
        result = []
        result_str = ''
        for tweet in Twitter.tweet_list:
            if tweet['author'] == user_name:
                result.append(tweet)
        if len(result) == 0:
            print('Nothing Found')
        else:
            self.sort_Date(result)
            for tweet in result:
                result_str += f"\nBy: {tweet['author']}\nDate: {tweet['date']}\n{tweet['message']}\n------------------------"
            print(result_str)

    def sort_Date(self, result_list):
        for index in range(1, len(result_list)):
            item_waiting = result_list[index]
            result_list.pop(index)
            for index2 in range(0, index):
                if Twitter.month.index(item_waiting['date'][0:3]) < Twitter.month.index(
                        result_list[index2]['date'][0:3]):
                    result_list.insert(index2, item_waiting)
                    break
                elif Twitter.month.index(item_waiting['date'][0:3]) == Twitter.month.index(
                        result_list[index2]['date'][0:3]):
                    if int(item_waiting['date'][4:-1]) <= int(result_list[index2]['date'][4:-1]):
                        result_list.insert(index2, item_waiting)
                        break
            else:
                result_list.insert(index, item_waiting)


twitter = Twitter()
twitter.twitter_main()
