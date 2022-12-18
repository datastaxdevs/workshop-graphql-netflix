```
mutation movies_fantasy {

  doctorstrange1: insertmovies_by_genre(
    value: { 
      genre:"Fantasy", 
      year:2016,
      title:"Doctor Strange",
      synopsis:"While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts.",
      duration:115,
      thumbnail:"https://i.imgur.com/AARIL26.mp4"}) {
    value{title}
  }

  fantastic_beast1: insertmovies_by_genre(
    value: { 
      genre:"Fantasy", 
      year:2016,
      title:"Fantastic Beasts and Where to Find Them",
      synopsis:"The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school.",
      duration:132,
      thumbnail:"https://i.imgur.com/NhenJym.mp4"}) {
    value{title}
  }

  sleeping_beauty1: insertmovies_by_genre(
    value: { 
      genre:"Fantasy", 
      year:2016,
      title:"The Curse of Sleeping Beauty",
      synopsis:"Thomas unexpectedly inherits a property with a mysterious curse.",
      duration:132,
      thumbnail:"https://i.imgur.com/LcqMMwG.mp4"}) {
    value{title}
  }

  lotr1: insertmovies_by_genre(
    value: { 
      genre:"Fantasy", 
      year:2001,
      title:"The Fellowship of the Ring",
      synopsis:"A meek Hobbit from the Shire and eight companions set out on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron.",
      duration:178,
      thumbnail:"https://i.imgur.com/YdhTLqF.mp4"}) {
    value{title}
  }

  mummy1: insertmovies_by_genre(
    value: { 
      genre:"Fantasy", 
      year:1999,
      title:"The Mummy",
      synopsis:"At an archaeological dig in the ancient city of Hamunaptra, an American serving in the French Foreign Legion accidentally awakens a mummy who begins to wreak havoc as he searches for the reincarnation of his long-lost love.",
      duration:124,
      thumbnail:"https://i.imgur.com/62tJ58E.mp4"}) {
    value{title}
  }
  
}
```