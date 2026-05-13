convo = True

print("Hello there! I am an AI bot.")
name = input("What is your name? ")
print()
print(f"Nice to meet you, {name}!")
print()

while convo:

    # Feeling Part
    feeling = input("How are you feeling today? ").lower()

    if "good" in feeling or "great" in feeling or "happy" in feeling:
        print("Wonderful!! I'm glad to hear that!")
    elif "sad" in feeling or "bad" in feeling or "depressed" in feeling:
        print("Hope you feel better!")
    elif "bye" in feeling:
        convo = False
    else:
        print("It's difficult to put into words, I can understand.")

    # Hobby Part
    print()
    hobby = input("What are your hobbies? Do you like Sports, Music, Arts or something else? ").lower()

    if "sports" in hobby:
        print("Great! Playing sports is a wonderful way of relaxing yourself, while at the same time keeping yourself fit.")

        # Hobby Part - Sports Edition
        print()
        sport = input("What sports do you like to play? ").lower()
        
        if "cricket" in sport:
            print("That's awesome! Cricket is one of the greatest sports all over the world. Staying at that crease to score those runs for your team, bowling with all your strength, and fielding to not just save runs, but to save your team the win - this wonderful mix makes the game as popular as it gets.")
            
            # Sports - Cricket Edition
            player = input("Would you like to know more about some players? ").lower()

            if "virat kohli" in player:
                print("Great choice! Virat Kohli, often called 'King Kohli,' is widely regarded as one of the greatest batsmen to ever play the game. As of early 2026, Virat Kohli has transitioned into the final and perhaps most legendary phase of his career.")
                print("Major career milestones of this legend include: Most ODI centuries (54), the only active player in the 28,000 international runs club (across all formats), and awards including the ICC Player of the Decade (2010–2020) and ICC Cricketer of the Year award in 2017 and 2018.")
                print("After 18 years of 'Ee Sala Cup Namde,' Kohli finally participated in RCB's maiden IPL Title win in 2025, marking a massive emotional milestone.")
                print("THE KEY PART? His Batting skills. His 'Cover Drive' technique relies on perfect head position (directly over the front toe) and a high elbow finish. And, using his exceptionally flexible wrists, Kohli can whip balls from outside off-stump through mid-wicket, making 'The Flick' shot a piece of cake for him.")

            elif "chris gayle" in player:
                print("The Universe Boss! Chris Gayle is the undisputed king of T20 cricket and arguably the most destructive opener the world has ever seen.")
                print("Major milestones: He is the first player to hit 14,000+ runs in T20s and holds the record for the highest individual score in T20 history — a staggering 175* off 66 balls.")
                print("Gayle wasn't just a player; he was an entertainer who brought the 'Cool' to cricket, becoming a global icon for T20 leagues from the IPL to the CPL.")
                print("THE KEY PART? Raw Power. His technique ignores traditional footwork in favor of incredible hand-eye coordination and a massive swing arc. If it's in his zone, it stays hit — often landing outside the stadium!")

            elif "ms dhoni" in player:
                print("Captain Cool! Mahendra Singh Dhoni is the mastermind who changed the face of Indian cricket through his leadership and lightning-fast wicketkeeping.")
                print("Major milestones: He is the only captain to win all three major ICC trophies (T20 World Cup, ODI World Cup, and Champions Trophy). As of 2026, his legacy as the ultimate finisher remains untouched.")
                print("Even years after his international retirement, his leadership at CSK redefined longevity, proving that a sharp cricketing brain is just as important as physical fitness.")
                print("THE KEY PART? Tactical Calm. Dhoni’s ability to keep his heart rate low under extreme pressure allowed him to pull off impossible chases. Plus, his 'Helicopter Shot' — using a powerful wrist flick to dig out yorkers — is a technical marvel.")

            elif "sachin tendulkar" in player:
                print("The God of Cricket! Sachin Tendulkar is the benchmark against which every modern batsman, including Kohli, is measured.")
                print("Major milestones: He is the only player to score 100 international centuries and was the first person to score a double century in ODIs. His career spanned a legendary 24 years.")
                print("For over two decades, he carried the hopes of a billion people, retiring in 2013 with nearly every batting record in the book under his name.")
                print("THE KEY PART? Technical Perfection. Sachin’s 'Straight Drive' is widely considered the most perfect shot in cricket history. His balance was so precise that he rarely needed to use excessive force to find the boundary.")

            elif "kane williamson" in player:
                print("The epitome of class! Kane Williamson is the backbone of New Zealand cricket and a member of the elite 'Fab Four'.")
                print("Major milestones: He famously captained the Black Caps to their first-ever World Test Championship title in 2021. As of 2026, he has stepped back from T20Is to focus on being NZ's all-time leading Test run-scorer.")
                print("Even in the 2026 franchise season, he remains a highly sought-after mentor, known for his incredible sportsmanship and 'nice guy' image.")
                print("THE KEY PART? Soft Hands. Kane plays the ball exceptionally late, right under his eyes. This 'waiting' technique allows him to guide even the fastest deliveries through third-man with pinpoint precision.")

            elif "pat cummins" in player:
                print("The Golden Boy of Australia! Pat Cummins has transformed from a world-class fast bowler into one of the most successful captains of the modern era.")
                print("Major milestones: In a legendary 2023-2024 run, he led Australia to both the World Test Championship and the ODI World Cup titles. In 2026, he continues to lead Sunrisers Hyderabad in the IPL with his signature tactical clarity.")
                print("Beyond cricket, he's known for his leadership off the field and his commitment to family, making him a true role model in the sport.")
                print("THE KEY PART? Relentless Accuracy. Cummins doesn't just bowl fast; he hits the 'corridor of uncertainty' ball after ball. His ability to extract bounce from even the flattest pitches makes him a nightmare for any top-order batter.")

            elif "jasprit bumrah" in player:
                print("The Boom! Jasprit Bumrah is arguably the most complete fast bowler in the world, capable of winning games in any conditions.")
                print("Major milestones: He was a vital part of India's 2024 T20 World Cup victory and holds the record for the most wickets by an Indian pacer in a single T20I season. As of May 2026, he remains Mumbai Indians' ultimate weapon.")
                print("Even when he isn't taking wickets, his economy rate is so low that he forces batters to make mistakes against the bowlers at the other end.")
                print("THE KEY PART? The Hyperextended Release. Bumrah’s unique, short run-up and stiff-arm action create an incredibly late release point. This makes his 145 clicks feel like 155, and his 'toe-crushing' yorker nearly impossible to dig out.")

            else:
                print("That player sounds like a legend in the making! I don't have their specific stats in my database yet, but I'm always learning more about the game.")

        elif "football" in sport or "soccer" in sport:
            print("That's awesome! Football is the world's most popular game for a reason. From the tactical brilliance on the pitch to the adrenaline of a last-minute goal, the beautiful game unites billions of fans across every continent.")
            
            # Sports - Football Edition
            player = input("Would you like to know more about some players? ").lower()

            if "lionel messi" in player:
                print("Great choice! Lionel Messi, often called 'La Pulga,' is widely regarded as the greatest to ever lace up a pair of boots. As of early 2026, he is preparing for one final world stage appearance, continuing to defy age with his vision.")
                print("Major career milestones include: A record 8 Ballon d'Or titles, leading Argentina to World Cup glory in 2022, and holding the record for most goals in a calendar year (91).")
                print("After conquering Europe, Messi’s move to Inter Miami transformed football in North America, bringing a level of 'Messi-mania' never seen before.")
                print("THE KEY PART? His Low Center of Gravity. Standing at 5'7\", his balance allows him to change direction instantly. His 'La Pausa' technique — the ability to suddenly slow down to wait for a defender to commit — makes his dribbling impossible to stop.")

            elif "cristiano ronaldo" in player:
                print("The GOAT of hard work! Cristiano Ronaldo, or CR7, is the ultimate goal-scoring machine and a symbol of athletic perfection.")
                print("Major milestones: He is the highest all-time goal scorer in official senior matches for both club and country. He has won 5 Champions League titles and was the first to reach 800 career goals.")
                print("Ronaldo revolutionized the game by showing that elite longevity is possible through extreme discipline and physical conditioning.")
                print("THE KEY PART? Aerial Prowess and Power. His vertical leap is comparable to NBA players, allowing him to 'hang' in the air. Combined with his 'knuckleball' shooting technique, he can score from literally anywhere on the pitch.")

            elif "neymar" in player:
                print("The Samba Star! Neymar Jr. carries the torch of Brazilian flair, combining elite playmaking with jaw-dropping skill.")
                print("Major milestones: He is Brazil's all-time leading goal scorer, surpassing even the great Pelé. He was a pivotal part of the famous 'MSN' trio at Barcelona that won the Treble.")
                print("Neymar brought the 'Joga Bonito' style back to the mainstream, making every match he plays a highlight reel.")
                print("THE KEY PART? Creative Flair. His 'Rainbow Flick' and 'Step-overs' aren't just for show; he uses them to unbalance defenders in 1v1 situations. His ability to play as both a winger and a #10 playmaker makes him a dual-threat.")

            elif "kylian mbappe" in player:
                print("The Speed Demon! Kylian Mbappé is the face of the new generation and arguably the best player in the world right now in 2026.")
                print("Major milestones: A World Cup winner at just 19 years old, and the first player to score a hat-trick in a World Cup final since 1966. He is already PSG's all-time leading scorer.")
                print("By 2026, his move to Real Madrid has solidified his status as the heir to the throne of global football.")
                print("THE KEY PART? Explosive Acceleration. Mbappé doesn't just run; he glides. His 'flick and go' move — knocking the ball past a defender and outrunning them — is the most feared sight for any backline in the world.")

            elif "erling haaland" in player:
                print("The Terminator! Erling Haaland is a freak of nature who seems built in a lab specifically to score goals.")
                print("Major milestones: He shattered the Premier League single-season scoring record in his debut year and reached 40 Champions League goals faster than anyone in history.")
                print("As of 2026, he continues to dominate the Golden Boot race, treating world-class defenders like training cones.")
                print("THE KEY PART? Physical Dominance. He combines the strength of a powerhouse with the speed of a sprinter. His 'Poacher’s Instinct' — knowing exactly where the ball will land before it even gets there — is what makes him so clinical.")

            elif "kevin de bruyne" in player:
                print("The Maestro! Kevin De Bruyne is the premier playmaker of his generation, seeing passes that other players don't even realize are possible.")
                print("Major milestones: A multi-time Premier League Player of the Season and the fastest player to reach 100 assists in the English top flight.")
                print("In 2026, he remains the heart of the midfield, orchestrating plays with surgical precision.")
                print("THE KEY PART? The 'Whip' Cross. KDB’s ability to hit a first-time cross with incredible curl and pace from the 'half-space' is his trademark. He doesn't just pass to a teammate; he passes to exactly where the teammate *will* be.")

            else:
                print("That player sounds like a future Ballon d'Or winner! I don't have their specific stats in my database yet, but the football world is full of rising stars.")

        elif "chess" in sport:
            print("The ultimate battle of wits! Chess is a fantastic way to sharpen your observation, patience, and strategic thinking skills.")
            
            # Sports - Chess Edition
            player = input("Would you like to know more about some players? (Magnus Carlsen, Viswanathan Anand, or Garry Kasparov?) ").lower()

            if "magnus carlsen" in player:
                print("The GOAT of the modern era! Magnus Carlsen has dominated the world rankings for over a decade with a style that is almost computer-like in its precision.")
                print("Major milestones: He held the World Chess Champion title from 2013 to 2023 and reached the highest Elo rating in history (2882). As of 2026, he remains the king of Speed Chess.")
                print("THE KEY PART? End-game Mastery. Magnus can turn the tiniest, most boring advantage into a win. He grinds his opponents down by making zero mistakes until they eventually crumble under the pressure.")

            elif "viswanathan anand" in player:
                print("The 'Lightning Kid' from India! Vishy Anand is the man who sparked the chess revolution in Asia.")
                print("Major milestones: A five-time World Chess Champion across different formats. Even in 2026, he is a top-tier competitor and a legendary mentor to the new generation of Indian Grandmasters.")
                print("THE KEY PART? Intuition and Speed. In his prime, Anand was known for playing incredibly fast, relying on a natural 'feel' for the board that allowed him to see winning moves in seconds.")

            elif "garry kasparov" in player:
                print("The legendary titan! Garry Kasparov's aggressive style and deep preparation changed how chess is played at the highest level.")
                print("Major milestones: He was the World Champion for 15 years and famously took on the IBM supercomputer 'Deep Blue' in a historic man-vs-machine battle.")
                print("THE KEY PART? Tactical Aggression. Kasparov didn't just want to win; he wanted to dominate. His 'Key Part' was his deep opening preparation, often surprising opponents with moves they hadn't seen in 100 years.")

            elif "bobby fischer" in player:
                print("The American Genius! Bobby Fischer was a lone wolf who took on the entire Soviet chess machine and won.")
                print("Major milestones: He ended the Soviet dominance of the World Chess Championship by defeating Boris Spassky in 1972. His book, 'My 60 Memorable Games,' is still a bible for serious students.")
                print("THE KEY PART? Precise Calculation. Fischer didn't play for 'traps'; he played for the truth of the position. He had an incredible ability to simplify complex boards into winning endgames with mathematical accuracy.")

            elif "mikhail tal" in player:
                print("The 'Magician from Riga'! Mikhail Tal was the most creative and daring attacking player in history.")
                print("Major milestones: He became the youngest World Champion in 1960. He was famous for his 'dark' and mysterious sacrifices that confused even the best defenders.")
                print("THE KEY PART? Psychological Chaos. Tal’s 'Key Part' was his willingness to play moves that were objectively risky but practically impossible to defend against in a real game. He forced his opponents to solve impossible puzzles under time pressure.")

        elif "basketball" in sport:
            print("The game of high-flyers! Basketball is an incredible mix of individual skill, explosive athleticism, and split-second teamwork.")
            
            # Sports - Basketball Edition
            player = input("Would you like to know more about some players? (LeBron James, Stephen Curry, or Michael Jordan?) ").lower()

            if "lebron james" in player:
                print("The 'King'! LeBron James is a freak of nature who has maintained elite performance for over two decades.")
                print("Major milestones: The NBA's all-time leading scorer and a 4-time NBA Champion. By 2026, his legacy as the most 'complete' player to ever live is set in stone.")
                print("THE KEY PART? Basketball IQ and Versatility. At 6'9\" and 250lbs, he has the strength of a power forward but the passing vision of a point guard. He controls the entire floor like a general.")

            elif "stephen curry" in player:
                print("The Chef! Steph Curry single-handedly changed how basketball is played by making the three-pointer the most important shot in the game.")
                print("Major milestones: The all-time leader in three-pointers made and a 2-time MVP. He proved that skill and shooting can overcome raw size and strength.")
                print("THE KEY PART? The Quick Release. Steph can get his shot off in just 0.4 seconds. Because he can shoot from literally anywhere (even the logo), defenders have to chase him all over the court, which opens up space for his team.")

            elif "kobe bryant" in player:
                print("The Black Mamba! Kobe Bryant is legendary for having the most intense work ethic in the history of the sport.")
                print("Major milestones: A 5-time NBA Champion and 18-time All-Star. His 81-point game in 2006 remains one of the greatest individual scoring feats ever.")
                print("THE KEY PART? Footwork and the Fadeaway. Kobe studied film relentlessly to master the 'Triple Threat' position. His ability to use his feet to create just enough space for a fadeaway jumper made him unguardable in the clutch.")

            elif "shaquille o'neal" in player or "shaq" in player:
                print("The Big Aristotle! Shaq was the most physically dominant force the NBA has ever seen.")
                print("Major milestones: A 4-time NBA Champion and 3-time Finals MVP. He was so powerful that he literally broke backboards during games.")
                print("THE KEY PART? Low Post Positioning. Once Shaq got deep into the 'paint,' it was over. He used his massive frame to seal off defenders, making his 'Drop Step' and power dunk an unstoppable sequence.")


        elif "tennis" in sport:
            print("The ultimate test of endurance! Tennis is a sport of grace, power, and incredible mental resilience.")
            
            # Sports - Tennis Edition
            player = input("Would you like to know more about some players? (Roger Federer, Rafael Nadal, or Novak Djokovic?) ").lower()

            if "roger federer" in player:
                print("The Maestro! Federer made tennis look like ballet with his effortless movement and signature one-handed backhand.")
                print("Major milestones: 20 Grand Slam titles and a record for the most consecutive weeks at World No. 1. He is the global ambassador for 'class' in sports.")
                print("THE KEY PART? The Forehand Flick. Federer didn't need a huge backswing; he used his wrists to whip the ball at incredible angles, making it look easy while hitting winners from defensive positions.")

            elif "novak djokovic" in player:
                print("The Serbinator! Novak Djokovic is statistically the greatest to ever play the game, known for his 'Elastic' defense.")
                print("Major milestones: Holding the record for the most Grand Slam titles in men's history. As of 2026, his fitness levels still rival players ten years younger than him.")
                print("THE KEY PART? The Return of Serve. Novak is the greatest returner ever. He uses his incredible flexibility to reach balls that should be aces, neutralizing the opponent's biggest weapon immediately.")

            elif "serena williams" in player:
                print("The GOAT of Women's Tennis! Serena Williams dominated the tour for over two decades with sheer power and mental toughness.")
                print("Major milestones: 23 Grand Slam singles titles, the most in the Open Era. She achieved the 'Serena Slam'—holding all four majors at once—twice in her career.")
                print("THE KEY PART? The Tactical Serve. Serena’s serve is widely considered the greatest ever. Her ball toss was identical for every type of serve, making it impossible for opponents to read whether she was going for a flat ace or a wide kick.")

            elif "rafael nadal" in player or "rafa" in player:
                print("The King of Clay! Rafael Nadal is the ultimate warrior of the court, known for his 'never-say-die' attitude.")
                print("Major milestones: A record 14 French Open titles and 22 Grand Slams. His rivalry with Federer and Djokovic is the most iconic era in tennis history.")
                print("THE KEY PART? Heavy Topspin. Rafa’s 'Key Part' is his buggy-whip forehand. He generates so much topspin (often over 3,200 RPM) that the ball bounces high and fast, pushing opponents way behind the baseline and forcing errors.")

        elif "badminton" in sport:
            print("The fastest racket sport in the world! Badminton requires lightning reflexes and unbelievable stamina.")
            
            # Sports - Badminton Edition
            player = input("Would you like to know more about some players? (Lin Dan or Viktor Axelsen?) ").lower()

            if "lin dan" in player:
                print("Super Dan! He is widely considered the greatest badminton player of all time.")
                print("Major milestones: The only player to complete the 'Super Grand Slam'—winning all nine major titles in the badminton world.")
                print("THE KEY PART? Deceptive Net Play. Lin Dan could make the shuttlecock 'tumble' over the net so tightly that opponents had no choice but to lift it, setting him up for his famous powerful smash.")

            elif "viktor axelsen" in player:
                print("The Great Dane! Axelsen has dominated the world rankings in the 2020s with his height and technical precision.")
                print("Major milestones: Back-to-back Olympic gold medalist and multiple World Championships. As of 2026, he is the man to beat on the world tour.")
                print("THE KEY PART? Steep Smash. Standing at 6'4\", Axelsen uses his height to hit the shuttle at a very sharp downward angle, making it nearly impossible for defenders to return.")


    elif "music" in hobby:
        print("Wow! That's a very soothing way to heal yourself. Music can lower stress and provide a creative outlet for your emotions.")
        print()
        music_type = input("Do you like to listen to music, or even play it yourself? ").lower()

        if "play" in music_type or "instrument" in music_type:
            instr = input("That's talent! Which instrument do you play? (Piano, Guitar, or Violin?) ").lower()
            if "piano" in instr:
                print("The King of Instruments! Playing the piano improves multi-tasking like nothing else.")
                print("THE KEY PART? Finger Independence. Master pianists develop the ability to control the pressure of each individual finger to highlight a melody.")
            elif "guitar" in instr:
                print("Excellent! The guitar is incredibly versatile, fitting into everything from rock to classical.")
                print("THE KEY PART? Synchronization. The real skill is the perfect timing between your picking hand and your fretting hand.")
        
        elif "listen" in music_type:
            genre = input("What genre do you prefer? ").lower()
            print(f"Awesome! {genre.capitalize()} music is a great choice. It's amazing how a melody can change your entire mood!")

    elif "arts" in hobby:
        print("Wonderful! Expressing yourself through art is a fantastic way to sharpen your focus and bring your unique imagination to life.")
        print()
        art_type = input("Which form of art do you enjoy most? (Painting, Sketching, or Digital Art?) ").lower()

        if "painting" in art_type:
            print("Painting is all about the soul! You're splashing your emotions onto a canvas.")
            print("THE KEY PART? Color Theory. Understanding how complementary colors create vibrance is the secret to a great painting.")
        elif "sketching" in art_type:
            print("The foundation of all visual art! Sketching allows you to capture the world with just a pencil.")
            print("THE KEY PART? Shading. Mastering contrast can turn a flat 2D drawing into a 3D masterpiece.")

    elif "coding" in hobby:
        print("That's impressive! Coding is like having a superpower  —  it allows you to build anything you can imagine while sharpening your logic.")
        print()
        lang = input("What all programming languages have you learnt yet? ").lower()
        if "python" in lang:
            print("Python is a fantastic choice! It's known for being readable and powerful.")
            print("THE KEY PART? Readability. Python’s philosophy is 'Simple is better than complex,' making it the leader in AI today.")
        else:
            print(f"That's great! Learning {lang.capitalize()} gives you a deep understanding of how to solve complex problems.")

    elif "bye" in hobby:
        convo = False
    
    else:
        print("Great! Hobbies always help people to cope with their stress, making it much much easier to live your life in a better way.")
        
    # --- Age Part ---
    print()
    age = input("What's your age? (Or type 'no' to skip): ").lower()

    # Check if the user wants to exit
    if "bye" in age:
        convo = False
        continue
    
    # Check if the user refused to share
    elif "not" in age or "no" in age:
        print("Oh! Not a problem. We can continue discussing other stuff if you don't wanna share your age.")

    # Check if the input is actually a number
    elif age.isdigit():
        q2 = int(age)

        if q2 == 18:
            print("Great! So you're officially an adult!")
            input("Wanna know about your new responsibilities and allowances? ")
        elif q2 <= 14:
            print(f"I see! {q2} is a great age to explore new things.")
            input("How's your school going? ")
        elif 15 <= q2 <= 17:
            print("Wow! This must be a crucial year for you.")
            input("What stream are you planning to take for the future? Science, Commerce, Humanities or something else? ")
        elif 19 <= q2 <= 39:
            print("The prime of life! You're likely right in the middle of building your career or pursuing your dreams.")
            input("Are you working or studying something you really enjoy right now? ")
        elif q2 >= 40:
            print("Great! It's been a long journey of life till here, isn't it? You must have so much wisdom to share!")
        else:
            print("That's an interesting age!")

    else:
        print("I didn't quite get that. Please type your age in numbers next time!")

    # Ambition Part
    print()
    amb = input("So, what are your ambitions in life?").lower()

    if "bye" in amb:
        convo = False
    elif "doctor" in amb:
        print("I see! Becoming a doctor is a marathon, not a sprint, but it's one of the few careers where you can directly impact human lives every single day.")
        print("Since you’re aiming for the white coat, you would require:")
        print("1. A strong academic foundation (especially in Biology and Organic Chemistry)")
        print("2. Clinical and Volunteer experience")
        print("3. Facing standardized exams, designed to test your critical thinking and scientific knowledge")
        print("4. Developing 'Soft Skills' like Empathy, Resilience and Ethics to communicate with patients better.")
        doc = input("What stage of the journey are you currently in  —  are you picking out your high school classes, or are you already looking at university options?")

    elif "engineer" in amb:
        print("A builder of the future! Engineering is about taking complex problems and turning them into functional solutions, whether it's through code, concrete, or circuits.")
        print("To succeed in this field, you'll generally need:")
        print("1. Advanced Mathematics and Physics skills to understand how the world works.")
        print("2. Proficiency in specialized software like CAD, MATLAB, or various programming languages.")
        print("3. A 'Systems Thinking' mindset — understanding how small parts affect the whole machine.")
        print("4. Teamwork and Project Management skills to bring large-scale ideas to life.")
        eng = input("Are you more interested in the physical side like Mechanical or Civil, or the digital side like Software engineering? ")

    elif ("chartered" in amb and "accountant" in amb) or "ca" in amb:
        print("The backbone of the economy! Becoming a CA is a badge of excellence in the financial world, requiring immense dedication and precision.")
        print("Your path to the CA designation involves:")
        print("1. Mastering Accountancy, Auditing, and Taxation laws.")
        print("2. Passing multiple levels of rigorous professional examinations.")
        print("3. Completing a mandatory practical training or 'articleship' under a practicing firm.")
        print("4. Maintaining high ethical standards and an eagle eye for detail.")
        ca_stage = input("Are you currently preparing for your foundation exams, or are you just starting to look into the syllabus? ")

    elif "teacher" in amb:
        print("The noblest profession! As a teacher, you don't just share information; you shape the way the next generation thinks and views the world.")
        print("To become an effective educator, you'll need:")
        print("1. Deep expertise in your chosen subject matter.")
        print("2. A formal teaching qualification or degree in Education.")
        print("3. Patience and Adaptability to cater to different learning styles in a classroom.")
        print("4. Public Speaking skills to keep your students engaged and inspired.")
        teach = input("Do you see yourself teaching young children, or would you prefer lecturing at a university level? ")

    elif "singer" in amb or "musician" in amb:
        print("A soul-stirring ambition! Being a professional singer is about much more than a good voice; it's about storytelling and connecting with an audience.")
        print("To make it in the music industry, focus on:")
        print("1. Vocal Training and health to ensure your voice stays strong over a long career.")
        print("2. Learning Music Theory or an instrument to help you compose your own work.")
        print("3. Understanding the 'Business' side — marketing, social media, and networking.")
        print("4. Performance Experience — from small open mics to recording in a studio.")
        sing = input("Do you enjoy performing live for a crowd, or do you prefer the creative process of recording in a studio? ")

    elif "artist" in amb:
        print("A creator of worlds! Being a professional artist means translating your unique vision into a medium that others can experience.")
        print("To grow as an artist, you would require:")
        print("1. Constant practice to refine your technical skills (anatomy, light, color, and composition).")
        print("2. Building a Portfolio that showcases your best and most consistent work.")
        print("3. Learning Digital Tools (like Photoshop or Blender) alongside traditional mediums.")
        print("4. Resilience — the ability to handle critique and keep creating regardless of the trends.")
        art = input("Do you lean more towards traditional painting and sketching, or are you interested in Digital Art and Animation? ")

    elif "lawyer" in amb or "advocate" in amb:
        print("A defender of justice! Law is a challenging but rewarding field for those who love logic, debate, and reading.")
        print("Your legal journey will require:")
        print("1. Exceptional Reading and Analytical skills to interpret complex statutes.")
        print("2. A Law degree followed by passing your regional Bar Exam.")
        print("3. The ability to argue a case persuasively while staying composed under pressure.")
        print("4. A commitment to research — often spending hours finding that one perfect precedent.")
        law = input("Are you interested in the drama of the courtroom, or do you prefer the strategic side of Corporate Law?")

    elif "scientist" in amb or "space" in amb:
        print("Exploring the unknown! Whether it's the deep ocean or the stars above, a career in science is for the endlessly curious.")
        print("To join the scientific community, you'll need:")
        print("1. A Ph.D. or advanced research degree in your specialized field.")
        print("2. The 'Scientific Method' — forming hypotheses and being willing to fail.")
        print("3. Data Analysis skills to make sense of your experiments.")
        print("4. Collaboration — science is a team sport played across the whole globe.")
        sci = input("Does the mystery of the deep space fascinate you, or are you more interested in the secrets of our own planet? ")

    else:
        print("That sounds like a fascinating ambition! Every career has its own unique challenges, but with passion and a solid plan, you can definitely reach your goal.")
        print("The most important things in any field are:")
        print("1. Consistency and Hard Work.")
        print("2. Continuous Learning (the world changes fast!)")
        print("3. Networking with people who are already where you want to be.")



    if convo == False:
        print(f"I see. It's been great talking to you, {name}. See you later!")