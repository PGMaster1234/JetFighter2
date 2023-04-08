import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# screen = pygame.display.set_mode((1200, 650))
clock = pygame.time.Clock()
fps = 60

screen_width = screen.get_width()
screen_height = screen.get_height()

font15 = pygame.font.Font("freesansbold.ttf", 15)
font20 = pygame.font.Font("freesansbold.ttf", 20)
font50 = pygame.font.Font("freesansbold.ttf", 50)
font100 = pygame.font.Font("freesansbold.ttf", 100)

transition_image = pygame.image.load('transition_image.png')


class First:
    def __init__(self):
        pass
    movement_speed_ppf = 0  # ppf is pixels per second - Higher means move faster
    turn_radius_int = 0  # This is how much will be added each frame so it will be ~ 0.01 or 0.05 - Higher = Faster Turn
    reload_speed_seconds = 0  # Base amount that random int is added to to create slight variability in reload time
    dmg = 0  # How much dmg each bullet does
    hp_int = 0  # Base amount of hp - Higher is more hp
    bullet_speed_int = 0  # Base speed of bullet - Higher means faster
    bullet_spray_radians = 0  # This is the max spray offset that can occur - Higher means more spread
    bullet_type = 'standard'
    image = 0
    x = 0
    y = 0
    angle = 0
    rotated_image = 0
    shooting = False
    bullets = []
    hitbox = 0
    max_hp = 0
    hp_change = 0


class Second:
    def __init__(self):
        pass

    movement_speed_ppf = 0  # ppf is pixels per second - Higher means move faster
    turn_radius_int = 0  # This is how much will be added each frame so it will be ~ 0.01 or 0.05 - Higher = Faster Turn
    reload_speed_seconds = 0  # Base amount that random int is added to to create slight variability in reload time
    dmg = 0  # How much dmg each bullet does
    hp_int = 0  # Base amount of hp - Higher is more hp
    bullet_speed_int = 0  # Base speed of bullet - Higher means faster
    bullet_spray_radians = 0  # This is the max spray offset that can occur - Higher means more spread
    bullet_type = 'standard'
    image = 0
    x = 0
    y = 0
    angle = 0
    rotated_image = 0
    shooting = False
    bullets = []
    hitbox = 0


class ColorSet:
    def __init__(self):
        pass

    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (150, 150, 150)
    dark_blue = (32, 78, 128)
    grey_dark_blue = (61, 93, 128)
    greyer_dark_blue = (80, 100, 128)
    blue = (98, 149, 204)
    light_blue = (123, 186, 255)
    extra_light_blue = (191, 222, 255)
    red = (133, 78, 75)
    dark_red = (132, 63, 76)
    extra_dark_red = (131, 38, 67)


red_basic_image = pygame.image.load('jet_type1.png').convert(screen)
blue_basic_image = pygame.image.load('jet_type2.png').convert(screen)
red_sniper_image = pygame.image.load('jet_type9.png').convert(screen)
blue_sniper_image = pygame.image.load('jet_type10.png').convert(screen)
red_gunner_image = pygame.image.load('jet_type5.png').convert(screen)
blue_gunner_image = pygame.image.load('jet_type6.png').convert(screen)
red_cannon_image = pygame.image.load('jet_type3.png').convert(screen)
blue_cannon_image = pygame.image.load('jet_type4.png').convert(screen)
red_zippy_image = pygame.image.load('jet_type7.png').convert(screen)
blue_zippy_image = pygame.image.load('jet_type8.png').convert(screen)

# og was 96x122 and then was changed to 48x61
# also added 5 to each of them bc they were looking smol - exception for cannon cause it already pretty thicc
# ANOTHER exception bc zippy is still too smol so im making it 10 more bigger
# making em smaller now cause i realized they look too big so -40
basicX = 37  # 3/2 * 48
basicY = 56  # 3/2 * 61
sniperX = 37  # 3/2 * 48
sniperY = 56  # 3/2 * 61
gunnerX = 41  # 7/4 * 48
gunnerY = 72  # 7/4 * 48
cannonX = 56  # 2 * 48
cannonY = 82  # 2 * 61
zippyX = 47  # 3/2 * 48
zippyY = 66  # 3/2 * 61

scaled_red_basic_image = pygame.transform.scale(pygame.image.load('jet_type1.png').convert(screen), (basicX, basicY))
scaled_blue_basic_image = pygame.transform.scale(pygame.image.load('jet_type2.png').convert(screen), (basicX, basicY))
scaled_red_sniper_image = pygame.transform.scale(pygame.image.load('jet_type9.png').convert(screen), (sniperX, sniperY))
scaled_blue_sniper_image = pygame.transform.scale(pygame.image.load('jet_type10.png').convert(screen),
                                                  (sniperX, sniperY))
scaled_red_gunner_image = pygame.transform.scale(pygame.image.load('jet_type5.png').convert(screen), (gunnerX, gunnerY))
scaled_blue_gunner_image = pygame.transform.scale(pygame.image.load('jet_type6.png').convert(screen),
                                                  (gunnerX, gunnerY))
