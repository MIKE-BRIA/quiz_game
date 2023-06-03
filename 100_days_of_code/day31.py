def colorchange(color):
    if color=='red':
        return('\033[31m')
    elif color=='white':
        return('\033[0m')
    elif color=='blue':
        return('\033[34m')
    elif color=='yellow':
        return('\033[33m')
    elif color=='green':
        return('\033[32m')
    elif color=='purple':
        return('\033[35m')
    
title= f"{colorchange('red')}={colorchange('white')}={colorchange('blue')}= {colorchange('yellow')}Music App {colorchange('blue')}={colorchange('white')}={colorchange('red')}="

print (f"{title: ^120}")
print(f"🔥▶️\t{colorchange('white')}Bimax Air")
print(f"\t{colorchange('yellow')}Brad")

prev = 'prev'
next = 'next'
pause= 'pause'

print(f"{colorchange('white')}{prev}")
print(f"{colorchange('green')}{next:^30}")
print(f"{colorchange('purple')}{pause:>30}")

print()
print()
print()
title="WELCOME TO"
print(f"{colorchange('white')}{title: ^80}")
duk=f"{colorchange('red')}-{colorchange('blue')}-  {colorchange('purple')}ARMBOOK  {colorchange('blue')}-{colorchange('red')}-"
print(f"{duk:>73}")
print()
                                                                                                                      
sub=f"{colorchange('yellow')}definitely not a rip off of "
print(f"{sub:>55}")
luk=f"{colorchange('yellow')} a certain other social networking site."
print(f"{luk:>70}")

print()
print()
cub=f"{colorchange('red')}Honest"
print(f"{cub:>48}")
print()
print()
user=f"{colorchange('white')}Username:"
pas=f"{colorchange('white')}Password:"

print(f"{user:>50}")
print(f"{pas:>50}")
