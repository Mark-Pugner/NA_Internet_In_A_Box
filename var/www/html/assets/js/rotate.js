var art =  [	
	{'Art': '3rRkVVeumZ.png', 'Source': 'https://noagendaartgenerator.com/artwork/15799', 'Artist': 'm000se', 'Title': 'Slaves No More'},
	{'Art': '0v9QBMnH04.png', 'Source': 'https://noagendaartgenerator.com/artwork/15130', 'Artist': 'Chaibudesh', 'Title': 'That’s True'},
	{'Art': '81wM8K9fo8.png', 'Source': 'https://noagendaartgenerator.com/artwork/15061', 'Artist': 'Sir Uncle Dave', 'Title': 'My Exit Stategy'},
	{'Art': 'EQ4Nj90sVw.png', 'Source': 'https://noagendaartgenerator.com/artwork/15048', 'Artist': 'Chaibudesh', 'Title': 'One Dollar Eye of Horus'},
	{'Art': 'rvozZOaSoX.png', 'Source': 'https://noagendaartgenerator.com/artwork/15053', 'Artist': 'Chaibudesh', 'Title': 'Ladies Selfie Squad Car Bomb'},
	{'Art': '81znDnKuwq.png', 'Source': 'https://noagendaartgenerator.com/artwork/14221', 'Artist': 'Mike Riley', 'Title': 'China is Less Explicit Asshole'},
	{'Art': '9YeMZJ3HGv.png', 'Source': 'https://noagendaartgenerator.com/artwork/14155', 'Artist': 'MountainManSteve', 'Title': 'You Betta Greta'},
	{'Art': 'PajReQvhQA.png', 'Source': 'https://noagendaartgenerator.com/artwork/13532', 'Artist': 'pewDpie', 'Title': 'Who\'s the "man"!?'},
	{'Art': '5bvA7DqU3E.png', 'Source': 'https://noagendaartgenerator.com/artwork/13533', 'Artist': 'Mike Riley', 'Title': 'green bugs and goat'},
	{'Art': 'nVkOXPktoO.png', 'Source': 'https://noagendaartgenerator.com/artwork/13434', 'Artist': 'MountainManSteve', 'Title': 'What is your cat trying to tell you.'},
	{'Art': 'kxPpm2Yhkp.png', 'Source': 'https://noagendaartgenerator.com/artwork/13337', 'Artist': 'Mike Riley', 'Title': 'clockwork'},
	{'Art': 'Nq041r2t5m.png', 'Source': 'https://noagendaartgenerator.com/artwork/13160', 'Artist': 'wadewinstonwilso', 'Title': 'NO AGENDA'},
	{'Art': 'QajKZERhwO.png', 'Source': 'https://noagendaartgenerator.com/artwork/13119', 'Artist': 'Melvin Gibstein', 'Title': 'bad graff'},
	{'Art': 'BWYZeXYhV8.png', 'Source': 'https://noagendaartgenerator.com/artwork/13158', 'Artist': "Darren O'Neill", 'Title': 'No Agenda Records Evergreen'},
	{'Art': '4m4AJzGszM.png', 'Source': 'https://noagendaartgenerator.com/artwork/12114', 'Artist': 'OfficerDoofy', 'Title': 'Doofy Salutes Adam!'},
	{'Art': 'RaQRDBBC7P.png', 'Source': 'https://noagendaartgenerator.com/artwork/11855', 'Artist': 'chocolatyshatnr', 'Title': 'CohenTransmittal'},
	{'Art': 'XvX4nZAfxl.png', 'Source': 'https://noagendaartgenerator.com/artwork/11667', 'Artist': 'Jake', 'Title': 'pseudo-addiction with show name'},
	{'Art': 'av3r8ORuZr.png', 'Source': 'https://noagendaartgenerator.com/artwork/11374', 'Artist': "Darren O'Neill", 'Title': 'Here\'s No Agenda'},
	{'Art': '9YY5GVzSNj.png', 'Source': 'https://noagendaartgenerator.com/artwork/11069', 'Artist': 'Tyler Brown', 'Title': 'Trump Inspirations'},
	{'Art': '1OGbov5FDG.png', 'Source': 'https://noagendaartgenerator.com/artwork/10210', 'Artist': 'Mike Riley', 'Title': 'Ike Don\'t Dance'},
]



function getRandomImage() {
  //var images = ["image1.jpg","image2.jpg","image3.jpg"];

  //return images[Math.floor(Math.random() * images.length)];

  artInfo = art[Math.floor(Math.random() * art.length)];
  return artInfo;
}

function displayRandomImage() {
	artInfo = getRandomImage();
	var htmlImage = document.getElementById("rotatingArt").src = "images/" + artInfo['Art'];
	htmlImage.src = getRandomImage();
	var htmlTitle = document.getElementById("imageTitle").innerHTML = artInfo['Title'];
	var htmlArtist = document.getElementById("imageArtist").innerHTML = artInfo['Artist'];
}