scaled_red_cannon_image = pygame.transform.scale(pygame.image.load('jet_type3.png').convert(screen), (cannonX, cannonY))
scaled_blue_cannon_image = pygame.transform.scale(pygame.image.load('jet_type4.png').convert(screen),
                                                  (cannonX, cannonY))
scaled_red_zippy_image = pygame.transform.scale(pygame.image.load('jet_type7.png').convert(screen), (zippyX, zippyY))
scaled_blue_zippy_image = pygame.transform.scale(pygame.image.load('jet_type8.png').convert(screen), (zippyX, zippyY))

default_jet_image_width = red_basic_image.get_width()
default_jet_image_height = red_basic_image.get_height()


class JetTypes:
    def __init__(self):
        pass

    class Basic:
        def __init__(self):
            pass
        red_img = red_basic_image
        blue_img = blue_basic_image
        turn_radius = 0.05  # 0.02 for zippy - 0.05 for basic - 0.20 for cannon (multiply by 500 for ui)
        movement_speed = 3  # 2 for cannon - 3 for basic - 5 for zippy (multiply by 20 for ui)
        reload_speed = 100  # 20 for gunner - 50 for basic - 100 for cannon (reciprocal * 2000 for ui)
        dmg = 40  # 10 for basic, 5 for gunner and zippy, 20 for cannon and sniper
        toughness = 200  # 300 for cannon - 200 for gunner/basic - 100 for zippy (divide by 3 for ui)
        bullet_speed = 10  # 10 for sniper - 5 for basic/zippy - 3 for gunner (multiply by 10 for ui)
        bullet_type = 'standard'  # mini, standard, or hefty
        bullet_spread = 0.05
        hitbox = pygame.Rect(0, 0, basicX, basicY)

    class Gunner:
        def __init__(self):
            pass

        red_img = red_gunner_image
        blue_img = blue_gunner_image
        turn_radius = 0.05  # 0.02 for zippy - 0.05 for basic - 0.20 for cannon (multiply by 500 for ui)
        movement_speed = 3  # 2 for cannon - 3 for basic - 5 for zippy (multiply by 20 for ui)
        reload_speed = 400  # 20 for gunner - 50 for basic - 100 for cannon (reciprocal * 2000 for ui)
        dmg = 20  # 10 for basic, 5 for gunner and zippy, 20 for cannon and sniper
        toughness = 100  # 300 for cannon - 200 for gunner/basic - 100 for zippy (divide by 3 for ui)
        bullet_speed = 6  # 10 for sniper - 5 for basic/zippy - 3 for gunner (multiply by 10 for ui)
        bullet_type = 'mini'  # mini, standard, or hefty
        bullet_spread = 0.2
        hitbox = pygame.Rect(0, 0, gunnerX, gunnerY)

    class Cannon:
        def __init__(self):
            pass

        red_img = red_cannon_image
        blue_img = blue_cannon_image
        turn_radius = 0.04  # 0.02 for zippy - 0.05 for basic - 0.20 for cannon (multiply by 500 for ui)
        movement_speed = 3  # 2 for cannon - 3 for basic - 5 for zippy (multiply by 20 for ui)
        reload_speed = 25  # 20 for gunner - 50 for basic - 100 for cannon (reciprocal * 2000 for ui)
        dmg = 60  # 10 for basic, 5 for gunner and zippy, 20 for cannon and sniper
        toughness = 400  # 300 for cannon - 200 for gunner/basic - 100 for zippy (divide by 3 for ui)
        bullet_speed = 6  # 10 for sniper - 5 for basic/zippy - 3 for gunner (multiply by 10 for ui)
        bullet_type = 'hefty'  # mini, standard, or hefty
        bullet_spread = 0.05
        hitbox = pygame.Rect(0, 0, cannonX, cannonY)

    class Zippy:
        def __init__(self):
            pass

        red_img = red_zippy_image
        blue_img = blue_zippy_image
        turn_radius = 0.1     # 0.02 for zippy - 0.05 for basic - 0.20 for cannon (multiply by 500 for ui)
        movement_speed = 3  # 2 for cannon - 3 for basic - 5 for zippy (multiply by 20 for ui)
        reload_speed = 150  # 20 for gunner - 50 for basic - 100 for cannon (reciprocal * 2000 for ui)
        dmg = 20  # 10 for basic, 5 for gunner and zippy, 20 for cannon and sniper
        toughness = 200  # 300 for cannon - 200 for gunner/basic - 100 for zippy (divide by 3 for ui)
        bullet_speed = 10  # 10 for sniper - 5 for basic/zippy - 3 for gunner (multiply by 10 for ui)
        bullet_type = 'mini'  # mini, standard, or hefty
        bullet_spread = 0.05
        hitbox = pygame.Rect(0, 0, zippyX / 2, zippyY / 2)

    class Sniper:
        def __init__(self):
            pass

        red_img = red_sniper_image
        blue_img = blue_sniper_image
        turn_radius = 0.05  # 0.02 for zippy - 0.05 for basic - 0.20 for cannon (multiply by 500 for ui)
        movement_speed = 3  # 2 for cannon - 3 for basic - 5 for zippy (multiply by 20 for ui)
        reload_speed = 75  # 20 for gunner - 50 for basic - 100 for cannon (reciprocal * 2000 for ui)
        dmg = 60  # 10 for basic, 5 for gunner and zippy, 20 for cannon and sniper
        toughness = 200  # 300 for cannon - 200 for gunner/basic - 100 for zippy (divide by 3 for ui)
        bullet_speed = 20  # 10 for sniper - 5 for basic/zippy - 3 for gunner (multiply by 10 for ui)
        bullet_type = 'standard'  # mini, standard, or hefty
        bullet_spread = 0.025
        hitbox = pygame.Rect(0, 0, sniperX, sniperY)


