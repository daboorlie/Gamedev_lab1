import pygame
import random

def rect_2x3(x, y, surf, color):
    rectangle = pygame.Rect(x, y, 120, 80)
    pygame.draw.rect(surf, color, rectangle, 3)
    pygame.draw.line(surf, color, (x+40, y), (x+40, y+80), 1)
    pygame.draw.line(surf, color, (x+80, y), (x+80, y+80), 1)
    pygame.draw.line(surf, color, (x, y+40), (x+120, y+40), 1)

def btn(x, y, surf, color, text):
    rectangle = pygame.Rect(x, y, 80, 40)
    pygame.draw.rect(surf, color, rectangle, 3)
    f = pygame.font.SysFont('serif', 24)
    text = f.render(text, True, color)
    surf.blit(text, (x+5, y+5))

def pickMatrix(mat_list):
    m = mat_list[random.randint(0,4)]
    return m

def createMatrix(m0):
    for i in range (0,6):
        for j in range (0,6):
            m1[i][j] = m0[i][j]
    for i in range (0,6):
        for j in range (0,6):
            d = random.randint(1,100)
            if d <= 50:
                m1[i][j] = 0
    return m1

def printText(val, x, y, sc, color, size):
    val = str(val)
    f = pygame.font.SysFont('serif', size)
    text = f.render(val, True, color)
    sc.blit(text, (x+10, y))

def printMatrix(m, sc, color):
    for i in range (0,6):
        for j in range (0,6):
            if m[i][j] != 0:
                printText(m[i][j], 60 + 40*j, 60 + 40*i, sc, color, 36)

def countValues(m, val):
    count = 0
    for i in range (0,6):
        for j in range (0,6):
            if m[i][j] == val:
                count += 1
    return count

