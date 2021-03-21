import ducks

flock = ducks.Flock()
donald = ducks.Duck()
rene = ducks.Duck()
myne = ducks.Duck()
lyne = ducks.Duck()
dyne = ducks.Duck()
fyne = ducks.Duck()

#let's add_duck

flock.add_duck(donald)
flock.add_duck(rene)
flock.add_duck(myne)
flock.add_duck(lyne)
flock.add_duck(dyne)
flock.add_duck(fyne)

flock.migrate()