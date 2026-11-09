from pico2d import (
    SDL_KEYDOWN, SDL_QUIT, SDLK_0, clear_canvas,
    get_canvas_height, get_canvas_width, get_events, load_image, update_canvas,
)

import game_framework
import game_world
import play_mode


image = None
BALL_SIZES = {SDLK_0: 0}


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    image = None


def update():
    play_mode.update()


def render():
    clear_canvas()
    game_world.render()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()


def handle_events(events=None):
    if events is None:
        events = get_events()

    for index, event in enumerate(events):
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key in BALL_SIZES:
            play_mode.boy.ball_size = BALL_SIZES[event.key]
            game_framework.pop_mode(resume_previous=False)
            play_mode.handle_events(events[index + 1:])
            return
        play_mode.boy.handle_event(event)
