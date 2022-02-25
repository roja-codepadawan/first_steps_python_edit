import pygal
#import pagal library

worldmap = pygal.maps.world.World()
#create a world map

worldmap.title = 'Countries'
#sea the title of the map

worldmap.add('Random Data', {
  'aq' : 10,
  'cd' : 30,
  'de' : 40,
  'eg' : 50,
  'ga' : 45, 
  'hk' : 23,
  'in' : 70,
  'jp' : 54,
  'nz' : 41,
  'kz' : 32,
  'us' : 66,
})
#adding the countries

worldmap.render_to_file('abc.svg')
#save into the file

print("Success")