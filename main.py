def on_left_pressed():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . . . . . c c . . . 
                        . . . . . . . c c c c 6 3 c . . 
                        . . . . . . c 6 3 3 3 3 6 c . . 
                        . . c c . c 6 c c 3 3 3 3 3 c . 
                        . b 5 5 c 6 c 5 5 c 3 3 3 3 3 c 
                        . f f 5 c 6 c 5 f f 3 3 3 3 3 c 
                        . f f 5 c 6 c 5 f f 6 3 3 3 c c 
                        . b 5 5 3 c 3 5 5 c 6 6 6 6 c c 
                        . . b 5 5 3 5 5 c 3 3 3 3 3 3 c 
                        . . c 5 5 5 5 b c c 3 3 3 3 3 3 
                        . . c 4 5 5 4 b 5 5 c 3 3 3 c . 
                        . c 5 b 4 4 b b 5 c c b b b . . 
                        . c 4 4 b 5 5 5 4 c 4 4 4 5 b . 
                        . c 5 4 c 5 5 5 c 4 4 4 c 5 c . 
                        . c 5 c 5 5 5 5 c 4 4 4 c c c . 
                        . . c c c c c c c . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . c c . . . . 
                        . . . . . . c c c c 6 3 c . . . 
                        . . . . . c 6 6 3 3 3 6 c . . . 
                        . . . . c 6 6 3 3 3 3 3 3 c . . 
                        b c c c 6 6 c c 3 3 3 3 3 3 c . 
                        b 5 5 c 6 c 5 5 c 3 3 3 3 3 c . 
                        f f 5 c 6 c 5 f f 6 3 3 3 c c . 
                        f f 5 c c c 5 f f 6 6 6 6 c c . 
                        . b 5 5 3 5 5 c 3 3 3 3 3 3 c . 
                        . c 5 5 5 5 4 c c c 3 3 3 3 c . 
                        . c 4 5 5 4 4 b 5 5 c 3 3 c . . 
                        . c 5 b 4 4 b b 5 c b b c . . . 
                        . c c 5 4 c 5 5 5 c c 5 c . . . 
                        . . . c c 5 5 5 5 c c c c . . . 
                        . . . . c c c c c c . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . c c . . . 
                        . . . . . . . c c c c 6 3 c . . 
                        . . . . . . c 6 6 3 3 3 6 c . . 
                        . . . . . c 6 6 3 3 3 3 3 3 c . 
                        . b c c c 6 6 c c 3 3 3 3 3 3 c 
                        . b 5 5 c 6 c 5 5 c 3 3 3 3 3 c 
                        . f f 5 c 6 c 5 f f 6 3 3 3 c c 
                        . f f 5 c c c 5 f f 6 6 6 6 c c 
                        . . b 5 5 3 5 5 c c c 3 3 3 3 c 
                        . . c 5 5 5 5 5 b 5 5 c 3 3 3 c 
                        . c 4 4 5 5 4 4 b b 5 c 3 3 c . 
                        . c 5 5 b 4 4 4 b 5 5 5 b c . . 
                        . c 5 5 5 4 4 4 c 5 5 5 c b . . 
                        . . c c c c 4 c 5 5 5 5 c c . . 
                        . . . . c c c c c c c c c c . .
            """),
            img("""
                . . . . . . . . . . . c c . . . 
                        . . . . . . . c c c c 6 3 c . . 
                        . . . . . . c 6 3 3 3 3 6 c . . 
                        . . c c . c 6 c c 3 3 3 3 3 c . 
                        . b 5 5 c 6 c 5 5 c 3 3 3 3 3 c 
                        . f f 5 c 6 c 5 f f 3 3 3 3 3 c 
                        . f f 5 c 6 c 5 f f 6 3 3 3 c c 
                        . b 5 5 3 c 3 5 5 c 6 6 6 6 c c 
                        . . b 5 5 3 5 5 c 3 3 3 3 3 3 c 
                        . c c 5 5 5 5 4 c c 3 3 3 3 3 c 
                        c 5 5 4 5 5 4 c 5 5 c 3 3 3 c . 
                        b 5 4 b 4 4 4 c 5 5 5 b c c . . 
                        c 4 5 5 b 4 4 c 5 5 5 c b b . . 
                        c 5 5 5 c 4 c 5 5 5 5 c c 5 b . 
                        c 5 5 5 5 c 4 c c c c c c 5 c . 
                        . c c c c c c . . . . . c c c .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . . c c . . . . . . . . . . . 
                        . . c 3 6 c c c c . . . . . . . 
                        . . c 6 3 3 3 3 6 c . . . . . . 
                        . c 3 3 3 3 3 c c 6 c . c c . . 
                        c 3 3 3 3 3 c 5 5 c 6 c 5 5 b . 
                        c 3 3 3 3 3 f f 5 c 6 c 5 f f . 
                        c c 3 3 3 6 f f 5 c 6 c 5 f f . 
                        c c 6 6 6 6 c 5 5 3 c 3 5 5 b . 
                        c 3 3 3 3 3 3 c 5 5 3 5 5 b . . 
                        c 3 3 3 3 3 c c b 5 5 5 5 c . . 
                        . c 3 3 3 c 5 5 b 4 5 5 4 c . . 
                        . . b b b c c 5 b b 4 4 b 5 c . 
                        . b 5 4 4 4 c 4 5 5 5 b 4 4 c . 
                        . c 5 c 4 4 4 c 5 5 5 c 4 5 c . 
                        . c c c 4 4 4 c 5 5 5 5 c 5 c . 
                        . . . . . . . c c c c c c c . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . c c . . . . . . . . . . 
                        . . . c 3 6 c c c c . . . . . . 
                        . . . c 6 3 3 3 6 6 c . . . . . 
                        . . c 3 3 3 3 3 3 6 6 c . . . . 
                        . c 3 3 3 3 3 3 c c 6 6 c c c b 
                        . c 3 3 3 3 3 c 5 5 c 6 c 5 5 b 
                        . c c 3 3 3 6 f f 5 c 6 c 5 f f 
                        . c c 6 6 6 6 f f 5 c c c 5 f f 
                        . c 3 3 3 3 3 3 c 5 5 3 5 5 b . 
                        . c 3 3 3 3 c c c 4 5 5 5 5 c . 
                        . . c 3 3 c 5 5 b 4 4 5 5 4 c . 
                        . . . c b b c 5 b b 4 4 b 5 c . 
                        . . . c 5 c c 5 5 5 c 4 5 c c . 
                        . . . c c c c 5 5 5 5 c c . . . 
                        . . . . . . c c c c c c . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . c c . . . . . . . . . . . 
                        . . c 3 6 c c c c . . . . . . . 
                        . . c 6 3 3 3 6 6 c . . . . . . 
                        . c 3 3 3 3 3 3 6 6 c . . . . . 
                        c 3 3 3 3 3 3 c c 6 6 c c c b . 
                        c 3 3 3 3 3 c 5 5 c 6 c 5 5 b . 
                        c c 3 3 3 6 f f 5 c 6 c 5 f f . 
                        c c 6 6 6 6 f f 5 c c c 5 f f . 
                        c 3 3 3 3 c c c 5 5 3 5 5 b . . 
                        c 3 3 3 c 5 5 b 5 5 5 5 5 c . . 
                        . c 3 3 c 5 b b 4 4 5 5 4 4 c . 
                        . . c b 5 5 5 b 4 4 4 b 5 5 c . 
                        . . b c 5 5 5 c 4 4 4 5 5 5 c . 
                        . . c c 5 5 5 5 c 4 c c c c . . 
                        . . c c c c c c c c c c . . . .
            """),
            img("""
                . . . c c . . . . . . . . . . . 
                        . . c 3 6 c c c c . . . . . . . 
                        . . c 6 3 3 3 3 6 c . . . . . . 
                        . c 3 3 3 3 3 c c 6 c . c c . . 
                        c 3 3 3 3 3 c 5 5 c 6 c 5 5 b . 
                        c 3 3 3 3 3 f f 5 c 6 c 5 f f . 
                        c c 3 3 3 6 f f 5 c 6 c 5 f f . 
                        c c 6 6 6 6 c 5 5 3 c 3 5 5 b . 
                        c 3 3 3 3 3 3 c 5 5 3 5 5 b . . 
                        c 3 3 3 3 3 c c 4 5 5 5 5 c c . 
                        . c 3 3 3 c 5 5 c 4 5 5 4 5 5 c 
                        . . c c b 5 5 5 c 4 4 4 b 4 5 b 
                        . . b b c 5 5 5 c 4 4 b 5 5 4 c 
                        . b 5 c c 5 5 5 5 c 4 c 5 5 5 c 
                        . c 5 c c c c c c 4 c 5 5 5 5 c 
                        . c c c . . . . . c c c c c c .
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    global mySprite2
    info.start_countdown(5)
    info.change_score_by(1)
    mySprite2.destroy()
    mySprite2 = sprites.create(img("""
            . . . . . 3 3 b 3 3 d d 3 3 . . 
                    . . . . 3 1 1 d 3 d 1 1 1 1 3 . 
                    . . . 3 d 1 1 1 d 1 1 1 d 3 1 3 
                    . . 3 d d 1 1 1 d d 1 1 1 3 3 3 
                    . 3 1 1 d 1 1 1 1 d d 1 1 b . . 
                    . 3 1 1 1 d 1 1 1 1 1 d 1 1 3 . 
                    . b d 1 1 1 d 1 1 1 1 1 1 1 3 . 
                    . 4 b 1 1 1 1 d d 1 1 1 1 d 3 . 
                    . 4 4 d 1 1 1 1 1 1 d d d b b . 
                    . 4 d b d 1 1 1 1 1 1 1 1 3 . . 
                    4 d d 5 b d 1 1 1 1 1 1 1 3 . . 
                    4 5 d 5 5 b b d 1 1 1 1 d 3 . . 
                    4 5 5 d 5 5 d b b b d d 3 . . . 
                    4 5 5 5 d d d d 4 4 b 3 . . . . 
                    . 4 5 5 5 4 4 4 . . . . . . . . 
                    . . 4 4 4 . . . . . . . . . . .
        """),
        SpriteKind.food)
    mySprite2.set_position(randint(5, 155), randint(5, 115))
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

