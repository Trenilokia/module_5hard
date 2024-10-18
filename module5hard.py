from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __repr__(self):
        return f"{self.nickname}"

    def __str__(self):
        return f"{self.nickname}"


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

    def __time_now___(self, s=0):
        pass


class UrTube:

    def __init__(self):
        self.videos = []
        self.users = []
        self.current_user = None

    def register(self, nickname, password, age):
        password = hash(password)
        for i in self.users:
            if i.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def login(self, nickname, password):
        if nickname in self.users[nickname] and self.users[nickname].password == hash(password):
            self.current_user = self.users[nickname]

    def __eq__(self, other):
        return self.current_user == other

    def __ne__(self, other):
        return self.current_user != other

    def logout(self):
        self.current_user = None

    def add(self, *args):
        result = []
        for i in args:
            if args not in self.videos:
                result.append(i)
        self.videos += result

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
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for i in self.videos:
            if title in str(i):
                video = i
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу')
                    return
                for k in range(video.duration):
                    print(video.time_now + k + 1, end=' ')
                    sleep(1)
                    if k == video.duration - 1:
                        print('Конец видео')
                        video.time_now = 0


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
