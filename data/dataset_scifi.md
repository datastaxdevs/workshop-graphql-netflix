```
mutation movies_scifi {

 terminator2: insertmovies_by_genre(
    value: { 
      genre:"Sci-Fi", 
      year:1991,
      title:"Terminator 2",
      synopsis:"A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her ten year old son, John Connor, from a more advanced and powerful cyborg.",
      duration:137,
      thumbnail:"https://i.imgur.com/0RworbR.mp4"}) {
    value{title}
   }

 inception: insertmovies_by_genre(
    value: { 
      genre:"Sci-Fi", 
      year:2010,
      title:"Inception",
      synopsis:"Cobb steals information from his targets by entering their dreams.",
      duration:121,
      thumbnail:"https://i.imgur.com/RPa4UdO.mp4"}) {
    value{title}
   }
  
  prometheus: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2012,
      title:"Prometheus",
      synopsis:"After a clue to mankind's origins is discovered, explorers are sent to the darkest corner of the universe.",
      duration:134,
      thumbnail:"https://i.imgur.com/L8k6Bau.mp4"}) {
    value{title}
    }
  
  	aliens: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:1986,
      title:"Aliens",
      synopsis:"Ellen Ripley is sent back to the planet LV-426 to establish contact with a terraforming colony.",
      duration:134,
      thumbnail:"https://i.imgur.com/QvkrnyZ.mp4"}) {
    value{title}
    }
  
    bladeRunner: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:1982,
      title:"Blade Runner",
      synopsis:"Young Blade Runner K's discovery of a long-buried secret leads him to track down former Blade Runner Rick Deckard.",
      duration:145,
      thumbnail:"https://i.imgur.com/xhhvmj1.mp4"}) {
    value{title}
    }

    starTrek: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:1995,
      title:"Star Trek",
      synopsis:"Star trek, the next generation",
      duration:134,
      thumbnail:"https://i.imgur.com/CyBAqqD.mp4"}) {
    value{title}
    }

    wonderWoman: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2017,
      title:"Wonder Woman",
      synopsis:"When a pilot crashes and tells of conflict in the outside world, Diana, an Amazonian warrior in training, leaves home.",
      duration:134,
      thumbnail:"https://i.imgur.com/WHf4VQf.mp4"}) {
    value{title}
    }
    
    looper: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2012,
      title:"Looper",
      synopsis:"In the near future, the mob sends their victims back in time to get them executed by the loopers.",
      duration:156,
      thumbnail:"https://i.imgur.com/B1v1FRi.mp4"}) {
    value{title}
    }

    exMachina: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year: 2015,
      title:"Ex machina",
      synopsis:"Caleb Smith, a young programmer, gets a chance to become a part of a strange scientific experiment.",
      duration:134,
      thumbnail:"https://i.imgur.com/CeFGCCH.mp4"}) {
    value{title}
    }

    doctorStrange: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2016,
      title:"Doctor Strange",
      synopsis:"In an accident, Stephen Strange, a famous neurosurgeon, loses the ability to use his hands.",
      duration:156,
      thumbnail:"https://i.imgur.com/VAiM0Pr.mp4"}) {
    value{title}
    }

    her: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2013,
      title:"Her",
      synopsis:" A sensitive and soulful man earns a living by writing personal letters for other people.",
      duration:134,
      thumbnail:"https://i.imgur.com/y3NCz30.mp4"}) {
    value{title}
    }     

    theMartian: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2015,
      title:"The Martian",
      synopsis:"During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew.",
      duration:134,
      thumbnail:"https://i.imgur.com/DffSwK0.mp4"}) {
    value{title}
    }

    deadpool: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2016,
      title:"Deadpool",
      synopsis:"A wisecracking mercenary gets experimented on and becomes immortal but ugly, and sets out to track down the man who ruined his looks.",
      duration:156,
      thumbnail:"https://i.imgur.com/BmasM7v.mp4"}) {
    value{title}
    }
    
    upgrade: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year: 2018,
      title:"Upgrade",
      synopsis:"Grey, a technophobe, suffers paralysis and loses his wife during an attack.",
      duration:123,
      thumbnail:"https://i.imgur.com/UgnxAc5.mp4"}) {
    value{title}
    }

    okra: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2018,
      title:"Okra",
      synopsis:"For 10 idyllic years, young Mija has been caretaker and constant companion to Okja - a massive animal and an even bigger friend.",
      duration:123,
      thumbnail:"https://i.imgur.com/ieICjCJ.mp4"}) {
    value{title}
    }

    xMen: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2000,
      title:"X-men",
      synopsis:"X-Men is an American superhero film based on the fictional superhero team of the same name",
      duration:134,
      thumbnail:"https://i.imgur.com/8Fj0T1U.mp4"}) {
    value{title}
    }

    batmanBegins: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2005,
      title:"Batman Begins",
      synopsis:"After witnessing his parents' death, Bruce learns the art of fighting to confront injustice.",
      duration:125,
      thumbnail:"https://i.imgur.com/f5mRd6r.mp4"}) {
    value{title}
    } 

    ironMan: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2008,
      title:"Iron Man",
      synopsis:"After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
      duration:132,
      thumbnail:"https://i.imgur.com/Y9pEiJH.mp4"}) {
    value{title}
    }
    
    kong: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2017,
      title:"Kong: Skull Island",
      synopsis:"A crew that reaches Skull Island to map it, is attacked by a humongous ape.",
      duration:145,
      thumbnail:"https://i.imgur.com/rXA51dG.mp4"}) {
    value{title}
    }

    aliens3: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:1992,
      title:"aliens 3",
      synopsis:"Ellen Ripley's escape pod crash-lands on Fiorina 161, a penal colony planet terrorised by an alien.",
      duration:145,
      thumbnail:"https://i.imgur.com/HrChN9I.mp4"}) {
    value{title}
    }

    avatar: insertmovies_by_genre(value: { 
      genre:"Sci-Fi", 
      year:2009,
      title:"Avatar",
      synopsis:"A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world.",
      duration:134,
      thumbnail:"https://i.imgur.com/lrAI1jQ.mp4"}) {
    value{title}
    }
}
```