import settings
def height_prct(percentage):
    return settings.HEIGHT * percentage / 100

def width_prct(percentage):
    return settings.WIDTH * percentage / 100

print(height_prct(50)) # 360.0