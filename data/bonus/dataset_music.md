```
mutation movies_music {

  goldenage1: insertmovies_by_genre(
    value: { 
      genre:"Music & Musicals", 
      year:2004,
      title:"The Golden Age",
      synopsis:"A seemingly perfect family looks to fix their problems with the help of Miss Clara, an older, wiser woman.",
      duration:114,
      thumbnail:"https://i.imgur.com/SQyPd7N.mp4"}) {
    value{title}
  }

   whiplash1: insertmovies_by_genre(
    value: { 
      genre:"Music & Musicals", 
      year:2014,
      title:"Whiplash",
      synopsis:"A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
      duration:106,
      thumbnail:"https://i.imgur.com/ZTOIYrc.mp4"}) {
    value{title}
  }

}
```