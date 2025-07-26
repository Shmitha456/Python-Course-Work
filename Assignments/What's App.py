n=int(input("Enter the no of messages: "))
chat={}
for i in range(n):
    name,message=input().split(':')
    if name in chat:
        chat[name].append((i,message))
    else:
        chat[name]=[(i,message)]

print(chat)


while True:
    print("1.Count total number of messages ")
    print("2.Identify unique users in the chat")
    print("3.Count total words in the chat ")
    print("4.Calculate average words per message ")
    print("5.Find the longest message sent ")
    print("6.Find the most active user ")
    print("7.Get message count for a specific user ")
    print("8.Find the most frequently used word by a specific user")
    print("9.Retrieve the first and last message sent by a user")
    print("10.Check if a user is present in the chat")
    print("11.Find commonly repeated words ")
    print("12.Identify the user with the longest average message length ")
    print("13.Count how many messages mention a specific user ")
    print("14.Remove duplicate messages ")
    print("15.Sort messages alphabetically ")
    print("16.Extract all questions asked in the chat ")
    print("17.Calculate the reply ratio between two users ")
    print("18.Check for deleted messages")
    print("19.Exit ")

    ch=int(input("Enter your choice: "))
    if ch==1:
        print(f"The count of total number of messages: {n}")

    elif ch==2:
        print(f'The Unique users in the chat: {set(chat.keys())}')

    elif ch==3:
        total_words = sum(len(message.split()) for messages in chat.values() for _, message in messages)
        print(f'Total words in the chat:')
        print(total_words)
    
    elif ch==4:
        total_messages = sum(len(messages) for messages in chat.values())
        total_words = sum(len(message.split()) for messages in chat.values() for _, message in messages)
        if total_messages > 0:
            average_words = total_words / total_messages
            print(f'Average words per message: {average_words}')
        else:
            print('No messages to calculate average words.')

    elif ch==5:
        longest_message = ''
        for messages in chat.values():
            for _, message in messages:
                if len(message) > len(longest_message):
                    longest_message = message
        print(f'The longest message sent: {longest_message}')

    elif ch==6:
        user_activity = {user: len(messages) for user, messages in chat.items()}
        most_active_user = max(user_activity, key=user_activity.get)
        print(f'The most active user: {most_active_user}')

    elif ch==7:
        user = input("Enter the username to get message count: ")
        if user in chat:
            print(f'Message count for {user}: {len(chat[user])}')
        else:
            print(f'User {user} not found.')

    elif ch==8:
        user = input("Enter the username to find frequently used word: ")
        if user in chat:
            words = {}
            for _, message in chat[user]:
                for word in message.split():
                    words[word] = words.get(word, 0) + 1
            most_frequent_word = max(words, key=words.get)
            print(f'Most frequently used word by {user}: {most_frequent_word}')
        else:
            print(f'User {user} not found.')

    elif ch==9:
        user = input("Enter the username to retrieve first and last message: ")
        if user in chat:
            first_message = chat[user][0][1]
            last_message = chat[user][-1][1]
            print(f'First message: {first_message}, Last message: {last_message}')
        else:
            print(f'User {user} not found.')

    elif ch==10:
        user = input("Enter the username to check presence: ")
        if user in chat:
            print(f'User {user} is present in the chat.')
        else:
            print(f'User {user} is not present in the chat.')

    elif ch==11:
        from collections import Counter
        all_words = []
        for messages in chat.values():
            for _, message in messages:
                all_words.extend(message.split())
        common_words = Counter(all_words).most_common(5)
        print('Commonly repeated words:', common_words)

    elif ch==12:
        user_avg_length = {user: sum(len(message) for _, message in messages) / len(messages) if messages else 0 for user, messages in chat.items()}
        longest_avg_user = max(user_avg_length, key=user_avg_length.get)
        print(f'User with the longest average message length: {longest_avg_user}')

    elif ch==13:
        user = input("Enter the username to count mentions: ")
        mention_count = 0
        for messages in chat.values():
            for _, message in messages:
                if user in message:
                    mention_count += 1
        print(f'Number of messages mentioning {user}: {mention_count}')
    
    elif ch==14:
        unique_messages = set()
        for messages in chat.values():
            for message in messages:
                unique_messages.add(message[1])
        print('Messages after removing duplicates:', unique_messages)
    
    elif ch==15:
        sorted_messages = []
        for messages in chat.values():
            sorted_messages.extend(messages)
        sorted_messages.sort(key=lambda x: x[1])
        print('Messages sorted alphabetically:')
        for idx, message in enumerate(sorted_messages):
            print(f"{idx+1}: {message[1]}")
    
    elif ch==16:
        questions = []
        for messages in chat.values():
            for _, message in messages:
                if message.endswith('?'):
                    questions.append(message)
        print('Questions asked in the chat:')
        for question in questions:
            print(question)

    elif ch==17:
        user1 = input("Enter the first username: ")
        user2 = input("Enter the second username: ")
        replies = 0
        for messages in chat.get(user1, []):
            if messages[1].startswith(f'@{user2}'):
                replies += 1
        total_messages = len(chat.get(user1, []))
        if total_messages > 0:
            reply_ratio = replies / total_messages
            print(f'Reply ratio of {user1} to {user2}: {reply_ratio}')
        else:
            print(f'No messages from {user1} to calculate reply ratio.')

    elif ch==18:
        deleted_messages = []
        for messages in chat.values():
            for _, message in messages:
                if message.startswith('[deleted]'):
                    deleted_messages.append(message)
        if deleted_messages:
            print('Deleted messages found:')
            for msg in deleted_messages:
                print(msg)
        else:
            print('No deleted messages found.')

    elif ch==19:
        print("Exiting the chat analysis program.")
        break
    else:
        print("Invalid Choice!!!")