mySprite3: Sprite = None
mySprite2: Sprite = None
mySprite: Sprite = None
info.set_score(0)
mySprite = sprites.create(img("""
        . . . . . . . . . . . c c . . . 
            . . . . . . . c c c c 6 3 c . . 
            . . . . . . c 6 3 3 3 3 6 c . . 
            . . c c . c 6 c c 3 3 3 3 3 c . 
            . b 5 5 c 6 c 5 5 c 3 3 3 3 3 c 
            . f f 5 c 6 c 5 f f 3 3 3 3 3 c 
            . f f 5 c 6 c 5 f f 6 3 3 3 c c 
            . b 5 5 3 c 3 5 5 c 6 6 6 6 c c 
            . . b 5 5 3 5 5 c 3 3 3 3 3 3 c 
            . c c 5 5 5 5 5 b c c 3 3 3 3 c 
            c 5 5 4 5 5 5 4 b 5 5 c 3 3 c . 
            b 5 4 b 4 4 4 4 b b 5 c b b . . 
            c 4 5 5 b 4 b 5 5 5 4 c 4 5 b . 
            c 5 5 5 c 4 c 5 5 5 c 4 c 5 c . 
            c 5 5 5 5 c 5 5 5 5 c 4 c 5 c . 
            . c c c c c c c c c . . c c c .
    """),
    SpriteKind.player)
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffffffffffcffffffffffcffffffffffffffffffffff
        ffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffcffffffffffffffffcbcffffffffffffffffffffc
        fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffff
        fffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffffffffffff
        fff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbfffffffffffffff3fffffffffffffffffffffbbbffffffffffff
        ffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffffffb3bffffffffffffffffffffcbcffffffffffff
        f33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccfffffffffffffffffffff33333ffffffffffffccffffffffffffffffffff
        ff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffffff3b3fffffffffffffccffffffffffffffffffff
        ffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffffffbfbfffffffffffffffffffffffffffffcfffff
        fffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcffff
        fffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcffffffffffffffffcffffffffffffffffffffffcfffff
        ffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffffffffffffffcbcfffffffffffffffffffffffffff
        fffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcfffffffffffffcfffffffffffffffffffffffffcffffffffffff
        fffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffcfffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffffffffffccfffffcffffffffffffffffffffffffff
        ffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffffffffffccfffffffffffffcccccccccccffffffff
        ffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffffffffffffffffffffccccccccccccccccccccffff
        fffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccffffffffffffffccccccccccccccccccccccccccf
        ccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffcccccccccccccccccccccccccccccccfffffffffccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
        bbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccbbbbbbbb
        bbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbccccccccccbbbbbbbbbbbbb
        bbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbb
        bbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbbbbbbbbbbb3333333bbbbbbbbb33cbbbbbbbbbbbb
        bbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbbbbbbbbb33cccccbb33bbbbbbbccbbccbbbbbbbbb
        bbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbbbbbbbbbcccbbbbbcccbbbbbbbbccccbbbbbbbbbb
        3bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb333333333bbbbbbbcccccccccbbbbbbbbbbbbbbb33333333
        333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb333bbbbbbbcccccbbbbbbbbbbbbbbb333ccbbbbb
        cc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccccc3bbbbbbbbbbbbbbbbbbbbbbbbbbb3cccbbbccc
        cccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcccccbbbbbbbbbbbb333bbbbbb3bbbbbcccbbbbbcc
        cccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccccccbbbbbbbbbbbb333bbbbbbbbbbbbcccccccccc
        cbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbcccccccc
        bbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb3333bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
        bbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbbbbb333333bbb33ddddddddddddddddd33bbbbbbb
        bbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bbbbb33333ddddddddddddddddddddddddddddd3bb
        dddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddddddddddddddddddddddddddddddddddd33333ddd
        dddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33ddddddddddddddd3333333333ddddddd33dddd33d
        dddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbddddddddddddd333ddddddddd33dddddbbbbbbbbd
        ddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbddddddddddddd333d3bbbbbbbbd33dddddbbbbbbdd
        ddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33dddddddddddddddddddddddd33bbbbbbbbbbbb33ddddddddddddd
        ddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbddddddddddddddddddddddddddbbbbbbbbbbbbbbdddddddddddddd
        ddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3dddddddddddddddddddddddddddd3bbbbbbbbbb3ddddddddddddddd
        d333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333ddddddddddddddddddd333333ddddddddd333333dddddddddddddddddd
        333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3333333333dddddddddddddddddddddddddddddd3
        33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd33333333dddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333d
        33ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd3333ddddddddddddddddddddd333dddddddddddd33
        d333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333ddddddddddddddddd333dddddddddddddddd
        ddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3dddd33ddddddddddddddd33dddd3bbbbbbbbbbb3d
        b3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbbb3dd3ddddddddddddddd3dd3bbbbbbbbbbbbbbbb
        bb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbbbb333ddddddddddddddd33bbbbbbbbbbbbbbbbbb
        bbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbbbbb3dddddddddddddddd3bbbbbbbbbbbbbbbbbbb
        b3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbbb3ddddddddddddddddddd3bbbbbbbbbbbbbbbbbb
        dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33dddddddddddddddddddddddd3bbbbbbbbbbbbb33
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd
        dddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddddddddddddd3333333333333ddddddddddddddddd
        dddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddddddddd333333333333333333333ddddddddddddd
        dddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddddddd3333333333333333ddd3333333dddddddddd
        dd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddddd3333333333333333333dddddd333333ddddddd
        3333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd3333333333333333333333333ddddddddddddddd333
        33333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd33333333333333333333333333333333dddddddd333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
        3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
