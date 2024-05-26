import pygame
import random
import math

# 初始化pygame
pygame.init()

# 屏幕尺寸
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids Model")

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 定义Boid类
class Boid:
    def __init__(self):
        self.size = 4
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.angle = random.uniform(0, math.pi * 2)
        self.speed = 3
        self.point_list = [(self.x+self.size*2*math.cos(self.angle), self.y+self.size*2*math.sin(self.angle)), (self.x+self.size*0.5*math.sin(self.angle), self.y-self.size*0.5*math.cos(self.angle)), (self.x-self.size*0.5*math.sin(self.angle), self.y+self.size*0.5*math.cos(self.angle)) ]

    # 更新位置
    def update(self, flock):
        self.rule3(flock)
        self.rule1(flock)
        self.rule2(flock)
        self.move()
        

    # 群聚行为
    def rule1(self, flock):
        alpha = 0.9
        gathering = 40
        move_x, move_y = 0, 0
        l = 0
        for boid in flock:
            if boid != self:
                dist = math.sqrt((self.x - boid.x)**2 + (self.y - boid.y)**2)
                if dist < gathering:
                    l+=1
                    move_x += (gathering-dist)*(boid.x - self.x)/gathering
                    move_y += (gathering-dist)*(boid.y - self.y)/gathering
        if l!=0:
            self.angle = alpha * self.angle + (1-alpha)*math.atan2(move_y, move_x)

    # 分离行为
    def rule2(self, flock):
        alpha = 0.8
        separation= 10
        move_x, move_y = 0, 0
        l = 0
        for boid in flock:
            if boid != self:
                dist = math.sqrt((self.x - boid.x)**2 + (self.y - boid.y)**2)
                if dist < separation:
                    l += 1
                    move_x += (separation-dist)*(boid.x - self.x)/separation
                    move_y += (separation-dist)*(boid.y - self.y)/separation
        if l != 0:
            self.angle = (alpha * self.angle - (1-alpha)*(math.atan2(move_y, move_x)+0.5*math.pi))

    # 一致行为
    def rule3(self, flock):
        alpha = 0.9
        average= 40
        move_angle = 0
        l = 0
        for boid in flock:
            if boid != self:
                dist = math.sqrt((self.x - boid.x)**2 + (self.y - boid.y)**2)
                if dist < average:
                    move_angle += boid.angle
                    l += 1
        if l == 0:
            pass
        else:
            move_angle /=l
            self.angle = alpha * self.angle + (1-alpha)*move_angle

    # 移动
    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        # 确保Boid在屏幕内
        self.x %= WIDTH
        self.y %= HEIGHT
        self.point_list = [(self.x+self.size*2*math.cos(self.angle), self.y+self.size*2*math.sin(self.angle)), (self.x+self.size*0.5*math.sin(self.angle), self.y-self.size*0.5*math.cos(self.angle)), (self.x-self.size*0.5*math.sin(self.angle), self.y+self.size*0.5*math.cos(self.angle)) ]
        

# 创建Boids群体
num_boids = 50
boids = [Boid() for _ in range(num_boids)]

# 主循环
running = True
while running:
    screen.fill(BLACK)
    
    # 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新和绘制Boids
    for boid in boids:
        boid.update(boids)
        pygame.draw.polygon(screen, RED, boid.point_list)

    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(20)

pygame.quit()


