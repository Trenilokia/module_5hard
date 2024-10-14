
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"{self.title}"

    def __str__(self):
        return f"{self.title}"

    #    def __contains__(self, item):
    #        return item in self.title

    def __time_now___(self, s=0):
        pass


class UrTube:

    def __init__(self):
        self.videos = []
        self.users = {}
        self.current_user = []

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {self.users[nickname]} уже существует")
        else:
            self.users[nickname] = User(nickname, password, age)
            current_user = self.users[nickname]
            return self.users[nickname]

    def login(self, nickname, password):
        if self.users[nickname].password == hash(password):
            self.current_user = self.users[nickname]
            return True

    def logout(self):
        if self.register != self.current_user:
            self.current_user = None

    def add(self, *args):
        result = []
        for i in args:
            if args not in self.videos:
                result.append(i)
        self.videos += result
        return self.videos

    def __contains__(self, item):
        return item in self.videos

    def get_videos(self, search_word):
        search_word = search_word.lower()
        found = []
        for i in self.videos[::]:
            if search_word in str(i).lower():
                found.append(i)
        return found

    def watch_video(self, title):
        video = next((x for x in self.videos if x.title == title), None)
        if video is not None:
            for i in video.duration:
                print(i)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)



