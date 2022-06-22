```
mutation movies_italian {

 ottoemezzo: insertmovies_by_genre(
    value: { 
      genre:"Italian", 
      year:1963,
      title:"8 1/2",
      synopsis:"A harried movie director retreats into his memories and fantasies.",
      duration:138,
      thumbnail:"https://i.imgur.com/KeF2Cr9.mp4"}) {
    value{title}
  }
}
```
