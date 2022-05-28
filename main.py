class Student:
    # [assignment] Skeleton class. Add your code here
        
   def __init__(self, name, age, track, score):
            self.name = str(name)
            self.age = int(age)
            self.track = list(track)
            self.score = str(score)
            
   def change_name(self, c_n):
          self.name = str(c_n)
        
   def change_age(self, c_age):
   	   self.age = int(c_age)
   	   
   def add_track(self, a_track):
   	  self.a_track = list(a_track)
   	  return self.track.extend(self.a_track)   	  
   
   def get_score(self):
   	   return self.score	   	   


Bob = Student("Bob", 26, ["FE","BE"], 20.90)
''' overriden objects
print(Bob.name)
print(Bob.age)
print(Bob.track)
print(Bob.score)
'''
print("My name is", Bob.name, "my age is", Bob.age, "my track is", Bob.track, "my score is", Bob.score)


# Expected methods
Bob.change_name("peter")
Bob.change_age(34)
Bob.add_track(["UI/UX"])
Bob.get_score()


print(Bob.name)
print(Bob.age)
print(Bob.track)
print(Bob.score)
print("My name is", Bob.name, "my age is", Bob.age, "my track is", Bob.track, "my score is", Bob.score)
