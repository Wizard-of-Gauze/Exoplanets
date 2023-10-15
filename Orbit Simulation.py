import pygame
import numpy as np
pygame.init()

width, height = 800, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Transit Simulation')

AU = 1.495978707e11
dt = 86400

yellow = (255, 255, 0)
dark_grey = (80, 78, 81)
white = (255, 255, 255)
green = (0, 128, 0)
red = (255, 0, 0)
orange = (255, 140, 0)
gold = (255, 215, 0)
dark_blue = (0, 0, 139)
blue = (100, 149, 237)
brown = (139, 69, 19)

class Planet:
    G = 6.67430e-11
    AU = 1.495978707e11
    scale = 250 / AU
    
    def __init__(self, name, location, velocity, mass, color, size): 
        self.name = name
        self.location = location
        self.velocity = velocity
        self.mass = mass
        self.color = color
        self.location_orbit = [] #Append updated locations to this list
        self.velocity_orbit = [] #Append updated velocities to this list
        self.location_update = np.array([0, 0])
        self.velocity_update = np.array([0, 0])
        self.size = size
   
    def draw(self, win):
        x = self.location[0] * self.scale + width/2
        y = self.location[1] * self.scale + height/2
        
        if len(self.location_orbit) > 2: 
            updated_points = []
            for point in self.location_orbit:
                x, y = point
                x = x * self.scale + width/2
                y = y * self.scale + height/2
                updated_points.append((x, y))
            
        pygame.draw.lines(win,  self.color, False, updated_points, 2)
        pygame.draw.circle(win, self.color, (x,y), self.size)
        
    def acceleration(self, loc, planets):
        acceleration = np.array([0,0]) 
        for planet in planets: 
            if self != planet: 
                radius = planet.location - loc 
                radius_mag = np.linalg.norm(radius)
                acceleration_mag = (self.G * planet.mass)/(radius_mag**2)
                acceleration = acceleration + acceleration_mag * (radius/radius_mag) 
        return acceleration
            
    def RK4(self, dt, planets):
        k1 = self.velocity
        m1 = self.acceleration(self.location, planets)
        mid_point = self.location + k1 * (dt/2)
        k2 = self.velocity + m1*(dt/2)
        m2 = self.acceleration(mid_point, planets)
        mid_point2 = self.location + k2 * (dt/2)
        k3 = self.velocity + m2 * (dt/2)
        m3 = self.acceleration(mid_point2, planets)
        next_point = self.location + k3 * dt
        k4 = self.velocity + m3 * dt
        m4 = self.acceleration(next_point, planets)
        
        location_update = self.location_update = (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
        velocity_update = self.velocity_update = (dt/6)*(m1 + 2*m2 + 2*m3 + m4)
        
        return location_update, velocity_update

        
    def update(self, planets):
        for planet in planets:
            if self != planet:
                location_update, velocity_update = self.RK4(dt, planets)
                self.location = self.location + location_update
                self.velocity = self.velocity + velocity_update
                self.location_orbit.append(self.location)
                self.velocity_orbit.append(self.velocity)
            
def main():
    run = True
    clock = pygame.time.Clock()
    
    sun = Planet('Sun', np.array([0, 0]), np.array([0, 0]), 1.98892 * 10**30, yellow, 30)
    asteroid = Planet('Asteroid', np.array([-0.5*AU, 0]), np.array([0, 5000]), 1.98892 * 10**30, brown, 8)
    mercury = Planet('Mercury', np.array([-0.4*AU, 0]), np.array([0, 47360]), 3.285 * 10**23, dark_grey, 10)
    venus = Planet('Venus', np.array([-0.72*AU, 0]), np.array([0, 35020]), 4.867 * 10**24, white, 15)
    earth = Planet('Earth', np.array([-1*AU,0]), np.array([0, 29783]), 5.9742 * 10**24, dark_blue, 15)
    mars = Planet('Mars', np.array([-1.52*AU,0]), np.array([0, 24080]), 6.39 * 10**23, red, 12)
    #jupiter = Planet('Jupiter', np.array([5.2*AU, 0]), np.array([0, 13060]), 1.89813 * 10**27, orange)
    #saturn = Planet('Saturn', np.array([9.5*AU, 0]), np.array([0, 9670]), 5.683 * 10**26, gold)
    #uranus = Planet('Uranus', np.array([19.8*AU, 0]), np.array([0, 6790]), 8.681 * 10**25, blue)
    #neptune = Planet('Neptune', np.array([30.1*AU, 0]), np.array([0, 5450]), 1.024 * 10**26, dark_blue)
    
    planets = [sun, asteroid, mercury, venus, earth, mars]
    
    while run:
        clock.tick(60)
        win.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        for planet in planets:
            planet.update(planets)
            planet.draw(win)
            
        pygame.display.update()
        
    pygame.quit()
    
main()
    

        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
