import sys
import pygame
import pathlib
import os

import style
import load


class App:
    def __init__(self):

        self.PATH_TO_DATA = pathlib.Path(__file__).parent.parent / "data"

        self.plains = [
            self.PATH_TO_DATA / "image" / "plains" / plain
            for plain in os.listdir(self.PATH_TO_DATA / "image" / "plains")
        ]

        self.level = 1

        self.click_sound = pygame.mixer.Sound(self.PATH_TO_DATA / "music" / "click_music.wav")


    def start_page(self, screen):
        width, height = screen.get_width(), screen.get_height()

        screen.fill(style.BACKGROUND_COLOR_GAME)

        # <==== Кнопка "Играть" ====>
        button_play_x = width // 2
        button_play_y = height // 2
        button_play_width = 300
        button_play_height = 80

        button_play_rect = pygame.Rect(
            button_play_x - button_play_width // 2,
            button_play_y - button_play_height // 2,
            button_play_width,
            button_play_height,
        )

        pygame.draw.rect(
            screen,
            style.BACKGROUND_COLOR_BUTTON,
            button_play_rect,
            0,
            25,
        )
        pygame.draw.rect(
            screen,
            style.BACKGROUND_COLOR_BUTTON_BORDER,
            button_play_rect,
            5,
            25,
        )

        font = pygame.font.SysFont("spendthrift", 60)
        text_for_button_play = font.render("Играть", True, style.TEXT_COLOR_BUTTON)

        text_for_button_play_x = button_play_x - text_for_button_play.get_width() // 2
        text_for_button_play_y = button_play_y - text_for_button_play.get_height() // 2

        screen.blit(text_for_button_play, (text_for_button_play_x, text_for_button_play_y))
        # <==== Кнопка "Играть" ====>

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos_x, pos_y = event.pos
                    if button_play_rect.collidepoint(pos_x, pos_y):
                        self.click_sound.play()
                        Game(screen)
                if event.type == pygame.MOUSEMOTION:
                    pos_x, pos_y = event.pos
                    if button_play_rect.collidepoint(pos_x, pos_y):
                        pygame.draw.rect(
                            screen,
                            style.BACKGROUND_COLOR_BUTTON_HOVER,
                            button_play_rect,
                            0,
                            25,
                        )
                        pygame.draw.rect(
                            screen,
                            style.BACKGROUND_COLOR_BUTTON_BORDER,
                            button_play_rect,
                            5,
                            25,
                        )
                        text_for_button_play = font.render("ТЫК", True, style.TEXT_COLOR_BUTTON_HOVER)
                        text_for_button_play_x = button_play_x - text_for_button_play.get_width() // 2
                        text_for_button_play_y = button_play_y - text_for_button_play.get_height() // 2
                        screen.blit(text_for_button_play, (text_for_button_play_x, text_for_button_play_y))
                    else:
                        pygame.draw.rect(
                            screen,
                            style.BACKGROUND_COLOR_BUTTON,
                            button_play_rect,
                            0,
                            25,
                        )
                        pygame.draw.rect(
                            screen,
                            style.BACKGROUND_COLOR_BUTTON_BORDER,
                            button_play_rect,
                            5,
                            25,
                        )
                        text_for_button_play = font.render("Играть", True, style.TEXT_COLOR_BUTTON)
                        text_for_button_play_x = button_play_x - text_for_button_play.get_width() // 2
                        text_for_button_play_y = button_play_y - text_for_button_play.get_height() // 2
                        screen.blit(text_for_button_play, (text_for_button_play_x, text_for_button_play_y))
            pygame.display.flip()


