"""
1) Attributes : A set of properties of a widget that defines its visual appearance on the computer screen and how it
                responds to user events. Here we will discuss about the attributes of label and pack :

2) Attributes of label :- The label widget is a standard Tkinter widget use to display a text or image on the screen.
                        - There are lot of attributes of label widget. Some important attributes are discussed below....

                          1) bg : The normal background displayed behind the label and indicator.
                          2) fg : This option specifies the color of the text (foreground color). If you are displaying
                                  a bitmap, this is the color that will appear at the position of the 1 bits in the
                                  bitmap.
                          3) padx : Extra space added to the left and right of the text within the widget. Default is 1.
                          4) pady : Extra space added above and below the text within the widget. Default is 1.
                          5) relief : Specifies the appearance of a decorative border around the label. There are five
                                      types of reliefs, such that FLAT,RAISED,SUNKEN,GROOVE and RIDGE. The default is
                                      FLAT.
                          6) font : If you are displaying text in this label ( With the text OR textvariable option ),
                                    the font option specifies the style , size and other characteristics (i.e bold,ita-
                                    lic etc.) of the font snd in this style the text will be displayed.
                          7) text : To display one OR more lines of text in a label widget, set this option to a string
                                    containing the text. Internal newlines ("\n") will force a line break.
                          8) justify : Specifies how multiple lines of text will be aligned with respect to each other:
                                       LEFT for flush left, CENTER for centered ( default ) OR RIGHT for right-justified.
                          9) height : The vertical dimension of the new frame .
                          10) width : The horizontal dimension of the new frame. If this option is not set , the label
                                      will be sized to fit its contents.

3) Attributes of Pack :-The pack geometry manager packs widgets in row OR columns. We can use options like fill, expand
                        and side to control this geometry manager.
                        1) fill : Determines whether widgets fills any extra space allocated to it by the picker, or
                                  keep its own minimal dimensions: NONE (default), X(fill only horizontally), Y(fill
                                  only vertically), OR BOTH(fill both horizontally and vertically).
                        2) side : Determines which side of the parent widgets packs against : TOP, BOTTOM, LEFT, RIGHT.
                                  The default is TOP.
                        3) anchor : Anchors are used to define where text is positioned relative to a reference point .
                                    The anchor attributes are : n,s,e,w,center,nw,sw,ne and se. The default is center.

"""

from tkinter import *

root = Tk()
root.geometry('630x300')
root.title('My GUI with GBG')

# Important label options :
# text : adds the text
# bg : background
# fg : foreground
# font : sets the font
# 1. font = ("comicsansms", 19, "bold")
# 2. font = "comicsansms 19 bold"
# padx : x padding
# pady : y padding
# relief : border styling - SUNKEN, RAISED, GROOVE, RIDGE.



title_label = Label(text='''If you are displaying text in this label ( With the text OR textvariable option ),
                            \nthe font option specifies the style , size and other characteristics (i.e bold,ita-
                            \nlic etc.) of the font snd in this style the text will be displayed.''', bg="darkblue",
                            fg="white",padx="10",pady="20",font="comicsansms 10 bold", borderwidth=30, relief=SUNKEN)

# Important of pack options :
# ancher = nw
# side = top, bottom, left, right.
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor="sw", fill=X)

title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)

root.mainloop()
