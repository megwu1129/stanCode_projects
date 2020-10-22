"""
File: My drawing
Name: Meg Wu
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    I'm gonna make a slot machine that has some cute cartoon figures in it.
    """
    window = GWindow(width=700, height=700, title="Meg's painting")

    background1 = GRect(700, 700)
    background1.filled = True
    background1.fill_color = 'lightcyan'
    background1.color = 'lightcyan'
    window.add(background1)

    slottop = GRect(35, 40, x=310, y=60)
    slottop.filled = True
    slottop.fill_color = 'orange'
    slottop.color = 'orange'
    window.add(slottop)

    slot1 = GRect(450, 80, x=100, y=90)
    slot1.filled = True
    slot1.fill_color = 'teal'
    slot1.color = 'teal'
    window.add(slot1)

    slot2 = GRect(435, 350, x=107, y=171)
    slot2.filled = True
    slot2.fill_color = 'salmon'
    slot2.color = 'salmon'
    window.add(slot2)

    slot3 = GRect(420, 50, x=115, y=105)
    slot3.filled = True
    slot3.fill_color = 'peachpuff'
    slot3.color = 'peachpuff'
    window.add(slot3)

    slotbody1 = GRect(130, 260, x=120, y=190)
    slotbody1.filled = True
    slotbody1.fill_color = 'ivory'
    slotbody1.color = 'ivory'
    window.add(slotbody1)

    slotbody2 = GRect(130, 260, x=260, y=190)
    slotbody2.filled = True
    slotbody2.fill_color = 'ivory'
    slotbody2.color = 'ivory'
    window.add(slotbody2)

    slotbody3 = GRect(130, 260, x=400, y=190)
    slotbody3.filled = True
    slotbody3.fill_color = 'ivory'
    slotbody3.color = 'ivory'
    window.add(slotbody3)

    slot5 = GRect(450, 150, x=100, y=500)
    slot5.filled = True
    slot5.fill_color = 'teal'
    slot5.color = 'teal'
    window.add(slot5)

    slot7 = GRect(100, 30, x=280, y=620)
    slot7.filled = True
    slot7.fill_color = 'salmon'
    slot7.color = 'salmon'
    window.add(slot7)


    slotline = GRect(380, 10, x=130, y=470)
    slotline.filled = True
    slotline.fill_color = 'teal'
    slotline.color = 'teal'
    window.add(slotline)

    slot6 = GRect(220, 60, x=215, y=500)
    slot6.filled = True
    slot6.fill_color = 'salmon'
    slot6.color = 'salmon'
    window.add(slot6)

    slotball1 = GOval(35, 35, x=240, y=510)
    slotball1.filled = True
    slotball1.fill_color = 'orange'
    slotball1.color = 'orange'
    window.add(slotball1)

    slotball2 = GOval(35, 35, x=310, y=510)
    slotball2.filled = True
    slotball2.fill_color = 'orange'
    slotball2.color = 'orange'
    window.add(slotball2)

    slotball3 = GOval(35, 35, x=380, y=510)
    slotball3.filled = True
    slotball3.fill_color = 'orange'
    slotball3.color = 'orange'
    window.add(slotball3)

    side2 = GRect(10, 160, x=560, y=340)
    side2.filled = True
    side2.fill_color = 'teal'
    side2.color = 'teal'
    window.add(side2)

    side1 = GRect(35, 100, x=555, y=500)
    side1.filled = True
    side1.fill_color = 'peachpuff'
    side1.color = 'peachpuff'
    window.add(side1)

    side3 = GOval(30, 30, x=550, y=320)
    side3.filled = True
    side3.fill_color = 'orange'
    side3.color = 'orange'
    window.add(side3)

    label1 = GLabel('stanCode', x=288, y=650)
    label1.font = '-20'
    label1.filled = True
    label1.color = 'darkgrey'
    window.add(label1)


    minionface = GOval(100, 100, x=275, y=220)
    minionface.filled = True
    minionface.fill_color = 'yellow'
    minionface.color ='yellow'
    window.add(minionface)

    headgear = GRect(100, 8, x=275, y=264)
    headgear.filled = True
    window.add(headgear)

    minionglass = GOval(35, 35, x=308, y=250)
    minionglass.filled = True
    minionglass.fill_color = 'grey'
    minionglass.color = 'grey'
    window.add(minionglass)

    minioneye = GOval(22, 22, x=314, y=256)
    minioneye.filled = True
    minioneye.fill_color = 'white'
    minioneye.color = 'white'
    window.add(minioneye)

    minioneyeball = GOval(11, 11, x=320, y=262)
    minioneyeball.filled = True
    window.add(minioneyeball)

    minionline1 = GLine(315, 218, 320, 230)
    window.add(minionline1)
    minionline2 = GLine(325, 216, 325, 230)
    window.add(minionline2)
    minionline3 = GLine(337, 216, 330, 230)
    window.add(minionline3)

    minionmouth1 = GOval(18, 18, x=317, y=293)
    minionmouth1.filled = True
    window.add(minionmouth1)

    minionmouth2 = GOval(18, 15, x=317, y=290)
    minionmouth2.filled = True
    minionmouth2.fill_color = 'yellow'
    minionmouth2.color = 'yellow'
    window.add(minionmouth2)

    minionmouth3 = GRect(18, 10, x=317, y=292)
    minionmouth3.filled = True
    minionmouth3.fill_color = 'yellow'
    minionmouth3.color = 'yellow'
    window.add(minionmouth3)

    bearface = GOval(100, 90, x=135, y=220)
    bearface.filled = True
    bearface.fill_color = 'wheat'
    bearface.color = 'wheat'
    window.add(bearface)

    bearnose1 = GOval(45, 28, x=162, y=260)
    bearnose1.filled = True
    bearnose1.fill_color = 'white'
    bearnose1.color = 'white'
    window.add(bearnose1)

    bearleye = GOval(10, 10, x=158, y=256)
    bearleye.filled = True
    window.add(bearleye)

    bearreye = GOval(10, 10, x=200, y=256)
    bearreye.filled = True
    window.add(bearreye)

    bearmouth1 = GOval(10, 10, x=175, y=275)
    bearmouth1.filled = True
    window.add(bearmouth1)

    bearmouth2 = GOval(10, 10, x=172, y=272)
    bearmouth2.filled = True
    bearmouth2.fill_color = 'ivory'
    bearmouth2.color = 'ivory'
    window.add(bearmouth2)

    bearmouth3 = GOval(10, 10, x=185, y=275)
    bearmouth3.filled = True
    window.add(bearmouth3)

    bearmouth4 = GOval(10, 10, x=187, y=272)
    bearmouth4.filled = True
    bearmouth4.fill_color = 'ivory'
    bearmouth4.color = 'ivory'
    window.add(bearmouth4)

    bearnose2 = GOval(10, 8, x=178, y=272)
    bearnose2.filled = True
    window.add(bearnose2)

    bearlear = GOval(18, 18, x=145, y=215)
    bearlear.filled = True
    bearlear.fill_color ='wheat'
    bearlear.color ='wheat'
    window.add(bearlear)

    bearrear = GOval(18, 18, x=207, y=215)
    bearrear.filled = True
    bearrear.fill_color = 'wheat'
    bearrear.color = 'wheat'
    window.add(bearrear)

    bigeyeface = GOval(90, 88, x=420, y=225)
    bigeyeface.filled = True
    bigeyeface.fill_color = 'lightgreen'
    bigeyeface.color = 'lightgreen'
    window.add(bigeyeface)

    bigeyeeye1 = GOval(53, 50, x=438, y=245)
    bigeyeeye1.filled = True
    bigeyeeye1.fill_color = 'white'
    bigeyeeye1.color = 'white'
    window.add(bigeyeeye1)

    bigeyeeye2 = GOval(31, 29, x=450, y=255)
    bigeyeeye2.filled = True
    window.add(bigeyeeye2)

    bigeyeeyeball = GOval(7, 7, x=463, y=265)
    bigeyeeyeball.filled = True
    bigeyeeyeball.fill_color = 'white'
    bigeyeeyeball.color='white'
    window.add(bigeyeeyeball)

    bigeyemouth1 = GOval(15, 5, x=458, y=302)
    bigeyemouth1.filled = True
    window.add(bigeyemouth1)

    bigeyemouth2 = GRect(15, 5, x=458, y=298)
    bigeyemouth2.filled = True
    bigeyemouth2.fill_color = 'lightgreen'
    bigeyemouth2.color = 'lightgreen'
    window.add(bigeyemouth2)

    baymaxface = GOval(92, 85, x=135, y=340)
    baymaxface.filled = True
    baymaxface.fill_color = 'ivory'
    baymaxface.color = 'grey'
    window.add(baymaxface)

    baymaxleye = GOval(11, 12, x=160, y=376)
    baymaxleye.filled = True
    window.add(baymaxleye)

    baymaxreye = GOval(11, 12, x=195, y=376)
    baymaxreye.filled = True
    window.add(baymaxreye)

    baymaxnose = GRect(36, 3, x=160, y=380)
    baymaxnose.filled = True
    window.add(baymaxnose)

    lotsoface = GOval(90, 83, x=277, y=340)
    lotsoface.filled = True
    lotsoface.fill_color = 'indianred'
    lotsoface.color = 'indianred'
    window.add(lotsoface)

    lotsonose1 = GOval(55, 45, x=294, y=370)
    lotsonose1.filled = True
    lotsonose1.fill_color = 'mistyrose'
    lotsonose1.color = 'mistyrose'
    window.add(lotsonose1)

    lotsonose2 = GOval(37, 25, x=304, y=375)
    lotsonose2.filled = True
    lotsonose2.fill_color = 'sienna'
    lotsonose2.color = 'sienna'
    window.add(lotsonose2)

    lotsoleye = GOval(8, 8, x=307, y=363)
    lotsoleye.filled = True
    window.add(lotsoleye)

    lotsoreye = GOval(8, 8, x=330, y=363)
    lotsoreye.filled = True
    window.add(lotsoreye)

    lotsoeyerbrow = GOval(15, 4, x=327, y=355)
    lotsoeyerbrow.filled = True
    lotsoeyerbrow.fill_color = 'sienna'
    window.add(lotsoeyerbrow)

    lotsoeyelbrow = GOval(15, 4, x=300, y=355)
    lotsoeyelbrow.filled = True
    lotsoeyelbrow.fill_color = 'sienna'
    window.add(lotsoeyelbrow)

    lotsolear1 = GOval(18, 15, x=285, y=335)
    lotsolear1.filled = True
    lotsolear1.fill_color = 'indianred'
    lotsolear1.color = 'indianred'
    window.add(lotsolear1)

    lotsorear1 = GOval(18, 15, x=342, y=336)
    lotsorear1.filled = True
    lotsorear1.fill_color = 'indianred'
    lotsorear1.color = 'indianred'
    window.add(lotsorear1)

    lotsolear2 = GOval(10, 8, x=290, y=340)
    lotsolear2.filled = True
    lotsolear2.fill_color = 'mistyrose'
    lotsolear2.color = 'mistyrose'
    window.add(lotsolear2)

    lotsorear2 = GOval(10, 8, x=346, y=340)
    lotsorear2.filled = True
    lotsorear2.fill_color = 'mistyrose'
    lotsorear2.color = 'mistyrose'
    window.add(lotsorear2)

    baymaxface = GOval(92, 85, x=420, y=340)
    baymaxface.filled = True
    baymaxface.fill_color = 'ivory'
    baymaxface.color = 'grey'
    window.add(baymaxface)

    baymaxleye = GOval(11, 12, x=445, y=376)
    baymaxleye.filled = True
    window.add(baymaxleye)

    baymaxreye = GOval(11, 12, x=478, y=376)
    baymaxreye.filled = True
    window.add(baymaxreye)

    baymaxnose = GRect(36, 3, x=450, y=380)
    baymaxnose.filled = True
    window.add(baymaxnose)




















if __name__ == '__main__':
    main()