class Game(App):
    def __init__(self, screen):
        super().__init__()

        self.game_page(screen)

    def game_page(self, screen):
        self.render_decoration(screen)
        self.create_user(screen)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.start_page(screen)
            pygame.display.flip()

    def render_decoration(self, screen):
        width, height = screen.get_width(), screen.get_height()

        screen.fill(style.BACKGROUND_COLOR_GAME)

        # <==== Таблица "Уровень" ====>
        button_play_x = width // 4 // 2
        button_play_y = height // 12 // 2
        button_play_width = 300
        button_play_height = 100

        button_play_rect = pygame.Rect(
            button_play_x - button_play_width // 2,
            button_play_y - button_play_height // 2,
            button_play_width,
            button_play_height,
        )

        pygame.draw.rect(
            screen,
            style.BACKGROUND_COLOR_TABLE,
            button_play_rect,
            0,
            25,
        )
        pygame.draw.rect(
            screen,
            style.BACKGROUND_COLOR_TABLE_BORDER,
            button_play_rect,
            5,
            25,
        )

        font = pygame.font.SysFont("spendthrift", 40)
        text_for_button_play = font.render("Уровень:", True, style.TEXT_COLOR_TABLE)

        text_for_button_play_x = button_play_x - text_for_button_play.get_width() // 2
        text_for_button_play_y = button_play_y - text_for_button_play.get_height() // 1.1

        screen.blit(text_for_button_play, (text_for_button_play_x, text_for_button_play_y))

        font = pygame.font.SysFont("spendthrift", 50)
        text_for_button_play = font.render("1", True, style.TEXT_COLOR_TABLE_VALUE)

        text_for_button_play_x = button_play_x - text_for_button_play.get_width() // 2
        text_for_button_play_y = button_play_y

        screen.blit(text_for_button_play, (text_for_button_play_x, text_for_button_play_y))
        # <==== Таблица "Уровень" ====>

        # <==== Таблица "Счет" ====>
        button_play_x = width - width // 4 // 2
        button_play_y = height // 12 // 2
        button_play_width = 300
        button_play_height = 100

        button_play_rect = pygame.Rect(
            button_play_x - button_play_width // 2,
            button_play_y - button_play_height // 2,
            button_play_width,
            button_play_height,
        )

        pygame.draw.rect(
            screen,
            style.BACKGROUND_COLOR_TABLE,
            button_play_rect,
            0,
            25,
        )
        pygame.draw.rect(
            screen,
            style.BACKGROUND_COLOR_TABLE_BORDER,
            button_play_rect,
            5,
            25,
        )

        font = pygame.font.SysFont("spendthrift", 40)
        text_for_button_play = font.render("Счет:", True, style.TEXT_COLOR_TABLE)

        text_for_button_play_x = button_play_x - text_for_button_play.get_width() // 2
        text_for_button_play_y = button_play_y - text_for_button_play.get_height() // 1.1

        screen.blit(text_for_button_play, (text_for_button_play_x, text_for_button_play_y))

        font = pygame.font.SysFont("spendthrift", 50)
        text_for_button_play = font.render("0", True, style.TEXT_COLOR_TABLE_VALUE)

        text_for_button_play_x = button_play_x - text_for_button_play.get_width() // 2
        text_for_button_play_y = button_play_y

        screen.blit(text_for_button_play, (text_for_button_play_x, text_for_button_play_y))
        # <==== Таблица "Счет" ====>
        pygame.display.flip()

    def create_user(self, screen):
        width, height = screen.get_width(), screen.get_height()

        pygame.display.flip()

        user_image = pygame.transform.scale(
            load.load_image(self.plains[self.level - 1]),
            (150, 150)
        )
        self.user_image_x = width // 2 - user_image.get_width() // 2
        self.user_image_y = height - height // 6
        screen.blit(user_image, (self.user_image_x, self.user_image_y))

    @staticmethod
    def terminate():
        """Выход из приложения"""
        pygame.quit()
        sys.exit()


def main():
    pygame.init()
    screen_size = (1600, 1200)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("SPACE_WAR")

    app = App()
    app.start_page(screen)


if __name__ == "__main__":
    main()