def matrixMerge(m1, m2):
    m_merged = [[0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]
    for i in range (0,6):
        for j in range (0,6):
            if m1[i][j] != 0:
                m_merged[i][j] = m1[i][j]
            else:
                if m2[i][j] != 0:
                    m_merged[i][j] = m2[i][j]
    return m_merged

m1 = [[6, 2, 5, 1, 4, 3],
    [4, 1, 3, 5, 2, 6],
    [2, 5, 1, 6, 3, 4],
    [3, 4, 6, 2, 5, 1],
    [5, 6, 4, 3, 1, 2],
    [1, 3, 2, 4, 6, 5]]

m2 = [[6, 1, 4, 2, 3, 5],
    [3, 5, 2, 1, 4, 6],
    [2, 4, 6, 5, 1, 3],
    [1, 3, 5, 4, 6, 2],
    [4, 2, 3, 6, 5, 1],
    [5, 6, 1, 3, 2, 4]]

m3 = [[4, 6, 2, 1, 3, 5],
    [5, 3, 1, 6, 4, 2],
    [3, 2, 6, 5, 1, 4],
    [1, 4, 5, 3, 2, 6],
    [2, 5, 3, 4, 6, 1],
    [6, 1, 4, 2, 5, 3]]

m4 = [[1, 5, 2, 3, 4, 6],
    [6, 3, 4, 1, 5, 2],
    [3, 4, 1, 2, 6, 5],
    [2, 6, 5, 4, 1, 3],
    [4, 2, 6, 5, 3, 1],
    [5, 1, 3, 6, 2, 4]]

m5 = [[3, 6, 4, 2, 5, 1],
    [1, 5, 2, 6, 3, 4],
    [6, 4, 5, 3, 1, 2],
    [2, 1, 3, 4, 6, 5],
    [4, 3, 1, 5, 2, 6],
    [5, 2, 6, 1, 4, 3]]


matrixes = [m1, m2, m3, m4, m5]

width = 360
height = 480
fps = 30

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (160, 160, 160)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()

click_sound = pygame.mixer.Sound("click.wav")
correct_sound = pygame.mixer.Sound("correct.wav")
incorrect_sound = pygame.mixer.Sound("incorrect.wav")
win_sound = pygame.mixer.Sound("win.wav")
lose_sound = pygame.mixer.Sound("lose.wav")

screen.fill(white)
rect_2x3(60, 60, screen, black)
rect_2x3(60, 140, screen, black)
rect_2x3(60, 220, screen, black)
rect_2x3(180, 60, screen, black)
rect_2x3(180, 140, screen, black)
rect_2x3(180, 220, screen, black)
btn(20, 400, screen, black, 'Create')
printText(1, 60, 310, screen, gray, 36)
printText(2, 100, 310, screen, gray, 36)
printText(3, 140, 310, screen, gray, 36)
printText(4, 180, 310, screen, gray, 36)
printText(5, 220, 310, screen, gray, 36)
printText(6, 260, 310, screen, gray, 36)
game_started = False

running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] > 20 and mouse_pos[0] < 100 and mouse_pos[1] > 400 and mouse_pos[1] < 440:
                pygame.mixer.Sound.play(click_sound)
                screen.fill(white)
                rect_2x3(60, 60, screen, black)
                rect_2x3(60, 140, screen, black)
                rect_2x3(60, 220, screen, black)
                rect_2x3(180, 60, screen, black)
                rect_2x3(180, 140, screen, black)
                rect_2x3(180, 220, screen, black)
                btn(20, 400, screen, black, 'Create')
                printText(1, 60, 310, screen, gray, 36)
                printText(2, 100, 310, screen, gray, 36)
                printText(3, 140, 310, screen, gray, 36)
                printText(4, 180, 310, screen, gray, 36)
                printText(5, 220, 310, screen, gray, 36)
                printText(6, 260, 310, screen, gray, 36)

                m = pickMatrix(matrixes)
                m_disp = createMatrix(m)
                m_correct = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
                m_incorrect = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
                printMatrix(m_disp, screen, black)
                value = 0
                lives = 3
                txt = "Lives: " + str(lives)
                printText(txt, 260, 400, screen, black, 18)
                game_started = True

            if mouse_pos[0] > 60 and mouse_pos[0] < 100 and mouse_pos[1] > 310 and mouse_pos[1] < 350:
                pygame.mixer.Sound.play(click_sound)
                printText(1, 60, 310, screen, black, 36)
                printText(2, 100, 310, screen, gray, 36)
                printText(3, 140, 310, screen, gray, 36)
                printText(4, 180, 310, screen, gray, 36)
                printText(5, 220, 310, screen, gray, 36)
                printText(6, 260, 310, screen, gray, 36)
                value = 1
            if mouse_pos[0] > 100 and mouse_pos[0] < 140 and mouse_pos[1] > 310 and mouse_pos[1] < 350:
                pygame.mixer.Sound.play(click_sound)
                printText(1, 60, 310, screen, gray, 36)
                printText(2, 100, 310, screen, black, 36)
                printText(3, 140, 310, screen, gray, 36)
                printText(4, 180, 310, screen, gray, 36)
                printText(5, 220, 310, screen, gray, 36)
                printText(6, 260, 310, screen, gray, 36)
                value = 2
            if mouse_pos[0] > 140 and mouse_pos[0] < 180 and mouse_pos[1] > 310 and mouse_pos[1] < 350:
                pygame.mixer.Sound.play(click_sound)
                printText(1, 60, 310, screen, gray, 36)
                printText(2, 100, 310, screen, gray, 36)
                printText(3, 140, 310, screen, black, 36)
                printText(4, 180, 310, screen, gray, 36)
                printText(5, 220, 310, screen, gray, 36)
                printText(6, 260, 310, screen, gray, 36)
                value = 3
            if mouse_pos[0] > 180 and mouse_pos[0] < 220 and mouse_pos[1] > 310 and mouse_pos[1] < 350:
                pygame.mixer.Sound.play(click_sound)
                printText(1, 60, 310, screen, gray, 36)
                printText(2, 100, 310, screen, gray, 36)
                printText(3, 140, 310, screen, gray, 36)
                printText(4, 180, 310, screen, black, 36)
                printText(5, 220, 310, screen, gray, 36)
                printText(6, 260, 310, screen, gray, 36)
                value = 4
            if mouse_pos[0] > 220 and mouse_pos[0] < 260 and mouse_pos[1] > 310 and mouse_pos[1] < 350:
                pygame.mixer.Sound.play(click_sound)
                printText(1, 60, 310, screen, gray, 36)
                printText(2, 100, 310, screen, gray, 36)
                printText(3, 140, 310, screen, gray, 36)
                printText(4, 180, 310, screen, gray, 36)
                printText(5, 220, 310, screen, black, 36)
                printText(6, 260, 310, screen, gray, 36)
                value = 5
            if mouse_pos[0] > 260 and mouse_pos[0] < 300 and mouse_pos[1] > 310 and mouse_pos[1] < 350:
                pygame.mixer.Sound.play(click_sound)
                printText(1, 60, 310, screen, gray, 36)
                printText(2, 100, 310, screen, gray, 36)
                printText(3, 140, 310, screen, gray, 36)
                printText(4, 180, 310, screen, gray, 36)
                printText(5, 220, 310, screen, gray, 36)
                printText(6, 260, 310, screen, black, 36)
                value = 6

            if mouse_pos[0] > 60 and mouse_pos[0] < 300 and mouse_pos[1] > 60 and mouse_pos[1] < 300 and value != 0 and game_started:
                screen.fill(white)
                rect_2x3(60, 60, screen, black)
                rect_2x3(60, 140, screen, black)
                rect_2x3(60, 220, screen, black)
                rect_2x3(180, 60, screen, black)
                rect_2x3(180, 140, screen, black)
                rect_2x3(180, 220, screen, black)
                btn(20, 400, screen, black, 'Create')
                if value == 1:
                    printText(1, 60, 310, screen, black, 36)
                    printText(2, 100, 310, screen, gray, 36)
                    printText(3, 140, 310, screen, gray, 36)
                    printText(4, 180, 310, screen, gray, 36)
                    printText(5, 220, 310, screen, gray, 36)
                    printText(6, 260, 310, screen, gray, 36)
                if value == 2:
                    printText(1, 60, 310, screen, gray, 36)
                    printText(2, 100, 310, screen, black, 36)
                    printText(3, 140, 310, screen, gray, 36)
                    printText(4, 180, 310, screen, gray, 36)
                    printText(5, 220, 310, screen, gray, 36)
                    printText(6, 260, 310, screen, gray, 36)
                if value == 3:
                    printText(1, 60, 310, screen, gray, 36)
                    printText(2, 100, 310, screen, gray, 36)
                    printText(3, 140, 310, screen, black, 36)
                    printText(4, 180, 310, screen, gray, 36)
                    printText(5, 220, 310, screen, gray, 36)
                    printText(6, 260, 310, screen, gray, 36)
                if value == 4:
                    printText(1, 60, 310, screen, gray, 36)
                    printText(2, 100, 310, screen, gray, 36)
                    printText(3, 140, 310, screen, gray, 36)
                    printText(4, 180, 310, screen, black, 36)
                    printText(5, 220, 310, screen, gray, 36)
                    printText(6, 260, 310, screen, gray, 36)
                if value == 5:
                    printText(1, 60, 310, screen, gray, 36)
                    printText(2, 100, 310, screen, gray, 36)
                    printText(3, 140, 310, screen, gray, 36)
                    printText(4, 180, 310, screen, gray, 36)
                    printText(5, 220, 310, screen, black, 36)
                    printText(6, 260, 310, screen, gray, 36)
                if value == 6:
                    printText(1, 60, 310, screen, gray, 36)
                    printText(2, 100, 310, screen, gray, 36)
                    printText(3, 140, 310, screen, gray, 36)
                    printText(4, 180, 310, screen, gray, 36)
                    printText(5, 220, 310, screen, gray, 36)
                    printText(6, 260, 310, screen, black, 36)
                
                printMatrix(m_disp, screen, black)

                mat_i = (mouse_pos[1] - 60) // 40
                mat_j = (mouse_pos[0] - 60) // 40
                if m_disp[mat_i][mat_j] == 0:
                    m_correct[mat_i][mat_j] = 0
                    m_incorrect[mat_i][mat_j] = 0
                    if value == m[mat_i][mat_j]:
                        pygame.mixer.Sound.play(correct_sound)
                        m_correct[mat_i][mat_j] = value
                    else:
                        pygame.mixer.Sound.play(incorrect_sound)
                        m_incorrect[mat_i][mat_j] = value
                        lives -= 1
                printMatrix(m_correct, screen, blue)
                printMatrix(m_incorrect, screen, red)

                txt = "Lives: " + str(lives)
                printText(txt, 260, 400, screen, black, 18)

                if lives == 0:
                    pygame.mixer.Sound.play(lose_sound)
                    screen.fill(white)
                    rect_2x3(60, 60, screen, black)
                    rect_2x3(60, 140, screen, black)
                    rect_2x3(60, 220, screen, black)
                    rect_2x3(180, 60, screen, black)
                    rect_2x3(180, 140, screen, black)
                    rect_2x3(180, 220, screen, black)
                    btn(20, 400, screen, black, 'Create')
                    printText(1, 60, 310, screen, gray, 36)
                    printText(2, 100, 310, screen, gray, 36)
                    printText(3, 140, 310, screen, gray, 36)
                    printText(4, 180, 310, screen, gray, 36)
                    printText(5, 220, 310, screen, gray, 36)
                    printText(6, 260, 310, screen, gray, 36)

                    m = pickMatrix(matrixes)
                    m_disp = createMatrix(m)
                    m_correct = [[0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0]]
                    m_incorrect = [[0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0]]
                    printMatrix(m_disp, screen, black)
                    value = 0
                    lives = 3
                    txt = "Lives: " + str(lives)
                    printText(txt, 260, 400, screen, black, 18)
                    game_started = True
                    printText("You lose!", 150, 440, screen, red, 22)

                if countValues(matrixMerge(m_disp,m_correct),0) == 0:
                    pygame.mixer.Sound.play(win_sound)
                    screen.fill(white)
                    rect_2x3(60, 60, screen, black)
                    rect_2x3(60, 140, screen, black)
                    rect_2x3(60, 220, screen, black)
                    rect_2x3(180, 60, screen, black)
                    rect_2x3(180, 140, screen, black)
                    rect_2x3(180, 220, screen, black)
                    btn(20, 400, screen, black, 'Create')
                    printText(1, 60, 310, screen, gray, 36)
                    printText(2, 100, 310, screen, gray, 36)
                    printText(3, 140, 310, screen, gray, 36)
                    printText(4, 180, 310, screen, gray, 36)
                    printText(5, 220, 310, screen, gray, 36)
                    printText(6, 260, 310, screen, gray, 36)

                    m = pickMatrix(matrixes)
                    m_disp = createMatrix(m)
                    m_correct = [[0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0]]
                    m_incorrect = [[0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0]]
                    printMatrix(m_disp, screen, black)
                    value = 0
                    lives = 3
                    txt = "Lives: " + str(lives)
                    printText(txt, 260, 400, screen, black, 18)
                    game_started = True
                    printText("You win!", 150, 440, screen, blue, 22)

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()