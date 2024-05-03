from flask import Flask
from flask import render_template, redirect, url_for
from flask import Response, request, jsonify
app = Flask(__name__)


video_games = [
    {
        "id": 1,
        "title": "Red Dead Redemption 2",
        "media_link": "https://www.rockstargames.com/reddeadredemption2/",
        "description": "Red Dead Redemption 2 is an epic tale of life in America at the dawn of the modern age. Developed by Rockstar Games, it's a prequel to the 2010 game Red Dead Redemption. Players explore a vast open world set in the American Wild West, featuring unparalleled attention to detail, a deep narrative, and immersive gameplay experiences. The game has been praised for its story, characters, and the vast, open-world environment.",
        "year_released": 2018,
        "features": ["Open-world exploration", "Deep narrative", "Immersive gameplay", "Attention to detail"],
        "image": "https://media-rockstargames-com.akamaized.net/mfe6/prod/__common/img/f2e22cd503abffa304796f40246a203a.png"
    },
    {
        "id": 2,
        "title": "Cyberpunk 2077",
        "media_link": "https://www.cyberpunk.net/",
        "description": "Cyberpunk 2077 is an open-world, action-adventure story set in Night City, a megalopolis obsessed with power, glamour, and body modification. Players assume the role of V, a mercenary outlaw going after a one-of-a-kind implant that is the key to immortality. Featuring a vast city to explore, a multitude of choices that affect the story, and cutting-edge visuals, it's known for its deep narrative and vibrant world.",
        "year_released": 2020,
        "features": ["Open-world exploration", "Deep narrative", "Vast customization options", "Dynamic world"],
        "image": "https://static.cdprojektred.com/cms.cdprojektred.com/cp_pl/media/screenshot/684x385/c94a2b44f3b48db05522cd872e6728371e5520da.jpg"
    },
    {
        "id": 3,
        "title": "FIFA 24",
        "media_link": "https://www.ea.com/en-au/games/ea-sports-fc/fc-24",
        "description": "FIFA 24 continues the tradition of the FIFA series, offering unparalleled football simulation. It brings improved gameplay mechanics, more realistic physics, and an enhanced AI that provides a more immersive football experience. The game features updated rosters, kits, and leagues, along with the introduction of new stadiums and modes. FIFA 24 is celebrated for its attention to detail, realism, and the comprehensive FIFA Ultimate Team experience.",
        "year_released": 2023,
        "features": ["Realistic gameplay mechanics", "Enhanced AI", "Updated rosters and leagues", "FIFA Ultimate Team"],
        "image": "https://media.contentapi.ea.com/content/dam/ea/fc/fc-24/common/gameplay/fc24-pre-order-founders.jpg.adapt.1456w.jpg"
    },
    {
        "id": 4,
        "title": "GTA 6",
        "media_link": "https://www.rockstargames.com/GTA6",
        "description": "GTA 6 sets a new benchmark for open-world games, expanding the franchise with its most ambitious setting yet. While details are fictional here, players can expect a vast, dynamic world that combines high-stakes heists, deep narrative, and immersive gameplay. Set across multiple cities, the game promises to push the boundaries of player freedom, storytelling, and gameplay mechanics, continuing the series' legacy of controversy, critical acclaim, and commercial success.",
        "year_released": 2024,
        "features": ["Multi-city open world", "Deep narrative", "Enhanced gameplay mechanics", "High-stakes heists"],
        "image": "https://staticg.sportskeeda.com/editor/2024/02/3ed68-17091702222571-1920.jpg?w=840"
    },
    {
        "id": 5,
        "title": "The Witcher 3: Wild Hunt",
        "media_link": "https://thewitcher.com/en/witcher3",
        "description": "The Witcher 3: Wild Hunt is a story-driven, next-generation open world role-playing game set in a visually stunning fantasy universe full of meaningful choices and impactful consequences. Players control Geralt of Rivia, a monster hunter searching for his missing adopted daughter. The game is known for its deep narrative, expansive world, and complex character interactions. With hundreds of hours of content, it has been critically acclaimed as one of the best RPGs of all time.",
        "year_released": 2015,
        "features": ["Expansive open world", "Deep narrative", "Complex characters", "Meaningful choices"],
        "image": "https://static.cdprojektred.com/cms.cdprojektred.com/witcher3/media/screenshot/979x511/08336916df25262078e418792359286202fcd819.jpg"
    },

    {
        "id": 6,
        "title": "Hogwarts Legacy",
        "media_link": "https://www.hogwartslegacy.com/en-us",
        "description": "Hogwarts Legacy is an immersive, open-world action RPG set in the world first introduced in the Harry Potter books. Explore and discover magical beasts, customize your character and craft potions, master spell casting, upgrade talents, and become the wizard you want to be. Experience Hogwarts in the 1800s; your character is a student who holds the key to an ancient secret that threatens to tear the wizarding world apart.",
        "year_released": 2023,
        "features": ["Open-world exploration", "Magical beasts discovery", "Potion crafting and spell casting", "In-depth character customization"],
        "image": "https://cdn-hogwartslegacy.warnerbrosgames.com/media/screen-07-t.jpg"
    },
    {
        "id": 7,
        "title": "Star Wars: Jedi Survivor",
        "media_link": "https://www.ea.com/games/starwars/jedi/jedi-survivor",
        "description": "Star Wars: Jedi Survivor continues the epic journey of Cal Kestis. Set five years after the events of Jedi: Fallen Order, this action-adventure game combines exploration, puzzle-solving, and combat across various Star Wars locations. Jedi Survivor expands on its predecessor's success, offering new Force abilities, lightsaber fighting styles, and an engaging story that delves deeper into the dark times following the collapse of the Jedi Order.",
        "year_released": 2024,
        "features": ["Expanded Force abilities", "Multiple lightsaber styles", "Deep narrative", "Iconic Star Wars locations exploration"],
        "image": "https://media.contentapi.ea.com/content/dam/ea/starwars/star-wars-jedi-survivor/screenshots/sjws-releasedate-screenshot-06-r01-v01-wm.jpg.adapt.crop16x9.818p.jpg"
    },
    {
        "id": 8,
        "title": "The Last of Us",
        "media_link": "https://www.xplaystation.com/en-us/the-last-of-us/",
        "description": "The Last of Us is a genre-defining experience blending survival and action elements to tell a character-driven story about a population decimated by a modern plague. Cities are abandoned and being reclaimed by nature, the infected lurk in the shadows, and survivors are killing each other for food, weapons, or whatever they can get their hands on. Joel, a brutal survivor, and Ellie, a brave young teenage girl who is wise beyond her years, must work together if they hope to survive their journey across the US.",
        "year_released": 2013,
        "features": ["Character-driven story", "Survival and action gameplay", "Dynamic enemy encounters", "Beautiful but dangerous world exploration"],
        "image": "https://gmedia.playstation.com/is/image/SIEPDC/TLOUTEST-HBO-Keyart-01-en-06dec22?$1200px$"
    },
    {
        "id": 9,
        "title": "God of War",
        "media_link": "https://www.playstation.com/en-us/god-of-war/",
        "description": "God of War is a breathtaking journey into a mythological Norse realm, focusing on the bond between Kratos, the God of War, and his son Atreus. Leaving behind the Greek mythology of previous games, this title explores Norse legends, with the duo facing gods and monsters of a world unfamiliar to them. The game revamps the series with a more intimate, over-the-shoulder free camera, a deep narrative, and a combat system that combines strategy with visceral action.",
        "year_released": 2018,
        "features": ["Norse mythology setting", "Deep narrative focus", "Revamped combat system", "Exploration of a mythological realm"],
        "image": "https://wallpapers.com/images/high/god-of-war-ii-screenshot-q2ln1i5b6wuutb6d.webp"
    },
    {
        "id": 10,
        "title": "Minecraft",
        "media_link": "https://www.minecraft.net/en-us",
        "description": "Minecraft is a game about placing blocks and going on adventures. Explore randomly generated worlds and build amazing things from the simplest of homes to the grandest of castles. Play in creative mode with unlimited resources or mine deep into the world in survival mode, crafting weapons and armor to fend off dangerous mobs. You can create, explore, and survive alone or with friends on mobile devices, Switch, Xbox, PlayStation, and PC.",
        "year_released": 2011,
        "features": ["Infinite world exploration", "Creative and survival modes", "Building and crafting", "Multiplatform multiplayer"],
        "image": "https://www.minecraft.net/content/dam/games/minecraft/screenshots/Tame_DesertCarousel_440x250.jpg"
    }
]


