import pygame
from settings import WIDTH, HEIGHT


class Menu:
    """可以用鍵盤或滑鼠選擇的選單（主選單、暫停選單都能用）"""

    def __init__(self, title, options, fill_background=True):
        self.title = title
        self.fill_background = fill_background   # 暫停選單設 False，才看得到後面的遊戲畫面
        self.options = options        # 例如 ["START", "QUIT"]
        self.selected = 0             # 目前選到第幾個（從 0 開始算）

        self.title_font = pygame.font.SysFont(None, 100)
        self.option_font = pygame.font.SysFont(None, 50)

        self.color_normal = (180, 180, 190)     # 沒選到：灰白色
        self.color_selected = (255, 220, 100)   # 選到：金色

    def option_rect(self, i):
        """第 i 個選項的按鈕範圍（滑鼠判斷和畫按鈕都用它）"""
        w, h = 340, 60
        x = (WIDTH - w) // 2
        y = 330 + i * 80              # 每個按鈕往下排 80 像素
        return pygame.Rect(x, y, w, h)

    def handle_event(self, event):
        """處理輸入。選定某個選項時回傳它的名字，否則回傳 None"""
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
                self.selected = (self.selected - 1) % len(self.options)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                self.selected = (self.selected + 1) % len(self.options)
            elif event.key == pygame.K_RETURN:
                return self.options[self.selected]

        elif event.type == pygame.MOUSEMOTION:
            for i in range(len(self.options)):
                if self.option_rect(i).collidepoint(event.pos):
                    self.selected = i

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i in range(len(self.options)):
                if self.option_rect(i).collidepoint(event.pos):
                    return self.options[i]

        return None

    def draw(self, screen):
        if self.fill_background:
            screen.fill((20, 20, 40))

        # 標題
        title_img = self.title_font.render(self.title, True, (255, 255, 255))
        screen.blit(title_img, title_img.get_rect(center=(WIDTH // 2, 200)))

        # 選項按鈕
        for i, text in enumerate(self.options):
            rect = self.option_rect(i)
            if i == self.selected:
                color = self.color_selected
                pygame.draw.rect(screen, (60, 60, 90), rect, border_radius=12)   # 按鈕底色
                pygame.draw.rect(screen, color, rect, 3, border_radius=12)       # 按鈕外框
            else:
                color = self.color_normal
            img = self.option_font.render(text, True, color)
            screen.blit(img, img.get_rect(center=rect.center))
