```
mutation movies_horror {
 
 ava1: insertmovies_by_genre(
    value: { 
      genre:"Horror", 
      year:2015,
      title:"Ava's possession.",
      synopsis:"A young woman recovers from a demonic possession.",
      duration:89,
      thumbnail:"https://i.imgur.com/l6krM70.mp4"}) {
    value{title}
  }

  rotting1: insertmovies_by_genre(
    value: { 
      genre:"Horror", 
      year:2016,
      title:"Little Dead Rotting Hood",
      synopsis:"The residents of a small town discover that something more sinister than killer wolves is lurking in the backwoods: first the wolves start turning up dead...then people.",
      duration:88,
      thumbnail:"https://i.imgur.com/C2XcrZJ.mp4"}) {
    value{title}
  }

  room1: insertmovies_by_genre(
    value: { 
      genre:"Horror", 
      year:2015,
      title:"Room",
      synopsis:"Held captive for 7 years in an enclosed space, a woman and her young son finally gain their freedom, allowing the boy to experience the outside world for the first time.",
      duration:118,
      thumbnail:"https://i.imgur.com/Fx5iKwZ.mp4"}) {
    value{title}
  }

  conjuring1: insertmovies_by_genre(
    value: { 
      genre:"Horror", 
      year:2016,
      title:"The Conjuring 2",
      synopsis:"Ed and Lorraine Warren travel to North London to help a single mother raising four children alone in a house plagued by a supernatural spirit.",
      duration:134,
      thumbnail:"https://i.imgur.com/j3qBgq8.mp4"}) {
    value{title}
  }
  
}
```