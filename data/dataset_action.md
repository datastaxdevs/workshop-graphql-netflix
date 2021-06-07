```
mutation movies_actions {
  
  creed_1: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:2015,
      title:"Creed",
      synopsis:"The former World Heavyweight Champion Rocky Balboa serves as a trainer and mentor to Adonis Johnson, the son of his late friend and former rival Apollo Creed.",
      duration:133,
      thumbnail:"https://i.imgur.com/NQTuLtb.mp4"}) {
    value{title}
  }
  
  creed_2: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:2005,
      title:"Creed",
      synopsis:"The former World Heavyweight Champion Rocky Balboa serves as a trainer and mentor to Adonis Johnson, the son of his late friend and former rival Apollo Creed.",
      duration:133,
      thumbnail:"https://i.imgur.com/NQTuLtb.mp4"}) {
    value{title}
  }
  
  creed_3: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:1995,
      title:"Creed",
      synopsis:"The former World Heavyweight Champion Rocky Balboa serves as a trainer and mentor to Adonis Johnson, the son of his late friend and former rival Apollo Creed.",
      duration:133,
      thumbnail:"https://i.imgur.com/NQTuLtb.mp4"}) {
    value{title}
  }
  
  furious7_1: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:2015,
      title:"Furious7",
      synopsis:"Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.",
      duration:137,
      thumbnail:"https://i.imgur.com/7ax74eb.mp4"}) {
    value{title}
  }
  
  furious7_2: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:2005,
      title:"Furious7",
      synopsis:"Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.",
      duration:137,
      thumbnail:"https://i.imgur.com/7ax74eb.mp4"}) {
    value{title}
  }
  
  furious7_3: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:1995,
      title:"Furious7",
      synopsis:"Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.",
      duration:137,
      thumbnail:"https://i.imgur.com/7ax74eb.mp4"}) {
    value{title}
  }
  
  guardian_1: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:2014,
      title:"Guardians of the Galaxy",
      synopsis:"A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.",
      duration:121,
      thumbnail:"https://i.imgur.com/AylKL2G.mp4"}) {
    value{title}
  }
  
  guardian_2: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:2004,
      title:"Guardians of the Galaxy",
      synopsis:"A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.",
      duration:121,
      thumbnail:"https://i.imgur.com/AylKL2G.mp4"}) {
    value{title}
  }
  
  guardian_3: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:1994,
      title:"Guardians of the Galaxy",
      synopsis:"A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.",
      duration:121,
      thumbnail:"https://i.imgur.com/AylKL2G.mp4"}) {
    value{title}
  }
  
  suicide_1: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:2016,
      title:"Suicide Squad",
      synopsis:"A secret government agency recruits some of the most dangerous incarcerated super-villains to form a defensive task force. Their first mission: save the world from the apocalypse.",
      duration:123,
      thumbnail:"https://i.imgur.com/hwUzoyu.mp4"}) {
    value{title}
  }
  
  suicide_2: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:2006,
      title:"Suicide Squad",
      synopsis:"A secret government agency recruits some of the most dangerous incarcerated super-villains to form a defensive task force. Their first mission: save the world from the apocalypse.",
      duration:123,
      thumbnail:"https://i.imgur.com/hwUzoyu.mp4"}) {
    value{title}
  }
  suicide_3: insertmovies_by_genre(
    value: { 
      genre:"Action", 
      year:1996,
      title:"Suicide Squad",
      synopsis:"A secret government agency recruits some of the most dangerous incarcerated super-villains to form a defensive task force. Their first mission: save the world from the apocalypse.",
      duration:123,
      thumbnail:"https://i.imgur.com/hwUzoyu.mp4"}) {
    value{title}
  }

}
```