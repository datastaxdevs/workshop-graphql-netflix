```
mutation movies_documentaries {

  firstp1: insertmovies_by_genre(
    value: { 
      genre:"Documentaries", 
      year:2011,
      title:"First Position",
      synopsis:"A documentary that follows six young dancers from around the world as they prepare for the Youth America Grand Prix, one of the most prestigious ballet competitions in the world.",
      duration:95,
      thumbnail:"https://i.imgur.com/Coz5yzb.mp4"}) {
    value{title}
  }

  firstp2: insertmovies_by_genre(
    value: { 
      genre:"Documentaries", 
      year:2001,
      title:"First Position",
      synopsis:"A documentary that follows six young dancers from around the world as they prepare for the Youth America Grand Prix, one of the most prestigious ballet competitions in the world.",
      duration:95,
      thumbnail:"https://i.imgur.com/Coz5yzb.mp4"}) {
    value{title}
  }

  firstp3: insertmovies_by_genre(
    value: { 
      genre:"Documentaries", 
      year:1991,
      title:"First Position",
      synopsis:"A documentary that follows six young dancers from around the world as they prepare for the Youth America Grand Prix, one of the most prestigious ballet competitions in the world.",
      duration:95,
      thumbnail:"https://i.imgur.com/Coz5yzb.mp4"}) {
    value{title}
  }

  firstp4: insertmovies_by_genre(
    value: { 
      genre:"Documentaries", 
      year:1981,
      title:"First Position",
      synopsis:"A documentary that follows six young dancers from around the world as they prepare for the Youth America Grand Prix, one of the most prestigious ballet competitions in the world.",
      duration:95,
      thumbnail:"https://i.imgur.com/Coz5yzb.mp4"}) {
    value{title}
  }

  path1: insertmovies_by_genre(
    value: { 
      genre:"Documentaries", 
      year:2007,
      title:"Path of glory",
      synopsis:"After refusing to attack an enemy position, a general accuses the soldiers of cowardice and their commanding officer must defend them.",
      duration:88,
      thumbnail:"https://i.imgur.com/xZid5oj.mp4"}) {
    value{title}
  }

   path2: insertmovies_by_genre(
    value: { 
      genre:"Documentaries", 
      year:1997,
      title:"Path of glory",
      synopsis:"After refusing to attack an enemy position, a general accuses the soldiers of cowardice and their commanding officer must defend them.",
      duration:88,
      thumbnail:"https://i.imgur.com/xZid5oj.mp4"}) {
    value{title}
  }

   path3: insertmovies_by_genre(
    value: { 
      genre:"Documentaries", 
      year:1987,
      title:"Path of glory",
      synopsis:"After refusing to attack an enemy position, a general accuses the soldiers of cowardice and their commanding officer must defend them.",
      duration:88,
      thumbnail:"https://i.imgur.com/xZid5oj.mp4"}) {
    value{title}
  }

   path4: insertmovies_by_genre(
    value: { 
      genre:"Documentaries", 
      year:2017,
      title:"Path of glory",
      synopsis:"After refusing to attack an enemy position, a general accuses the soldiers of cowardice and their commanding officer must defend them.",
      duration:88,
      thumbnail:"https://i.imgur.com/xZid5oj.mp4"}) {
    value{title}
  }

  
}
```
