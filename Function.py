import pygame
from random import randrange
pygame.init()


def pygameInit(snakesize, startLenSnack):
    arr = []
    for i in range(startLenSnack, 0, -1):
        arr.append({"x": (snakesize * 8) - i * snakesize, "y": 40, "applenotinbody": 1})
    return arr

def paint(screen,  blue,  body,  snakesize, red, obj,  textcolor):
    font = pygame.font.SysFont("comicsans", 23)
    score = font.render(f"score: {len(body)-3}",1, textcolor)
    with open("record.txt", "r", encoding="utf-8") as f:
        record = font.render(f"record:{f.read()}", True, textcolor)
    for item in body:
        pygame.draw.rect(screen, blue,  rect=(item["x"], item["y"], snakesize, snakesize))
    pygame.draw.rect(screen, red,  rect=(obj["Applex"], obj["Appley"], snakesize, snakesize))
    screen.blit(score, (10, 10))
    screen.blit(record, (10, 30))

def move(arr, object):
    for item in range(len(arr) - 1, 0, -1):
        arr[item]["x"] = arr[item - 1]["x"]
        arr[item]["y"] = arr[item - 1]["y"]
    arr[0]["x"] += object["xchanched"]
    arr[0]["y"] += object["ychanched"]
    return arr

def createapple(obj, snakesize, wight, height):
    obj["Applex"] = randrange(0, wight,snakesize)
    obj["Appley"] = randrange(0, height,snakesize)

    return obj

def collision(body, wight, height, obj, start):
    if body[0]["x"] >= wight or body[0]["x"] <= 0 or body[0]["y"] <= 0 or body[0]["y"] >= height:
        obj["InGame"] = False
    if not start:
        for num in range(len(body) - 1, 0, -1):
            if body[0]["x"] == body[num]["x"] and body[0]["y"] == body[num]["y"]:
                obj["InGame"] = False


    return obj
        
def collisiontoapple(body,snakesize, obj, wight, height):

    if body[0]["x"] == obj["Applex"] and body[0]["y"] == obj["Appley"]:
        if obj["xchanched"] == 20 or obj["xchanched"] == -20:
            body.append({"x": body[len(body) - 1]["x"] - snakesize, "y": body[len(body) - 1]["y"]})
        else:
            body.append({"x": body[len(body) - 1]["x"], "y": body[len(body) - 1]["y"] - snakesize})
        
        createapple(obj, snakesize, wight, height)
        return body
    
def SnakeEvent(obj, snakesize):
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if keys[pygame.K_a] and obj["direction"] != "Right":
            obj["xchanched"] = -snakesize
            obj["ychanched"] = 0
            obj["direction"] = "Left"
            return obj
        if keys[pygame.K_d] and obj["direction"] != "Left":
            obj["xchanched"] = snakesize
            obj["ychanched"] = 0
            obj["direction"] = "Right"
            return obj
        if keys[pygame.K_w] and obj["direction"] != "Down":
            obj["xchanched"] = 0
            obj["ychanched"] = -snakesize
            obj["direction"] = "Up"
            return obj
        if keys[pygame.K_s] and obj["direction"] != "Up":
            obj["xchanched"] = 0
            obj["ychanched"] = snakesize
            obj["direction"] = "Down"
            return obj
        if keys[pygame.K_ESCAPE]:
            obj["InGame"] = False
            return obj
        if event.type == pygame.QUIT:
            obj["InGame"] = False
    return obj