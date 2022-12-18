```
mutation movies_dramas {

 girl1: insertmovies_by_genre(
    value: { 
      genre:"Dramas", 
      year:2016,
      title:"The girl on the Train",
      synopsis:"A divorcee becomes entangled in a missing persons investigation that promises to send shockwaves throughout her life.",
      duration:112,
      thumbnail:"https://i.imgur.com/yinQyyT.mp4"}) {
    value{title}
  }

}
```