```
mutation movies_french {

 amelie1: insertmovies_by_genre(
    value: { 
      genre:"French", 
      year:2001,
      title:"Amelie",
      synopsis:"Amélie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.",
      duration:122,
      thumbnail:"https://i.imgur.com/fan0H9k.mp4"}) {
    value{title}
  }
  
}
```