# ROUTES

@app.route('/')
def welcome():
    popular_games = video_games[:3]
    return render_template('game_homepage.html', games=popular_games)

# AJAX FUNCTIONS


@app.route('/get_popular_games')
def get_popular_games():
    popular_games = video_games
    return render_template('all_game.html', games=popular_games)


@app.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search', '').strip().lower()
    if not search_query:
        return redirect(url_for('welcome'))
    
    filtered_games = [
        game for game in video_games 
        if search_query in game['title'].lower()
        or any(search_query in feature.lower() for feature in game['features'])
        or search_query in game["description"].lower()
        or search_query == str(game['year_released'])]
    
    count_result = len(filtered_games)
    return render_template('search.html', games=filtered_games, search_query=search_query, result_count=count_result)


@app.route('/view/<int:game_id>')
def game_details(game_id):
    game = next((game for game in video_games if game["id"] == game_id), None)
    if game:
        return render_template('game_details.html', game=game)
    else:
        return "Game not found", 404
    

@app.route('/add')
def add_data():
    return render_template('add_data.html')


@app.route('/submit_data', methods=['POST'])
def submit_data():
    title = request.form.get('title')
    media_link = request.form.get('media_link')
    description = request.form.get('description')
    year_released = request.form.get('year_released')
    features = request.form.get('features')
    image = request.form.get('image')
    if not title or not media_link or not description or not year_released or not features or not image:
        return jsonify({'success': False, 'error': 'All Fields Must be Filled!'})
    
    try:
        year_released = int(year_released)
    except ValueError:
        return jsonify({'success': False, 'error': 'Year Released must be a valid Number!'})
    
    new_game = {
        'id': len(video_games) + 1,
        'title': title,
        'media_link': media_link,
        'description': description,
        'year_released': year_released,
        'features': features.split(','),
        'image': image
    }

    video_games.append(new_game)

    return jsonify({'success': True, 'view_url': url_for('game_details', game_id=new_game['id'])})


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_data(id):
    game = next((g for g in video_games if g['id']==id), None)

    if not game:
        return "Game Not Found", 404
    
    if request.method == 'POST':
       game['title'] = request.form['title']
       game['media_link'] = request.form['media_link']
       game['description'] = request.form['description']
       game['year_released'] = request.form['year_released']
       game['features'] = request.form['features'].split(',')
       game['image'] = request.form['image']

       return jsonify({'success': True, 'view_url': url_for('game_details', game_id=game['id'])})
    
    return render_template('edit.html', game=game)

if __name__ == '__main__':
    app.run(debug=True)
