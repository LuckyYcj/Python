#!/usr/bin/env python
# coding=gbk
# -*- coding : utf-8 -*-
import random
import pygame

PANEL_width = 1600
PANEL_highly = 800
FONT_PX = 15

pygame.init()

# ����һ�����Ǵ���

winSur = pygame.display.set_mode((PANEL_width, PANEL_highly))

font = pygame.font.SysFont("123.ttf", 25)

bg_suface = pygame.Surface((PANEL_width, PANEL_highly), flags=pygame.SRCALPHA)

pygame.Surface.convert(bg_suface)

bg_suface.fill(pygame.Color(0, 0, 0, 28))

winSur.fill((0, 0, 0))

# ���ְ�

# texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]


# ��ĸ��

letter = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c',

          'v', 'b', 'n', 'm']

texts = [

    font.render(str(letter[i]), True, (0, 255, 0)) for i in range(26)

]

# ����Ļ�Ŀ����������ڻ����Ϸż������겢����һ���б�

column = int(PANEL_width / FONT_PX)

drops = [0 for i in range(column)]

while True:

    # �Ӷ����л�ȡ�¼�

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            exit()

        elif event.type == pygame.KEYDOWN:

            chang = pygame.key.get_pressed()

            if (chang[32]):
                exit()

    # ����ͣһ�θ����ĺ�����

    pygame.time.delay(30)

    # ���±༭ͼ��ڶ������������Ͻ�����

    winSur.blit(bg_suface, (0, 0))

    for i in range(len(drops)):

        text = random.choice(texts)

        # ���±༭ÿ��������ͼ��

        winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))

        drops[i] += 1

        if drops[i] * 10 > PANEL_highly or random.random() > 0.95:
            drops[i] = 0

    pygame.display.flip()
