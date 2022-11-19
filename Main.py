from Function import *

clock = pygame.time.Clock()
snakesize = 20
height = 20 * snakesize
wight = 20 * snakesize
blue = "#60878E"
green = "#16A546"
red = "#C04747"
textcolor = "#B71F1F"
fakestart = True
global object
object = {"xchanched": snakesize, "ychanched": 0, "InGame": True, "direction": "Right"}
screen = pygame.display.set_mode((wight, height))
pygame.display.set_icon(pygame.image.load('snake.png'))
startLenSnack = 3
global body
body = []
fps = 10

pygame.display.set_caption("Snake Game")
body = pygameInit(snakesize, startLenSnack)
object["Applex"] = body[0]["x"]
object["Appley"] = body[0]["y"]
applenotinbody = True



while object["InGame"]:
    """Checking apple not in snake"""
    while True:
        for item in body:
            if item["x"] == object["Applex"] and item["y"] == object["Appley"]:
                object = createapple(object, snakesize, wight, height)
            else:
                break
        for item in body:
            if applenotinbody:
                applenotinbody = True
                break
        if applenotinbody:
            break

    # ClearWindow
    screen.fill(blue)
    object = SnakeEvent(object, snakesize)
    body = move(body, object)
    collisiontoapple(body,snakesize, object, wight, height)
    try:
        with open("record.txt", "r", encoding="utf-8") as f:
            record = int(f.read())
            if record < len(body) - 3:
                with open("record.txt", "w", encoding="utf-8") as file:
                    file.write(f"{len(body) - 3}")
    except ValueError:
        font = pygame.font.SysFont("comicsans", 36)
        error = font.render("Error in file record!!!", True, textcolor)
        screen.blit(error,(45, height/2))
        clock.tick(10000)
        object["InGame"] = False
    object = collision(body, wight, height, object, fakestart)
    paint(screen,  green,  body,  snakesize, red, object, textcolor)
    pygame.display.update()
    clock.tick(fps)
    fakestart = False