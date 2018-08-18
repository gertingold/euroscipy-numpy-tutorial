from pyx import canvas, color, deco, path, text, unit

text.set(text.LatexRunner)
text.preamble(r'\usepackage[sfdefault,scaled=.85,lining]{FiraSans}\usepackage{newtxsf}')
text.preamble(r'\usepackage{nicefrac}')
unit.set(xscale=1.4, wscale=1.2)

c = canvas.canvas()
r = 0.05
for n in range(1, 5):
    c.stroke(path.circle(n, 0, r))
    c.stroke(path.circle(-n, 0, r))
c.stroke(path.circle(0, 0, r), [deco.filled([color.grey(0)])])
dx = 0.1
dy = 0.3
c.stroke(path.curve(dx, dx, dy, dy, 1-dy, dy, 1-dx, dx), [deco.earrow])
c.text(0.5, dy+0.1, '+1', [text.halign.center])
c.stroke(path.curve(-dx, dx, -dy, dy, -1+dy, dy, -1+dx, dx), [deco.earrow])
c.text(-0.5, dy+0.1, '-1', [text.halign.center])
c.writePDFfile()
