import os, sys, pygame
from pygame.locals import *
import objects, config

#ゲームの処理モジュール

class State:
    """
    ゲームの状態に関するクラス
    """

    def handle(self, event):
        """
        イベント処理
        """
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    def first_display(self, screen):
        """
        初回の画面表示関数。画面を背景色で塗りつぶす。
        """
        screen.fill(config.background_color)
        #変更内容を画面に反映させる
        pygame.display.flip()

    def display(self, screen):
        """
        2回目以降の画面表示関数。何を行わない。
        """
        pass

class Level(State):
    """
    ゲームのプレイ画面。
    落下させた重りの数をカウント、スプライトの移動などを行う
    """

    def __init__(self, number=1):
        self.number = number
        #このレベルでかわす、重さの残り数
        self.remaining = config.weights_per_level

        speed = config.drop_speed
        #レベルが1上がるごとにスピードが増す
        speed += (self.number - 1) * config.speed_increase
        #ウェイトとバナナを生成する
        self.weight = objects.Weight(speed)
        self.banana = objects.Banana()
        both = self.weight, self.banana  #もっとスプライトを増やすこともできる
        self.sprites = pygame.sprite.RenderUpdates(both)

    def update(self, game):
        """
        前のフレームからゲーム情報を更新する
        """
        #全スプライトの更新
        self.sprites.update()
        #バナナが重りと接触する場合、ゲームをGameOver状態に切り替える
        if self.banana.touches(self.weight):
            game.next_state = GameOver()
        #重りが地面に着地したら重りをリセットする
        #レベル中の全ての重りをかわした場合はゲームをLevelCleard状態に切り替える
        elif self.weight.landed:
            self.weight.reset()
            self.remaining -= 1
            if self.remaining == 0:
                game.next_state = LevelCleared(self.number)

    def display(self, screen):
        """
        2回目以降の画面表示関数。（オーバーライド関数）
        """
        screen.fill(config.background_color)
        updates = self.sprites.draw(screen)
        pygame.display.update(updates)

class Paused(State):
    """
    ゲームの一時停止状態。（ポーズ）
    キーボードのキーかマウスのボタンを押すと解除される
    """
    finished = 0 #一時停止を解除したかどうか
    image = None #画像を使う場合はそのファイル名を設定する
    text = ''    #メッセージのテキストを設定する

    def handle(self, event):
        """
        イベントを処理する
        Stateのイベント（ゲームの終了）を処理してから、
        キーやマウスが操作されたらfinishedを1にする。
        """
        State.handle(self, event)
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.finished = 1

    def update(self, game):
        """
        レベルを更新する。キーが押されるかマウスがクリックされた場合、
        ゲームに対してself.next_state()が表している状態に切り替える
        """
        if self.finished:
            game.next_state = self.next_state()

    def first_display(self, screen):
        """
        初回のPausedステートの表示。
        画像がある場合は描画し、テキストをレンダリングする。
        """
        #まず、画面を背景色で塗りつぶして消去する
        screen.fill(config.background_color)

        #フォントとサイズを指定
        font = pygame.font.SysFont(config.font_name, config.font_size)

        #メッセージテキストの先頭と末尾の空行を削除する
        lines = self.text.strip().splitlines()

        #テキストの高さを取得する
        height = len(lines) * font.get_linesize()

        #テキストの配置位置を求める
        center, top = screen.get_rect().center
        top -= height // 2

        #表示する画像がある場合
        if self.image:
            #画像を読み込む
            image = pygame.image.load(self.image).convert()
            #画像の長方形境界を取得する
            r = image.get_rect()
            #画像をテキストの20ピクセル上に配置する
            r.midbottom = center, top - 20
            #画像を画面に転送する
            screen.blit(image, r)

        antialias = 1   #テキストを滑らかにする
        black = 0, 0, 0 #黒色（テキストの色）

        #各行をレンダリングする
        for line in lines:
            text = font.render(line.strip(), antialias, black)
            r = text.get_rect()
            r.midtop = center, top
            screen.blit(text, r)
            top += font.get_linesize()

        #全変更内容を表示に反映させる
        pygame.display.flip()

class Info(Paused):
    """
    ゲームについての情報を表示する状態
    レベル状態に遷移
    """
    next_state = Level
    text = '''
    In this game you are a banana.
    "Weight" is falling, but Dodge it and survive.'''

class StartUp(Paused):
    '''
    タイトル画面。
    その後はInfo状態に移行。
    '''
    next_state = Info
    image = config.splash_image

    text = '''
    A game in which fruits protect ourselves
    Welcome to Squish ...
    '''

class LevelCleared(Paused):
    """
    レベルクリア画面。
    次のレベル状態へ遷移する。
    """
    def __init__(self, number):
        self.number = number
        self.text = '''Level{} Cleared
        Click to start the next level'''.format(self.number)

    def next_state(self):
        return Level(self.number + 1)

class GameOver(Paused):
    """
    ゲームオーバー画面。
    """
    next_state = Level
    text = '''
    GameOver.
    Click to replay the game, click [Esc] to end.'''

class Game:
    """
    メインであるイベントループを処理するゲームオブジェクト
    """

    def __init__(self, *args):
        #ゲームと画像を格納しているディレクトリを取得する
        path = os.path.abspath(args[0])
        dir = os.path.split(path)[0]
        #取得したディレクトリに移動する（画像ファイルを開くため）
        os.chdir(dir)
        #無の状態で開始
        self.state = None
        #イベントループの初回でStartUpに遷移する
        self.next_state = StartUp()

    def run(self):
        """
        ゲームプログラムが動き出す関数
        初期化処理を実行後、メインイベントループに入る
        """
        pygame.init()   #全モジュールを初期化するために必要

        #ウィンドウモードか全画面モードのどちらで表示するか決める
        flag = 0
        if config.full_screen:
            flag = FULLSCREEN
        screen_size = config.screen_size
        screen = pygame.display.set_mode(screen_size, flag)

        pygame.display.set_caption('Squish')
        pygame.mouse.set_visible(False)

        clock= pygame.time.Clock()

        #メインループ
        while True:
            #状態が変更されている場合、新しい状態に移行する。
            if self.state != self.next_state:
                self.state = self.next_state
                self.state.first_display(screen)
            #イベント処理（キーやマウスの処理）
            for event in pygame.event.get():
                self.state.handle(event)
            #更新処理
            self.state.update(self)
            #ステートを表示する
            self.state.display(screen)

            clock.tick(60)

if __name__ == '__main__':
    game = Game(*sys.argv)
    game.run()