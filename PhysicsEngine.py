import pygame,sys,pymunk

def create_apple(space):
    body = pymunk.Body(2000,100,body_type=pymunk.Body.DYNAMIC)
    body.postion = (640,1000)
    shape = pymunk.Circle(body, 50)
    space.add(body,shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen,(0,0,200),(pos_x,pos_y),80)

#staging
pygame.init()
screen = pygame.display.set_mode((1280,720))
time = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,9.8)
apples = []
apples.append(create_apple(space))

while True: #Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((217,217,217))
    draw_apples(apples)
    space.step(1/50) #Time Step Update Loop
    pygame.display.update()
    time.tick(120)