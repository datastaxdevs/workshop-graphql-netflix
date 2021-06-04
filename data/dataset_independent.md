mutation movies_independent {

 enteringred1: insertmovies_by_genre(
    value: { 
      genre:"Independent", 
      year:2019,
      title:"Entering red",
      synopsis:"A woman walks into a bar and is sold the life of her dreams.",
      duration:12,
      thumbnail:"https://i.imgur.com/K7ERYIB.mp4"}) {
    value{title}
  }

  warroom1: insertmovies_by_genre(
    value: { 
      genre:"Independent", 
      year:2019,
      title:"War Room",
      synopsis:"A seemingly perfect family looks to fix their problems with the help of Miss Clara, an older, wiser woman.",
      duration:120,
      thumbnail:"https://i.imgur.com/ZFFosSD.mp4"}) {
    value{title}
  }
  
}