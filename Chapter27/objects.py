import pygame, config, os
from random import randrange

#squishゲームに登場するオブジェクト

class SquishSprite(pygame.sprite.Sprite):
    """
    Squishの全スプライトのスーパークラス
    """
    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -config.margin * 2
        self.area = screen.get_rect().inflate(shrink, shrink)

class Weight(SquishSprite):
    """
    重り。毎フレーム、speedの値だけ落下する。
    """
    def __init__(self, speed):
        super().__init__(config.weight_image)
        self.speed = speed
        self.reset()

    def reset(self):
        """
        画面最上部のランダムな位置に重りを移動する
        """
        x = randrange(self.area.left, self.area.right)
        self.rect.midbottom = x, 0

    def update(self):
        """
        次のフレームでの表示用に重りを更新する
        画面下端に達したかどうかを判定するlanded属性を更新する。
        """
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.area.bottom

class Banana(SquishSprite):
    """
    プレイヤーが移動させるバナナ。
    位置は常に画面最下部付近で、水平方向はマウスの現在位置で決まる
    """
    def __init__(self):
        super().__init__(config.banana_image)
        self.rect.bottom = self.area.bottom
        #以下は画像内のバナナでない領域を示す。
        #重りがこの領域に入っても当たったことにならない
        self.pad_top = config.banana_pad_top
        self.pad_side = config.banana_pad_side

    def update(self):
        """
        次のフレームでの表示用にバナナを更新する
        バナナの中心のx座標をマウスの現在のx座標に設定して、
        clampメソッドで移動の許容範囲内に留まるように修正する
        """
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect = self.rect.clamp(self.area)

    def touches(self, other):
        """
        バナナが重りとぶつかったかどうか判定する
        """
        #バナナ画像の当たり判定を縮小
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        #当たり判定の下部をバナナの下端に位置するように移動
        bounds.bottom = self.rect.bottom
        #バナナとotherがぶつかっているかどうか判定
        return bounds.colliderect(other.rect)
