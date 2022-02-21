class Character:

    # 特殊メソッド: __****__ の形で表記される特定の条件を満たすと実行される特殊な関数
    # コンストラクタ __init__ : インスタンス化される際に実行
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 100
        self.atk = 10

    def attack(self, target):
        target.hp -= self.atk
        print(f'{self.name}の攻撃。{self.atk}ダメージを与えた。')

    def print_status(self):
        print(f'name: {self.name}')
        print(f'HP: {self.hp}')
        print(f'MP: {self.mp}')
        print(f'attack: {self.atk}')

class Player(Character):
    def healing(self, power):
        if self.mp >= power:
            self.mp -= power
            self.hp += power
        else:
            print('MPが足りません。')

class Enemy(Character):
    def power_up(self, power):
        if self.mp >= power:
            self.mp -= power
            self.atk += power
        else:
            print('MPが足りません。')



print('<<<バンタンクエスト>>> 敵を倒そう')

hero = Player('You')
enemy = Enemy('enemy')

while True:
    print()
    hero.print_status()
    enemy.print_status()

    print(f'\n{hero.name}のターン')
    command = input('1: 攻撃, 2: 回復 → ')
    if command == '1':
        enemy.attack(enemy)
    elif command == '2':
        hero.healing(50)
    else:
        print('false')

    print(f'\n{enemy.name}のターン')
    enemy.attack(hero)

    if enemy.hp <= 0:
        print(f'{enemy.name}を倒した')
        break
    if hero.hp <= 0:
        print(f'{hero.name}は力尽きた')
        break