select_basic_rect = pygame.Rect((screen_width/6) - default_jet_image_width/2 - 20, screen_height/4 - 20,
                                default_jet_image_width + 40, default_jet_image_height + 40)
# The -20s are offsets to align the outline with the jet image and center it
# They are 20 because the outline is 40 bigger in length and width than the jet image, so a space of 20
# is needed on both sides to center the outline
select_sniper_rect = pygame.Rect((2 * screen_width/6) - default_jet_image_width/2 - 20, screen_height/4 - 20,
                                 default_jet_image_width + 40, default_jet_image_height + 40)
select_zippy_rect = pygame.Rect((3 * screen_width/6) - default_jet_image_width/2 - 20, screen_height/4 - 20,
                                default_jet_image_width + 40, default_jet_image_height + 40)
select_cannon_rect = pygame.Rect((4 * screen_width/6) - default_jet_image_width/2 - 20, screen_height/4 - 20,
                                 default_jet_image_width + 40, default_jet_image_height + 40)
select_gunner_rect = pygame.Rect((5 * screen_width/6) - default_jet_image_width/2 - 20, screen_height/4 - 20,
                                 default_jet_image_width + 40, default_jet_image_height + 40)


select_movement_speed = 3
select_turn_radius = 0.05
select_reload_speed = 100
select_dmg = 10
select_toughness = 200
select_bullet_speed = 24
select_bullet_type = 'standard'
select_bullet_spread = 0.05
select_jet_image = blue_basic_image
select_hitbox = pygame.Rect(0, 0, 0, 0)

select_display_bullet_timer = 500
bullet_width = 5
select_display_bullets = []

mini_bullet_radius = 4
standard_bullet_radius = 9
hefty_bullet_radius = 14

select_stat_bar_movement_speed_change = 0

select_basic = False
select_sniper = False
select_zippy = False
select_cannon = False
select_gunner = False

stat_bar_width = 20
stat_bar_length = 400
space_between_stat_bars = 50

select_jet_outline_width = 2
select_jet_outline_curve = 50

select_jet_rect = pygame.Rect(screen_width/2 - 100, 3 * screen_height/4 + 100, 200, 61.5)

first_picking_jet = True
transition = False
transition_x = 0
transition_speed = 60
transition_speed_change = -0.5
reset_transition_speed = transition_speed
reset_transition_speed_change = transition_speed_change

transition_timer_ready = False
background_is_red = False
color = ColorSet.dark_blue
color2 = ColorSet.blue


you_must_pick_a_jet = False

