from pyx import canvas, color, deco, path, style, text, unit

def draw_square(x, y, kante):
    c.stroke(path.rect(x, y, kante, kante), [style.linewidth.thick])

text.set(text.LatexRunner)
text.preamble(r'\usepackage{arev}\usepackage[T1]{fontenc}')
unit.set(xscale=1.3, wscale=1.2)
c = canvas.canvas()

kante = 1
dist = 0.2
punkte = 1
nrboxes = 3
nrpoints = 3

for n in range(nrboxes):
    x = n*(kante+dist)
    draw_square(x, 0, kante)
    c.text(x+0.5*kante, kante+0.2, n, [text.halign.center])
    nstr = ""
    if n>0: nstr = "%+i" % n
    c.text(x+0.5*kante, -0.2, 'N'+nstr, [text.halign.center, text.valign.top])
    x = (n+nrboxes)*(kante+dist)+dist+punkte
    draw_square(x, 0, kante)
    c.text(x+0.5*kante, kante+0.2, 'N'+str(n-3), [text.halign.center])
    c.text(x+0.5*kante, -0.2, str(n-3), [text.halign.center, text.valign.top])

xoffset = nrboxes*(kante+dist)
for n in range(nrpoints):
    c.fill(path.circle(xoffset+(0.5+n)*punkte/nrpoints, 0.5*kante, 0.05*kante))

c.writePDFfile()