"""))
controller.move_sprite(mySprite, 80, 80)
mySprite.set_stay_in_screen(True)
info.start_countdown(4)
mySprite2 = sprites.create(img("""
        . . . . . 3 3 b 3 3 d d 3 3 . . 
            . . . . 3 1 1 d 3 d 1 1 1 1 3 . 
            . . . 3 d 1 1 1 d 1 1 1 d 3 1 3 
            . . 3 d d 1 1 1 d d 1 1 1 3 3 3 
            . 3 1 1 d 1 1 1 1 d d 1 1 b . . 
            . 3 1 1 1 d 1 1 1 1 1 d 1 1 3 . 
            . b d 1 1 1 d 1 1 1 1 1 1 1 3 . 
            . 4 b 1 1 1 1 d d 1 1 1 1 d 3 . 
            . 4 4 d 1 1 1 1 1 1 d d d b b . 
            . 4 d b d 1 1 1 1 1 1 1 1 3 . . 
            4 d d 5 b d 1 1 1 1 1 1 1 3 . . 
            4 5 d 5 5 b b d 1 1 1 1 d 3 . . 
            4 5 5 d 5 5 d b b b d d 3 . . . 
            4 5 5 5 d d d d 4 4 b 3 . . . . 
            . 4 5 5 5 4 4 4 . . . . . . . . 
            . . 4 4 4 . . . . . . . . . . .
    """),
    SpriteKind.food)

def on_forever():
    global mySprite3
    if info.score() == 10:
        mySprite3 = sprites.create(img("""
                . . . . . . . . . . . . . . 
                            e e e . . . . e e e . . . . 
                            c d d c . . c d d c . . . . 
                            c b d d f f d d b c . . . . 
                            c 3 b d d b d b 3 c . . . . 
                            f b 3 d d d d 3 b f . . . . 
                            e d d d d d d d d e . . . . 
                            e d 2 d d d d 2 d e . b f b 
                            f d d 2 d d 2 d d f . f d f 
                            f b d d b b d d 2 b f f d f 
                            . f 2 2 2 2 2 2 d b b d b f 
                            . f d d d d d d d f f f f . 
                            . . f d b d f d f . . . . . 
                            . . . f f f f f f . . . . .
            """),
            SpriteKind.enemy)
        mySprite3.set_bounce_on_wall(True)
forever(on_forever)