x = 0
picking_jet = True
running_game = False
while picking_jet:

    color = ColorSet.dark_blue
    if background_is_red:
        color = ColorSet.dark_red
    color2 = ColorSet.blue
    if background_is_red:
        color2 = ColorSet.extra_dark_red
    click = False

    x += 1
    y = 5 * math.sin(0.08 * x)

    screen.fill(ColorSet.grey_dark_blue)
    if transition_timer_ready:
        background_is_red = True
    if background_is_red:
        screen.fill(ColorSet.red)
    if first_picking_jet:
        background_is_red = False

    mx, my = pygame.mouse.get_pos()

    pygame.draw.line(screen, ColorSet.white, (screen_width / 2, 0), (screen_width / 2, screen_height))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            picking_jet = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                picking_jet = False
    # --------------------------------------------- Blit images of jet types
    if background_is_red:
        screen.blit(red_basic_image, ((screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
        screen.blit(red_sniper_image, ((2 * screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
        screen.blit(red_zippy_image, ((3 * screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
        screen.blit(red_cannon_image, ((4 * screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
        screen.blit(red_gunner_image, ((5 * screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
    else:
        screen.blit(blue_basic_image, ((screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
        screen.blit(blue_sniper_image, ((2 * screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
        screen.blit(blue_zippy_image, ((3 * screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
        screen.blit(blue_cannon_image, ((4 * screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
        screen.blit(blue_gunner_image, ((5 * screen_width / 6) - default_jet_image_width / 2, screen_height / 4))
    # --------------------------------------------- Blit names of jet types
    # screen.blit(font20.render('Basic', True, ColorSet.white), ((screen_width/6) - default_jet_image_width/2,
    #                                                           screen_height/4 + 10))
    # --------------------------------------------- Moving rectangle around image of jet when mouse is touching jet rect
    if select_basic_rect.collidepoint((mx, my)) or select_basic:
        pygame.draw.rect(screen, color,
                         pygame.Rect(select_basic_rect.x - y,
                                     select_basic_rect.y - y, select_basic_rect.width + (2 * y),
                                     select_basic_rect.height + (2 * y)),
                         select_jet_outline_width, select_jet_outline_curve)
        if click:
            select_basic = True
            select_sniper = False
            select_zippy = False
            select_cannon = False
            select_gunner = False

    if select_sniper_rect.collidepoint((mx, my)) or select_sniper:
        pygame.draw.rect(screen, color,
                         pygame.Rect(select_sniper_rect.x - y,
                                     select_sniper_rect.y - y, select_sniper_rect.width + (2 * y),
                                     select_sniper_rect.height + (2 * y)),
                         select_jet_outline_width, select_jet_outline_curve)
        if click:
            select_basic = False
            select_sniper = True
            select_zippy = False
            select_cannon = False
            select_gunner = False

    if select_cannon_rect.collidepoint((mx, my)) or select_cannon:
        pygame.draw.rect(screen, color,
                         pygame.Rect(select_cannon_rect.x - y,
                                     select_cannon_rect.y - y, select_cannon_rect.width + (2 * y),
                                     select_cannon_rect.height + (2 * y)),
                         select_jet_outline_width, select_jet_outline_curve)
        if click:
            select_basic = False
            select_sniper = False
            select_zippy = False
            select_cannon = True
            select_gunner = False
    if select_gunner_rect.collidepoint((mx, my)) or select_gunner:
        pygame.draw.rect(screen, color,
                         pygame.Rect(select_gunner_rect.x - y,
                                     select_gunner_rect.y - y, select_gunner_rect.width + (2 * y),
                                     select_gunner_rect.height + (2 * y)),
                         select_jet_outline_width, select_jet_outline_curve)
        if click:
            select_basic = False
            select_sniper = False
            select_zippy = False
            select_cannon = False
            select_gunner = True
    if select_zippy_rect.collidepoint((mx, my)) or select_zippy:
        pygame.draw.rect(screen, color,
                         pygame.Rect(select_zippy_rect.x - y,
                                     select_zippy_rect.y - y, select_zippy_rect.width + (2 * y),
                                     select_zippy_rect.height + (2 * y)),
                         select_jet_outline_width, select_jet_outline_curve)
        if click:
            select_basic = False
            select_sniper = False
            select_zippy = True
            select_cannon = False
            select_gunner = False
    # --------------------------------------------- Stat bars below jets
    if select_basic:
        select_movement_speed = JetTypes.Basic.movement_speed
        select_turn_radius = JetTypes.Basic.turn_radius
        select_reload_speed = JetTypes.Basic.reload_speed
        select_dmg = JetTypes.Basic.dmg
        select_toughness = JetTypes.Basic.toughness
        select_bullet_speed = JetTypes.Basic.bullet_speed
        select_bullet_type = JetTypes.Basic.bullet_type
        select_bullet_spread = JetTypes.Basic.bullet_spread
        if first_picking_jet:
            select_jet_image = scaled_blue_basic_image
        else:
            select_jet_image = scaled_red_basic_image
        select_hitbox = JetTypes.Basic.hitbox
    if select_sniper:
        select_movement_speed = JetTypes.Sniper.movement_speed
        select_turn_radius = JetTypes.Sniper.turn_radius
        select_reload_speed = JetTypes.Sniper.reload_speed
        select_dmg = JetTypes.Sniper.dmg
        select_toughness = JetTypes.Sniper.toughness
        select_bullet_speed = JetTypes.Sniper.bullet_speed
        select_bullet_type = JetTypes.Sniper.bullet_type
        select_bullet_spread = JetTypes.Sniper.bullet_spread
        if first_picking_jet:
            select_jet_image = scaled_blue_sniper_image
        else:
            select_jet_image = scaled_red_sniper_image
        select_hitbox = JetTypes.Sniper.hitbox
    if select_zippy:
        select_movement_speed = JetTypes.Zippy.movement_speed
        select_turn_radius = JetTypes.Zippy.turn_radius
        select_reload_speed = JetTypes.Zippy.reload_speed
        select_dmg = JetTypes.Zippy.dmg
        select_toughness = JetTypes.Zippy.toughness
        select_bullet_speed = JetTypes.Zippy.bullet_speed
        select_bullet_type = JetTypes.Zippy.bullet_type
        select_bullet_spread = JetTypes.Zippy.bullet_spread
        if first_picking_jet:
            select_jet_image = scaled_blue_zippy_image
        else:
            select_jet_image = scaled_red_zippy_image
        select_hitbox = JetTypes.Zippy.hitbox
    if select_cannon:
        select_movement_speed = JetTypes.Cannon.movement_speed
        select_turn_radius = JetTypes.Cannon.turn_radius
        select_reload_speed = JetTypes.Cannon.reload_speed
        select_dmg = JetTypes.Cannon.dmg
        select_toughness = JetTypes.Cannon.toughness
        select_bullet_speed = JetTypes.Cannon.bullet_speed
        select_bullet_type = JetTypes.Cannon.bullet_type
        select_bullet_spread = JetTypes.Cannon.bullet_spread
        if first_picking_jet:
            select_jet_image = scaled_blue_cannon_image
        else:
            select_jet_image = scaled_red_cannon_image
        select_hitbox = JetTypes.Cannon.hitbox
    if select_gunner:
        select_movement_speed = JetTypes.Gunner.movement_speed
        select_turn_radius = JetTypes.Gunner.turn_radius
        select_reload_speed = JetTypes.Gunner.reload_speed
        select_dmg = JetTypes.Gunner.dmg
        select_toughness = JetTypes.Gunner.toughness
        select_bullet_speed = JetTypes.Gunner.bullet_speed
        select_bullet_type = JetTypes.Gunner.bullet_type
        select_bullet_spread = JetTypes.Gunner.bullet_spread
        if first_picking_jet:
            select_jet_image = scaled_blue_gunner_image
        else:
            select_jet_image = scaled_red_gunner_image
        select_hitbox = JetTypes.Gunner.hitbox

    pygame.draw.rect(screen, color, (screen_width/2-stat_bar_length/2,
                                     screen_height/2, stat_bar_length, stat_bar_width), 2)
    pygame.draw.rect(screen, color, (screen_width/2-stat_bar_length/2,
                                     screen_height/2 + space_between_stat_bars,
                                     stat_bar_length, stat_bar_width), 2)
    pygame.draw.rect(screen, color, (screen_width/2-stat_bar_length/2,
                                     screen_height/2 + space_between_stat_bars * 2,
                                     stat_bar_length, stat_bar_width), 2)
    pygame.draw.rect(screen, color, (screen_width/2-stat_bar_length/2,
                                     screen_height/2 + space_between_stat_bars * 3,
                                     stat_bar_length, stat_bar_width), 2)
    pygame.draw.rect(screen, color, (screen_width/2-stat_bar_length/2,
                                     screen_height/2 + space_between_stat_bars * 4,
                                     stat_bar_length, stat_bar_width), 2)
    pygame.draw.rect(screen, color, (screen_width / 2 - stat_bar_length / 2,
                                     screen_height / 2 + space_between_stat_bars * 5,
                                     stat_bar_length, stat_bar_width), 2)

#    select_stat_bar_movement_speed_change = ((select_movement_speed * 130) - (select_display_movement_speed * 130))
#    if abs((select_movement_speed * 130) - (select_display_movement_speed * 130)) > 1:
#        select_display_movement_speed += select_stat_bar_movement_speed_change/50
#        select_stat_bar_movement_speed_change -= select_stat_bar_movement_speed_change/50

    pygame.draw.rect(screen, ColorSet.white, pygame.Rect(screen_width/2-stat_bar_length/2, screen_height/2,
                                                         abs(int(select_movement_speed * 130)), stat_bar_width))
    pygame.draw.rect(screen, ColorSet.white, (screen_width/2-stat_bar_length/2,
                                              screen_height/2 + space_between_stat_bars,
                                              int(4/select_turn_radius), stat_bar_width))
    pygame.draw.rect(screen, ColorSet.white, (screen_width/2-stat_bar_length/2,
                                              screen_height/2 + space_between_stat_bars * 2,
                                              select_reload_speed, stat_bar_width))
    pygame.draw.rect(screen, ColorSet.white, (screen_width/2-stat_bar_length/2,
                                              screen_height/2 + space_between_stat_bars * 3,
                                              select_toughness, stat_bar_width))
    pygame.draw.rect(screen, ColorSet.white, (screen_width/2-stat_bar_length/2,
                                              screen_height/2 + space_between_stat_bars * 4,
                                              select_bullet_speed * 35, stat_bar_width))
    pygame.draw.rect(screen, ColorSet.white, (screen_width / 2 - stat_bar_length / 2,
                                              screen_height / 2 + space_between_stat_bars * 5,
                                              select_dmg * 20, stat_bar_width))

    screen.blit(font20.render('Movement Speed', True, ColorSet.white),
                (screen_width/2-stat_bar_length/2+110, screen_height/2 - 20))
    # +~130 is to center the text
    screen.blit(font20.render('Turn Radius', True, ColorSet.white), (screen_width/2-stat_bar_length/2+135,
                                                                     screen_height/2 + space_between_stat_bars - 20))
    screen.blit(font20.render('Reload Speed', True, ColorSet.white),
                (screen_width/2-stat_bar_length/2+130, screen_height/2 + space_between_stat_bars * 2 - 20))
    screen.blit(font20.render('Toughness', True, ColorSet.white), (screen_width/2-stat_bar_length/2+150,
                                                                   screen_height/2 + space_between_stat_bars * 3 - 20))
    screen.blit(font20.render('Bullet Speed', True, ColorSet.white),
                (screen_width/2-stat_bar_length/2+140, screen_height/2 + space_between_stat_bars * 4 - 20))
    screen.blit(font20.render('Bullet Damage', True, ColorSet.white),
                (screen_width / 2 - stat_bar_length / 2 + 130, screen_height / 2 + space_between_stat_bars * 5 - 20))

    if select_bullet_type == 'hefty':
        pygame.draw.circle(screen, color, (screen_width / 2 + 500,
                                           screen_height / 2 + space_between_stat_bars * 2), 100, 0)
    if select_bullet_type == 'standard':
        pygame.draw.circle(screen, color, (screen_width / 2 + 500,
                                           screen_height / 2 + space_between_stat_bars * 2), 40, 0)
    if select_bullet_type == 'mini':
        pygame.draw.circle(screen, color, (screen_width / 2 + 500,
                                           screen_height / 2 + space_between_stat_bars * 2), 20, 0)

    pygame.draw.circle(screen, ColorSet.black, (screen_width / 2 + 500,
                                                screen_height / 2 + space_between_stat_bars * 2), 100, 3)
    pygame.draw.circle(screen, ColorSet.black, (screen_width / 2 + 500,
                                                screen_height / 2 + space_between_stat_bars * 2), 40, 3)
    pygame.draw.circle(screen, ColorSet.black, (screen_width / 2 + 500,
                                                screen_height / 2 + space_between_stat_bars * 2), 20, 3)
    # (screen_height/2 + space_between_stat_bars * 2) so that it is at the same height as the middle stat bar

    select_display_bullet_timer -= select_reload_speed
    if select_display_bullet_timer < 0:
        select_display_bullets.append([screen_width/4,
                                       screen_height/2 + space_between_stat_bars * 4,
                                       random.uniform(select_bullet_spread, -select_bullet_spread),
                                       select_bullet_speed,
                                       60,
                                       select_bullet_type])
        select_display_bullet_timer = 2500

    for select_bullet in select_display_bullets:
        if select_bullet[5] == 'mini':
            bullet_width = mini_bullet_radius
        if select_bullet[5] == 'standard':
            bullet_width = standard_bullet_radius
        if select_bullet[5] == 'hefty':
            bullet_width = hefty_bullet_radius
        select_bullet[0] += select_bullet[3] * 0.1 * math.sin(select_bullet[2])
        select_bullet[1] -= select_bullet[3] * 0.1 * math.cos(select_bullet[2])
        select_bullet[4] -= 0.03 * select_bullet[3]
        if select_bullet[4] <= 0:
            select_display_bullets.remove(select_bullet)
        pygame.draw.circle(screen, ColorSet.black, (select_bullet[0], select_bullet[1]), bullet_width)

    pygame.draw.rect(screen, color, select_jet_rect, 0, 100)
    screen.blit(font20.render('Select Jet', True, ColorSet.white), (select_jet_rect.x + 52, select_jet_rect.y + 22))

    if select_jet_rect.collidepoint((mx, my)):
        if first_picking_jet:
            if click:
                if select_gunner or select_zippy or select_sniper or select_basic or select_cannon:
                    First.movement_speed_ppf = select_movement_speed
                    First.turn_radius_int = select_turn_radius
                    First.reload_speed_seconds = select_reload_speed
                    First.hp_int = select_toughness
                    First.hp_change = 0
                    First.max_hp = select_toughness
                    First.bullet_speed_int = select_bullet_speed
                    First.bullet_type = select_bullet_type
                    First.bullet_spray_radians = select_bullet_spread
                    First.image = select_jet_image
                    First.hitbox = select_hitbox
                    first_picking_jet = False
                    transition = True
                    select_basic = False
                    select_sniper = False
                    select_zippy = False
                    select_cannon = False
                    select_gunner = False
                else:
                    you_must_pick_a_jet = True
        else:
            if click:
                if select_gunner or select_zippy or select_sniper or select_basic or select_cannon:
                    Second.movement_speed_ppf = select_movement_speed
                    Second.turn_radius_int = select_turn_radius
                    Second.reload_speed_seconds = select_reload_speed
                    Second.hp_int = select_toughness
                    Second.hp_change = 0
                    Second.max_hp = select_toughness
                    Second.bullet_speed_int = select_bullet_speed
                    Second.bullet_type = select_bullet_type
                    Second.bullet_spray_radians = select_bullet_spread
                    Second.image = select_jet_image
                    Second.hitbox = select_hitbox
                    transition = True
                    running_game = True
                    picking_jet = False
                    select_basic = False
                    select_sniper = False
                    select_zippy = False
                    select_cannon = False
                    select_gunner = False
                else:
                    you_must_pick_a_jet = True

    if select_gunner or select_zippy or select_sniper or select_basic or select_cannon:
        you_must_pick_a_jet = False
    if you_must_pick_a_jet:
        pygame.draw.rect(screen, color,
                         pygame.Rect(screen_width / 2 - 540 - y/2,
                                     screen_height / 2 - 20 - y/2, 1040 + y, 130 + y), 0, 50)
        screen.blit(font100.render('You Must Pick A Jet', True, color2),
                    (screen_width / 2 - 500, screen_height / 2))
    if transition:
        transition_x += 1
        transition_speed += transition_speed_change
        transition_speed_change += 0.006
    if transition_x * transition_speed > 2 * screen_width:
        transition = False
        transition_speed = reset_transition_speed
        transition_speed_change = reset_transition_speed_change
        transition_x = 0
    if (transition_x * transition_speed) > screen_width:
        transition_timer_ready = True

    if transition:
        screen.blit(pygame.transform.scale(transition_image, (screen_width, screen_height)),
                    (transition_x * transition_speed - screen_width, 0))

    pygame.display.update()
    clock.tick(fps)

first_boosting = False
first_turning_left = False
first_turning_right = False
first_slowing_down = False

first_bullet_reload_speed_timer = 0

second_boosting = False
second_turning_left = False
second_turning_right = False
second_slowing_down = False
second_bullet_reload_speed_timer = 0

transition_stun = True


class FightLeft:

    def __init__(self):
        pass

    x = screen_width
    y = screen_height
    image = pygame.Rect(x, y, 50, 50)


class FightRight:

    def __init__(self):
        pass

    x = screen_width
    y = screen_height
    image = pygame.Rect(x, y, 10, 10)


global_jet_moving_speed = 1

boosting_strength = 1.3

while running_game:

    click = False

    screen.fill(ColorSet.red)

    # ------------------------------ Updating First Hitbox

    First.hitbox.x = (First.x - First.hitbox.width / 2)
    First.hitbox.y = (First.y - First.hitbox.height / 2)

    # ------------------------------ Updating Second Hitbox

    Second.hitbox.x = (Second.x - Second.hitbox.width / 2)
    Second.hitbox.y = (Second.y - Second.hitbox.height / 2)

    # ------------------------------ Inputs

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            picking_jet = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                picking_jet = False
                running_game = False
            if event.key == pygame.K_w:
                first_boosting = True
            if event.key == pygame.K_a:
                first_turning_left = True
            if event.key == pygame.K_d:
                first_turning_right = True
            if event.key == pygame.K_s:
                first_slowing_down = True

            if event.key == pygame.K_UP:
                second_boosting = True
            if event.key == pygame.K_LEFT:
                second_turning_left = True
            if event.key == pygame.K_RIGHT:
                second_turning_right = True
            if event.key == pygame.K_DOWN:
                second_slowing_down = True

            if event.key == pygame.K_1:
                First.shooting = True
            if event.key == pygame.K_p:
                Second.shooting = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                first_boosting = False
            if event.key == pygame.K_a:
                first_turning_left = False
            if event.key == pygame.K_d:
                first_turning_right = False
            if event.key == pygame.K_s:
                first_slowing_down = False

            if event.key == pygame.K_UP:
                second_boosting = False
            if event.key == pygame.K_LEFT:
                second_turning_left = False
            if event.key == pygame.K_RIGHT:
                second_turning_right = False
            if event.key == pygame.K_DOWN:
                second_slowing_down = False

            if event.key == pygame.K_1:
                First.shooting = False

            if event.key == pygame.K_p:
                Second.shooting = False

    # ------------------------------ First Movement
    if first_turning_right:
        First.angle -= First.turn_radius_int
    if first_turning_left:
        First.angle += First.turn_radius_int

    if first_slowing_down:
        First.x += global_jet_moving_speed * (First.movement_speed_ppf * math.sin(First.angle) / 2)
        First.y += global_jet_moving_speed * (First.movement_speed_ppf * math.cos(First.angle) / 2)
    else:
        First.x += global_jet_moving_speed * First.movement_speed_ppf * math.sin(First.angle)
        First.y += global_jet_moving_speed * First.movement_speed_ppf * math.cos(First.angle)
    if first_boosting:
        First.x += global_jet_moving_speed * boosting_strength * (First.movement_speed_ppf * math.sin(First.angle))
        First.y += global_jet_moving_speed * boosting_strength * (First.movement_speed_ppf * math.cos(First.angle))

    First.rotated_image = pygame.transform.rotate(First.image, (First.angle * 180 / math.pi))
    screen.blit(First.rotated_image, (First.x - int(First.rotated_image.get_width() / 2),
                                      First.y - int(First.rotated_image.get_height() / 2)))

    # ------------------------------ Second Movement
    if second_turning_right:
        Second.angle -= Second.turn_radius_int
    if second_turning_left:
        Second.angle += Second.turn_radius_int

    if second_slowing_down:
        Second.x += global_jet_moving_speed * (Second.movement_speed_ppf * math.sin(Second.angle) / 2)
        Second.y += global_jet_moving_speed * (Second.movement_speed_ppf * math.cos(Second.angle) / 2)
    else:
        Second.x += global_jet_moving_speed * Second.movement_speed_ppf * math.sin(Second.angle)
        Second.y += global_jet_moving_speed * Second.movement_speed_ppf * math.cos(Second.angle)
    if second_boosting:
        Second.x += global_jet_moving_speed * boosting_strength * (Second.movement_speed_ppf * math.sin(Second.angle))
        Second.y += global_jet_moving_speed * boosting_strength * (Second.movement_speed_ppf * math.cos(Second.angle))

    Second.rotated_image = pygame.transform.rotate(Second.image, (Second.angle * 180 / math.pi))
    screen.blit(Second.rotated_image, (Second.x - int(Second.rotated_image.get_width() / 2),
                                       Second.y - int(Second.rotated_image.get_height() / 2)))

    # ------------------------------ First Shooting

    if First.bullet_type == 'standard':
        First.bullet_type = standard_bullet_radius
    if First.bullet_type == 'mini':
        First.bullet_type = mini_bullet_radius
    if First.bullet_type == 'hefty':
        First.bullet_type = hefty_bullet_radius

    first_bullet_reload_speed_timer -= First.reload_speed_seconds
    if First.shooting:
        if first_bullet_reload_speed_timer < 0:
            First.bullets.append([pygame.Rect(First.x + 3 * (First.movement_speed_ppf * math.sin(First.angle)),
                                              First.y + 3 * (First.movement_speed_ppf * math.cos(First.angle)),
                                              First.bullet_type/2, First.bullet_type/2),
                                  First.bullet_type, First.bullet_speed_int, First.angle])
            first_bullet_reload_speed_timer = 2500
    for bullet in First.bullets:
        bullet[0].x += bullet[2] * math.sin(bullet[3])
        bullet[0].y += bullet[2] * math.cos(bullet[3])
        pygame.draw.circle(screen, ColorSet.black, (bullet[0].x, bullet[0].y), bullet[1])
        if bullet[0].colliderect(Second.hitbox):
            Second.hp_change -= First.dmg
            First.bullets.remove(bullet)

    # ------------------------------ Second Shooting

    if Second.bullet_type == 'standard':
        Second.bullet_type = standard_bullet_radius
    if Second.bullet_type == 'mini':
        Second.bullet_type = mini_bullet_radius
    if Second.bullet_type == 'hefty':
        Second.bullet_type = hefty_bullet_radius

    second_bullet_reload_speed_timer -= Second.reload_speed_seconds
    if Second.shooting:
        if second_bullet_reload_speed_timer < 0:
            Second.bullets.append([pygame.Rect(Second.x + 3 * (Second.movement_speed_ppf * math.sin(Second.angle)),
                                               Second.y + 3 * (Second.movement_speed_ppf * math.cos(Second.angle)),
                                               Second.bullet_type/2, Second.bullet_type/2),
                                  Second.bullet_type, Second.bullet_speed_int, Second.angle])
            second_bullet_reload_speed_timer = 2500
    for bullet2 in Second.bullets:
        bullet2[0].x += bullet2[2] * math.sin(bullet2[3])
        bullet2[0].y += bullet2[2] * math.cos(bullet2[3])
        pygame.draw.circle(screen, ColorSet.black, (bullet2[0].x, bullet2[0].y), bullet2[1])
        if bullet2[0].colliderect(First.hitbox):
            First.hp_change -= Second.dmg
            Second.bullets.remove(bullet2)

    # ------------------------------ First Health display

    if abs(First.hp_change) > 1:
        First.hp_int += First.hp_change/50
        First.hp_change -= First.hp_change/50

    r = abs(150 - ((150 / First.max_hp) * First.hp_int))
    g = abs((255 / First.max_hp) * First.hp_int)
    first_hp_color = (r, g, 50)
    pygame.draw.rect(screen, first_hp_color, pygame.Rect(50, 20, First.hp_int, 20))

    # ------------------------------ Second Health display

    if abs(Second.hp_change) > 1:
        Second.hp_int += Second.hp_change / 50
        Second.hp_change -= Second.hp_change / 50

    r = abs(150 - ((150 / Second.max_hp) * Second.hp_int))
    g = abs((255 / Second.max_hp) * Second.hp_int)
    second_hp_color = (r, g, 50)
    pygame.draw.rect(screen, second_hp_color, pygame.Rect(950, 20, Second.hp_int, 20))

    # Keep jets still before game starts

    if transition_stun:
        FightLeft.image.x = FightLeft.x
        FightLeft.image.y = FightLeft.y

        FightLeft.x += 5  # (screen_width/2 - FightLeft.x)/10
        FightLeft.y += 5

        FightRight.image.x = FightRight.x
        FightRight.image.y = FightRight.y

    pygame.draw.rect(screen, ColorSet.blue, FightLeft.image)

    # ------------------------------ Debugging

    # Show hitboxes of jets
    #pygame.draw.rect(screen, ColorSet.black, First.hitbox)
    #pygame.draw.rect(screen, ColorSet.black, Second.hitbox)

    pygame.display.update()
    clock.tick(fps)
