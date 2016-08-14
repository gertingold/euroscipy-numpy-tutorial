from pyx import canvas, color, deco, path, text, unit

text.set(text.LatexRunner)
text.preamble(r'\usepackage{arev}\usepackage[T1]{fontenc}')
unit.set(xscale=1.2, wscale=1.5)
c = canvas.canvas()

ht = 0.5
wd = 2
dist = 0.2
textcolor = color.hsb(0.02, 1, 0.6)
for n in range(6):
    x = n*(wd+dist)
    c.stroke(path.rect(x, 0, wd, ht))
    c.text(x+0.5*wd, 0.5*ht, str(n), [text.halign.center, text.valign.middle])
for n in range(3):
    x = n*(wd+dist)
    c.stroke(path.curve(x-dist/3, ht+0.5*dist,
                        x+0.3*wd, ht+3*dist,
                        x+0.7*wd, ht+3*dist,
                        x+wd+dist/3, ht+0.5*dist),
             [deco.earrow.large])
    c.text(x+0.5*wd, ht+3.2*dist, r'\Large 8', [text.halign.center, textcolor])
c.stroke(path.curve(-dist/3, -0.5*dist,
                    0.5*wd, -5*dist,
                    2.5*wd+2*dist, -5*dist,
                    3*wd+2.3*dist, -0.5*dist),
         [deco.earrow.large])
c.text(1.5*wd+dist,-5.2*dist, r'\Large 24',
       [text.halign.center, text.valign.top, textcolor])

c.writePDFfile()
